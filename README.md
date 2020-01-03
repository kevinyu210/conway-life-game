# Conway's Game of Life

My implementation of Conway's Game Of Life using Python. This implementation has some basic functionalities that allow you to interact with the cells.

## How it works

### Game of Life rules

* Neighbor = Any of the 8 cells surrounding a single cell
* Any live cell with fewer than two live neighbours dies, as if by underpopulation.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by overpopulation.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

### Functionalities

* Play - Resumes activity of all cells
* Pause - Pauses activity of all cells
* Step - All cells enter next state in their lifecycle based on Conway logic
* Click - Click on screen to add more cells (Better to do this when game is paused)

## Getting Started

Instructions for getting a copy of this game running on your local machine

### Ingredients

* Python
* Python Tkinter module

### Instructions

First clone the repo by running this on your command line:
```
git clone https://github.com/kevinyu210/conway-life-game
```
Then enter the directory
```
cd conway-life-game
```
Finally, run:
```
python conway_main.py
```
or
```
python3 conway_main.py
```
