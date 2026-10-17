# VIDEOJUEGOS
# Las vidas del juego son solo 3, si el usuario
# pierde una vida puede seguir jugando, pero cuando
# las vidas sean menores o iguales a 0, el juego
# se detendra

print("Bienvenido a mi videojuego")

# vidas = 3

# while vidas > 0:
#     print(f"Tienes {vidas} vidas")
#     respuesta = input("¿Quieres perder una vida? (s/n): ")
#     if respuesta == "s":
#         vidas = vidas - 1
#         print("Has perdido una vida")

# print("Fin del juego, no tienes vidas")

# Ejercicio N° 02    
# Contraseñas
# El usuario va iniciar con una contraseña de 0 digitos
# password = ""
# Tiene que venir un bucle usando while, que se ejecutara
# mientras que la contraseña sea diferente a python
# Y pedira al usuario que ingrese la contraseña correcta
# al final deben de mostrar un print que diga
# "Contraseña correcta"

password=""
valido = False

while not valido:
    print("Ingrese la constraseña correcta")
    password = input("Ingrese la contraseña: ")
    if password == "python":
        valido = True
        
print("Contraseña correcta")
