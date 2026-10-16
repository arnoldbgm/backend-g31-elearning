# Diccionario
# Nos va a permitir almacenar los datos usando
# clave y valor

superheroe = {
    "nombre": "Batman",
    "edad": 35,
    "superpoder": "Super millonario",
    "volar": False,
    "amigos": ["Superman", "Mujer Maravilla"]
}

# Acceder a un valor
superheroe["superpoder"]
superheroe.get("superpoder")

# Agregar un valor
superheroe["ciudad"] = "Gotica" 

# Editar un valor
superheroe["edad"] = 34

# Eliminar una key => llave
superheroe.pop("volar")

print(superheroe)