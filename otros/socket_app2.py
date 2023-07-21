from socket import *
import csv
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('my_model.h5')

etiquetas = {0: 'adelante', 1: 'derecha', 2: 'izquierda'}

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2022))
s.listen(10)
print("Iniciando programa")
conectado = True

#f = open('datos.csv', 'a', newline='')
#writer = csv.writer(f)

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
                    
                    print(etiquetas[prediccion])
                    
                    validador = False
                    contador = 0
                    data_X = []
                    data_X2 = None
        else:
            conectado = False

    print("cliente desconectado")
    cliente.close()
    
s.close()
print("fin de programa")