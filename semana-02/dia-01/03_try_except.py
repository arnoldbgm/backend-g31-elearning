# Try - Except
# Vamos a lograr manipular los errores
try:
    numero = int(input("Ingresa un numero"))
    if numero < 0:
        raise Exception("No se permiten numeros negativos")
    print(f"Tu numero es {numero}")
except Exception:
    print("Tuvimos un error con el numero")
finally:
    print("Fin del programa")

# Capturar errores especificos
# ValueError => El valor tiene un formato incorrecto
# ZeroDivisionError => Se intenta dividir entre cero
# NameError => Se esta usando una variable no creada
# ImportError => No se puede importar un modulo
# Exception => Un salvavidas cuando no conoces el error especifico

