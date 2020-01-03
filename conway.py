import tkinter
import copy
from random import randint

class GameScreen():
    def __init__(self, gridWidth=60, gridHeight=60, cellSize=10):
        self.keepLiving = True
        # Spacing
        self.previousGameState = [[0 for i in range(gridHeight)] for j in range(gridWidth)]
        # randomX = randint(0, gridWidth)
        # randomY = randint(0, gridHeight)

        # self.previousGameState[randomX][randomY] = 1
        # self.previousGameState[randomX+1][randomY] = 1
        # self.previousGameState[randomX+1][randomY+1] = 1

        self.currentGameState = copy.deepcopy(self.previousGameState)
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.cellSize = cellSize
        self.gridPixelWidth = gridWidth * cellSize + gridWidth - 1
        self.gridPixelHeight = gridHeight * cellSize + gridHeight - 1
        self.root = tkinter.Tk()
        self.root.title("Connnnnnwaaaayyyyyyy")
        # -1 because tkinter adds an extra line on bottom and right edges
        self.mainCanvas = tkinter.Canvas(self.root, width = self.gridPixelWidth -1, height = self.gridPixelHeight -1, bg = "black")
        self.mainCanvas.pack()

    def clearAll(self):
        print("Clearing Canvas")
        self.mainCanvas.delete("all")

    def killCell(self, x, y):
        # print("Clear a single square/cell")
        topLeftCorner = (x * (self.cellSize +1), self.gridPixelHeight - (y+1) * (self.cellSize) -y)
        bottomRightCorner = (topLeftCorner[0]+self.cellSize, topLeftCorner[1] + self.cellSize)
        self.mainCanvas.create_rectangle(topLeftCorner[0],topLeftCorner[1], bottomRightCorner[0], bottomRightCorner[1], fill = "black")


    def birthCell(self,x,y):
        # print("Give birth to a single square/cell")
        topLeftCorner = (x * (self.cellSize +1), self.gridPixelHeight - (y+1) * (self.cellSize) -y)
        bottomRightCorner = (topLeftCorner[0]+self.cellSize, topLeftCorner[1] + self.cellSize)
        self.mainCanvas.create_rectangle(topLeftCorner[0],topLeftCorner[1], bottomRightCorner[0], bottomRightCorner[1], fill = "grey")

    def startLiving(self):
        self.keepLiving = True
        self.continueLiving()
    
    def continueLiving(self):
        if (self.keepLiving):
            self.step()
        self.mainCanvas.after(100, self.continueLiving)

    def step(self):
        for x in range(self.gridWidth):
            for y in range(self.gridHeight):
                neighborCount = 0
                # If not touching left wall
                if (x > 0):
                    # Neighbor on left
                    if (self.previousGameState[x-1][y]):
                        neighborCount +=1
                    # Neighbor on bottom left
                    if (y > 0 and self.previousGameState[x-1][y-1]):
                        neighborCount +=1
                    # Neighbor on top left 
                    if (y < self.gridHeight-1 and self.previousGameState[x-1][y+1]):
                        neighborCount +=1

                # If not touching right wall
                if (x < self.gridWidth-1):
                    # Neighbor on right
                    if (self.previousGameState[x+1][y]):
                        neighborCount +=1
                    # Neighbor on bottom right
                    if (y > 0 and self.previousGameState[x+1][y-1]):
                        neighborCount +=1
                    # Neighbor on top right
                    if (y < self.gridHeight-1 and self.previousGameState[x+1][y+1]):
                        neighborCount +=1

                if (y > 0 and self.previousGameState[x][y-1]):
                    neighborCount +=1
                if (y < self.gridHeight-1 and self.previousGameState[x][y+1]):
                    neighborCount +=1


                # Live Cell
                if (self.previousGameState[x][y]):
                    if (neighborCount < 2 or neighborCount > 3):
                        self.currentGameState[x][y] = 0
                        self.killCell(x,y)
                # Dead Cell
                else:
                    if (neighborCount == 3):
                        self.currentGameState[x][y] = 1
                        self.birthCell(x,y)

        # Instead of deep-copying, it would be easier to just update previousGameState individually. 
        self.previousGameState = copy.deepcopy(self.currentGameState)

        

    def pauseLiving(self):
        self.keepLiving = False

    def drawCurrentState(self):
        for x in range(self.gridWidth):
            for y in range(self.gridHeight):
                if (self.currentGameState[x][y]):
                    # self.mainCanvas.create_rectangle(topLeftCorner[0],topLeftCorner[1], bottomRightCorner[0], bottomRightCorner[1], fill = "grey")
                    self.birthCell(x,y)
                else:
                    self.killCell(x,y)
                    # self.mainCanvas.create_rectangle(topLeftCorner[0],topLeftCorner[1], bottomRightCorner[0], bottomRightCorner[1], fill = "black")

    def sampleDraw(self):
        self.drawCurrentState()

    def addCell(self, event):
        # if (event.x > self.gridPixelWidth or event.x < 0)
        xIndex = event.x//(self.cellSize+1)
        yIndex = (self.gridPixelHeight-event.y)//(self.cellSize+1)
        self.previousGameState[xIndex][yIndex] = 1
        self.currentGameState[xIndex][yIndex]=1
        self.birthCell(xIndex,yIndex)

if __name__ == "__main__":
    gameScreen = GameScreen()
    clearButton = tkinter.Button(gameScreen.root, text = "Clear", command = gameScreen.clearAll)
    stepButton = tkinter.Button(gameScreen.root, text = "Step", command = gameScreen.step)
    playButton = tkinter.Button(gameScreen.root, text = "Play", command = gameScreen.startLiving)
    pauseButton = tkinter.Button(gameScreen.root, text = "Pause", command = gameScreen.pauseLiving)
    sampleDrawButton = tkinter.Button(gameScreen.root, text = "Draw Current State", command = gameScreen.sampleDraw)
    stepButton.pack()
    playButton.pack()
    pauseButton.pack()
    sampleDrawButton.pack()
    # clearButton.pack()

    gameScreen.mainCanvas.bind("<Button-1>", gameScreen.addCell)

    gameScreen.root.mainloop()
    gameScreen.startLiving()
    
   