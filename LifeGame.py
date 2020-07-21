import console, time
from lib.Component import *

s = [38, 38]#input().rstrip().split(' ')
height = int(s[0])
width = int(s[1])
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
world.setInitAlive()
#world.setInitGliderGun()
#world.setInitBlinker()

console.set_font('Menlo',8)
print(world.show())

for i in range(300):
	world.nextEra()
	world.progress()
	console.clear()
	print(str(world.show()))
	print('count:',i)
	time.sleep(0.1)

console.set_font()
