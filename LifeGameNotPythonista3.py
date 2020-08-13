import os
import time
from lib.Component import Cell, World

height = 38
width = 38
cellCount = height * width

world = World(height, width)
index = 0

# init
for r in range(height):
	for c in range(width):
		cell = Cell(index)
		cell.setPos(r, c)
		world.setCell(cell)
		cell.setNeighborhood(height, width)
		index = index + 1

methodList = world.getGenesisMethodList()
print('選択する初期配置の番号を入力してください')
for m in methodList.items():
	print(m[0], ':', m[1])
methodNo = int(input().rstrip())
method = methodList.get(methodNo)

genResult = world.genesis(method)
try:
	if genResult != 0:
		if len(genResult) == 0:
			raise Exception('初期配置ファイルが存在しません')
		print('選択するファイルの番号を入力してください')
		for file in genResult.items():
			print(file[0], ':', file[1])
		fileNo = int(input().rstrip())
		fileName = genResult.get(fileNo)
		world.genesis(method, fileName)
	
	for i in range(300):
		world.nextEra()
		world.progress()
		os.system('cls')
		print(str(world.show()))
		print('count:',i)
		time.sleep(0.05)
except Exception as e:
	print(e)
finally:
	pass
