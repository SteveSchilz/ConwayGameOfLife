
Conway's game of life is is a simple simulation that depicts "cells" that live or die
based on how many neighbors they have as time progresses. 
 
The game can be fully described in a few short rules, however, surprisingly complex
behaviors can result, a phenomenon known as "emergent behavior."

A good place to start learning about the game is the [Wikipedia Page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life),
and there are many examples online. 

I am interested in comparing the effort it takes to create Conway's game of Life
from first principles, vs using a chatbot envirionment to get the game up and 
running. 

#Rules (From Wikipedia)
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.

Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
These rules, which compare the behaviour of the automaton to real life, can be condensed into the following:

Any live cell with two or three live neighbours survives.
Any dead cell with three live neighbours becomes a live cell.
All other live cells die in the next generation. Similarly, all other dead cells stay dead.
The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick.[nb 1] Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.


Design:
This 