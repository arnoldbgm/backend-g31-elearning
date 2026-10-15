# 🎯 Bucles en Python: Uso de `for`

Los bucles `for` permiten **iterar** sobre cualquier objeto **iterable**, ejecutando un bloque de código por cada elemento. Son fundamentales para procesar secuencias de datos de forma clara y concisa.

> 💡 **Dato útil**: En Python, un iterable es cualquier objeto que puede devolver sus elementos uno a uno, como listas, cadenas, diccionarios, conjuntos, e incluso generadores.

---

## 🔄 Iterar Listas

```python
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)
```

Cada ciclo, la variable `fruta` toma el valor de un elemento de la lista.

---

## 🔤 Iterar Cadenas

Las cadenas de texto también son iterables: cada carácter se procesa por separado.

```python
cadena = "Hola, mundo!"
for caracter in cadena:
    print(caracter)
```

---

## 🔢 Índices con `enumerate()`

`enumerate()` devuelve pares `(índice, valor)`, útil cuando necesitas la posición:

```python
frutas = ["manzana", "pera", "mandarina"]
for idx, valor in enumerate(frutas):
    print(f"Índice {idx}: {valor}")
```

---

## 🔀 Bucles Anidados

Puedes colocar un bucle dentro de otro para iteraciones combinadas:

```python
letras = ["A", "B", "C"]
numeros = [1, 2, 3]
for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")
```

---

## 🚨 Control de Flujo: `break` y `continue`

- **`break`**: Detiene el bucle por completo.
- **`continue`**: Salta a la siguiente iteración, omitiendo el resto del bloque.

```python
animales = ["perro", "gato", "loro", "pez"]
for animal in animales:
    if animal == "loro":
        print("¡Encontré al loro! Deteniendo bucle.")
        break

for animal in animales:
    if animal == "loro":
        continue  # Salta imprimir el loro
    print(animal)
```

---

## 🐍 Comprensión de Listas (List Comprehension)

Sintaxis compacta para crear listas nuevas a partir de iterables:

```python
animales = ["perro", "gato", "ratón", "loro", "pez"]
mayusculas = [a.upper() for a in animales]
pares = [n for n in range(1, 11) if n % 2 == 0]
```

---

## ✅ Buenas Prácticas

1. **Evita** modificar la lista mientras la iteras.
2. Usa **nombres claros** para las variables de iteración.
3. Prefiere las **list comprehensions** para transformaciones simples.

---

# 🧩 Ejercicios con `for`

## Ejercicio 1: Números Pares
Imprime los números pares del 2 al 20 inclusive.

```python
numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
```

## Ejercicio 2: Media de Lista
```python
numeros = [10, 20, 30, 40, 50]
```
Calcula la media usando un bucle `for`.

```python
numeros = [10, 20, 30, 40, 50]
total = sum(numeros)
media = total / len(numeros)
print(media)
```

## Ejercicio 3: Máximo de Lista
```python
numeros = [15, 5, 25, 10, 20]
```
Encuentra el número máximo sin usar `max()`.

```python
numeros = [15, 5, 25, 10, 20]
numeros.sort()
print(numeros[-1])
```

## Ejercicio 4: Filtrar por Longitud
```python
palabras = ["casa", "árbol", "sol", "elefante", "luna"]
```
Crea una lista con palabras de más de 5 letras.

```python
palabras = ["casa", "árbol", "sol", "elefante", "luna"]
mayusculas = [palabra for palabra in palabras if len(palabre) > 5]
print(mayusculas)
```

## Ejercicio 5: Contar Palabras por Letra
```python
palabras = ["casa", "árbol", "sol", "elefante", "luna", "coche"]
```
Pide al usuario una letra y cuenta cuántas palabras comienzan con ella (ignorando mayúsculas).

```python
palabras = ["casa", "árbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce la letra a buscar: ")
contador = 0
for palabra in palabras:
    if palabra.startswith(letra):
        contador += 1
print(contador)
```