# python -m venv venv
# venv\Scripts\activate
# Instalan lo que necesiten
# pip freeze > requirements.txt

from flask import Flask, request

app = Flask(__name__)

jugadores = [
    {"id": 1, "nombre": "Paolo Guerrero", "edad": 41, "posicion": "Delantero", "equipo": "Alianza Lima", "seleccion": "Perú"},
    {"id": 2, "nombre": "André Carrillo", "edad": 33, "posicion": "Extremo", "equipo": "Al Hilal", "seleccion": "Perú"},
    {"id": 3, "nombre": "Renato Tapia", "edad": 29, "posicion": "Mediocampista", "equipo": "Leganés", "seleccion": "Perú"},
    {"id": 4, "nombre": "Lionel Messi", "edad": 38, "posicion": "Delantero", "equipo": "Inter Miami", "seleccion": "Argentina"},
    {"id": 5, "nombre": "Vinícius Jr", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
    {"id": 6, "nombre": "Cristiano Ronaldo", "edad": 41, "posicion": "Delantero", "equipo": "Al Nassr", "seleccion": "Portugal"},
    {"id": 7, "nombre": "Kylian Mbappé", "edad": 27, "posicion": "Delantero", "equipo": "Real Madrid", "seleccion": "Francia"},
    {"id": 8, "nombre": "Erling Haaland", "edad": 26, "posicion": "Delantero", "equipo": "Manchester City", "seleccion": "Noruega"},
    {"id": 9, "nombre": "Jude Bellingham", "edad": 23, "posicion": "Mediocampista", "equipo": "Real Madrid", "seleccion": "Inglaterra"},
    {"id": 10, "nombre": "Luka Modrić", "edad": 41, "posicion": "Mediocampista", "equipo": "AC Milan", "seleccion": "Croacia"},
    {"id": 11, "nombre": "Neymar Jr", "edad": 34, "posicion": "Extremo", "equipo": "Santos", "seleccion": "Brasil"},
    {"id": 12, "nombre": "Robert Lewandowski", "edad": 38, "posicion": "Delantero", "equipo": "Barcelona", "seleccion": "Polonia"},
    {"id": 13, "nombre": "Mohamed Salah", "edad": 34, "posicion": "Extremo", "equipo": "Liverpool", "seleccion": "Egipto"},
    {"id": 14, "nombre": "Kevin De Bruyne", "edad": 35, "posicion": "Mediocampista", "equipo": "Napoli", "seleccion": "Bélgica"},
    {"id": 15, "nombre": "Harry Kane", "edad": 33, "posicion": "Delantero", "equipo": "Bayern Múnich", "seleccion": "Inglaterra"},
    {"id": 16, "nombre": "Rodri", "edad": 30, "posicion": "Mediocampista", "equipo": "Manchester City", "seleccion": "España"},
    {"id": 17, "nombre": "Federico Valverde", "edad": 28, "posicion": "Mediocampista", "equipo": "Real Madrid", "seleccion": "Uruguay"},
    {"id": 18, "nombre": "Lautaro Martínez", "edad": 29, "posicion": "Delantero", "equipo": "Inter de Milán", "seleccion": "Argentina"},
    {"id": 19, "nombre": "Virgil van Dijk", "edad": 35, "posicion": "Defensa", "equipo": "Liverpool", "seleccion": "Países Bajos"},
    {"id": 20, "nombre": "Alisson Becker", "edad": 33, "posicion": "Portero", "equipo": "Liverpool", "seleccion": "Brasil"},
]

@app.route("/api/v1/jugadores", methods=["GET"])
def todos_jugadores():
    return {
        "msg": "Resultado exitoso",
        "data": jugadores
    }

# RETO 01
# Crear el endpoint /api/v1/jugador/<id>
# Este endpoint se encargara de traer un unico jugador
# Si el ID no existe, se debe de retornar un mensaje de
# error
# {
#    msg:  "No existe el jugador buscado"
# }
# Y si existe el jugador se debe retornar toda su 
# informacion
# GET
@app.route("/api/v1/jugador/<int:id>", methods=["GET"])
def jugador_id(id):
    for jugador in jugadores:
        if jugador["id"] == id:
            return {
                "msg": "Jugador encontrado",
                "data": jugador
            }, 200

    return {
        "msg": "Jugador no encontrado"
    }, 400

# POST - Insertar datos
# Se debe de crear un endpoint llamado /api/v1/registrar
# Este endpoint debe de leer los datos que recibe
# Debe insertar estos datos dentro de nuestro arreglo
# de jugadores

@app.route("/api/v1/registrar", methods=["POST"])
def registrar_jugador():
    # Siempre que te encuentres en un post
    # debes de capturar el body que te envia el cliente
    # Para capturar la informacion tu usas el request
    # {
    #    "nombre": "Lapadula",
    #    "seleccion": "Peru"
    # }
    # from flask import request
    informacion_recibida = request.json
    # Validaciones
    # Yo deseo validar que siempre se envie
    # el nombre, id, posicion
    if not informacion_recibida["nombre"]:
        return {
            "msg": "Debes de colocar un nombre"
        }

    if not informacion_recibida["id"]:
        return {
            "msg": "Debes de colocar un id"
        }

    if not informacion_recibida["posicion"]:
        return {
            "msg": "Debes de colocar la posicion"
        }
    
    jugadores.append(informacion_recibida)
    return {
        "msg": "Registro exitoso"
    }, 201

# PUT
# Se necesita un endpoint para poder actualizar
# los de un jugador
# /api/v1/actualizar/<id>

@app.route("/api/v1/actualizar/<int:id>" ,methods=["PUT"])
def actualizar_jugador(id):
    for jugador in jugadores:
        if jugador["id"] == id:
            # Aqui vendra nuesta logica para actualizar
            # sus datos del jugador
            datos_recibidos = request.json
            # {
            #     "nombre": "Paolin",
            #     "equipo": "UCV"
            # }
            for campo in datos_recibidos:
                if campo in jugador:
                    jugador[campo] = datos_recibidos[campo]

    return {
        "msg": "Actualizacion completa"
    }, 200

# DELETE
# Se solicita que se tenga el endpoint
# /api/v1/eliminar/1
# Debe de permitir eliminar un jugador

@app.route("/api/v1/eliminar/<int:id>", methods=["DELETE"])
def eliminar_jugador(id):
    for jugador in jugadores:
        if jugador["id"] == id:
            jugadores.remove(jugador)

    return {
        "msg": "Jugador elminado exitosamente"
    }, 200

app.run()