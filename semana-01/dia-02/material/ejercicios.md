# 🧠 Ejercicios — Día 2: Estructuras de datos y control de flujo

Cada tema tiene un **Demo** (el profe codea en vivo) y un **Reto** (los alumnos resuelven algo similar con una dificultad extra).

---

## 1. Listas + `for` — Recorrer y devolver valores

### 1A — Demo: Promedio de notas

```python
notas = [14, 8, 17, 11, 6, 20, 13, 9]
```

El profe muestra cómo usar un `for` para calcular:

1. El **promedio**
2. Cuántos **aprobaron** (nota >= 11)
3. La nota más **alta** y la más **baja**
4. Si alguien sacó **20**

> ⚠️ Usá `for`, no `sum()`, `max()` ni `min()`.

<details>
<summary><b>Solución (demo)</b></summary>

```python
notas = [14, 8, 17, 11, 6, 20, 13, 9]

suma = 0
aprobados = 0
mas_alta = notas[0]
mas_baja = notas[0]
hay_veinte = False

for nota in notas:
    suma += nota
    if nota >= 11:
        aprobados += 1
    if nota > mas_alta:
        mas_alta = nota
    if nota < mas_baja:
        mas_baja = nota
    if nota == 20:
        hay_veinte = True

promedio = suma / len(notas)

print(f"Promedio: {promedio:.1f}")
print(f"Aprobados: {aprobados} de {len(notas)}")
print(f"Nota mas alta: {mas_alta}")
print(f"Nota mas baja: {mas_baja}")
print(f"Alguien saco 20? {'Si' if hay_veinte else 'No'}")
```

</details>

---

### 1B — Reto: Temperaturas

Un sensor registró estas temperaturas en °C:

```python
temperaturas = [22, 31, 28, 35, 18, 40, 27, 33, 15]
```

Hacé un programa que:

1. Convierta cada temperatura a **Fahrenheit** (`°F = °C × 9/5 + 32`) y guarde los resultados en una nueva lista
2. Encuentre la temperatura más **alta** y la más **baja** (en °C)
3. Cuente cuántas superaron los **30°C**
4. Muestre el **promedio** en °C

**Plus:** Mostrá las temperaturas originales y convertidas en paralelo:

```
22°C = 71.6°F  |  31°C = 87.8°F  |  ...
```

<details>
<summary><b>Solución (reto)</b></summary>

```python
temperaturas = [22, 31, 28, 35, 18, 40, 27, 33, 15]

fahrenheit = []
suma = 0
mas_alta = temperaturas[0]
mas_baja = temperaturas[0]
calurosos = 0

for t in temperaturas:
    f = (t * 9/5) + 32
    fahrenheit.append(f)
    suma += t
    if t > mas_alta:
        mas_alta = t
    if t < mas_baja:
        mas_baja = t
    if t > 30:
        calurosos += 1

promedio = suma / len(temperaturas)

for i in range(len(temperaturas)):
    print(f"{temperaturas[i]}°C = {fahrenheit[i]:.1f}°F")

print(f"\nMas alta: {mas_alta}°C")
print(f"Mas baja: {mas_baja}°C")
print(f"Calurosos (>30°C): {calurosos}")
print(f"Promedio: {promedio:.1f}°C")
```

</details>

---

## 2. Listas + condicionales — Filtrar datos

### 2A — Demo: Filtrar productos baratos

```python
productos = [
    {"nombre": "Laptop", "precio": 2499.99, "stock": 15},
    {"nombre": "Mouse", "precio": 45.50, "stock": 30},
    {"nombre": "Teclado", "precio": 120.00, "stock": 8},
    {"nombre": "Parlante", "precio": 75.00, "stock": 20},
]
```

El profe muestra cómo:

1. Mostrar solo los productos con **precio menor a S/100**
2. Mostrar solo los que tienen **stock menor a 10**
3. Encontrar el **producto más caro**
4. Crear una lista de **nombres** de productos con más de 10 unidades (con comprensión de listas)

