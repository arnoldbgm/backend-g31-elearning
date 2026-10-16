# Los BOOLEANOS
# True y False
# Contralar el flujo de nuestra aplicacion

# and
# Que ambos valores deben de ser True (Verdaderos)

print( True and False)  # False
print( True and True)   # True

# Solicitar que tenga DNI y sea mayor de edad
# una operacion

dni = True
mayor_de_Edad = True

if dni and mayor_de_Edad:
    print("Adelante puedes operarte")
else:
    print("No puedes operarte")

# or
# Que al menos un valor debe de ser True (veradero)

# Para entrar a la sala VIP
# Tener un amigo promotor ó tener la pulsera verde

amigo_promotor = False
pulsera_verde = True

if amigo_promotor or pulsera_verde:
    print("Adelante puedes ingresar a la fiesta")
else:
    print("No puedes ingresar a la fiesta")