edad = int(input("¿Cuantos años tienes? ")) # 30 int
tiene_dni = input("¿Tienes DNI? (S/N)")

if not tiene_dni == "S":
    print("No puede votar")
elif edad < 16:
    print("No puedes votar, eres menor de edad")
elif edad <= 17:
    print("Voto optativo")
elif edad <= 69:
    print("Voto obligatorio")
else:
    print("Voto optativo, por tu edad mayor de 70")