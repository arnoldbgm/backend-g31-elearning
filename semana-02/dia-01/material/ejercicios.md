# 🧠 Ejercicios — Día 1 (Semana 2): Funciones y manejo de errores

Cada tema tiene un **Demo** (el profe codea en vivo) y un **Reto** (los alumnos resuelven algo similar con una dificultad extra).

---

## 1. Funciones + `try-except` — Validar números

### 1A — Demo: ¿Es número o no?

El profe muestra una función simple que pide un número entero y lo devuelve. Si el usuario ingresa cualquier cosa que no sea número, muestra un mensaje de error.

```python
def pedir_entero(mensaje):
    # pedir un valor con input()
    # intentar convertirlo a int
    # si falla, mostrar "Eso no es un número"
    # si funciona, devolver el número
```

Probarla así:

```python
edad = pedir_entero("¿Cuántos años tenés? ")
print(f"Tenés {edad} años")
```

<details>
<summary><b>Solución (demo)</b></summary>

```python
def pedir_entero(mensaje):
    try:
        numero = int(input(mensaje))
        return numero
    except ValueError:
        print("Eso no es un número, pe.")

edad = pedir_entero("¿Cuántos años tenés? ")
print(f"Tenés {edad} años")
```

</details>

**¿Qué pasó?** Si el usuario ingresa un número válido, `int()` funciona y `edad` tiene el valor. Si ingresa cualquier otra cosa como "hola" o "12.5", `int()` lanza un `ValueError`, el `except` lo captura, muestra un mensaje y la función devuelve `None` (porque no hay `return`). El programa no se cae.

---

### 1B — Reto: ¿Es número y además válido?

Creá una función `pedir_nota(mensaje)` que pida un número entero **y** verifique que esté entre **0 y 20**. Si no es número o está fuera de rango, mostrá un mensaje distinto para cada caso.

Probala con:

```python
nota = pedir_nota("Ingresa tu nota: ")
if nota is not None:
    if nota >= 11:
        print(f"Aprobaste con {nota}")
    else:
        print(f"Desaprobaste con {nota}")
```

Llamala **dos veces** para pedir 2 notas. Mostrá el promedio final (solo si ambas son válidas).

**Plus:** Hacé que la función reciba un parámetro opcional `minimo=0` para personalizar el límite inferior.

<details>
<summary><b>Solución (reto)</b></summary>

```python
def pedir_nota(mensaje, minimo=0):
    try:
        nota = int(input(mensaje))
    except ValueError:
        print("Eso no es un número válido.")
        return None

    if nota < minimo or nota > 20:
        print(f"La nota debe estar entre {minimo} y 20.")
        return None

    return nota

nota1 = pedir_nota("Ingresa la primera nota: ")
nota2 = pedir_nota("Ingresa la segunda nota: ")

if nota1 is not None and nota2 is not None:
    promedio = (nota1 + nota2) / 2
    print(f"Promedio: {promedio}")
else:
    print("No se pudo calcular el promedio porque una nota no fue válida.")
```

</details>

---

## 2. Funciones + listas — Procesar datos con validación

### 2A — Demo: Buscar el número menor en una lista

El profe muestra una función que recibe una lista de números y devuelve el menor:

```python
def encontrar_menor(numeros):
    # validar que la lista no esté vacía
    # devolver el número más pequeño
```

Probarla con:

```python
datos = [15, 8, 23, 4, 19, 11]
print(f"El menor es: {encontrar_menor(datos)}")
```

Además, mostrar cómo manejar el caso de lista vacía (KeyError, IndexError o validación manual).

<details>
<summary><b>Solución (demo)</b></summary>

```python
def encontrar_menor(numeros):
    try:
        menor = numeros[0]
        for n in numeros:
            if n < menor:
                menor = n
        return menor
    except IndexError:
        print("La lista está vacía, no se puede encontrar el menor.")
        return None

datos = [15, 8, 23, 4, 19, 11]
print(f"El menor es: {encontrar_menor(datos)}")
```

</details>

---

### 2B — Reto: Analizador de lista

Creá una función `analizar_lista(numeros)` que reciba una lista de números y **devuelva un diccionario** con:

