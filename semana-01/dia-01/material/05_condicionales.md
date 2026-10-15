# 📜 Sentencias Condicionales en Python (if, elif, else)

Las sentencias condicionales son fundamentales en cualquier lenguaje de programación, y permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.

## 📝 Sentencia Simple Condicional (if)

Podemos usar la palabra clave `if` para ejecutar un bloque de código solo si se cumple una condición específica:

```python
edad = 18
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")
```

Si la condición no se cumple, el bloque de código dentro del `if` no se ejecuta:

```python
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")
```

---

## 📜 Sentencia Condicional con `else`

El comando `else` se usa para ejecutar un bloque de código si no se cumple la condición del `if`:

```python
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")
```

---

## 📜 Sentencia Condicional con `elif`

El bloque `elif` (else if) permite comprobar múltiples condiciones. Solo se ejecutará el primer bloque de código cuyo `if` o `elif` sea verdadero:

```python
nota = 5
if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("Notable!")
elif nota >= 5:
  print("¡Aprobado!")
else:
  print("¡No está calificado!")
```

---

## 🔗 Condiciones Múltiples

Podemos combinar varias condiciones utilizando operadores lógicos como `and`, `or`, y `not`.

### `and`
El operador `and` devuelve `True` si ambas condiciones son verdaderas:

```python
edad = 16
tiene_carnet = True
if edad >= 18 and tiene_carnet:
  print("Puedes conducir 🚗")
else:
  print("POLICIA 🚔!!!1!!!")
```

### `or`
El operador `or` devuelve `True` si al menos una de las condiciones es verdadera:

```python
edad = 16
tiene_carnet = True
if edad >= 18 or tiene_carnet:
  print("Puedes conducir en la Isla Margarita 🚗")
else:
  print("Paga al policía y te deja conducir!!!")
```

### `not`
El operador `not` invierte el valor de una condición:

```python
es_fin_de_semana = False
if not es_fin_de_semana:
  print("¡No es fin de semana!")
```

---

## 🔁 Anidar Condicionales

Podemos colocar un condicional dentro de otro. Sin embargo, es recomendable evitar esta práctica si es posible para mantener el código más limpio.

```python
edad = 20
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la disco")
```

Una mejor forma de hacerlo es:

```python
if edad < 18:
  print("No puedes entrar a la disco")
elif tiene_dinero:
  print("Puedes ir a la discoteca")
else:
  print("Quédate en casa")
```

---

## 💡 Evaluación de Condiciones

En Python, ciertos valores son evaluados como `True` o `False` en una condición. Por ejemplo:

- El número `0` es considerado `False`.
- El número `5` es considerado `True`.
- Una cadena vacía `""` es considerada `False`.

```python
numero = 5
if numero: # True
  print("El número no es cero")

numero = 0
if numero: # False
  print("Aquí no entrará nunca")
```

---

## 🔀 Comparación y Asignación

Es importante no confundir la asignación `=` con la comparación `==`:

```python
numero = 3 # Asignación
es_el_tres = numero == 3 # Comparación

if es_el_tres:
  print("El número es 3")
```

---

## ⚡ Condicionales en Una Línea: Ternarias

Las condicionales también se pueden escribir en una sola línea con una expresión ternaria:

```python
edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)
```

---

# 🧠 Ejercicios

## Ejercicio 1: Determinar el mayor de dos números
Pide al usuario que introduzca dos números y muestra un mensaje indicando cuál es mayor o si son iguales.

```python
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Ambos números son iguales")
```

---

## Ejercicio 2: Calculadora simple
Pide al usuario dos números y una operación (`+`, `-`, `*`, `/`). Realiza la operación y muestra el resultado, manejando la división entre cero.

```python
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)
elif operacion == "*":
    print(num1 * num2)
elif operacion == "/":
    if num2 == 0:
        print("Error: No se puede dividir entre cero")
    else:
        print(num1 / num2)
else:
    print("Operación no válida")
```

---

## Ejercicio 3: Año bisiesto
Pide al usuario que introduzca un año y determina si es bisiesto. Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

```python
anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"{anio} es un año bisiesto")
else:
    print(f"{anio} no es un año bisiesto")
```

---

## Ejercicio 4: Categorizar edades
Pide al usuario que introduzca una edad y la clasifique en:

- Bebé (0-2 años)
- Niño (3-12 años)
- Adolescente (13-17 años)
- Adulto (18-64 años)
- Adulto mayor (65 años o más)

```python
edad = int(input("Introduce tu edad: "))

if edad <= 2:
    print("Eres un bebé")
elif edad <= 12:
    print("Eres un niño")
elif edad <= 17:
    print("Eres un adolescente")
elif edad <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
```