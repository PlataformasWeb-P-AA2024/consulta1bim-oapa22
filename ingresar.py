from pymongo import MongoClient
import csv

# conexion a mongo
client = MongoClient('localhost', 27017)

# db es el nombre de la base y collection la coleccion
db = client['tenis']
coleccion = db['partidos']

# abrir el csv
archivo = open('atp_tennis.csv', "r")

encabezado = archivo.readline().strip().split(',')

# leer el archivo
lector = csv.DictReader(archivo, fieldnames=encabezado, delimiter=',')

for fila in lector:
    coleccion.insert_one(fila)

# cerrar el archivo
archivo.close

# imprimir la coleccion
#resultado = coleccion.find()
#for l in resultado:
#    print(l)







