persona = {
   "nombre": "Ana",
   "edad": 30,
   "ciudad": "Madrid"
}

# Mi nombre es Ana tengo 30 y vivo en Madrid

print(f"Mi nombre es {persona['nombre']} tengo {persona['edad']} y vivo en {persona['ciudad']}")

persona["edad"] = 31

print(persona)

persona["deporte"] = "Gimnasia"

print(persona)

persona.pop("edad")

print(persona)

estudiantes = [
   {
      "id": 1,
      "nombre": "Arnold",
      "ciudad": "Arequipa"
   },
   {
      "id": 2,
      "nombre": "Juan",
      "ciudad": "Puno",
      "deportes": [
                   'Futbol', 
                   'Basket', 
                   'Golf',
                  ]
   },
   {
      "id": 3,
      "nombre": "Carlos",
      "ciudad": "Lima"
   }
]

# estudiantes[1]["deportes"] = ['Futbol', 'Basket', 'Golf']

estudiantes[1]["deportes"].append({
                                    'hobbies': 'dota',
                                    'musica': 'rock'   
})

print(estudiantes[1])

# El metodo que devuelve las claves

print(persona.keys())

# Listar solo los valores de tu diccionario

print(persona.values())

print(persona.items())


equipo_mundial = {
   'nombre': 'Brasil',
   'campeon_del_mundo': True,
   'campeonatos': 5
}

for clave in equipo_mundial:
   print(f"La clave es {clave} el valor es {equipo_mundial[clave]}")


[('nombre', 'Brase'), ('campeon_del_mundo', True), ('campeonatos', 5)]

for clave, valor in equipo_mundial.items():
   print(f"La clave es .... {clave} -> {valor}")