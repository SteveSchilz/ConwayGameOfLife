This document describes choices made and problems solved in the Python implementation 
of Conway's Game of Life.  This was my first implementation of the game, and I chose
Python because it's a popular, widely available scripting language, 
that I have some familiarity but not really a lot of experience.



# Toolkit
I have very limited experience in Python, so I'm starting from scratch here. 
However, my experience in other languages guides me as to what to ask, and I
arrived at the following selections fairly rapidly

 * Coding Language Python (3.8.5)
 * GUI Toolkit [tkinter](https://docs.python.org/3/library/tkinter.html#)
 * File Format: [JSON](https://www.w3schools.com/js/js_json_intro.asp), [GeeksForGeek-Reading and Writing JSON in python](https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/)


## **Gui Toolkit Selection** 
I knew I wanted some clickable main area, and since I'm initially writing on a desktop,
I thought a standard main window type thing would be good. A mobile interface might be 
fun too, but, programming is still a desktop-first activity.  Sooo. 

I googled "Python Main Window with clickable main window Hello world", and found 
this description of [PySimpleGui](https://realpython.com/pysimplegui-python/) on the 
RealPython website.  There, they discuss four available toolkits, and state that the 
[TKinter]() toolkit is the most common and built in, although maybe not the easiest. 


## **GUI implementation**
Created hello world by following this [Python GUI: Build your first application using TKInter](https://www.simplilearn.com/tutorials/python-tutorial/python-graphical-user-interface-gui)
I Choose "grid" layout manager:   There are 3 layout managers: auto-layout: pack(), pixel based: place(x=10,y=10), and grid(row=0, column=1)

Overall implementation was pretty straightforward, and took about 1 day of work, despite me having to 
look up EVERYTHING, such as "GUI Hello World", "Python Avoid Globals", "Object oriented python", 
"tkinter frames", avoiding globals, how to use ENUMs, string formatting, loops, etc. etc 


# Problems encountered and solved:
  * Was not running from command line (bcause it exited). added window.mainloop(), based on [StackOverflow: tkinter not working from command line script](https://stackoverflow.com/questions/57399880/tkinter-not-working-when-run-from-command-line-python-script) 
  * Gui Structure (wrap in App function, create self) [Runestone Academy: GUI Program Structure](https://runestone.academy/ns/books/published/thinkcspy/GUIandEventDrivenProgramming/08_gui_program_structure.html)
  * Implemented color screen using an emum to choose colors found at:  [Wellesley tkinter colors](http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html)
  * *Avoid Null Objects* - appending .grid(row,col) to object definition results in a null object, because .grid() returns 0. This caused me a bunch of pain.
  * Timer object: Cribbed from examples [here](https://stackoverflow.com/questions/55881099/how-do-i-start-a-timer-when-i-click-on-an-entry-widget), [here](https://thinkinfi.com/how-to-make-a-stopwatch-gui-in-python-tkinter/), and [stackOverflow tkinter use after method](https://stackoverflow.com/questions/25753632/tkinter-how-to-use-after-method)
 


## **File Format**
I only needed a simple file format, and files are probably not very large.  A bit of 
googling shows that the common "JSON" format is natively supported in Python. 
Easy peasy. 

