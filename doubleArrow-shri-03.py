'''
Program: Double Arrow
Author: Shrikant Sharma
Description: This program recreates the Double Arrow figure
Filename: doubleArrow-shri-03.py
Purpose: Recreate the Double Arrow Figure
Revisions:
    00: access turtle module, establish a drwaing indow, and get create a turtle object
    01: recreate the Double Arrow Figure
    02: turtle in the center
'''
# there are no literal constants
# there are no class definitions
# there are no function definitions
### STEP 1: Access, establish, and create a turtle object
# access the turtle module
import turtle
# establish a drawing window
canvas = turtle.Screen()
# create a turtle object
tom = turtle.Turtle()
### STEP 2: Recreate the double arrow figure
# picks up the turtles pen
tom.penup()
# moves the turtle to position 0,50
tom.goto(0, 50)
# puts down the turtles pen
tom.pendown()
# moves the turtle by the 100
tom.forward(100)
# turns the turtle counter clockwise by 90
tom.left(90)
# moves the turtle by the 50
tom.forward(50)
# turns the turtle clockwise by 90
tom.right(90)
# turns the turtle counter clockwise by 44.42
tom.right(44.42)
# moves the turtle by the 141.42
tom.forward(141.42)
# turns the turtle clockwise by 90
tom.right(90)
# moves the turtle by the 141.42
tom.forward(141.42)
# turns the turtle clockwise by 90
tom.right(90)
# turns the turtle clockwise by 45.48
tom.right(45.58)
# moves the turtle by the 50
tom.forward(50)
# turns the turtle counter clockwise by 90
tom.left(90)
# moves the turtle by the 200
tom.forward(200)
# turns the turtle counter clockwise by 90
tom.left(90)
# moves the turtle by the 50
tom.forward(50)
# turns the turtle clockwise by 90
tom.right(90)
# turns the turtle clockwise by 45.48
tom.right(45.58)
# moves the turtle by the 141.42
tom.forward(141.42)
# turns the turtle clockwise by 90
tom.right(90)
# moves the turtle by the 141.42
tom.forward(141.42)
# turns the turtle clockwise by 90
tom.right(90)
# turns the turtle clockwise by 44.42
tom.right(44.42)
# moves the turtle by the 50
tom.forward(50)
# turns the turtle counter clockwise by 90
tom.left(90)
# moves the turtle by the 100
tom.forward(100)
# picks up the turtles pen
tom.penup()
### STEP 3: Turtle in the center
tom.goto(0, 0)

