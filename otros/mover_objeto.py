import turtle
import time

posponer = 0.1

wn = turtle.Screen()
wn.title("mover objeto")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

objeto = turtle.Turtle()
objeto.speed(0)
objeto.shape("square")
objeto.color("white")
objeto.penup()
objeto.goto(0, 0)
objeto.direction = "stop"

def arriba():
    objeto.direction = "up"
    
def abajo():
    objeto.direction = "down"

def izquierda():
    objeto.direction = "left"
    
def derecha():
    objeto.direction = "right"

def mov():
    if objeto.direction == "up":
        y = objeto.ycor()
        objeto.sety(y + 20)
        objeto.direction = "stop"
    
    if objeto.direction == "down":
        y = objeto.ycor()
        objeto.sety(y - 20)
        objeto.direction = "stop"
    
    if objeto.direction == "left":
        x = objeto.xcor()
        objeto.setx(x - 20)
        objeto.direction = "stop"
        
    if objeto.direction == "right":
        x = objeto.xcor()
        objeto.setx(x + 20)
        objeto.direction = "stop"

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()
    mov()
    time.sleep(posponer)