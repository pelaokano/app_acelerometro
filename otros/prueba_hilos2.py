from threading import Thread, current_thread, get_native_id
import time
import turtle
import numpy as np

validador = True
mover = "stop"
posponer = 0.1

def grafico():
    
    global mover 
    mover = "stop"
       
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

    def mov():
        global mover
        if mover == "up":
            y = objeto.ycor()
            if y >= 300 or y <= -300:
                mover = "stop"
            else:
                objeto.sety(y + 20)
                mover = "stop"
        
        if mover == "down":
            y = objeto.ycor()
            if y >= 300 or y <= -300:
                mover = "stop"
            else:
                objeto.sety(y - 20)
                mover = "stop"
        
        if mover == "left":
            x = objeto.xcor()
            if x >= 300 or x <= -300:
                mover = "stop"
            else:
                objeto.setx(x - 20)
                mover = "stop"
            
        if mover == "right":
            x = objeto.xcor()
            if x >= 300 or x <= -300:
                mover = "stop"
            else:
                objeto.setx(x + 20)
                mover = "stop"

    while True:
        wn.update()
        mov()
        time.sleep(posponer)
        
        if mover == "salir":
            break


def funcion1():
    global mover
    dictMover = {1: "up", 2: "down", 3: "left", 4: "right"}
    contador = 0
    
    while True:
        indice = np.random.randint(1,4)
        mover = dictMover[indice]
        time.sleep(0.5)
        contador += 1
               
        if contador > 50:
            mover = "salir"
            break

hilo1 = Thread(target=grafico)
hilo2 = Thread(target=funcion1)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
       
        