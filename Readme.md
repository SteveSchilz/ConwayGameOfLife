
**Conway's Game of Life** is is a simple simulation that depicts "cells" that live or die
based on how many neighbors they have as time progresses. 
 
The game can be fully described in a few short rules, however, surprisingly complex
behaviors can result, a phenomenon known as "emergent behavior."

A good place to start learning about the game is the [Wikipedia Page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life),
and there are many examples online. Other good links:
 * [Guardian.com:the-game-of-life-a-beginners-guide](https://www.theguardian.com/science/alexs-adventures-in-numberland/2014/dec/15/the-game-of-life-a-beginners-guide)
 

I am interested in comparing the effort it takes to create Conway's game of Life
from first principles, vs using a chatbot envirionment to get the game up and 
running. 

#Rules (From Wikipedia)
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

  * Any live cell with fewer than two live neighbours dies, as if by underpopulation.
  * Any live cell with two or three live neighbours lives on to the next generation.
  * Any live cell with more than three live neighbours dies, as if by overpopulation.
  * Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behaviour of the automaton to real life, can be condensed into the following:

  * Any live cell with two or three live neighbours survives.
  * Any dead cell with three live neighbours becomes a live cell.
  * All other live cells die in the next generation. Similarly, all other dead cells stay dead.
  
The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick.[nb 1] Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.


# Design:
Requirements: 
 * want a graphical programming environment in a common, cross-platform language
 * Implement the Game of life 
 * Keep core logic separate from the UI.
 * Be able to save and load initial conditions to a file 
 
# Behavior 
 Initially, the program will open in "initialization mode", sized to a default size, 
 perhaps occupying 75% of the screen real estate. 

*Main Display*
Program will open in a classic window, with "File" and "Run" menus
Main window of screen will contain the game of life field, an array of boxes
Buttons, perhaps in a control bar at the bottom are available to control 

*Initialization Mode*
 * User can select the number of cells on screen, 
 * when user changes size or loads a file, the screen will redraw
 * There is a file menu with "save" and "load" buttons.  
 * user can click on any cell to toggle state "alive" (dark), or "dead" (light)
 * Initially all cells are light, except for perhaps a default pattern.
 * There is a "Run" button
 * Status Fields:
   * Size of Grid
   * Number of cells alive
   * Iterations (seconds?)
   
*Run Mode*
 When the user clicks "Run", the "Run" buttion function changes to "Stop", and 
 the game begins iterating. At each step a new status for each cell of the array
 is calculated based on the number of neighbors as given in rules. 
 
 After the core logic updates the cells, each cell that changed will 
 be redrawn, and the statistics for number of cells will be updated.
 If the number of cells goes to zero, or the stop button is clicked, the 
 game returns to the initialization mode. 
 
# Implementation Details* 

 
## GUI implementation
Created hello world by following this [Python GUI: Build your first application using TKInter](https://www.simplilearn.com/tutorials/python-tutorial/python-graphical-user-interface-gui)
I Choose "grid" layout manager:   There are 3 layout managers: auto-layout: pack(), pixel based: place(x=10,y=10), and grid(row=0, column=1)

Overall implementation was pretty straightforward, and took about 1 day of work, despite me having to 
look up EVERYTHING, such as "GUI Hello World", "Python Avoid Globals", "Object oriented python", 
"tkinter frames", avoiding globals, how to use ENUMs, string formatting, loops, etc. etc 


Problems encountered and solved:
  * Was not running from command line (bcause it exited). added window.mainloop(), based on [StackOverflow: tkinter not working from command line script](https://stackoverflow.com/questions/57399880/tkinter-not-working-when-run-from-command-line-python-script) 
  * Gui Structure (wrap in App function, create self) [Runestone Academy: GUI Program Structure](https://runestone.academy/ns/books/published/thinkcspy/GUIandEventDrivenProgramming/08_gui_program_structure.html)
  * Implemented color screen using an emum to choose colors found at:  [Wellesley tkinter colors](http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html)
  * *Avoid Null Objects* - appending .grid(row,col) to object definition results in a null object, because .grid() returns 0. This caused me a bunch of pain.
  * Timer object: Cribbed from examples [here](https://stackoverflow.com/questions/55881099/how-do-i-start-a-timer-when-i-click-on-an-entry-widget), [here](https://thinkinfi.com/how-to-make-a-stopwatch-gui-in-python-tkinter/), and [stackOverflow tkinter use after method](https://stackoverflow.com/questions/25753632/tkinter-how-to-use-after-method)
 
## Game Of Life Engine
The game basically requires running a live/die function for each cell based on what it's 
neighbors are. This will require the following steps

```
    For (each cell not in row/col 0 or last row col)
         generate count of number of living neighbors from the nearest 8 neigbhors
         calculate new status using game rules
         update cell state
```

Because the array is described as infinite, we use the outside ring as a non-displayed
boundary area, This implies that the size of the array is actually Width+2, Height+2

 
## *File Save Data*
File will use a JSON file format, with the extension "json". 
Only the live cells will be saved. 
{
  "Description" : Default initial state"
  "width" : 220
  "height" : 100
  "liveCells" : [
    { 1, 1 }, 
    { 4, 5 }
  ]
} 


# Tools and Languages
I have very limited experience in Python, so I'm starting from scratch here. 
However, my experience in other languages guides me as to what to ask, and I
arrived at the following selections fairly rapidly

 * Coding Language Python (3.8.5)
 * GUI Toolkit [tkinter](https://docs.python.org/3/library/tkinter.html#)
 * Graphics: [YEd](https://www.yworks.com/products/yed)
 * File Format: [JSON](https://www.w3schools.com/js/js_json_intro.asp), [GeeksForGeek-Reading and Writing JSON in python](https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/)


## **Language:** I selected Python, because it's a popular, widely available scripting language, 
that I have some familiarity but not really a lot of experience.


## **Gui Toolkit** 
I knew I wanted some clickable main area, and since I'm initially writing on a desktop,
I thought a standard main window type thing would be good. A mobile interface might be 
fun too, but, programming is still a desktop-first activity.  Sooo. 

I googled "Python Main Window with clickable main window Hello world", and found 
this description of [PySimpleGui](https://realpython.com/pysimplegui-python/) on the 
RealPython website.  There, they discuss four available toolkits, and state that the 
[TKinter]() toolkit is the most common and built in, although maybe not the easiest. 

**File Format**
I only needed a simple file format, and files are probably not very large.  A bit of 
googling shows that the common "JSON" format is natively supported in Python. 
Easy peasy. 

   
# Attributions 

## Images
  ** From the Wikipedia Page for Conway's Game of life:*
    * Trefoil Knot GIF:  By Raphaelaugusto - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=52336285
    * Glider Cell Image: 


# Todo List

  * **DONE** Basic Graphics Layout*
  * **DONE** Time Runs/Stops
  * **DONE** Basic Game Engine Working
  * Add File Save/Load Features (main menu? or more buttons?)
  * Add Reset to last initial conditions button (Special save to hidden file?) 
  * Hide border row/columns, avoid click there. (Diff Size? Set color to be a frame? THey do participate in game though)
  * Add the ability to set Game Board Size (to 100x100?)
  * Clean up print statements (consider using debugPrint() with print debug flag or log file?)*
  * Instructions
     * Add Instructions (Modify Bigger picture to include Title and "click for instructions label")
     * Add Short readme with instructions, link to Wiki Page
     * Make the Trefoil knot animate? 
  * Move lot of readme to "Python/Devnotes.md", simplify readme.
  * Consider Rearchitecting class structure to further separate Game Engine and UI.
  * Time: Add description label, extend digits to DD:HH:MM:SS 
  * Count: Add count of live cells, terminate game if it goes to zero
  * Redo layout using pack? 
  * Add Responsiveness to resizing window*
  * Save/Restore Window Position (multimonitor separate), and game board size between runs
  * Add toolbar with ability to drag common shapes onto the board (load subset of array)

  * Add Drag to draw? 
  * Keyboard Control? 