- `"promedio"`: el promedio
- `"mayor"`: el número más grande
- `"menor"`: el número más chico
- `"hay_negativos"`: True si hay al menos un número negativo

La función debe:
- Lanzar `ValueError` si la lista está vacía
- Lanzar `TypeError` si algún elemento no es número (usá `isinstance(n, (int, float))`)

Probala con estas listas:

```python
lista1 = [15, 8, 23, 4, 19, 11]
lista2 = []
lista3 = [10, "abc", 20]
```

Mostrá los resultados o los errores según corresponda.

**Plus:** Agregá un parámetro opcional `ignorar_errores=True` que, en vez de lanzar excepción, devuelva `None` si hay error.

<details>
<summary><b>Solución (reto)</b></summary>

```python
def analizar_lista(numeros, ignorar_errores=False):
    try:
        if not numeros:
            raise ValueError("La lista está vacía.")

        suma = 0
        mayor = numeros[0]
        menor = numeros[0]
        hay_negativos = False

        for n in numeros:
            if not isinstance(n, (int, float)):
                raise TypeError(f"Elemento '{n}' no es un número.")
            suma += n
            if n > mayor:
                mayor = n
            if n < menor:
                menor = n
            if n < 0:
                hay_negativos = True

        return {
            "promedio": suma / len(numeros),
            "mayor": mayor,
            "menor": menor,
            "hay_negativos": hay_negativos,
        }
    except (ValueError, TypeError) as e:
        if ignorar_errores:
            return None
        print(f"Error: {e}")
        return None

lista1 = [15, 8, 23, 4, 19, 11]
lista2 = []
lista3 = [10, "abc", 20]

for nombre, datos in [("lista1", lista1), ("lista2", lista2), ("lista3", lista3)]:
    resultado = analizar_lista(datos)
    print(f"{nombre}: {resultado}")
```

</details>

---

## 3. Funciones + diccionarios — Consultas con errores controlados

### 3A — Demo: Buscar cliente por código

El profe crea una función que busca un cliente por su código en un diccionario y devuelve sus datos:

```python
clientes = {
    "CL001": {"nombre": "Ana", "deuda": 150},
    "CL002": {"nombre": "Luis", "deuda": 0},
    "CL003": {"nombre": "Sofía", "deuda": 320},
}

def buscar_cliente(codigo):
    # devolver los datos del cliente
    # lanzar KeyError si no existe
```

Probarla con un código que existe y otro que no, mostrando cómo se maneja el error.

<details>
<summary><b>Solución (demo)</b></summary>

```python
clientes = {
    "CL001": {"nombre": "Ana", "deuda": 150},
    "CL002": {"nombre": "Luis", "deuda": 0},
    "CL003": {"nombre": "Sofía", "deuda": 320},
}

def buscar_cliente(codigo):
    try:
        return clientes[codigo.upper()]
    except KeyError:
        print(f"Cliente '{codigo}' no encontrado.")
        return None

dato = buscar_cliente("CL001")
if dato:
    print(f"Cliente: {dato['nombre']}, Deuda: S/{dato['deuda']}")

dato = buscar_cliente("CL999")
if dato:
    print(f"Cliente: {dato['nombre']}, Deuda: S/{dato['deuda']}")
```

</details>

---

### 3B — Reto: Cajero automático

Creá un diccionario con cuentas bancarias:

```python
cuentas = {
    "123": {"titular": "Ana", "saldo": 1500.00},
    "456": {"titular": "Luis", "saldo": 300.00},
    "789": {"titular": "Sofía", "saldo": 2500.00},
}
```

Implementá las siguientes **funciones**:

1. `consultar_saldo(num_cuenta)` — devuelve el saldo actual
2. `depositar(num_cuenta, monto)` — suma el monto al saldo
3. `retirar(num_cuenta, monto)` — resta el monto si hay saldo suficiente

**Reglas:**
- Cada función debe manejar sus propios errores con `try-except` **dentro de la función**
- Si la cuenta no existe, mostrá un mensaje y devolvé `None`
- Si el monto no es válido (no número, cero o negativo), mostrá un mensaje y devolvé `None`
- Si no hay saldo suficiente para retirar, mostrá un mensaje y devolvé `None`

Probá cada función mostrando resultados exitosos y errores.

