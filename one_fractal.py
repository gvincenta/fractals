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
import time
pen3 = Pen()
pen3.screen.bgcolor("black")
pen3.color("white")

def move_pens():




        #move pen3 upwards
        pen3.penup()
        pen3.bk(300)
        pen3.lt(90)
        pen3.fd(400)
        pen3.rt(90)
        pen3.pendown()


#So that it doesn't take tooooo loooonggg......

pen3.speed("fastest")


#Move pens

def fractals(length = 1000,minimum = 4, sides = 3):

        length = length / 2
        degree = 360 / sides
        
        if length > minimum:
                #where the magic happens
                for i in range(sides):

                        pen3.forward(length)
                        pen3.right(degree)

                        fractals(length,minimum,sides)
                        
        #hides turtles for aesthetics purposes

        pen3.ht()


def fractals_2(length = 1000,minimum = 4, sides = 3):

        length = length / 2
        degree = 360 / sides
        
        if length > minimum:
                pen3.right(degree)
                pen3.forward(length)
                fractals(length,minimum,sides)
                        
        #hides turtles for aesthetics purposes

        pen3.ht()



        

        
length = int(input("length?"))
minimum = int(input("minimum?"))
sides = int(input("sides of polygon?"))

move_pens()
fractals(length,minimum,sides)
time.sleep(1)
#Algorithms are fun!
