# 🧠 Ejercicios — Día 1: Fundamentos de Python

Ejercicios progresivos combinando `print()`, variables, tipos, casting, condicionales, operadores lógicos y ternarios.

---

## Ejercicio 1: Presentación profesional

Crea un programa que:

1. Pida al usuario: **nombre**, **edad**, **ciudad** y **lenguaje favorito**
2. Muestre una presentación como esta:

```
Hola, soy [nombre], tengo [edad] años, vivo en [ciudad] y programo en [lenguaje favorito].
```

3. Además, muestra el **tipo de dato** de cada variable usando `type()`
4. Calcula y muestra el **año de nacimiento aproximado** (asumiendo que ya cumplió años este año)

<details>
<summary><b>Solución</b></summary>

```python
nombre = input("Nombre: ")
edad = int(input("Edad: "))
ciudad = input("Ciudad: ")
lenguaje = input("Lenguaje favorito: ")

print(f"Hola, soy {nombre}, tengo {edad} anios, vivo en {ciudad} y programo en {lenguaje}.")

print(f"Tipo de nombre: {type(nombre)}")
print(f"Tipo de edad: {type(edad)}")
print(f"Tipo de ciudad: {type(ciudad)}")
print(f"Tipo de lenguaje: {type(lenguaje)}")

anio_nacimiento = 2026 - edad
print(f"Naciste aproximadamente en el anio {anio_nacimiento}.")
```

</details>

---

## Ejercicio 2: El analizador de tipos automático

Escribe un programa que:

1. Pida **un valor** al usuario (puede ser número, texto o cualquier cosa)
2. Sin usar `if`, determine qué tipo de dato es y muestre un mensaje como:
   - `<class 'int'>` → "Es un número entero"
   - `<class 'float'>` → "Es un número decimal"
   - `<class 'str'>` → "Es un texto"
   - `<class 'bool'>` → "Es un booleano"
3. **Reto:** Si es texto, muestra cuántos caracteres tiene usando `len()`

> **Pista:** `input()` siempre devuelve string. Para cambiar el tipo tenés que hacer casting. Pero podés comparar `type(valor)` directamente con `str`, `int`, etc.

<details>
<summary><b>Solución</b></summary>

```python
dato = input("Ingresa un valor: ")

if type(dato) == str:
    print("Es un texto")
    print(f"Tiene {len(dato)} caracteres")
elif type(dato) == int:
    print("Es un numero entero")
elif type(dato) == float:
    print("Es un numero decimal")
elif type(dato) == bool:
    print("Es un booleano")
```

</details>

---

## Ejercicio 3: Calculadora con menú

Crea un programa que muestre este menú:

```
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
```

El usuario elige una opción, ingresa **dos números**, y el programa muestra el resultado.

**Requisitos:**
- Si el usuario ingresa algo que no es un número, mostrá "Error: ingresa un número válido."
- Si elige dividir entre cero, mostrá "Error: no se puede dividir entre cero, causa."
- Si elige una opción inválida, mostrá "Opción inválida."


<details>
<summary><b>Solución</b></summary>

```python
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opcion (1-4): ")


num1 = float(input("Primer numero: "))
num2 = float(input("Segundo numero: "))

if opcion == "1":
    print(f"Resultado: {num1 + num2}")
elif opcion == "2":
    print(f"Resultado: {num1 - num2}")
elif opcion == "3":
    print(f"Resultado: {num1 * num2}")
elif opcion == "4":
    if num2 == 0:
        print("Error: no se puede dividir entre cero, causa.")
    else:
        print(f"Resultado: {num1 / num2}")
else:
    print("Opcion invalida.")

```

</details>

---

## Ejercicio 4: Sistema de votación peruano

Pide al usuario su **edad** y si **tiene DNI** (s/n). Determiná si puede votar según las reglas de Perú:

- Menor de 16 → No puede votar
- De 16 a 17 → Voto optativo (si tiene DNI)
- De 18 a 69 → Voto obligatorio (si tiene DNI)
- 70 a más → Voto optativo (si tiene DNI)
- Si no tiene DNI → No puede votar, sin importar la edad

