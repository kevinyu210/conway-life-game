import copy
try:
    import tkinter
except ImportError:
    import Tkinter

class GameScreen():
    def __init__(self, grid_width=60, grid_height=60, cell_size=10):
        self.keep_living = False
        # Initialize empty game state
        self.previous_state = [[0 for i in range(grid_height)] for j in range(grid_width)]
        self.current_state = copy.deepcopy(self.previous_state)
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size
        self.grid_pixel_width = grid_width * cell_size + grid_width - 1
        self.grid_pixel_height = grid_height * cell_size + grid_height - 1
        # Initialize tkinter interface
        self.root = tkinter.Tk()
        self.root.title("CONWAY")
        # -1 because tkinter adds an extra line on bottom and right edges
        self.main_canvas = tkinter.Canvas(self.root, width = self.grid_pixel_width -1, height = self.grid_pixel_height -1, bg = "black")
        self.main_canvas.pack()
        # Initialize buttons
        step_button = tkinter.Button(self.root, text = "Step", command = self.step)
        play_button = tkinter.Button(self.root, text = "Play", command = self.start_living)
        pause_button = tkinter.Button(self.root, text = "Pause", command = self.pause_living)
        play_button.pack()
        pause_button.pack()
        step_button.pack()
    
    def get_neighbor_count(self, x, y):
        neighborCount = 0
        # If not touching left wall
        if (x > 0):
            # Neighbor on left
            if (self.previous_state[x-1][y]):
                neighborCount +=1
            # Neighbor on bottom left
            if (y > 0 and self.previous_state[x-1][y-1]):
                neighborCount +=1
            # Neighbor on top left 
            if (y < self.grid_height-1 and self.previous_state[x-1][y+1]):
                neighborCount +=1

        # If not touching right wall
        if (x < self.grid_width-1):
            # Neighbor on right
            if (self.previous_state[x+1][y]):
                neighborCount +=1
            # Neighbor on bottom right
            if (y > 0 and self.previous_state[x+1][y-1]):
                neighborCount +=1
            # Neighbor on top right
            if (y < self.grid_height-1 and self.previous_state[x+1][y+1]):
                neighborCount +=1

        # Neighbor on bottom
        if (y > 0 and self.previous_state[x][y-1]):
            neighborCount +=1

        # Neighbor on top
        if (y < self.grid_height-1 and self.previous_state[x][y+1]):
            neighborCount +=1

        return neighborCount

    def step(self):
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                neighborCount = self.get_neighbor_count(x,y)
                # Live Cell
                if (self.previous_state[x][y]):
                    if (neighborCount < 2 or neighborCount > 3):
                        self.current_state[x][y] = 0

                # Dead Cell
                else:
                    if (neighborCount == 3):
                        self.current_state[x][y] = 1

        self.draw_current_state()
        self.previous_state = copy.deepcopy(self.current_state)

    def pause_living(self):
        self.keep_living = False

    def start_living(self):
        if (not self.keep_living):
            self.keep_living = True
            self.continue_living()
    
    def continue_living(self):
        if (self.keep_living):
            self.step()
        else:
            return
        self.main_canvas.after(50, self.continue_living)

    def draw_current_state(self):
        self.clear_canvas()
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if (self.current_state[x][y]):
                    self.birth_cell(x,y)
    
    def clear_canvas(self):
        self.main_canvas.delete("all")

    def kill_cell(self, x, y):
        top_left_corner = (x * (self.cell_size + 1), self.grid_pixel_height - (y + 1) * (self.cell_size) -y)
        bottom_right_corner = (top_left_corner[0] + self.cell_size, top_left_corner[1] + self.cell_size)
        self.main_canvas.create_rectangle(top_left_corner[0],top_left_corner[1], bottom_right_corner[0], bottom_right_corner[1], fill = "black")

    def birth_cell(self,x,y):
        top_left_corner = (x * (self.cell_size +1), self.grid_pixel_height - (y+1) * (self.cell_size) -y)
        bottom_right_corner = (top_left_corner[0] + self.cell_size, top_left_corner[1] + self.cell_size)
        self.main_canvas.create_rectangle(top_left_corner[0],top_left_corner[1], bottom_right_corner[0], bottom_right_corner[1], fill = "grey")

    def click_cell(self, event):
        x = event.x//(self.cell_size+1)
        y = (self.grid_pixel_height-event.y)//(self.cell_size+1)
        if (self.previous_state[x][y]):
            self.previous_state[x][y] = 0
            self.current_state[x][y]=0
            self.kill_cell(x,y)
        else:
            self.previous_state[x][y] = 1
            self.current_state[x][y]=1
            self.birth_cell(x,y)