<details>
<summary><b>Solución (demo)</b></summary>

```python
productos = [
    {"nombre": "Laptop", "precio": 2499.99, "stock": 15},
    {"nombre": "Mouse", "precio": 45.50, "stock": 30},
    {"nombre": "Teclado", "precio": 120.00, "stock": 8},
    {"nombre": "Parlante", "precio": 75.00, "stock": 20},
]

print("Precio menor a S/100:")
for p in productos:
    if p["precio"] < 100:
        print(f"  - {p['nombre']} (S/{p['precio']:.2f})")

print("\nStock bajo (< 10):")
for p in productos:
    if p["stock"] < 10:
        print(f"  - {p['nombre']} (stock: {p['stock']})")

mas_caro = productos[0]
for p in productos:
    if p["precio"] > mas_caro["precio"]:
        mas_caro = p
print(f"\nMas caro: {mas_caro['nombre']} (S/{mas_caro['precio']:.2f})")

nombres = [p["nombre"] for p in productos if p["stock"] > 10]
print(f"Con mas de 10 unidades: {nombres}")
```

</details>

---

### 2B — Reto: Clientes morosos

```python
clientes = [
    {"nombre": "Ana", "deuda": 150.00, "dias_atraso": 45},
    {"nombre": "Luis", "deuda": 0, "dias_atraso": 0},
    {"nombre": "Sofia", "deuda": 320.50, "dias_atraso": 60},
    {"nombre": "Carlos", "deuda": 75.00, "dias_atraso": 15},
    {"nombre": "Marta", "deuda": 0, "dias_atraso": 0},
]
```

Hacé un programa que:

1. Muestre los **morosos** (deuda > 0) con su deuda
2. Muestre los **morosos graves** (deuda > 100 Y días_atraso > 30)
3. Encuentre el **cliente con mayor deuda**
4. Cree una lista de **nombres de clientes sin deuda** (usando comprensión)

**Plus:** Calculá el **total de deuda acumulada** y mostrala.

<details>
<summary><b>Solución (reto)</b></summary>

```python
clientes = [
    {"nombre": "Ana", "deuda": 150.00, "dias_atraso": 45},
    {"nombre": "Luis", "deuda": 0, "dias_atraso": 0},
    {"nombre": "Sofia", "deuda": 320.50, "dias_atraso": 60},
    {"nombre": "Carlos", "deuda": 75.00, "dias_atraso": 15},
    {"nombre": "Marta", "deuda": 0, "dias_atraso": 0},
]

total_deuda = 0
mayor_deudor = clientes[0]

print("Morosos:")
for c in clientes:
    if c["deuda"] > 0:
        total_deuda += c["deuda"]
        print(f"  - {c['nombre']}: S/{c['deuda']:.2f}")
        if c["deuda"] > mayor_deudor["deuda"]:
            mayor_deudor = c

print("\nMorosos graves (deuda > 100 y atraso > 30 dias):")
for c in clientes:
    if c["deuda"] > 100 and c["dias_atraso"] > 30:
        print(f"  - {c['nombre']}: S/{c['deuda']:.2f} ({c['dias_atraso']} dias)")

print(f"\nMayor deudor: {mayor_deudor['nombre']} (S/{mayor_deudor['deuda']:.2f})")

sin_deuda = [c["nombre"] for c in clientes if c["deuda"] == 0]
print(f"Clientes sin deuda: {sin_deuda}")

print(f"\nTotal de deuda acumulada: S/{total_deuda:.2f}")
```

</details>

---

## 3. Diccionarios — Guardar y consultar datos

### 3A — Demo: Producto en tienda

```python
producto = {
    "codigo": "LAP-001",
    "nombre": "Laptop Gamer",
    "precio": 3499.99,
    "stock": 10,
    "categoria": "Electronica",
}
```

El profe muestra cómo:

