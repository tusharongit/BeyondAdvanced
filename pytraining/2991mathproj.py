"""
Write a new top-level module which asks the user for a 'project title', a 'number range (min/max)' and a 'mathematical technique (sum, mean, squares)'

Import the 'sanitize' module and use it to make sure the 'project title' is a title-case string

Also ensure the min and max values are cast as integers and the chosen technique matches one of the options (sum, mean or squares)

Write other modules to contain the functions which will:
- generate a range of numbers, given min and max
- return the mean of those numbers
- return a tuple of the squares of those numbers

Use your existing 'addStuff' method to return the sum of the range of numbers

Make use of imports for your new modules so they can be used to implement the chosen mathematical technique upon the range the user asked for

Write brief descriptive docstrings for each of your functions

Consider using if __name__ == '__main__': to write code-exercising lines within your new sub modules

Optional
--------
Find a way to ask for a 'step' value for the range, with a default of 1
Let the user provide more than one technique, so they might want both sum and mean 
Let the user choose what power (rather than just 'squares')
Find a way to chain operations, so they might find powers of 3 then sum those results and then find the mean
Write a function which will become a decorator for other functions.
  The purpose of this new function is to make all the parametes into integers, or else ignore them
  Apply this function as a decorator to the mean and square methods you have written
You could also alter the addStuff method to make use of this new decorator

Decide on a way to tell users what your project is capable of.
  For example, if they type 'h' you could return a nicely formatted bit of text explaining how they can use the code to find sum, mean or squares. Even better if you can make use of docstrings!
"""

from modules import sanitize  # existing
from modules import my_module # existing
from modules import mathop # new module for this project

print ("WELCOME TO THE MATHS PROJECT\n\n")
title = input ("Enter your project title: ")
#title = sanitize.cleanup(title)
#print(title)

num1 = int (input ("\nEnter a number : "))
num2 = int (input ("Enter another  : "))
nums = range (num1, num2)
sq = []
op = 0

while op < 1 or op > 4:
    print ("\nFor all numbers between", num1, "and", num2, "select the operation you want to do")
    print ("1 - sum of all numbers in that range")
    print ("2 - mean of all numbers in that range")
    print ("3 - square of all numbers in that range")
    op = int (input("Your choice (-1 to quit): "))
    if op == -1:
        break

print("\n***\n\nProject Title: ",sanitize.cleanup(title))

if op == 1:
    print("\nSum of all numbers between", num1, "and", num2, ":", my_module.addStuff(*nums))

if op == 2:
    print("\nMean of all numbers between", num1, "and", num2, ":", mathop.findMean(num1,num2))

if op == 3:
    print ("\nSquare of all numbers between", num1, "and", num2, ":", mathop.squareNums(num1,num2))

print ("\n\n***\n\n")