# Introduction

### What is python?
![python icon](https://realpython.com/learn/python-first-steps/images/pythonlogo.jpg)

1. Multi-purpose (Web, Robotics, Data Analysis, Machine Learning, Web Crawler, etc.)
2. Object Oriented
3. Interpreted language (C, C++ and Java are compiled language).
4. Focus on readability and efficiency

### Installation
Please download and install the latest python version (3.6.0) at https://www.python.org/downloads/

On Windows machines, the Python installation is usually placed in C:\Python36, though you can change this when you’re running the installer. To add this directory to your path, you can type the following command into the command prompt in a DOS box:
```
set path=%path%;C:\python36
```

Download a text editor or IDE to write python scripts. I would recommand sublime text, a popular choice for python editor. You may download it at https://www.sublimetext.com/3

### How to use python

There are two ways to use python: using the python interpreter or running the python scripts (*.py files).

##### To invoke the interpreter, type the "python" in your command prompt/terminal.

##### To run the python script, use the following command in your command prompt/terminal:
```
python your-script-name.py
```

### Syntax
1. Beginning with python
2. String and list
3. Dictionary and set
4. Flow control
5. Method
6. Module

### Exercise: sudoku generator

![sudoku board](https://upload.wikimedia.org/wikipedia/commons/f/ff/Sudoku-by-L2G-20050714.svg)

Rules: http://www.counton.org/sudoku/rules-of-sudoku.php

The program will first print the partially filled sudoku board, and then print out the answer after the user presses any key.

#### Your task:
- Complete the attempt_board method.
- The attempt_board method should try to fill up the 9*9 list which represent the board.
- Make use of the random module to make sure the numbers are placed randomly.
- The method attempt_board should return None if it fails to generate the puzzle. (generate_board will keep calling attempt_board until it generates a valid board).
