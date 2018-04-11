"""
By: Gilbert Vincenta
draws 4 fractals with n sides of polygon
recommendation:
1. general length = 1000 or 500, depending on screen size
2. for triangle: set sides of polygon =3, minimum = 4
3. for pentagon: set sides of polygon =5, minimum = 40
--- feel free to add more interesting phenomenons of your personal experiments here --- 
basic abstraction, recursion, and for loops
contact: ngvproject11323@gmail.com"""

from turtle import *

white_pen = Pen()
blue_pen = Pen()
purple_pen = Pen()
green_pen = Pen()
white_pen.screen.bgcolor("black")
green_pen.color("green")
purple_pen.color("purple")
white_pen.color("white")
blue_pen.color("blue")
def move_pens():

        #move pen1 to the left
        white_pen.penup()
        
        #change the number to change the position on screen
        white_pen.bk(400)
        
        white_pen.pendown()

        
        #move blue_pen to the right
        blue_pen.penup()

        #change the number to change its position on screen
        blue_pen.fd(400)
        
        blue_pen.pendown()


        #move purple_pen upwards
        purple_pen.penup()
        purple_pen.lt(90)

        #change the number to change its position on screen 
        purple_pen.fd(300)
        
        purple_pen.rt(90)
        purple_pen.pendown()


        #move green_pen downwards
        green_pen.penup()        
        green_pen.lt(90)

        #change the number to change its position on screen
        green_pen.bk(200)
        
        green_pen.rt(90)
        green_pen.pendown()

#So that it doesn't take tooooo loooonggg......
white_pen.speed("fastest")
blue_pen.speed("fastest")
purple_pen.speed("fastest")
green_pen.speed("fastest")

#Move pens

def fractals(length = 1000,minimum = 4, sides = 3):

        length = length / 2
        degree = 360 / sides
        
        if length > minimum:
                #where the magic happens                
                for i in range(sides):
                        white_pen.forward(length)
                        white_pen.right(degree)
                        blue_pen.forward(length)
                        blue_pen.right(degree)
                        purple_pen.forward(length)
                        purple_pen.right(degree)
                        green_pen.forward(length)
                        green_pen.right(degree)
                        fractals(length,minimum,sides)
                        
        #hides turtles for aesthetics purposes
        white_pen.ht()
        blue_pen.ht()
        purple_pen.ht()
        green_pen.ht()
        
length = int(input("length?"))
minimum = int(input("minimum?"))
sides = int(input("sides of polygon?"))

move_pens()
fractals(length,minimum,sides)

#Algorithms are fun!
