
import turtle
import math

 #construindo uma arvore 
def drawRectangle(t, width, height, color): 
    t.fillcolor(color) 
    t.begin_fill() 
    t.forward(width) 
    t.left(90) 
    t.forward(height) 
    t.left(90) 
    t.forward(width) 
    t.left(90) 
    t.forward(height) 
    t.left(90) 
    t.end_fill() 
    
def drawTriangle(t, length, color): 
    t.fillcolor(color) 
    t.begin_fill() 
    t.forward(length) 
    t.left(135) 
    t.forward(length / math.sqrt(2)) 
    t.left(90) 
    t.forward(length / math.sqrt(2)) 
    t.left(135) 
    t.end_fill() 
     
screen = turtle.Screen ( ) 
screen.bgcolor("#E0FFFF") 
tip = turtle.Turtle() 
tip.color ("black") 
tip.shape ("turtle") 
tip.speed (10) 
tip.penup() 
tip.goto(100, -130) 
tip.pendown() 
drawRectangle(tip, 20, 40, "brown") 
tip.penup() 
tip.goto(65, -90) 
tip.pendown() 
drawTriangle(tip, 90, "lightgreen") 
tip.penup() 
tip.goto(70, -45) 
tip.pendown() 
drawTriangle(tip, 80, "lightgreen") 
tip.penup() 
tip.goto(75, -5) 
tip.pendown() 
drawTriangle(tip, 70, "lightgreen")


# Criando a tartaruga para a casa
t = turtle.Turtle()
t.color("black")
t.shape("turtle")
t.speed(10)

def drawRectangle(t, width, height, color):

    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

# Telhado
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()

# Lateral da casa 
def drawParallelogram(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(120)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(90)
    t.end_fill()

# Frente da casa 
t.penup()
t.goto(-150, -120)
t.pendown()
drawRectangle(t, 100, 110, "yellow")

# Porta da frente 
t.penup()
t.goto(-120, -120)
t.pendown()
drawRectangle(t, 40, 60, "#8A2BE2")

# telhado frontal
t.penup()
t.goto(-150, -10)
t.pendown()
drawTriangle(t, 100, "red")

# lado da casa
t.penup()
t.goto(-50, -120)
t.pendown()
drawParallelogram(t, 60, 110, "yellow")

# janela
t.penup()
t.goto(-30, -60)
t.pendown()
drawParallelogram(t, 20, 30, "#BBFFFF")

# telhado lateral
t.penup()
t.goto(-50, -10)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.left(30)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(75)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(45)
t.end_fill()
turtle.done()
  
  #construindo uma arvore 
def drawRectangle(t, width, height, color): 
    t.fillcolor(color) 
    t.begin_fill() 
    t.forward(width) 
    t.left(90) 
    t.forward(height) 
    t.left(90) 
    t.forward(width) 
    t.left(90) 
    t.forward(height) 
    t.left(90) 
    t.end_fill() 
    
def drawTriangle(t, length, color): 
    t.fillcolor(color) 
    t.begin_fill() 
    t.forward(length) 
    t.left(135) 
    t.forward(length / math.sqrt(2)) 
    t.left(90) 
    t.forward(length / math.sqrt(2)) 
    t.left(135) 
    t.end_fill() 
     
screen = turtle.Screen ( ) 
screen.bgcolor("coral") 
tip = turtle.Turtle() 
tip.color ("black") 
tip.shape ("turtle") 
tip.speed (10) 
tip.penup() 
tip.goto(100, -130) 
tip.pendown() 
drawRectangle(tip, 20, 40, "brown") 
tip.penup() 
tip.goto(65, -90) 
tip.pendown() 
drawTriangle(tip, 90, "lightgreen") 
tip.penup() 
tip.goto(70, -45) 
tip.pendown() 
drawTriangle(tip, 80, "lightgreen") 
tip.penup() 
tip.goto(75, -5) 
tip.pendown() 
drawTriangle(tip, 70, "lightgreen")
