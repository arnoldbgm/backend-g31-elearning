# 🔨 Introducción a `print()` en Python

La función `print()` es una de las herramientas más básicas e importantes en Python. Su propósito es **mostrar información en la consola**, lo cual es fundamental para depurar, comunicar resultados o simplemente interactuar con el usuario.

> 💡 **Dato útil**: Aprender a usar `print()` será tu primer paso como programador, ¡y te acompañará durante toda tu vida como desarrollador!

---

## 🧼 Limpiar la consola (opcional)

Antes de comenzar a imprimir, es común limpiar la consola para que la salida sea más legible. Esto se puede lograr con el módulo `os` de Python, que permite ejecutar comandos del sistema operativo:

```python
from os import system

# Intenta limpiar la consola dependiendo del sistema operativo
if system("clear") != 0:
    system("cls")
```

---

## 📌 Uso básico de `print()`

```python
print("¡Hola, mundo!")
```

Puedes usar **comillas dobles** `" "` o **comillas simples** `' '` para definir cadenas de texto:

```python
print("Hola con comillas dobles")
print('Hola con comillas simples')
```

---

## 🧹 Imprimir varios elementos

Puedes imprimir múltiples valores separados por comas. Python los separará automáticamente con espacios:

```python
print("Python", "es", "genial")
```

---

## ⚙️ Personalizar la salida con `sep` y `end`

### 🔹 `sep`: define el separador entre elementos

```python
print("Python", "es", "potente", sep=" 🚀 ")
# Salida: Python 🚀 es 🚀 potente
```

### 🔹 `end`: define qué se imprime al final de la línea

```python
print("Primera parte", end="... ")
print("segunda parte")
# Salida: Primera parte... segunda parte
```

---

## 🔢 Imprimir otros tipos de datos

No solo puedes imprimir texto. También puedes imprimir números, resultados de operaciones, etc.

```python
print(2025)
print(3.14 + 2)
```

---

## 📝 Imprimir comillas dentro de una cadena

### ❌ Esto da error:

```python
# print("Este es un "error"")  # Error de sintaxis
```

### ✅ Soluciones:

**1. Usar comillas simples alrededor del texto:**

```python
print('Esto es una "pulgada"')
```

**2. Escapar comillas dobles con `\`:**

```python
print("Esto es una \"pulgada\"")
```

**3. Usar triple comillas (''' o """ ):**

```python
print("""Esto es una "pulgada" usando triple comillas""")
```

---

## ✅ Conclusión

La función `print()` es tu aliada para interactuar con el usuario y entender qué está pasando en tu programa. Dominarla desde el principio te ayudará a aprender y depurar más eficientemente.