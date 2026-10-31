# Desde la libreria flask quiero importar la Clase Flask
from flask import Flask, request

app = Flask(__name__)  # Se esta creando mi servidor

jugadores = [
    {"id": 1, "nombre": "Paolo Guerrero", "edad": 41, "posicion": "Delantero", "equipo": "Alianza Lima", "seleccion": "Peru"},
    {"id": 2, "nombre": "Andre Carrillo", "edad": 33, "posicion": "Extremo", "equipo": "Al Hilal", "seleccion": "Peru"},
    {"id": 3, "nombre": "Renato Tapia", "edad": 29, "posicion": "Mediocampista", "equipo": "Leganes", "seleccion": "Peru"},
    {"id": 4, "nombre": "Lionel Messi", "edad": 38, "posicion": "Delantero", "equipo": "Inter Miami", "seleccion": "Argentina"},
    {"id": 5, "nombre": "Vinicius Jr", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
    {"id": 6, "nombre": "Luis Diaz", "edad": 28, "posicion": "Extremo", "equipo": "Liverpool", "seleccion": "Colombia"},
    {"id": 7, "nombre": "Federico Valverde", "edad": 27, "posicion": "Mediocampista", "equipo": "Real Madrid", "seleccion": "Uruguay"},
    {"id": 8, "nombre": "Rodrygo", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
    {"id": 9, "nombre": "Julian Alvarez", "edad": 26, "posicion": "Delantero", "equipo": "Manchester City", "seleccion": "Argentina"},
    {"id": 10, "nombre": "Christian Cueva", "edad": 33, "posicion": "Mediocampista", "equipo": "Cienciano", "seleccion": "Peru"},
]

# Aqui vamos a crear nuestros endpoints
# Recuerda que estos deben ir encima de app.run()

# Necesitamos un endpoint en la raiz / que responda
# diciendo "Bienvenidos comensales" 
@app.route("/")  # Que ruta vamos agregar
def saludar():
   # REGLA DE ORO: Siempre se retorna informacion
   return "Bienvenidos comensales"

# Necesitamos un endpoint llamado "/milanesa"
# este debe de mostrar un print que diga PREPARANDO
# y luego debe de retornar "MILANESA PREPARADA!!!"

@app.route("/milanesa")
def preparar_milanesa():
   print("PREPARANDO")
   # Siempre van a retornar en JSON
   return {
      "msg": "La milanesa esta preparada",
      "author": "El chef"
   }

# Necesitamos un endpoint llamado "/jugadores"
# el cual debe de retornar a todos los jugadores mayores de 28
@app.route("/jugadores")
def jugadores_mayores():
   # Aqui va venir toda mi logica para obtener a los jugadores
   # mayores de 28
   jugadores_adultos = []
   for jugador in jugadores:
      if jugador["edad"] >= 28:
         jugadores_adultos.append(jugador)
   return {
      "msg": "Los jugadores mayores de 28 son",
      "resultado": jugadores_adultos
   }

# RETO 01
# Crear el endoint "/mediocampistas"
# Retornen a todos los mediocampistas peruanos
# El formato de retorno es el siguiente
# {
#   msg: "Resultado exitoso",
#   resultado:  VARIABLE_DONDE_GUARDARON_JUGADORES
#}

# Se desea implementar los argumentos dinamicos
# Si el usuario busca /jugador/1
# Se debe retornar el jugador con el id = 1
@app.route("/jugador/<int:id>")
def obtener_jugador(id):
   jugador_encontrado = {}
   for jugador in jugadores:
      if jugador["id"] == id:
         jugador_encontrado = jugador
         break

   return {
      "msg": "Encontramos al jugador",
      "data": jugador_encontrado
   }

# Tiendas Ripley
# ripley.com/televisores?precio_mayor=1500&marca=lg
# ? => Inicio de los parametros
# precio_mayor=1500 => Nuestro primer parametro
# & => Separar parametros
# marca=lg

# Crear el endoint "/buscador"
# Donde se pueda buscar a un jugador o varios jugadores
# de acuerdo a la posicion donde juega

# Query params
@app.route("/buscador")
def buscador_jugadores():
   # Para trabajar con los query params
   # Debes de importar el request de flask
   # solicitud
   # from flask import request
   # /buscador?posicion=Mediocampista
   posicion_query = request.args.get("posicion") #Extremo
   jugadores_filtrados = []
   for jugador in jugadores:
      if jugador["posicion"].lower() == posicion_query.lower():
         jugadores_filtrados.append(jugador)

   return {
      "msg": "Resultados exitoso",
      "data": jugadores_filtrados
   }


app.run() # Corra tu servidor