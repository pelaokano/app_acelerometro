from socket import *
import csv

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2022))
s.listen(10)
print("Iniciando programa")
conectado = True

f = open('datos.csv', 'a', newline='')
writer = csv.writer(f)

while True:
    conectado = True
    (cliente, addr) = s.accept()
    print("cliente conectado: ", addr)
    while conectado:
        data = cliente.recv(1024)
        if data:
            row = str(data).split(";")
            print(row)
            writer.writerow(row)
        else:
            conectado = False
            f.close()
    print("cliente desconectado")
    cliente.close()
s.close()
print("fin de programa")