1. Acceder a cada valor por su clave
2. Usar `get()` para evitar errores
3. Mostrar solo las **keys** con `keys()`, solo los **valores** con `values()`
4. Actualizar el stock después de una venta
5. Agregar una nueva clave `"descuento"`

<details>
<summary><b>Solución (demo)</b></summary>

```python
producto = {
    "codigo": "LAP-001",
    "nombre": "Laptop Gamer",
    "precio": 3499.99,
    "stock": 10,
    "categoria": "Electronica",
}

print("Nombre:", producto["nombre"])
print("Precio: S/", producto["precio"])
print("Stock:", producto.get("stock", "No especificado"))
print("Marca:", producto.get("marca", "No disponible"))

print("\nClaves:", list(producto.keys()))
print("Valores:", list(producto.values()))

producto["stock"] = 8
print(f"\nStock actualizado: {producto['stock']}")

producto["descuento"] = 10
print(f"Descuento agregado: {producto['descuento']}%")

print("\nProducto final:")
for k, v in producto.items():
    print(f"  {k}: {v}")
```

</details>

---

### 3B — Reto: Catálogo de productos

```python
catalogo = [
    {"codigo": "LAP-001", "nombre": "Laptop Gamer", "precio": 3499.99, "stock": 5},
    {"codigo": "MOU-001", "nombre": "Mouse Inalambrico", "precio": 45.50, "stock": 20},
    {"codigo": "TEC-001", "nombre": "Teclado Mecanico", "precio": 120.00, "stock": 0},
    {"codigo": "MON-001", "nombre": "Monitor 4K", "precio": 899.00, "stock": 3},
]
```

Hacé un programa que:

1. Muestre todos los productos con su **código**, **nombre** y **precio**
2. Permita al usuario **buscar un producto por código** y mostrar todos sus datos
3. Si el producto no existe, muestre "Producto no encontrado, pe."
4. Muestre los productos con **stock en cero** (agotados)
5. Calcule el **valor total del inventario** (suma de precio × stock de cada producto)

<details>
<summary><b>Solución (reto)</b></summary>

```python
catalogo = [
    {"codigo": "LAP-001", "nombre": "Laptop Gamer", "precio": 3499.99, "stock": 5},
    {"codigo": "MOU-001", "nombre": "Mouse Inalambrico", "precio": 45.50, "stock": 20},
    {"codigo": "TEC-001", "nombre": "Teclado Mecanico", "precio": 120.00, "stock": 0},
    {"codigo": "MON-001", "nombre": "Monitor 4K", "precio": 899.00, "stock": 3},
]

print("=== CATALOGO ===")
for p in catalogo:
    print(f"{p['codigo']} | {p['nombre']} | S/{p['precio']:.2f}")

codigo = input("\nBuscar codigo: ")
encontrado = None
for p in catalogo:
    if p["codigo"] == codigo.upper():
        encontrado = p
        break

if encontrado:
    print(f"\nCodigo: {encontrado['codigo']}")
    print(f"Nombre: {encontrado['nombre']}")
    print(f"Precio: S/{encontrado['precio']:.2f}")
    print(f"Stock: {encontrado['stock']}")
else:
    print("Producto no encontrado, pe.")

print("\nAgotados:")
for p in catalogo:
    if p["stock"] == 0:
        print(f"  - {p['nombre']}")

valor_total = 0
for p in catalogo:
    valor_total += p["precio"] * p["stock"]
print(f"\nValor total del inventario: S/{valor_total:.2f}")
```

</details>

---

## 4. Diccionarios + `for` — Conteo y frecuencias

### 4A — Demo: Conteo de votos

```python
votos = ["Python", "JS", "Python", "Go", "Python", "JS", "Ruby", "Go", "Python"]
```

El profe muestra cómo usar un diccionario para contar frecuencias:

