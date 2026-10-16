# paises = ["USA", "Japon", "Canada"]

# # for ALIAS in LISTA(ARREGLO):
# for pais in paises:
#     print(pais)

# print("######################")

# notas = [19, 12, 11, 18, 20]
# # Mostrar aquellos alumnos con nota mayor a 13
# for nota in notas:
#     if nota > 13:
#         print(f"Alumno aprobado con {nota}")

cadena = "Superman"
vocales = ["a", "e", "i", "o", "u"]

for caracter in cadena:
    if caracter not in vocales:
        print(caracter)

frutas = ["manzana", "pera", "mandarina"]
for idx, frutita in enumerate(frutas):
    print(f"Índice {idx}: {frutita}")


datos = [["12345678", "Juan", "M"], ["87654321", "Linda", "F"]]

for dato in datos:
    # dato => ["12345678", "Juan", "M"]
    for dato_personal in dato:
        print(dato_personal)
