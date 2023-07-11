import sys
import tkinter as tk
from tkinter import ttk
from enum import Enum
from array import *

# ----------------------------------------------------------------------------------------
# Enums 
# ----------------------------------------------------------------------------------------

class CELL_STATE(Enum):
    DEAD = 0
    ALIVE = 1

class GAME_STATE(Enum):
   EMPTY = 0
   STOP = 1
   RUN = 2

#
# Colors found at http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
#
class COLORS(str, Enum):
    BACKGROUND = "Gainsboro"
    ALIVE = "SpringGreen3"
    DEAD = "gray93"

class CONSTANTS(Enum):
    CELL_SIZE = 20          # Gui Size of cells in pixels
    CELL_PADDING = 2        # Gui Padding around cells
    GAME_WIDTH = 48         # width of active (non-border) cells
    GAME_HEIGHT = 16        # height of active (non-border cells)
    FRAME_TIME_MS = 500     # (milliseconds)
    BORDER_CELLS = 1        # Number of non-active(clickable) cells around the border

# ----------------------------------------------------------------------------------------
# Cell Object represents a single square and is alive or dead 
# ----------------------------------------------------------------------------------------
class Cell:

    def updateCellState(self, cell):
        cell.state = cell.newState
        if (cell.state == CELL_STATE.ALIVE):
            cell.frame.config(bg=str(COLORS.ALIVE.value))
        elif cell.state == CELL_STATE.DEAD:
           cell.frame.config(bg=str(COLORS.DEAD.value))


    def onClick(self, event):
        # Event params: num=mouse button, x, y (within cell)
        # print(vars(event))
        # print ("/n")
        if (self.state == CELL_STATE.DEAD):
            self.state = CELL_STATE.ALIVE
            self.frame.config(bg=str(COLORS.ALIVE.value))
        else:
           self.state = CELL_STATE.DEAD
           self.frame.config(bg=str(COLORS.DEAD.value))
        # print (" (" + str(i) + "," + str(j) + ")/n")


    def __init__(self, parent, rowIdx, colIdx):
        self.state = CELL_STATE.DEAD
        self.newState = CELL_STATE.DEAD
        self.rowIdx = rowIdx
        self.colIdx = colIdx
        self.frame = tk.Frame(master=parent)
        self.frame.config(height=CONSTANTS.CELL_SIZE.value, width=CONSTANTS.CELL_SIZE.value)
        self.frame.config(bg=str(COLORS.DEAD.value))
        self.frame.bind("<Button-1>", self.onClick)
        self.frame.grid(row=rowIdx, column=colIdx, padx=CONSTANTS.CELL_PADDING.value, pady=CONSTANTS.CELL_PADDING.value)
        #print ("Created Cell [{:d},{:d}]".format(rowIdx, colIdx))

def main():
    gol = GameOfLifeApp()
    gol.window.mainloop()
        