1. Recorrer la lista con `for`
2. Por cada elemento: si ya está en el diccionario, sumar 1; si no, inicializar en 1
3. Mostrar cada lenguaje con su cantidad de votos
4. Determinar el **ganador** (el que más votos tiene)

<details>
<summary><b>Solución (demo)</b></summary>

```python
votos = ["Python", "JS", "Python", "Go", "Python", "JS", "Ruby", "Go", "Python"]

conteo = {}

for v in votos:
    if v in conteo:
        conteo[v] += 1
    else:
        conteo[v] = 1

print("Resultados:")
for lenguaje in conteo:
    print(f"  {lenguaje}: {conteo[lenguaje]} voto(s)")

ganador = max(conteo, key=conteo.get)
print(f"\nGanador: {ganador} con {conteo[ganador]} votos!")
```

</details>

---

### 4B — Reto: Pedidos por mes

```python
pedidos = [
    {"mes": "Enero", "monto": 1200},
    {"mes": "Enero", "monto": 800},
    {"mes": "Febrero", "monto": 1500},
    {"mes": "Enero", "monto": 600},
    {"mes": "Febrero", "monto": 900},
    {"mes": "Marzo", "monto": 2000},
    {"mes": "Marzo", "monto": 1100},
    {"mes": "Febrero", "monto": 700},
]
```

Hacé un programa que:

1. Use un diccionario para contar **cuántos pedidos** hubo por mes
2. Use otro diccionario para sumar el **monto total** por mes
3. Muestre un resumen ordenado por mes:

```
Enero:   3 pedidos, S/2600.00
Febrero: 3 pedidos, S/3100.00
Marzo:   2 pedidos, S/3100.00
```

**Plus:** Determiná el mes con mayor monto acumulado.

<details>
<summary><b>Solución (reto)</b></summary>

```python
pedidos = [
    {"mes": "Enero", "monto": 1200},
    {"mes": "Enero", "monto": 800},
    {"mes": "Febrero", "monto": 1500},
    {"mes": "Enero", "monto": 600},
    {"mes": "Febrero", "monto": 900},
    {"mes": "Marzo", "monto": 2000},
    {"mes": "Marzo", "monto": 1100},
    {"mes": "Febrero", "monto": 700},
]

cantidad = {}
montos = {}

for p in pedidos:
    mes = p["mes"]
    if mes in cantidad:
        cantidad[mes] += 1
        montos[mes] += p["monto"]
    else:
        cantidad[mes] = 1
        montos[mes] = p["monto"]

print("Resumen de pedidos:")
for mes in cantidad:
    print(f"{mes}: {cantidad[mes]} pedidos, S/{montos[mes]:.2f}")

mejor_mes = max(montos, key=montos.get)
print(f"\nMes con mayor monto: {mejor_mes} (S/{montos[mejor_mes]:.2f})")
```

</details>

---

## 5. Funciones — Envolver lógica reutilizable

### 5A — Demo: Calcular factura

El profe muestra cómo crear una función que reciba datos y devuelva un resultado:

```python
def calcular_factura(precios, descuento=0, igv=True):
    # calcular subtotal, aplicar descuento, agregar IGV, devolver total
```

Probarla con:

```python
precios = [120.00, 45.50, 899.00, 250.00]
total = calcular_factura(precios, descuento=10)
```

La función debe mostrar el **desglose completo** (subtotal, descuento, IGV, total).

<details>
<summary><b>Solución (demo)</b></summary>

```python
def calcular_factura(precios, descuento=0, igv=True):
    subtotal = 0
    for p in precios:
        subtotal += p

    desc = subtotal * (descuento / 100)
    after_descuento = subtotal - desc
    impuesto = after_descuento * 0.18 if igv else 0
    total = after_descuento + impuesto

    print(f"Subtotal:      S/{subtotal:.2f}")
    if descuento > 0:
        print(f"Descuento({descuento}%): -S/{desc:.2f}")
    if igv:
        print(f"IGV (18%):     S/{impuesto:.2f}")
    print(f"Total:         S/{total:.2f}")
    return total

precios = [120.00, 45.50, 899.00, 250.00]
total = calcular_factura(precios, descuento=10)
print(f"\nTotal devuelto: S/{total:.2f}")
```

