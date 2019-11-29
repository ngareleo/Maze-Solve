from PIL import Image

workingImage = './Mazes/normal.png'

class ImageFinder:

	def __init__(self, image, image_grid = None):
		self.image = image
		self.image_grid = image_grid


	def create_imageGrid(self):#Returns a grid object with grayscale info

		working_image = self.image
		with Image.open(working_image) as f:
			print("Image opened")
			our_grid = create_grid(working_image)
			print(our_grid)
			image_data = list(f.getdata())
			print(f"Horizontal {f.size[0]}\nVertical {f.size[0]}")
			cc = 0 
			cr = 1
			while cc < len(image_data):
				col = 0
				for space in range(cc,f.size[0]*cr):
					our_grid[cr - 1].append(image_data[cc])
					cc+=1;col += 1
				cr += 1;col = 0
			self.image_grid = our_grid

	def print_grid(self):
		if self.image_grid == None:
			print("Image not found\nAdd Image")
		else:
			for line in self.image_grid:
				print(line)

#static functions

def create_grid(working_image):

	grid = []
	with Image.open(working_image) as f:
		nr = 0
		while nr < f.size[1]:
			grid.append([])
			nr += 1
	return grid


"""
ImageObj = ImageFinder(workingImage)
ImageObj.create_imageGrid()
ImageObj.print_grid()
"""