**Plus:** Creá una función `transferir(origen, destino, monto)` que use `retirar` y `depositar` internamente, manejando los errores de ambas.

<details>
<summary><b>Solución (reto)</b></summary>

```python
cuentas = {
    "123": {"titular": "Ana", "saldo": 1500.00},
    "456": {"titular": "Luis", "saldo": 300.00},
    "789": {"titular": "Sofía", "saldo": 2500.00},
}

def consultar_saldo(num_cuenta):
    try:
        return cuentas[num_cuenta]["saldo"]
    except KeyError:
        print(f"Cuenta '{num_cuenta}' no existe.")
        return None

def depositar(num_cuenta, monto):
    try:
        if num_cuenta not in cuentas:
            raise KeyError
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")
        cuentas[num_cuenta]["saldo"] += monto
        return cuentas[num_cuenta]["saldo"]
    except KeyError:
        print(f"Cuenta '{num_cuenta}' no existe.")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None

def retirar(num_cuenta, monto):
    try:
        if num_cuenta not in cuentas:
            raise KeyError
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")
        if cuentas[num_cuenta]["saldo"] < monto:
            raise ValueError(f"Saldo insuficiente. Disponible: S/{cuentas[num_cuenta]['saldo']:.2f}")
        cuentas[num_cuenta]["saldo"] -= monto
        return cuentas[num_cuenta]["saldo"]
    except KeyError:
        print(f"Cuenta '{num_cuenta}' no existe.")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None

def transferir(origen, destino, monto):
    saldo_origen = retirar(origen, monto)
    if saldo_origen is not None:
        depositar(destino, monto)
        return True
    return False

# Pruebas
print("=== CONSULTAS ===")
saldo = consultar_saldo("123")
if saldo is not None:
    print(f"Cuenta 123: S/{saldo:.2f}")

saldo = consultar_saldo("999")
if saldo is not None:
    print(f"Cuenta 999: S/{saldo:.2f}")

print("\n=== DEPÓSITOS ===")
nuevo = depositar("123", 500)
if nuevo is not None:
    print(f"Nuevo saldo cuenta 123: S/{nuevo:.2f}")

print("\n=== RETIROS ===")
nuevo = retirar("456", 400)
if nuevo is not None:
    print(f"Nuevo saldo cuenta 456: S/{nuevo:.2f}")

print("\n=== TRANSFERENCIA ===")
if transferir("456", "789", 100):
    print(f"Transferencia exitosa.")
    print(f"Saldo 456: S/{consultar_saldo('456'):.2f}")
    print(f"Saldo 789: S/{consultar_saldo('789'):.2f}")
```

</details>

---

## 4. Funciones + list comprehension — Filtrar y transformar datos

### 4A — Demo: Filtrar números pares

El profe muestra cómo crear una función que filtre solo los números pares de una lista usando comprensión de listas:

```python
def obtener_pares(numeros):
    # validar que la lista no esté vacía
    # devolver una nueva lista solo con los pares
```

Probarla con:

```python
datos = [15, 8, 23, 4, 19, 11, 6, 30, 7]
print(obtener_pares(datos))
```

Además mostrar cómo validar que todos los elementos sean números.

<details>
<summary><b>Solución (demo)</b></summary>

```python
def obtener_pares(numeros):
    try:
        if not numeros:
            raise ValueError("La lista está vacía.")

        for n in numeros:
            if not isinstance(n, (int, float)):
                raise TypeError(f"Elemento '{n}' no es un número.")

        return [n for n in numeros if n % 2 == 0]
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return []

datos = [15, 8, 23, 4, 19, 11, 6, 30, 7]
pares = obtener_pares(datos)
print(f"Números pares: {pares}")
```

</details>

---

### 4B — Reto: Clasificar y transformar

Creá una función `clasificar_numeros(numeros)` que reciba una lista de números y devuelva un diccionario con:

- `"pares"`: lista de números pares
- `"impares"`: lista de números impares
- `"mayores_que_10"`: lista de números mayores a 10
- `"doblados"`: lista con cada número multiplicado por 2

**Requisitos:**
- Usá comprensión de listas para cada clasificación
- Si la lista está vacía, lanzá `ValueError`
- Si algún elemento no es número, lanzá `TypeError`
- Probala con `datos = [3, 15, 8, 22, 7, 30, 11, 4]`

