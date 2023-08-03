
# **Conway's Game of Life**

This is a simple, ground up implementation of Conway's Game of Life, which is a simple 
simulation that depicts "cells" that live or die based on how many neighbors they have as time progresses. 
 
The game can be fully described in a few short rules, however, surprisingly complex
behaviors can result, a phenomenon known as "emergent behavior."

A good place to start learning about the game is the [Wikipedia Page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life),
and there are many examples of impiementations online.

Other good introductory links:
 * [Guardian.com:the-game-of-life-a-beginners-guide](https://www.theguardian.com/science/alexs-adventures-in-numberland/2014/dec/15/the-game-of-life-a-beginners-guide)
 * [YouTube: epic conway's game of life](https://www.youtube.com/watch?v=C2vgICfQawE)

# Problem Statement (From Wikipedia)

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

**Evolution Rules**

  * Any live cell with two or three live neighbours survives.
  * Any dead cell with three live neighbours becomes a live cell.
  * All other live cells die in the next generation. Similarly, all other dead cells stay dead.

 **Other Requirements**
 
  * The initial pattern constitutes the seed of the system. 
  * The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick.
  * Each generation is a pure function of the preceding one.
  * The rules continue to be applied repeatedly to create further generations.


# Design Notes:
## Goals: 
 * Implement the Game of life 
 * Use a GUI (graphical programming environment), i.e. not some command line textual interface
 * Use a common, cross-platform language
 * Keep core logic separate from the UI.
 * Be able to save and load initial conditions to a file 
 
## Additional Specifications 
**These are additional specifications for my particular implementation of this problem.**

 * The program will be in one of two states or modes *"Initialization Mode"* or *"Run Mode**
 * Initially, the program will open in *"Initialization Mode"*, sized to a default size, 
 *  When the user clicks the  "Run" control the program switches to *"Run Mode"*
 *  If the number of cells goes to zero, or the stop button is clicked, the game returns to *"Initialization Mode"* 
 

**Main Window**
Program will open in a classic window, containing the following elements
* Program Title
* The game of life field, an array of boxes
* Basic Control elements to Run, Stop, Clear game field, quit the protram
* File Save Control Elements: Save, Load.
  
**Initialization Mode**

 * User can select the number of cells on screen, 
 * When user changes size or loads a file, the screen will redraw
 * User can click on any cell to toggle state "alive" (dark), or "dead" (light)
 * Initially all cells are light, except for perhaps a default pattern.
 * Status Fields:
   * Size of Grid
   * Number of cells alive
   * Iterations (seconds?)
   
**Run Mode**

 * When the system enters *"Run Mode"* the "Run" control legend changes to "Stop", and  the game begins iterating.
 * At each step a new status for each cell of the array is calculated based on the number of neighbors as given in rules. 
 * After the core logic updates the cells, each cell that changed will  be redrawn, and the statistics for number of live cells will be updated.
  
## File Save Format

I only needed a simple file format, and files are probably not very large.

JSON is a good choice because it is human readable and should be supportable without
issue in pretty much every modern language.

Therefore game save file will use a JSON file format, with the extension "json". 
Only the live cells will be saved. 

Sample File:
``` lang-json
    {
      "Description" : Default initial state"
      "width" : 220
      "height" : 100
      "liveCells" : [
        { 1, 1 }, 
        { 4, 5 }
      ]
    } 
```

# **Implementation Details**

**Python:**
  * See [Python/PythonDevnotes.md](Python/PythonDevNotes.md). Requires Python 3.10 or higher

   
# Attributions
## Images

**From the Wikipedia Page for Conway's Game of life:**
  
* Trefoil Knot GIF:  [By Raphael Augusto - Own work, CC BY-SA 4.0](https://commons.wikimedia.org/w/index.php?curid=52336285)
* Glider Cell Image: [Gospers Glider Gun](https://en.wikipedia.org/wiki/File:Game_of_life_glider_gun.svg)

## Graphics

  * I use [YEd](https://www.yworks.com/products/yed) to produce flowharts and other drawings

