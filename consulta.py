from pymongo import MongoClient

# conexion a mongo
client = MongoClient('localhost', 27017)

# db es el nombre de la base y collection la coleccion
db = client['tenis']
coleccion = db['partidos']

#consulta
print('Listar los partidos que se jugaron en la semifinal y final')

consulta = {
    "$or": [
        {"Round": "The Final"},
        {"Round": "Semifinals"}
    ]
}

# mostrar campos espeficicos
proyeccion = {
    "Tournament": 1,
    "Round": 1,
    "Player_1": 1,
    "Player_2": 1,
    "Winner": 1,
    "Score": 1,
    "_id": 0
}

resultados = coleccion.find(consulta, proyeccion)

# imprimir resultados
for resultado in resultados:
    print(resultado)
