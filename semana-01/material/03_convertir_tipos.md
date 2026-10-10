# 🧠 Casting de Tipos en Python

El **casting de tipos** consiste en convertir explícitamente un valor de un tipo de dato a otro. Esto es útil cuando se necesita operar con tipos compatibles o realizar conversiones específicas para ciertos contextos.

---

## 🧩 Ejemplos Prácticos

### 1. Convertir una cadena a entero y sumarla
```python
print(2 + int("100"))  # Resultado: 102
```
> Convierte la cadena `"100"` en un entero y lo suma con `2`.

---

### 2. Convertir un número a cadena y concatenar
```python
print("100" + str(2))  # Resultado: "1002"
```
> Convierte el número `2` a cadena y lo concatena con `"100"`.

---

### 3. Convertir una cadena a `float` y mostrar su tipo
```python
print(type(float("3.1416")))  # Resultado: <class 'float'>
```
> Convierte la cadena `"3.1416"` a un número decimal (punto flotante).

---

### 4. Convertir un número decimal a entero (truncamiento)
```python
print(int(3.1416))  # Resultado: 3
```
> Elimina la parte decimal del número y lo convierte en un entero.

---

## 🔁 Conversión a Booleanos

### 5. Evaluar números como booleanos
```python
print(bool(3))    # True
print(bool(0))    # False
print(bool(-1))   # True
```
> Cualquier número distinto de `0` se considera `True`. Solo el `0` se interpreta como `False`.

---

### 6. Evaluar cadenas como booleanos
```python
print(bool(""))        # False
print(bool(" "))       # True
print(bool("False"))   # True
```
> Solo una cadena vacía (`""`) se considera `False`. Cualquier otra cadena (aunque contenga `"False"`) será `True`.

---

## 📐 Redondeo de números

### 7. Redondear un número decimal
```python
print(round(2.51))  # Resultado: 3
```
> Redondea el número al entero más cercano.

---

## ⚠️ Errores comunes

### 8. Intentar convertir texto no numérico a entero
```python
# print(int("Hola mundo"))  # ❌ ValueError
```
> Esto genera un `ValueError` porque `"Hola mundo"` no representa un número válido.

---

## ✅ Conclusión

El **casting de tipos** en Python te permite controlar el comportamiento de tus datos y prepararlos adecuadamente para operaciones matemáticas, lógicas o de presentación. Utiliza funciones como `int()`, `float()`, `str()`, `bool()` y `round()` para transformar valores de forma segura y efectiva.