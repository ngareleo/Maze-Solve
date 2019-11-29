from PIL import Image ,ImageDraw
from  Analysis import parse_image_data,save_image_data
image = './Mazes/maze_solution_01.png'

with Image.open(image)as i:

    grid = parse_image_data(i)
    save_image_data(grid,i)
    i.convert("1").save('new_file.png')