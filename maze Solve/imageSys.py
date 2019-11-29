#!/usr/bin/py

#Does the path finding

from imageFind import ImageFinder

"""\
	\\Step One
	1. Check maze validity
		::One opening and one closing point
	2. Look for starting point
	3. Create navigation sys
	4. Create node function
	5. Intergrate path finding

	Solve maze
"""
class maze:

	def __init__(self,starting_point,ending_point,maze_data):
		self.maze_data = maze_data
		self.starting_point = starting_point
		self.ending_point = ending_point

class node:

	def __init__(self,working_maze, mother_node = None , child_node = None, past_points = None, current_point = None):
		self.working_maze = working_maze
		self.mother_node = mother_node
		self.child_node = child_node
		self.past_points = past_points
		self.current_point = current_point

	def add_child(self,number):
		children = self.child_node
		possible_directions = find_directions()
		for i in range(number):
			children.append(node(
				working_maze=self.working_maze,
				mother_node=self,
				child_node=[],
				past_points=[],
				current_point= possible_directions[i],
			))

	def dead_point(self):
		cp = self.current_point
		pos = [self.working_maze[cp[0]],self.working_maze[cp[0]]]

class MazeMaster:
	
	def __init__(self,maze_data):

		self.maze_data = maze_data

	#step 1
	def create_maze_object(self):#Creates a maze object if valid

		global new_mazeObject

		our_maze_data  = self.maze_data
		st_point ,en_point = our_maze_data[0],our_maze_data[-1]
		maze_valid = False
		num_pixels = 0
		for pix in st_point:
			if pix == 1:
				num_pixels+=1
			if num_pixels > 1:
				print("Starting point of maze is Invalid")
				return maze_valid
		num_pixels = 0
		for c_pix in en_point:
			if c_pix == 1:
				num_pixels+=1
			if num_pixels > 1:
				print("End point of maze is invalid")
				return maze_valid
		new_mazeObject = maze(starting_point=find_starting_point(st_point),ending_point=find_starting_point(en_point),maze_data=[])
		print(f"New maze object cretaed {new_mazeObject}")
		return new_mazeObject


def find_starting_point(row):
	# Find the pixel the node should start on maze creation
	for pix in row :
		if pix == 1:
			return row.index(pix)
def find_directions (grid, maze_object_cp):
	# Returns a list of possible directions a node can go if it reaches to a branch
	pass

def look_around(grid,current_pos):
	# Returns the surrounding cells to the current position
	x , y = current_pos[0], current_pos[1]
	# left right up down
	neighbors = [[],[],[],[]]
	# We look at all directions
	if x - 1 < 0 :#left
		pass
	else:
		neighbors[0].append(grid[y][x-1])
	if x + 1 > len(grid[x]):# Right
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


workingImage = './Mazes/normal.png'# Sample maze

ImageObj = ImageFinder(workingImage)
ImageObj.create_imageGrid()

mazeMasterObj = MazeMaster(ImageObj.image_grid)

new_maze_object = mazeMasterObj.create_maze_object()
ImageObj.print_grid()
