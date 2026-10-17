# def pedir_entero(mensaje):
#     try:
#         numero = int(input(mensaje))
#         return numero
#     except Exception:
#         print("Esto no es un numero")

# edad = pedir_entero("¿Cuántos años tenés? ")
# print(f"Tenés {edad} años")

def pedir_nota(mensaje):
    try:
        nota = int(input(mensaje))
    except ValueError:
        print ("El dato ingresado no es un numero")
        return
    if nota > 20 or nota < 0:
        print("La nota no puede ser mayor a 20 ni menor a 0")
        return
    return nota

nota1 = pedir_nota("¿Introduce tu nota?")

print(nota1)