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
    CELL_SIZE = 20
    CELL_PADDING = 2
    GAME_WIDTH = 48
    GAME_HEIGHT = 16
    FRAME_TIME = 1 # (seconds)    
    
# ----------------------------------------------------------------------------------------
# Cell Object represents a single square and is alive or dead 
# ----------------------------------------------------------------------------------------
class Cell:
    def onClick(self, event):
        # Event params: num=mouse button, x, y (within cell)
        #print(event)
        if (self.state == CELL_STATE.DEAD):
            self.state = CELL_STATE.ALIVE
            self.frame.config(bg=str(COLORS.ALIVE.value))
        else:
           self.state = CELL_STATE.DEAD
           self.frame.config(bg=str(COLORS.DEAD.value))

        #print (" (" + str(i) + "," + str(j) + ")/n")

    def __init__(self, parent, rowIdx, colIdx):
        self.state = CELL_STATE.DEAD
        self.rowIdx = rowIdx
        self.colIdx = colIdx
        self.frame = tk.Frame(master=parent)
        self.frame.config(height=CONSTANTS.CELL_SIZE.value, width=CONSTANTS.CELL_SIZE.value)
        self.frame.config(bg=str(COLORS.DEAD.value))
        self.frame.bind("<Button-1>", self.onClick)
        self.frame.grid(row=rowIdx, column=colIdx, padx=CONSTANTS.CELL_PADDING.value, pady=CONSTANTS.CELL_PADDING.value)
        
           
def main():
    gol = GameOfLifeApp()
    gol.window.mainloop()
        

# ----------------------------------------------------------------------------------------
# Main App Class: Game of Life App 
# ----------------------------------------------------------------------------------------
class GameOfLifeApp:

    def updateTime(self, lblTime):
        #print(self.gameState.name)      #   OK
        print("ut: # {}".format(self.counter))
        if (self.gameState == GAME_STATE.RUN):
            self.counter = self.counter + 1
            mins,seconds = divmod(self.counter, 60)
            print(mins)
            print(seconds)
            self.lblTime.config(text="{}:{}".format(mins,seconds))
#            self.lblTime.after(50, self.updateTime(self.lblTime))

    # TODO: try to use parameters, so I don't have to reference self.objects
    #       when I tried, I could update locally, but doesn't propagate back.
    #       seems to work with the "counter_label", for some reason.
    def toggleRunButton(self, gameState, button):
        print ("trb:" + gameState.name + " " + button.cget('text'))
        match gameState:
            case GAME_STATE.EMPTY:
                print ("Empty")
            case GAME_STATE.STOP:
                self.btnRun.config(text="Stop")
                self.gameState = GAME_STATE.RUN
                print(self.lblTime.cget('text'))
                self.updateTime(self.lblTime)
            case GAME_STATE.RUN:
                self.btnRun.config(text="Run")
                self.gameState = GAME_STATE.STOP
            case _:
                print ("Impossible")
                self.gameState = GAME_STATE.EMPTY
        print("locals state=" + gameState.name + " button = " + button.cget('text'))
        print("self state  =" + self.gameState.name + " button = " + self.btnRun.cget('text'))

    def counter_label(self,label):
        def count():
            self.counter += 1
            label.config(text=str(self.counter))
            label.after(1000, count)
        count() 

    def __init__(self):
        self.gameState = GAME_STATE.STOP
        self.counter = 0
        self.height = CONSTANTS.GAME_HEIGHT.value
        self.width = CONSTANTS.GAME_WIDTH.value
        self.cellSize = CONSTANTS.CELL_SIZE.value

        # Main Window                
        self.window = tk.Tk()
        self.window.title("Conway's Game of Life")
        print("TKInter Versions {:.1f} {:.1f} ".format(tk.TclVersion,tk.TkVersion))
        print("Game State: " + self.gameState.name)
        print("Game Size:  (" + str(self.width) + "," + str(self.height) + ")")

        # Top of screen: Two Images
        self.imgLogo = tk.PhotoImage(file="../Images/Trefoil_knot_conways_game_of_life.gif").zoom(x=1)
        self.lblLogo = tk.Label(self.window, image=self.imgLogo).grid(row=0, column=0)
        self.imgLogo2 = tk.PhotoImage(file="../Images/gameOfLife.png").zoom(x=1)
        self.lblLogo2 = tk.Label(self.window, image=self.imgLogo2).grid(row=0, column=1)
        
        # Create Game Frame
        self.frameGame=tk.Frame(master=self.window)
        self.frameGame.config(height=self.height*self.cellSize, width=self.width*self.cellSize)
        self.frameGame.config(bg="gainsboro")
        self.frameGame.grid(row=1, column=0, columnspan=5, padx=1, pady=1) 

        # Fill in the game board
        self.cells = [[]]
        for i in range(0, self.height+1):
            for j in range(0, self.width+1):
                self.cells.insert(i*self.height+j, Cell(self.frameGame, i, j))    
                #print ("(" + str(i) + "," + str(j) +")")                
            #print ("/n")

        # Bottom = Controls and Buttons
        self.lblTime = tk.Label(self.window, text = "0:00")
        self.lblTime.grid(row=2, column=0)

        self.lblCounter = tk.Label(self.window, fg="dark green")
        self.counter_label(self.lblCounter)
        self.lblCounter.grid(row=2, column=1)
        
        self.btnRun = tk.Button(self.window, text="Run") #,command=toggleRunButton)
        self.btnRun.config(command=lambda:self.toggleRunButton(self.gameState, self.btnRun))
        self.btnRun.grid(row=2, column=2)
        
        self.btnQuit = tk.Button(self.window, text = "quit()", command=quit, fg="red").grid(row=2, column=3)
        
if __name__ == "__main__":
    main()
    