**Plus:** Si tiene 18+ pero no tiene DNI, mostrale: "Tramitá tu DNI ahorita".

<details>
<summary><b>Solución</b></summary>

```python
edad = int(input("Cuantos anios tienes? "))
tiene_dni = input("Tienes DNI? (s/n): ").lower()

if not tiene_dni == "s":
    print("No puedes votar porque no tienes DNI.")
    if edad >= 18:
        print("Tramita tu DNI ahorita.")
elif edad < 16:
    print("No puedes votar, eres muy pequenio.")
elif edad <= 17:
    print("Voto optativo.")
elif edad <= 69:
    print("Voto obligatorio.")
else:
    print("Voto optativo por edad.")
```

</details>

---

## Ejercicio 5: Tienda de ropa con descuentos combinados

Una tienda vende **remeras a S/25** y **jeans a S/60**. Ofrece descuentos por cantidad:

- 3+ remeras → **10% de descuento** en remeras
- 2+ jeans → **15% de descuento** en jeans
- Si el total (con descuentos aplicados) supera S/200 → **5% adicional** sobre el total final

Pide al usuario cuántas remeras y cuántos jeans compra. Mostrá el desglose completo:

```
Remeras: 3 x S/25 = S/75.00
Descuento remeras: -S/7.50
Jeans: 2 x S/60 = S/120.00
Descuento jeans: -S/18.00
Subtotal: S/169.50
Descuento adicional: -S/8.48
Total final: S/161.02
```

> **Pista:** Usá `round(valor, 2)` para mantener dos decimales.

<details>
<summary><b>Solución</b></summary>

```python
PRECIO_REMERA = 25
PRECIO_JEAN = 60

remeras = int(input("Cuantas remeras compras? "))
jeans = int(input("Cuantos jeans compras? "))

total_remeras = remeras * PRECIO_REMERA
total_jeans = jeans * PRECIO_JEAN
desc_remeras = 0
desc_jeans = 0

print(f"Remeras: {remeras} x S/{PRECIO_REMERA} = S/{total_remeras:.2f}")

if remeras >= 3:
    desc_remeras = total_remeras * 0.10
    print(f"Descuento remeras: -S/{desc_remeras:.2f}")

print(f"Jeans: {jeans} x S/{PRECIO_JEAN} = S/{total_jeans:.2f}")

if jeans >= 2:
    desc_jeans = total_jeans * 0.15
    print(f"Descuento jeans: -S/{desc_jeans:.2f}")

subtotal = total_remeras + total_jeans - desc_remeras - desc_jeans
print(f"Subtotal: S/{subtotal:.2f}")

if subtotal > 200:
    desc_adicional = subtotal * 0.05
    print(f"Descuento adicional: -S/{desc_adicional:.2f}")
    subtotal -= desc_adicional

print(f"Total final: S/{subtotal:.2f}")
```

</details>

---

## Ejercicio 6: Adivina el número (con pistas de distancia)

El programa guarda un número secreto entre **1 y 50**. El usuario intenta adivinarlo. El programa responde:

- **"¡Ganaste!"** si acierta
- **"¡Estuviste cerca!"** si la diferencia es exactamente 1
- **"Caliente"** si la diferencia está entre 2 y 5
- **"Tibio"** si la diferencia está entre 6 y 10
- **"Frío"** si la diferencia es mayor a 10
- Además, siempre muestra si el número ingresado está **por encima o por debajo** del secreto

**Plus:** Si el usuario ingresa un número fuera del rango 1-50, mostrá un mensaje de advertencia pero permití que intente igual.

<details>
<summary><b>Solución</b></summary>

```python
SECRETO = 37

numero = int(input("Adivina el numero secreto (1-50): "))

if numero < 1 or numero > 50:
    print("Ojo: el numero deberia estar entre 1 y 50.")

if numero == SECRETO:
    print("Ganaste!")
else:
    if numero < SECRETO:
        print("Esta por debajo.")
    else:
        print("Esta por encima.")

    diferencia = abs(numero - SECRETO)

    if diferencia == 1:
        print("Estuviste cerca!")
    elif diferencia <= 5:
        print("Caliente")
    elif diferencia <= 10:
        print("Tibio")
    else:
        print("Frio")
```

