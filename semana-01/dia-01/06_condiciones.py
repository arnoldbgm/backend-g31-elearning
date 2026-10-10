# Condicionales
# if , else, elif

# [Regla de oro]: La identacion y el orden

# Una persona quiere postular a la presidencia del Perú
# Requisito, debe de contar con mas de 35 años
# debe ser peruano de nacimiento

nombre = "Elvis"
edad = 30
peruano = True

if edad >= 35 and peruano == True:
    print(f"Sr {nombre} usted es apto para postularse como presidente")

else:
    print(f"Sr {nombre} usted NO ESTA APTO")


es_fin_de_semana = False
# Un if solo se va a ejecutar cuando la condicion es verdadera
#    True
if not es_fin_de_semana:
  print("¡No es fin de semana!")

# Ternario en Js
# CONDICION ? SI : NO
# Ternario en python
# SI if CONDICION else NO

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)