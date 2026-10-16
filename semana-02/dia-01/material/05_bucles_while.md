# 🔁 Introducción a los bucles `while` en Python

Los bucles `while` permiten ejecutar un bloque de código **repetidamente** mientras se cumpla una condición. Son ideales cuando no sabemos cuántas veces necesitaremos repetir algo, y solo queremos parar al cumplirse cierta condición.

> 💡 **Dato útil**: Un bucle `while` puede ejecutarse infinitamente si no se actualiza la condición correctamente.

---

## 🔢 Contador simple con `while`

```python
print("\n🔢 Bucle while simple")

i = 0
while i <= 5:
    print(i)
    i += 1  # ¡No olvides esto o el bucle será infinito!
```

---

## 🚪 Salir de un bucle con `break`

```python
print("\n🚪 Bucle while con break")

i = 0
while True:
    print(i)
    i += 1
    if i == 5:
        break  # Rompe el bucle cuando i es 5
```

---

## ⏭ Saltar iteraciones con `continue`

```python
print("\n⏭ Bucle while con continue")

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Salta los números pares
    print(i)
```

---

## 🧠 Ejercicios prácticos con `while`

### 1️⃣ Cuenta regresiva del 10 al 1

```python
print("\n⏳ Cuenta regresiva")

i = 10
while i > 0:
    print(i)
    i -= 1
```

---

### 2️⃣ Suma de números pares del 1 al 20

```python
print("\n➕ Suma de pares entre 1 y 20")

i = 1
suma = 0
while i <= 20:
    if i % 2 == 0:
        suma += i
    i += 1
print(f"Suma total: {suma}")
```

---

### 3️⃣ Calcular el factorial de un número

```python
print("\n🧮 Factorial de un número")

num = int(input("Introduce un número entero positivo: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"{num}! = {factorial}")
```

---

### 4️⃣ Validar una contraseña

```python
print("\n🔐 Validación de contraseña")

password = ""
while len(password) < 8:
    password = input("Introduce una contraseña (mínimo 8 caracteres): ")
    if len(password) < 8:
        print("❌ Demasiado corta.")
print("✅ Contraseña válida")
```

---

### 5️⃣ Tabla de multiplicar

```python
print("\n📊 Tabla de multiplicar")

n = int(input("Introduce un número: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
```

---

### 6️⃣ Números primos hasta N

```python
print("\n🔎 Números primos hasta N")

n = int(input("Introduce un número: "))
i = 2

while i <= n:
    es_primo = True
    j = 2
    while j * j <= i:
        if i % j == 0:
            es_primo = False
            break
        j += 1
    if es_primo:
        print(i)
    i += 1
```