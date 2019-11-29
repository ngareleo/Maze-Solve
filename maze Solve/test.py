from random import randint
"""""

def create_grid(x,y):

	result_grid = []
	for i in range(x+1):
		for j in range(y+1):
			result_grid.append([])
			result_grid[i].append(randint(1,243))
	return result_grid

for grid in create_grid(10,10):
	print(grid)
"""
test_grid = [
	[91,92,93,94,59,96,97,98],
	[12,22,23,24,25,26,27,18],
	[21,22,23,24,25,26,27,28],
	[31,32,33,34,35,36,37,38],
	[11,12,23,44,45,46,47,48],
	[15,52,53,54,55,56,57,58],
	[61,62,63,64,65,66,67,68],
	[71,72,73,74,75,76,77,78],
	]

CC,CR = 1,1

#function to look at surrounding cells

def look_around(grid,current_pos):
	x , y = current_pos[0] , current_pos[1]
	#left right up down
	neighbors = [[],[],[],[]]
	#We look at all directions
	if x - 1 < 0 :#left
		pass
	else:
		neighbors[0].append(grid[y][x-1])
	if x + 1 > len(grid[x]):#Right 
		pass 
	else:
		neighbors[1].append(grid[y][x + 1])  
	if y - 1 < 0:#Up
		pass
	else:
		neighbors[2].append(grid[y + 1][x])
	if y + 1 > len(grid[y]):#Down
		pass 
	else:
		neighbors[3].append(grid[y - 1][x])
	return neighbors

#We will move from (0,0) moving right , down until we reach the end of the grid

def move_stairs(arr,coordinates):

	x,y = coordinates[1],coordinates[0]
	cr ,cc = arr[y] , arr[y][x]
	current_value = [cr,cc]

	while cc != -1:

		#Movement loop
		x += 1
		cr ,cc = arr[x] , arr[y][x]
		current_value = [cc]
		print(f"current coordinate is : {current_value}")
		y += 1
		cr ,cc = arr[x] , arr[y][x]
		current_value = [cc]
		print(f"current coordinate is : {current_value}")


move_stairs(test_grid,[CR,CC])

		