</details>

---

## Ejercicio 7: Conversor de temperaturas

Crea un programa que muestre un menú:

```
1. Celsius -> Fahrenheit
2. Fahrenheit -> Celsius
3. Celsius -> Kelvin
4. Kelvin -> Celsius
```

El usuario elige una opción e ingresa el valor. El programa muestra el resultado con **2 decimales**.

**Reglas:**
- No se puede bajar de **-273.15°C** (cero absoluto). Si el usuario intenta convertir una temperatura menor, mostrá "Temperatura inválida: no puede estar por debajo del cero absoluto."
- En Kelvin, no se puede ingresar valores negativos.

**Plus:** Si la opción no es válida (1-4), mostrá "Opción inválida, causa."

<details>
<summary><b>Solución</b></summary>

```python
print("1. Celsius -> Fahrenheit")
print("2. Fahrenheit -> Celsius")
print("3. Celsius -> Kelvin")
print("4. Kelvin -> Celsius")

opcion = int(input("Elige una opcion (1-4): "))

if opcion == 1:
    celsius = float(input("Grados Celsius: "))
    if celsius < -273.15:
        print("Temperatura invalida: no puede estar por debajo del cero absoluto.")
    else:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
elif opcion == 2:
    fahrenheit = float(input("Grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    if celsius < -273.15:
        print("Temperatura invalida: no puede estar por debajo del cero absoluto.")
    else:
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
elif opcion == 3:
    celsius = float(input("Grados Celsius: "))
    if celsius < -273.15:
        print("Temperatura invalida: no puede estar por debajo del cero absoluto.")
    else:
        kelvin = celsius + 273.15
        print(f"{celsius}°C = {kelvin:.2f} K")
elif opcion == 4:
    kelvin = float(input("Grados Kelvin: "))
    if kelvin < 0:
        print("Temperatura invalida: Kelvin no puede ser negativo.")
    else:
        celsius = kelvin - 273.15
        print(f"{kelvin} K = {celsius:.2f}°C")
else:
    print("Opcion invalida, causa.")
```

</details>

---

## Ejercicio 8: Fortaleza de contraseñas

Pide al usuario que **cree una contraseña** y evaluá su fortaleza:

- **Débil**: menos de 6 caracteres
- **Media**: entre 6 y 10 caracteres
- **Fuerte**: más de 10 caracteres Y contiene al menos un número (`isdigit()`)
- **Muy fuerte**: más de 12 caracteres, contiene número, y NO es "contraseña" ni "123456789"

Mostrá un mensaje como:
```
Fortaleza: Fuerte ✓
```

**Plus:** Si la contraseña tiene menos de 4 caracteres, mostrá "Eso no es una contraseña, es un suspiro."

<details>
<summary><b>Solución</b></summary>

```python
password = input("Crea una contrasenia: ")

tiene_numero = False
for caracter in password:
    if caracter.isdigit():
        tiene_numero = True
        break

if len(password) < 4:
    print("Eso no es una contrasenia, es un suspiro.")
elif password == "contrasenia" or password == "123456789":
    print("Fortaleza: Debil (contrasenia muy comun)")
elif len(password) > 12 and tiene_numero:
    print("Fortaleza: Muy fuerte \u2713")
elif len(password) > 10 and tiene_numero:
    print("Fortaleza: Fuerte \u2713")
elif len(password) >= 6:
    print("Fortaleza: Media")
else:
    print("Fortaleza: Debil")
```

</details>

---

## Ejercicio 9: Validador de fechas

Pide al usuario un **día**, un **mes** y un **año** (por separado). El programa debe determinar si la fecha es **válida** o no.

**Reglas:**
- Los meses van de 1 a 12
- Los días dependen del mes:
  - Meses con **31 días**: enero (1), marzo (3), mayo (5), julio (7), agosto (8), octubre (10), diciembre (12)
  - Meses con **30 días**: abril (4), junio (6), setiembre (9), noviembre (11)
  - **Febrero (2)**: 28 días normalmente, **29 si es año bisiesto**
