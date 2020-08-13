from .FileUtil import FileUtil
import random

class Cell:
	def __init__(self, name):
		self.alive = 0
		self.nextAlive = 0
		self.name = name
		self.neighborhood = [-1] * 8
	def getName(self):
		return self.name
	def getNeighborhood(self):
		return self.neighborhood
	def isAlive(self):
		return True if self.alive == 1 else False
	def birth(self):
		self.alive = 1
	def death(self):
		self.alive = 0
	def setNextAlive(self, neighbours):
		if self.isAlive():
			if neighbours <= 1 or neighbours >= 4:
				self.nextAlive = 0
			else:
				self.nextAlive = 1
		else:
			if neighbours == 3:
				self.nextAlive = 1
			else:
				self.nextAlive = 0
	def progress(self):
		self.alive = self.nextAlive
	def setPos(self, r, c):
		self.r = r
		self.c = c
	def setNeighborhood(self, h, w):
		vt = 0
		hl = 0
		if self.r == 0:
			# 最上位行
			vt = 1
		elif self.r == h - 1:
			# 最下位行
			vt = 2
		if self.c == 0:
				# 最左列
				hl = 1
		elif self.c == w -1:
				# 最右列
				hl = 2
			
		if vt == 1 and hl == 1:
			self.neighborhood[4] = self.name + 1
			self.neighborhood[6] = self.name + w
			self.neighborhood[7] = self.name + w + 1
		elif vt == 1 and hl == 0:
			self.neighborhood[3] = self.name - 1
			self.neighborhood[4] = self.name + 1
			self.neighborhood[5] = self.name + w - 1
			self.neighborhood[6] = self.name + w
			self.neighborhood[7] = self.name + w + 1
		elif vt == 1 and hl == 2:
			self.neighborhood[3] = self.name - 1
			self.neighborhood[5] = self.name + w - 1
			self.neighborhood[6] = self.name + w
		elif vt == 0 and hl == 1:
			self.neighborhood[1] = self.name - w
			self.neighborhood[2] = self.name - w + 1
			self.neighborhood[4] = self.name + 1
			self.neighborhood[6] = self.name + w
			self.neighborhood[7] = self.name + w + 1
		elif vt == 0 and hl == 0:
			self.neighborhood[0] = self.name - w -1
			self.neighborhood[1] = self.name - w
			self.neighborhood[2] = self.name - w + 1
			self.neighborhood[3] = self.name - 1
			self.neighborhood[4] = self.name + 1
			self.neighborhood[5] = self.name + w - 1
			self.neighborhood[6] = self.name + w
			self.neighborhood[7] = self.name + w + 1
		elif vt == 0 and hl == 2:
			self.neighborhood[0] = self.name - w -1
			self.neighborhood[1] = self.name - w
			self.neighborhood[3] = self.name - 1
			self.neighborhood[5] = self.name + w - 1
			self.neighborhood[6] = self.name + w
		elif vt == 2 and hl == 1:
			self.neighborhood[1] = self.name - w
			self.neighborhood[2] = self.name - w + 1
			self.neighborhood[4] = self.name + 1
		elif vt == 2 and hl == 0:
			self.neighborhood[0] = self.name - w -1
			self.neighborhood[1] = self.name - w
			self.neighborhood[2] = self.name - w + 1
			self.neighborhood[3] = self.name - 1
			self.neighborhood[4] = self.name + 1
		elif vt == 2 and hl == 2:
			self.neighborhood[0] = self.name - w -1
			self.neighborhood[1] = self.name - w
			self.neighborhood[3] = self.name - 1
	def show(self):
		print('name:', self.name)
		print('alive:', self.alive)
		print('pos:',self.r,',',self.c)
		print('neb:', self.neighborhood)

class World:
	def __init__(self, width, height):
		self.cells = {}
		self.width = width
		self.height = height
	def setCell(self, cell):
		key = cell.getName()
		self.cells[key] = cell
	def getCell(self, name):
		return self.cells.get(name)
	def getNeighborAlive(self, cell):
		env = 0
		neighborhoodLst = cell.getNeighborhood()
		for n in neighborhoodLst:
			if n != -1:
				if self.cells.get(n).isAlive():
					env = env + 1
		cell.setNextAlive(env)
	def nextEra(self):
		for cell in self.cells.values():
			self.getNeighborAlive(cell)
	def progress(self):
		for cell in self.cells.values():
			cell.progress()
	
	def getGenesisMethodList(self):
		result = {1:'random', 2:'glider', 3:'blinker',4:'file'}
		return result
	def genesis(self, method, fileName = ''):
		recipe = []
		if 'random' == method:
			recipe = self.getRandomSet(0.5)
		elif 'glider' == method:
			recipe = self.getGliderGunset()
		elif 'blinker' == method:
			recipe = self.getBlinkerSet()
		elif 'file' == method and fileName == '':
			return FileUtil.getFileList()
		elif 'file' == method and fileName != '':
			recipe = FileUtil.loadInit(fileName)
		else:
			recipe = self.getRandomSet(0.9)
		index = 0
		for cell in self.cells.values():
			if index in recipe:
				cell.birth()
			index += 1
		return 0
	def getRandomSet(self, threshold):
		result = []
		for cell in range(len(self.cells)):
			if threshold > random.random():
				result.append(cell)
		FileUtil.saveInit(result)
		return result
	def getGliderGunset(self):
		return  [63, 
		99, 101, 
		127, 128, 135, 136, 149, 150,
		164, 168, 173, 174, 187, 188,
		191, 192, 201, 207, 211, 212,
		229, 230, 239, 243, 245, 246, 251, 253,
		277, 283, 291,
		316, 320,
		355, 356]
	def getBlinkerSet(self):
		return  [243, 244, 245]
	def show(self):
		visual = []
		index = 0
		for h in range(self.width):
			row = ''
			for w in range(self.height):
				if self.cells.get(index).isAlive():
					row += u" ■"
				else:
					row += u" □"
				index = index + 1
			visual.append(row)
		result = ''
		for h in range(self.height):
			result = result + str(visual[h])
			result = result + '\n'
		return result
