# 📋 Listas en Python: Guía Definitiva

Las **listas** son colecciones **ordenadas** y **mutables** que permiten almacenar múltiples elementos en una sola variable. Pueden contener datos de **distintos tipos** y son esenciales para gestionar secuencias en Python.

> 💡 **Dato útil**: A diferencia de las tuplas, las listas pueden modificarse después de su creación (añadir, eliminar o cambiar elementos).

---

## 🛠️ Crear Listas

Para definir una lista, utiliza corchetes `[]`:

```python
lista1 = [1, 2, 3, 4, 5]                       # Lista de enteros
lista2 = ["manzanas", "peras", "plátanos"]     # Lista de cadenas
lista3 = [1, "hola", 3.14, True]               # Lista de tipos mixtos
lista_vacia = []                               # Lista vacía
lista_de_listas = [[1, 2], ["calcetín", 4]]    # Lista de listas (matrices simples)
```

---

## 🔍 Acceder a Elementos

Usa índices (comienzan en 0) o índices negativos para contar desde el final:

```python
print(lista2[0])   # "manzanas"
print(lista2[-1])  # "plátanos"
print(lista_de_listas[1][0])  # "calcetín"
```

---

## 🍰 Slicing (Rebanado)

Extrae sublistas usando `[inicio:fin-1:paso]`:

```python
lista = [1, 2, 3, 4, 5]
print(lista[1:4])    # [2, 3, 4]
print(lista[:3])     # [1, 2, 3]
print(lista[3:])     # [4, 5]
print(lista[:])      # [1, 2, 3, 4, 5]
print(lista[::-1])   # [5, 4, 3, 2, 1] (inverso)
```

---

## ✏️ Modificar Listas

### Reasignar por índice

```python
lista = [1, 2, 3]
lista[0] = 20
print(lista)  # [20, 2, 3]
```

### Añadir elementos

- **Concatenación** (crea nueva lista):

  ```python
  lista = [1, 2, 3]
  nueva = lista + [4, 5]
  ```

- **Extend** (modifica lista existente):

  ```python
  lista += [6, 7]
  ```

---

## 📏 Obtener Longitud

Para saber cuántos elementos tiene una lista:

```python
print(len(lista))  # Número de elementos
```

---

## 🔧 Métodos Útiles de Listas

- `append(x)`: Añade `x` al final.
- `insert(i, x)`: Inserta `x` en la posición `i`.
- `remove(x)`: Elimina la primera aparición de `x`.
- `pop([i])`: Elimina y devuelve el elemento en la posición `i` (por defecto, el último).
- `index(x)`: Devuelve el índice de la primera aparición de `x`.
- `count(x)`: Cuenta cuántas veces aparece `x`.
- `sort()`: Ordena la lista (in-place).
- `reverse()`: Invierte el orden de la lista (in-place).
- `clear()`: Vacía la lista.

---

## ✅ Buenas Prácticas

1. **Evita** usar `+` repetidamente para añadir elementos: mejor `append` o `extend`.
2. **Comprende** la diferencia entre métodos que modifican la lista y operaciones que crean nuevas.
3. **Usa** slicing para copias superficiales (`lista[:]`) y evita aliasing no deseado.

---

# 🧠 Ejercicios

## Ejercicio 1: Mensaje Secreto
Use slicing y concatenación para obtener "secreto"

```python
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

secreto = "".join(mensaje[7:14])
print(secreto)  # "secreto"
```

## Ejercicios 2: Intercambio de Posiciones
Intercambia primer y último elemento con asignación por índice

```python
numeros = [10, 20, 30, 40, 50]

numeros[0], numeros[-1] = numeros[-1], numeros[0]
print(numeros)  # [50, 20, 30, 40, 10]
```

## Ejercicio 3: Sándwich de Listas
Combina todo en una lista llamada sandwich

```python
pan_arriba = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan_arriba + ingredientes + pan_abajo
print(sandwich)  # ['pan arriba', 'jamón', 'queso', 'tomate', 'pan abajo']
```

## Ejercicio 4: Duplicando la Lista
Crea una nueva lista duplicada: [1, 2, 3, 1, 2, 3]

```python
lista = [1, 2, 3]

lista_duplicada = lista * 2
print(lista_duplicada)  # [1, 2, 3, 1, 2, 3]
```

## Ejercicio 5: Extrayendo el Centro
Usa slicing para extraer el elemento central (30)
```python
lista = [10, 20, 30, 40, 50]

elemento_central = lista[len(lista) // 2]
print(elemento_central)  # 30
```

## Ejercicio 6: Reversa Parcial
Invierte solo la primera mitad: [3, 2, 1, 4, 5, 6]

```python
lista = [1, 2, 3, 4, 5, 6]

mitad = len(lista) // 2
lista[:mitad] = lista[:mitad][::-1]
print(lista)  # [3, 2, 1, 4, 5, 6]
```