- Un año es bisiesto si:
  - Es divisible por 4, **pero** si es divisible por 100 también debe ser divisible por 400

**Ejemplos:**
```
Día: 29, Mes: 2, Año: 2024 → Fecha válida (bisiesto)
Día: 29, Mes: 2, Año: 2025 → Fecha inválida (no es bisiesto)
Día: 31, Mes: 4, Año: 2026 → Fecha inválida (abril tiene 30 días)
Día: 15, Mes: 13, Año: 2026 → Fecha inválida (mes 13 no existe)
```

> **Pista:** Usá el operador `%` para verificar divisibilidad. Primero validá el mes, después los días según el mes.

<details>
<summary><b>Solución</b></summary>

```python
dia = int(input("Dia: "))
mes = int(input("Mes: "))
anio = int(input("Anio: "))

# Validar mes
if mes < 1 or mes > 12:
    print("Fecha invalida: mes no existe.")
else:
    # Determinar máximo de días según el mes
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dias = 31
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    else:  # mes == 2 (febrero)
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            max_dias = 29
        else:
            max_dias = 28

    # Validar día
    if dia < 1 or dia > max_dias:
        print("Fecha invalida.")
    else:
        print("Fecha valida!")
```

</details>

---

## Ejercicio 10: Cifrado César simple (reto)

El cifrado César desplaza cada letra un número fijo de posiciones en el alfabeto. Crea un programa que:

1. Pida una **letra minúscula** (de la 'a' a la 'z')
2. Pida un **número de desplazamiento** (1-10)
3. Muestre la letra resultante después del desplazamiento

**Reglas:**
- Usá `ord()` y `chr()` para convertir entre caracteres y números
- Si el desplazamiento se pasa de la 'z', debe **volver a empezar desde la 'a'** (circular)
- Si el usuario ingresa mayúscula, convertila automáticamente a minúscula con `.lower()`
- Si no ingresa una letra del alfabeto, mostrá "Eso no es una letra válida, pe."

**Ejemplos:**
```
Letra: z, Desplazamiento: 1 → a
Letra: a, Desplazamiento: 3 → d
Letra: m, Desplazamiento: 10 → w
```

<details>
<summary><b>Solución</b></summary>

```python
letra = input("Ingresa una letra (a-z): ").lower()
desplazamiento = int(input("Desplazamiento (1-10): "))

if len(letra) != 1 or not letra.isalpha():
    print("Eso no es una letra valida, pe.")
else:
    codigo = ord(letra)
    nueva_posicion = (codigo - ord("a") + desplazamiento) % 26
    letra_cifrada = chr(nueva_posicion + ord("a"))
    print(f"{letra} + {desplazamiento} = {letra_cifrada}")
```

</details>

---

## 🎯 Resumen de conceptos aplicados

| Ejercicio | `print()` | Variables | `type()` | Casting | Condicionales | Operadores lógicos | Ternario | Strings |
|-----------|:---------:|:---------:|:--------:|:-------:|:-------------:|:------------------:|:--------:|:-------:|
| 1. Presentación profesional | ✅ | ✅ | ✅ | ✅ | | | | |
| 2. Analizador de tipos | ✅ | ✅ | ✅ | | ✅ | | | ✅ |
| 3. Calculadora todoterreno | ✅ | ✅ | | ✅ | ✅ | ✅ | | ✅ |
| 4. Votación peruano | ✅ | ✅ | | ✅ | ✅ | ✅ | | |
| 5. Tienda descuentos | ✅ | ✅ | | ✅ | ✅ | | | |
| 6. Adivina distancia | ✅ | ✅ | | ✅ | ✅ | | | |
| 7. Conversor temperaturas | ✅ | ✅ | | ✅ | ✅ | | | |
| 8. Fortaleza contraseñas | ✅ | ✅ | | | ✅ | ✅ | | ✅ |
| 9. Analizador triángulos | ✅ | ✅ | | ✅ | ✅ | ✅ | | |
| 10. Cifrado César | ✅ | ✅ | | ✅ | ✅ | | | ✅ |