**Plus:** Agregá un parámetro opcional `solo_positivos=True` que filtre solo números positivos antes de clasificar (si `solo_positivos=True` y hay negativos, lanzá `ValueError`).

<details>
<summary><b>Solución (reto)</b></summary>

```python
def clasificar_numeros(numeros, solo_positivos=True):
    try:
        if not numeros:
            raise ValueError("La lista está vacía.")

        for n in numeros:
            if not isinstance(n, (int, float)):
                raise TypeError(f"Elemento '{n}' no es un número.")

        if solo_positivos:
            for n in numeros:
                if n < 0:
                    raise ValueError(f"Se encontró un número negativo ({n}) y solo se aceptan positivos.")
            datos = numeros
        else:
            datos = numeros

        return {
            "pares": [n for n in datos if n % 2 == 0],
            "impares": [n for n in datos if n % 2 != 0],
            "mayores_que_10": [n for n in datos if n > 10],
            "doblados": [n * 2 for n in datos],
        }
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return {}

datos = [3, 15, 8, 22, 7, 30, 11, 4]
resultado = clasificar_numeros(datos)
if resultado:
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")
```

</details>

---

## 5. Integración total — Procesar ventas con persistencia

### 5A — Demo: Registrar ventas

El profe muestra cómo crear un programa que registre ventas en una lista de diccionarios:

```python
def registrar_venta(ventas, producto, cantidad, precio):
    # validar que cantidad y precio sean números positivos
    # agregar un diccionario {"producto": ..., "cantidad": ..., "precio": ..., "total": ...}
    # devolver la lista actualizada
```

Probarla registrando 3 ventas y mostrando la lista final.

<details>
<summary><b>Solución (demo)</b></summary>

```python
def registrar_venta(ventas, producto, cantidad, precio):
    try:
        cantidad = int(cantidad)
        precio = float(precio)

        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return ventas
        if precio <= 0:
            print("El precio debe ser mayor a cero.")
            return ventas

        ventas.append({
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio,
            "total": cantidad * precio,
        })
    except (ValueError, TypeError):
        print("Cantidad y precio deben ser números.")

    return ventas

ventas = []
ventas = registrar_venta(ventas, "Laptop", 2, 2499.99)
ventas = registrar_venta(ventas, "Mouse", 5, 45.50)
ventas = registrar_venta(ventas, "Teclado", 3, 120.00)

for v in ventas:
    print(f"{v['producto']}: {v['cantidad']} x S/{v['precio']:.2f} = S/{v['total']:.2f}")
```

</details>

---

### 5B — Reto: Sistema completo de ventas

Creá las siguientes funciones para administrar ventas:

```python
def registrar_venta(ventas, producto, cantidad, precio):
    """Valida los datos, agrega la venta a la lista y la devuelve."""

def mostrar_resumen(ventas):
    """Muestra todas las ventas en formato tabular y el total general."""

def buscar_producto(ventas, nombre):
    """Filtra ventas cuyo nombre contenga el texto (sin importar mayúsculas). Devuelve la lista filtrada."""

def producto_mas_vendido(ventas):
    """Devuelve el nombre del producto con mayor cantidad vendida."""
```

**Programa principal:**

Usando las funciones, creá un programa que:

1. Registre **3 ventas** fijas (sin pedir input) usando `registrar_venta` con datos de prueba
2. Muestre el resumen con `mostrar_resumen`
3. Busque un producto con `buscar_producto` y muestre los resultados
4. Muestre cuál fue el producto más vendido con `producto_mas_vendido`

**Reglas:**
- `registrar_venta` debe validar que cantidad y precio sean números positivos con `try-except` **dentro de la función**
- `registrar_venta` debe mostrar el error por consola si los datos son inválidos
- El formato tabular debe verse así:

```
Producto             Cant  Precio     Total
---------------------------------------------
Laptop                  2 S/2499.99 S/ 4999.98
Mouse                   5 S/  45.50 S/  227.50
---------------------------------------------
            TOTAL GENERAL S/ 5227.48
```

**Plus:** Agregá una función `ventas_por_rango(ventas, min_precio, max_precio)` que devuelva una nueva lista con las ventas cuyo precio esté dentro del rango, y mostrá el resultado al final.

