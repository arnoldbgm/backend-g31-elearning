# Listas - Arrays

notas_alumnos = [15, 18, 19, 8]
lista_de_lista = [[1, 2], ["Calcetin", 4]]

# Muestrame la ultima nota de tus alumnos
print(notas_alumnos[-1]) # Muestra el ultimo elmt

# Muestrame el 2 que esta dentro de lista_de_lista
print(lista_de_lista[0][1]) # 2

# Reasignacion por indice
frutas = ["manzana", "mango", "uva", "cereza"]

frutas[2] = "piña"

nuevas_frutas = frutas + ["pera", "fresa"]

# ¿Cuanto elementos hay en mi lista?
len(frutas)

# Para insertar un elemento al final de la lista
# append
paises = ["USA", "Japon", "Canada", "Japon", "Japon"]
paises.append("Bolivia")
paises.count("Japon")