import csv
import os

os.system('echo %cd%')

 #Definimos una funcion que se llame csv_write, en ella vamos a aprender a escribir archivos
# def csv_write():
#     #Aqui vamos a abrir un archivo, llamado nuevo_1.csv abriendolo con escritura, esta apertura del archivo la llamaremos csv_writer 
#     with open ('nuevo_1.csv', 'w') as csv_writer:
#         escritor = csv.writer(csv_writer)
#         #Utilizamos la funcion csv.writer que se encuentra en la libreria csv, la cual hemos importado al principio
#         escritor.writerow(['Esto es un archivo csv']*10 + ['viernes'])
#         #Writerow sirve para escribir una linea y tenemos que meter en parentesis el contenido, aqui lo vamos a multiplicar por 10
#         escritor.writerow(['Estamos a jueves']*10 + ['fin'])

# csv_write()