<details>
<summary><b>Solución (reto)</b></summary>

```python
def registrar_venta(ventas, producto, cantidad, precio):
    try:
        cantidad = int(cantidad)
        precio = float(precio)

        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return ventas
        if precio <= 0:
            print("El precio debe ser mayor a cero.")
            return ventas
        if not producto.strip():
            print("El nombre del producto no es válido.")
            return ventas

        ventas.append({
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio,
            "total": round(cantidad * precio, 2),
        })
        print(f"Venta de '{producto}' registrada con éxito.")
    except (ValueError, TypeError):
        print("Cantidad y precio deben ser números.")

    return ventas

def mostrar_resumen(ventas):
    if not ventas:
        print("No hay ventas registradas.")
        return

    total_general = 0
    print(f"{'Producto':<20} {'Cant':>5} {'Precio':>8} {'Total':>10}")
    print("-" * 45)
    for v in ventas:
        print(f"{v['producto']:<20} {v['cantidad']:>5} S/{v['precio']:>6.2f} S/{v['total']:>7.2f}")
        total_general += v["total"]
    print("-" * 45)
    print(f"{'TOTAL GENERAL':>33} S/{total_general:>7.2f}")

def buscar_producto(ventas, nombre):
    return [v for v in ventas if nombre.lower() in v["producto"].lower()]

def producto_mas_vendido(ventas):
    if not ventas:
        return None

    cantidades = {}
    for v in ventas:
        if v["producto"] in cantidades:
            cantidades[v["producto"]] += v["cantidad"]
        else:
            cantidades[v["producto"]] = v["cantidad"]

    return max(cantidades, key=cantidades.get)

def ventas_por_rango(ventas, min_precio, max_precio):
    return [v for v in ventas if min_precio <= v["precio"] <= max_precio]

# --- Programa principal ---

ventas = []
ventas = registrar_venta(ventas, "Laptop", 2, 2499.99)
ventas = registrar_venta(ventas, "Mouse", 5, 45.50)
ventas = registrar_venta(ventas, "Teclado", 3, 120.00)
ventas = registrar_venta(ventas, "Monitor", 1, 0)  # debe fallar

print("\n=== RESUMEN DE VENTAS ===")
mostrar_resumen(ventas)

print("\n=== BUSCAR PRODUCTO: 'lap' ===")
resultados = buscar_producto(ventas, "lap")
if resultados:
    for v in resultados:
        print(f"  {v['producto']}: {v['cantidad']} x S/{v['precio']:.2f}")
else:
    print("  No se encontraron resultados.")

print("\n=== PRODUCTO MÁS VENDIDO ===")
mas_vendido = producto_mas_vendido(ventas)
if mas_vendido:
    print(f"  {mas_vendido}")
else:
    print("  No hay ventas registradas.")

print("\n=== VENTAS ENTRE S/50 Y S/500 ===")
rango = ventas_por_rango(ventas, 50, 500)
if rango:
    for v in rango:
        print(f"  {v['producto']} - S/{v['precio']:.2f}")
else:
    print("  No hay ventas en ese rango.")
```

</details>

---

## 🎯 Resumen de conceptos

| Ejercicio | Funciones | `try-except` | Listas | Dict | `for` | `raise` | Comprensión |
|-----------|:---------:|:------------:|:------:|:----:|:-----:|:-------:|:-----------:|
| 1A. Demo: ¿Es número o no? | ✅ | ✅ | | | | | |
| 1B. Reto: ¿Es número y válido? | ✅ | ✅ | | | | | |
| 2A. Demo: Buscar el menor | ✅ | ✅ | ✅ | | ✅ | ✅ | |
| 2B. Reto: Analizador de lista | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | |
| 3A. Demo: Buscar cliente | ✅ | ✅ | | ✅ | | ✅ | |
| 3B. Reto: Cajero automático | ✅ | ✅ | | ✅ | | ✅ | |
| 4A. Demo: Filtrar pares | ✅ | ✅ | ✅ | | ✅ | ✅ | ✅ |
| 4B. Reto: Clasificar datos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 5A. Demo: Registrar ventas | ✅ | ✅ | ✅ | ✅ | | ✅ | |
| 5B. Reto: Sistema ventas | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
