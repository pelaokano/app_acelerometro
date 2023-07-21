from threading import Thread, current_thread, get_native_id
import time
import turtle
import numpy as np
from socket import *
import tensorflow as tf

model = tf.keras.models.load_model('my_model.h5')
mover = "stop"


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
                objeto.sety(y + 40)
                mover = "stop"
        
        if mover == "down":
            y = objeto.ycor()
            if y >= 300 or y <= -300:
                mover = "stop"
            else:
                objeto.sety(y - 40)
                mover = "stop"
        
        if mover == "left":
            x = objeto.xcor()
            if x >= 300 or x <= -300:
                mover = "stop"
            else:
                objeto.setx(x - 40)
                mover = "stop"
            
        if mover == "right":
            x = objeto.xcor()
            if x >= 300 or x <= -300:
                mover = "stop"
            else:
                objeto.setx(x + 40)
                mover = "stop"
    
    def fSalir():
        global mover
        mover = "salir"
  
    wn.onkey(fSalir,'space')
    wn.listen()
    
    while True:
        wn.update()
        mov()
        time.sleep(0.01)
        
        if mover == "salir":
            break

def funcionSocket():
    global mover
    global model
    
    etiquetas = {0: 'up', 1: 'right', 2: 'left', 4: "stop"}
    validador = True
    
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 2022))
    s.listen(10)
    print("Iniciando programa")
    conectado = True
    
    contador = 0

    while True:
        conectado = True
        (cliente, addr) = s.accept()
        print("cliente conectado: ", addr)
        
        aux = []
        validador = False
        contador = 0
        data_X = []
        data_X2 = None
        
        while conectado:
            
            data = cliente.recv(1024)        
            
            if data:

                row = str(data).split(";")
                valor = int(row[-1].replace("'", ""))
                aux.append(valor)
                           
                if len(aux) > 2:
                    aux.pop(0)
                
                if len(aux) > 1 and aux[-1] == 1 and aux[-2] == 0:
                    validador = True
                    
                if validador == True:
                    data_X.append([float(row[1]), float(row[2]), float(row[3])])
                                  
                    contador += 1
                    
                    if contador >= 15:
                        data_X2 = np.array(data_X)
                        
                        prediccion = np.argmax(model.predict(data_X2.reshape(1, 15, 3)))
                        
                        #etiquetas = {0: 'up', 1: 'right', 2: 'left', 4: "stop"}
                        
                        mover = etiquetas[prediccion]
                        
                        print(etiquetas[prediccion])
                                                
                        validador = False
                        contador = 0
                        data_X = []
                        data_X2 = None
            else:
                conectado = False

        print("cliente desconectado")
        cliente.close()
        
        if mover == "salir":
            s.close()
            print("fin de programa")
            break
            

#implementación de hilos
hilo1 = Thread(target=grafico)
hilo2 = Thread(target=funcionSocket)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
       
        