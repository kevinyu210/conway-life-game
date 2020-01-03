import tkinter
import copy
from conway_gui import GameScreen

if __name__ == "__main__":
    game_screen = GameScreen()
    game_screen.main_canvas.bind("<Button-1>", game_screen.click_cell)
    game_screen.root.mainloop()
    game_screen.start_living()