# ----------------------------------------------------------------------------------------
# Main App Class: Game of Life App 
# ----------------------------------------------------------------------------------------
class GameOfLifeApp:

    # Main Algorithmic decision
    # 1. Any live cell with two or three live neighbours survives.
    # 2. Any dead cell with three live neighbours becomes a live cell.
    # 3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    def doesCellLive(self, cell, neighborCount):
        result = True
        if cell.state == CELL_STATE.ALIVE and neighborCount >= 2 and neighborCount <=3: 
                result = True
        elif cell.state == CELL_STATE.DEAD and neighborCount == 3:
                result = True
        else:
            result = False
        #print ("Cell {:>02d},{:>02d}] lives is {})".format(i, j, str(result))
        return result

    def getCell(self, i, j):
        return self.cells[ i ][ j ]

    def initCells(self):
        return [[Cell(self.frameGame, i, j) for j in range(self.cellWidth)] for i in range(self.cellHeight)]

    #
    # updateAllCells - goes through array and updates cell states
    #
    # note that we skip values around the edges so that we always have eight neighbors
    #
    def updateAllCells(self):

        # first pass: populate newStates
        for i in range(0, self.cellHeight):
            for j in range(0, self.cellWidth):
                neighborCount = 0
                curCell = self.getCell(i, j)
                for rowAdj in range(-1, 2):
                    for colAdj in range(-1,2):
                        # skip ourselves
                        if rowAdj == 0 and colAdj == 0:
                            continue
                        # skip indexes that are outside of array bounds
                        if i+rowAdj < 0 or i+rowAdj >= self.cellHeight or \
                           j+colAdj < 0 or j+colAdj >= self.cellWidth:
                            continue

                        neighborCell = self.getCell(i+rowAdj, j+colAdj)
                        if neighborCell.state == CELL_STATE.ALIVE:
                            neighborCount += 1
                            #print ("Neighbor Cell[{:>02d},{:>02d}] is {:s}".format(i+rowAdj,j+colAdj,neighborCell.state.name))

                #print ("cell[{:>02d},{:>02d}], id {:s} neighborCount = {:d}\n".format(i,j,curCell.state.name,neighborCount))
                if (self.doesCellLive(curCell, neighborCount)):
                    curCell.newState = CELL_STATE.ALIVE
                else:
                    curCell.newState = CELL_STATE.DEAD

        # second pass: update cell states        
        for i in range(0, self.cellHeight):
            for j in range(0, self.cellWidth):
                curCell = self.getCell(i, j)
                curCell.updateCellState(curCell)

    #
    # This is timer tick, happens once per second
    #
    # parameters: 
    #    self = GameApp object
    #    lblTime = tkinter button showing current time
    #    keepRunning = Boolean (True to keep running, false to single step)
    #
    def updateTime(self, lblTime):
        #print(vars(self))
        #print("\n")
        #print(self.gameState.name)              # OK
        #print("ut: # {}".format(self.counter))  # OK
        self.counter += 1
        mins,seconds = divmod(self.counter, 60)
        lblTime.config(text="{:0>2d}:{:0>2d}".format(mins,seconds))

        self.updateAllCells()
        if (self.gameState == GAME_STATE.RUN):
            self.window.after(CONSTANTS.FRAME_TIME_MS.value, self.updateTime, self.lblTime)

    # stepTime function single steps game
    def stepTime(self, gameState, increment):
        if increment == 0:
            return
        match gameState:
            case GAME_STATE.EMPTY:
                pass
            case GAME_STATE.STOP:
                self.counter += increment
                self.updateTime(self.lblTime)
            case GAME_STATE.RUN:
                pass
            case _:
                pass

    def clear(self):
        for i in range(0, self.cellHeight):
            for j in range(0, self.cellWidth):
                self.cells[i][j].newState = CELL_STATE.DEAD
                curCell = self.getCell(i, j)
                curCell.updateCellState(curCell)

    def toggleRunButton(self, gameState, button):
        match gameState:
            case GAME_STATE.EMPTY:
                pass
            case GAME_STATE.STOP:
                button.config(text = "Stop")
                self.counter = 0
                self.gameState = GAME_STATE.RUN    
                self.updateTime(self.lblTime)
            case GAME_STATE.RUN:
                button.config(text = "Run")
                self.btnRun.config(text="Run")
                self.gameState = GAME_STATE.STOP
            case _:
                self.gameState = GAME_STATE.EMPTY
        #print ("trb:" + gameState.name + " " + button.cget('text'))

    def __init__(self):
        self.gameState = GAME_STATE.STOP
        self.counter = 0
        self.cellHeight = CONSTANTS.GAME_HEIGHT.value + CONSTANTS.BORDER_CELLS.value*2
        self.cellWidth = CONSTANTS.GAME_WIDTH.value + CONSTANTS.BORDER_CELLS.value*2
        self.cellSize = CONSTANTS.CELL_SIZE.value

        print("================ Conway's Game of Life by Steve Schilz ===================")
        print("Python Version {:s}".format(sys.version))
        print(sys.version_info)
        print("TKInter Versions {:.1f} {:.1f} ".format(tk.TclVersion,tk.TkVersion))
        print("Game State: " + self.gameState.name)
        print("Game Size:  (" + str(self.cellWidth) + "," + str(self.cellHeight) + ")")

        # Main Window                
        self.window = tk.Tk()
        self.window.title("Conway's Game of Life")
        

        # Top of screen: Two Images
        self.imgLogo = tk.PhotoImage(file="../Images/Trefoil_knot_conways_game_of_life.gif").zoom(x=1)
        self.lblLogo = tk.Label(self.window, image=self.imgLogo)
        self.lblLogo.grid(row=0, column=0)
        self.imgLogo2 = tk.PhotoImage(file="../Images/gameOfLife.png").zoom(x=1)
        self.lblLogo2 = tk.Label(self.window, image=self.imgLogo2)
        self.lblLogo2.grid(row=0, column=1, columnspan=4)
        
        # Create Game Frame
        self.frameGame=tk.Frame(master=self.window)
        self.frameGame.config(height=self.cellHeight*self.cellSize, width=self.cellWidth*self.cellSize)
        self.frameGame.config(bg="gainsboro")
        self.frameGame.grid(row=1, column=0, columnspan=5, padx=1, pady=1) 

        # Fill in the game board
        self.cells = self.initCells()
        
        # Bottom = Controls and Buttons
        self.lblTime = tk.Label(self.window, text = "0:00")
        self.lblTime.grid(row=2, column=0)
        
        self.btnRun = tk.Button(self.window, text="Run")
        self.btnRun.config(command=lambda:self.toggleRunButton(self.gameState, self.btnRun))
        self.btnRun.grid(row=2, column=1)

        self.btnStepFwd = ttk.Button(self.window, text = "Step")
        self.btnStepFwd.config(command=lambda:self.stepTime(self.gameState, +1))
        self.btnStepFwd.grid(row=2, column=2)

        self.btnClear = ttk.Button(self.window, text = "Clear")
        self.btnClear.config(command=lambda:self.clear())
        self.btnClear.grid(row=2, column=3)

        self.btnQuit = tk.Button(self.window, text = "quit()", command=quit, fg="red")
        self.btnQuit.grid(row=2, column=4)

        
        
if __name__ == "__main__":
    main()
    