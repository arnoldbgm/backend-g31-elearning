# RETO 01
nombre = input("¿Cual es tu nombre?")
edad = input("¿Cual es tu edad?")
ciudad = input("¿Cual es tu ciudad?")
lenguaje = input("¿Cual es tu lenguaje favorito?")

print(f"Hola, soy {nombre}, tengo {edad} años, vivo en {ciudad} y programo en {lenguaje}.")

print(nombre, type(nombre))
print(edad, type(edad))

anio_nacimiento = 2026 - int(edad)
print(f"Tu año de naciemiento aproximado es el {anio_nacimiento}")