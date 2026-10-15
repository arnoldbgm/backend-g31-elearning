# 🧠 Comprender los tipos de datos en Python con `type()`

Python cuenta con varios tipos de datos fundamentales. La función `type()` permite saber cuál es el tipo de un valor o variable.

> 📘 **`type(valor)` devuelve el tipo de dato del valor proporcionado.**

---

## 🔢 Tipos numéricos

### 🔸 `int` — Números enteros

```python
print(type(10))      # int
print(type(0))       # int
print(type(-5))      # int
print(type(12345678901234567890))  # int de gran tamaño
```

### 🔸 `float` — Números decimales

```python
print(type(3.14))    # float
print(type(1.0))     # float
print(type(1e3))     # float (notación científica = 1000.0)
```

### 🔸 `complex` — Números complejos

```python
print(type(1 + 2j))  # complex
```

---

## 🔤 Texto con `str`

Las cadenas de texto también son un tipo de dato:

```python
print(type("Hola"))          # str
print(type(""))              # str vacío
print(type("123"))           # str (aunque parezca un número)
print(type("""Texto
multilínea"""))  # str multilinea
```

---

## 🔘 Booleanos con `bool`

Los valores `True` y `False` representan verdadero y falso:

```python
print(type(True))     # bool
print(type(False))    # bool
print(type(1 < 2))     # bool (resultado de una comparación)
```

---

## 🚫 Valor nulo con `NoneType`

El tipo `NoneType` representa la ausencia de valor:

```python
print(type(None))  # NoneType
```

---

## ✅ Conclusión

Conocer los tipos de datos es esencial para programar correctamente. `type()` te ayuda a identificarlos y entender cómo interactúan dentro de tu código.