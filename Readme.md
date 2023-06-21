
**Conway's Game of Life** 
This is a simple, ground up implementation of Conway's Game of Life, which is a simple 
simulation that depicts "cells" that live or die based on how many neighbors they have as time progresses. 
 
The game can be fully described in a few short rules, however, surprisingly complex
behaviors can result, a phenomenon known as "emergent behavior."

A good place to start learning about the game is the [Wikipedia Page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life),
and there are many examples online. Other good links:
 * [Guardian.com:the-game-of-life-a-beginners-guide](https://www.theguardian.com/science/alexs-adventures-in-numberland/2014/dec/15/the-game-of-life-a-beginners-guide)
 

I am interested in comparing the effort it takes to create Conway's game of Life
from first principles, vs using a chatbot environment to get the game up and 
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


# Design Notes:
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
 
 
## Game Of Life Calculations 
The game basically requires running a live/die function for each cell based on what it's 
neighbors are. This will require the following steps

```
    For (each cell not in row/col 0 or last row col)
         generate count of number of living neighbors from the nearest 8 neigbhors
         calculate new status using game rules
         update cell state
```

Because the array is described as infinite, we use the outside ring as a non-displayed
boundary area, This implies that the size of the array is actually Width+2, Height+2. 
Also note that this means the actie cells are from [1..GameHeight, 1..GameWidth]

 
## *File Save Format
I only needed a simple file format, and files are probably not very large.  . 
JSON is a good choice because it is human readable and should be supportable without
issue in pretty much every modern language.

Therefor game save file will use a JSON file format, with the extension "json". 
Only the live cells will be saved. 

Sample File:
    {
      "Description" : Default initial state"
      "width" : 220
      "height" : 100
      "liveCells" : [
        { 1, 1 }, 
        { 4, 5 }
      ]
    } 


# Implementation Details* 

  * Python: See [Python/PythonDevnotes.md](Python/PythonDevNotes.md). Requires Python 3.10 or higher

   
# Attributions

## Images
  ** From the Wikipedia Page for Conway's Game of life:*
    * Trefoil Knot GIF:  By Raphaelaugusto - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=52336285
    * Glider Cell Image: 

## Graphics
  * I use [YEd](https://www.yworks.com/products/yed) to produce flowharts and other drawings