</details>

---

### 5B — Reto: Analizar ventas

Creá una función `analizar_ventas(ventas)` que reciba una lista como esta:

```python
ventas = [
    {"producto": "Laptop", "cantidad": 2, "precio": 2499.99},
    {"producto": "Mouse", "cantidad": 5, "precio": 45.50},
    {"producto": "Teclado", "cantidad": 3, "precio": 120.00},
    {"producto": "Monitor", "cantidad": 1, "precio": 899.00},
]
```

La función debe **devolver un diccionario** con:

- `"total_ingresos"`: suma de cantidad × precio de cada venta
- `"producto_mas_vendido"`: nombre del producto con mayor cantidad
- `"cantidad_total"`: suma de todas las cantidades
- `"ingresos_por_producto"`: diccionario con producto → ingreso generado

**Plus:** Hacé que acepte un parámetro opcional `min_ingreso` para filtrar productos que generaron menos de ese monto.

<details>
<summary><b>Solución (reto)</b></summary>

```python
def analizar_ventas(ventas, min_ingreso=0):
    total_ingresos = 0
    cantidad_total = 0
    ingresos_por_producto = {}
    cantidades = {}

    for v in ventas:
        ingreso = v["cantidad"] * v["precio"]
        total_ingresos += ingreso
        cantidad_total += v["cantidad"]

        prod = v["producto"]
        if prod in ingresos_por_producto:
            ingresos_por_producto[prod] += ingreso
            cantidades[prod] += v["cantidad"]
        else:
            ingresos_por_producto[prod] = ingreso
            cantidades[prod] = v["cantidad"]

    mas_vendido = max(cantidades, key=cantidades.get)

    resultado = {
        "total_ingresos": total_ingresos,
        "producto_mas_vendido": mas_vendido,
        "cantidad_total": cantidad_total,
        "ingresos_por_producto": ingresos_por_producto,
    }

    if min_ingreso > 0:
        filtrados = {
            p: i for p, i in ingresos_por_producto.items()
            if i >= min_ingreso
        }
        resultado["ingresos_filtrados"] = filtrados

    return resultado

ventas = [
    {"producto": "Laptop", "cantidad": 2, "precio": 2499.99},
    {"producto": "Mouse", "cantidad": 5, "precio": 45.50},
    {"producto": "Teclado", "cantidad": 3, "precio": 120.00},
    {"producto": "Monitor", "cantidad": 1, "precio": 899.00},
]

resultado = analizar_ventas(ventas, min_ingreso=200)
for k, v in resultado.items():
    print(f"{k}: {v}")
```

</details>

---

## 🎯 Resumen de conceptos

| Ejercicio | Listas | `for` | Dict | Funciones | Comprehensions |
|-----------|:------:|:-----:|:----:|:---------:|:--------------:|
| 1A. Demo: Promedio notas | ✅ | ✅ | | | |
| 1B. Reto: Temperaturas | ✅ | ✅ | | | |
| 2A. Demo: Filtrar productos | ✅ | ✅ | ✅ | | ✅ |
| 2B. Reto: Clientes morosos | ✅ | ✅ | ✅ | | ✅ |
| 3A. Demo: Producto tienda | | | ✅ | | |
| 3B. Reto: Catálogo productos | ✅ | ✅ | ✅ | | |
| 4A. Demo: Conteo votos | ✅ | ✅ | ✅ | | |
| 4B. Reto: Pedidos por mes | ✅ | ✅ | ✅ | | |
| 5A. Demo: Calcular factura | ✅ | ✅ | | ✅ | |
| 5B. Reto: Analizar ventas | ✅ | ✅ | ✅ | ✅ | ✅ |
