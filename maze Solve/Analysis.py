from PIL import Image, ImageDraw
import sys
""""
PIL.ImageDraw.ImageDraw.line(xy, fill=None, width=0, joint=None)
Draws a line between the coordinates in the xy list.

Parameters:
xy – Sequence of either 2-tuples like [(x, y), (x, y), ...] or numeric values like [x, y, x, y, ...].
fill – Color to use for the line.
width –
The line width, in pixels.

New in version 1.1.5.

Note

This option was broken until version 1.1.6.

joint –
Joint type between a sequence of lines. It can be “curve”,
for rounded edges, or None.
New in version 5.3.0.

"""
# Solve maze and draw a red line of the maze solution path
sys.setrecursionlimit(10**9)
def look_left(grid,x,y,dir):
    #print("Looking left")
    #print(f"{grid[x][y+1]}")
    if grid[x][y - 1] == 1:
        #print("Found")
        dir.append([x,y-1])
def look_right(grid, x, y, dir):
    #print("Looking right")
    if grid[x][y + 1] == 1:
       # print("Found")
        dir.append([x, y + 1])
def look_up(grid, x, y, dir):
    #print("Looking up")
    if grid[x - 1][y] == 1:
        #print("Found")
        dir.append([x - 1, y])
def look_down(grid, x, y, dir):
    #print("Looking down")
    #print(f"{grid[x + 1][y]}")
    if grid[x + 1][y] == 1:
        #print("Found")
        dir.append([x + 1, y])

class node:

    loop_done = False
    def __init__(self, grid, current_pos, path_made, dead_end, children, end, mother = None,):
        self.current_pos = current_pos
        self.grid = grid
        self.path_made = path_made
        self.mother = mother
        self.children = children
        self.dead_end = bool(dead_end)
        self.end = end
        self.path_made.append(self.current_pos)


    def create_children(self,number,possiblities):

        for child in range(number):
            new_child = (node(
                mother=self,
                grid=self.grid,
                children=[],
                current_pos=[possiblities[child][0],possiblities[child][1]],
                path_made=[],
                dead_end=False,
                end = False
            ))
            self.children.append(new_child)
            print(f"Child created : Current pos {new_child.current_pos}")

    def look_around(self):
        current_posi = self.current_pos
        current_grid = self.grid
        x, y = current_posi[0], current_posi[1]
        directions = []
        # Sort corners and edges first
        if x == 0:
            if y == 0:
                look_right(current_grid,x,y,directions)
                look_down(current_grid, x, y, directions)
            elif y == -1:
                look_left(current_grid, x, y, directions)
                look_down(current_grid, x, y, directions)
            else:
                look_right(current_grid, x, y, directions)
                look_left(current_grid, x, y, directions)
                look_down(current_grid, x, y, directions)
        elif x == -1:
            if y == 0:
                look_up(current_grid, x, y, directions)
                look_right(current_grid, x, y, directions)
            elif y == -1:
                look_up(current_grid, x, y, directions)
                look_left(current_grid, x, y, directions)
            else:
                look_up(current_grid, x, y, directions)
                look_right(current_grid, x, y, directions)
                look_left(current_grid, x, y, directions)
        else:
            look_right(current_grid, x, y, directions)
            look_left(current_grid, x, y, directions)
            look_up(current_grid, x, y, directions)
            look_down(current_grid, x, y, directions)
        if len(self.path_made) == 0:
            pass
        else:
            for path in self.path_made:
                if path in directions:
                    directions.remove(path)
        if self.mother == None:
            pass
        else:
            for locals in self.mother.path_made:
                if locals in directions:
                    directions.remove(locals)
        print(f"Possiblitie are {directions}")
        return directions

    def move(self):
        if self.dead_end:
            self.stop_routine()
        elif self.end == True:
            pass
        else:
            possible_directions = self.look_around()
            if len(possible_directions) > 1:
                self.create_children(len(possible_directions), possible_directions)
                self.dead_end = True
                for child in self.children:
                    child.start_routine()
            elif len(possible_directions) == 0:
                self.dead_end = True
            else:
                self.current_pos = possible_directions[0]
                self.path_made.append(self.current_pos)
                print(f"Current pos: {self.current_pos}")
                print(f"Path made: {self.path_made}")

    def start_routine(self):
        while not node.loop_done and not self.dead_end:
            self.is_end()
            self.move()

    def stop_routine(self):
        pass

    def is_end(self):
        print("Look at end")
        if self.current_pos[0] == len(self.grid) - 1:
            if self.grid[-1][self.current_pos[1]] == 1:
                print("Found end")
                self.end = True
                for path in self.path_made:
                    correct_path.append(path)
                self.trace_path()

    def trace_path(self):
        starting_point = [0, find_points(self.grid, 0)]
        """
        me = self
        print("Tracing path")
        if not me.mother:
            node.loop_done = True
        else:
            if starting_point not in me.path_made:
                for path in me.path_made:
                    correct_path.append(path)
                me.mother.trace_path()
            else:
                for path in me.path_made:
                    correct_path.append(path)
                node.loop_done = True
        """
        mother = self.mother
        print("Tracing path")
        if not mother:
            node.loop_done = True
        else:
            if mother.path_made[0] is not starting_point:
                for path in mother.path_made:
                    correct_path.append(path)
                mother.trace_path()
            else:
                for path in mother.path_made:
                    correct_path.append(path)
                node.loop_done = True


def find_points(grid, row):
    for pix in grid[row]:
        if pix == 1:
            return grid[row].index(pix)

def parse_image_data(opened_image):

    grid = []
    for i in range(opened_image.size[1]):
        grid.append([])
    cc = 0
    data_list = list(opened_image.getdata())
    cr = 0
    while cc < len(data_list) and cr < opened_image.size[1]:
        for j in range(opened_image.size[0]):
            grid[cr].append(data_list[cc])
            cc += 1
        cr += 1
    return grid

def save_image_data(grid,f):
    with open('grid2.txt', 'w') as gt:
        dir_x = []
        for i in range(f.size[0]):
            dir_x.append(i % 10)
        gt.write(" \t" + str(dir_x) + "\n\n")
        for i in range(f.size[1]):
            gt.write(str(i) + "\t" + str(grid[i]) + "\n")

def run(main_image):
    with Image.open(main_image) as f:

        grid = parse_image_data(f)
        maze_node = node(grid=grid, current_pos=[0,find_points(grid,0)],path_made=[],children=[],dead_end=False,end = False)


        game_end = [-1,find_points(grid,-1)]
        print(grid[-1][31])
        maze_node.start_routine()
        print(sorted(correct_path))
        newImage = f.convert(mode='RGB')
        drawing_object = ImageDraw.Draw(newImage)

        for pix in sorted(correct_path):
            drawing_object.point([pix[1],pix[0]],fill=(255,0,0))
        newImage.save('solved_maze2.png')
        print(str(list(newImage.getdata())))


working_image = './Mazes/perfect2k_2.png'
correct_path = []

run(working_image)


