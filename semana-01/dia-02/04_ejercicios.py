notas = [14, 8, 17, 11, 6, 20, 13, 9]

# Promedio => Sumando todas las notas y diviendo entre la cantidad
# de notas

notas_acumuladas = 0
aprobado = 0
nota_veinte = False
nota_alta = notas[0]
nota_baja = notas[0]

for nota in notas:
    notas_acumuladas = notas_acumuladas + nota
    if nota >= 11:
        # aprobado = aprobado + 1
        aprobado += 1
    if nota == 20:
        nota_veinte = True
    if nota > nota_alta:
        nota_alta = nota
    if nota < nota_baja:
        nota_baja = nota
    
print(f"El promedio de la clase es {notas_acumuladas/len(notas)}")
print(f"El numero de aprobados es {aprobado}")
print(f"¿Hubo algun veinte? {nota_veinte}")
print(f"La nota mas alta {nota_alta}")
print(f"La nota mas baja {nota_baja}")