def saludar(nombre, apellido):
    # aqui viene todo mi codigo
    print("Hola amigos")
    print("Un gusto en conocerlos")
    print(f"Mi nombre es {nombre} {apellido}")

# saludar("Juan", "Santibañez")
# saludar(apellido="Del Valle", nombre="Alberto")

# def sumar (n1, n2, n3, n4):
#     total = n1 + n2 + n3 + n4
#     return total

# *args
def suma_global(*argument):
    total = 0
    for numero in argument:
        total = total + numero
    print(total)
    return total

suma_global(10,5,100,3000)


# **kwargs

def calulcarBalance(deposito, retiro):
    print(deposito - retiro)
    return deposito - retiro

cliente = {
    "deposito": 15000,
    "retiro": 3000
}

# calulcarBalance(retiro=cliente["retiro"], deposito=cliente["deposito"])
calulcarBalance(**cliente)