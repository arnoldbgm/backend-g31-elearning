# 🧠 Introducción a las Funciones en Python

Las funciones en Python son bloques de código reutilizables que te permiten organizar tu programa en partes lógicas. Son fundamentales para escribir código limpio, organizado y reutilizable.

---

## 🔧 ¿Qué es una función?

Una función es un bloque de código que solo se ejecuta cuando se le llama. Puedes pasarle datos (argumentos) y puede devolver un resultado.

---

## ✨ Definir una función

Usamos la palabra clave `def` para definir una función.

```python
def saludar():
    print("¡Hola!")
```

Llamamos a la función así:

```python
saludar()  # Salida: ¡Hola!
```

---

## 📦 Funciones con parámetros

```python
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Paolo")  # Salida: ¡Hola, Paolo!
```

---

## 🔄 Retornar valores

Puedes devolver valores con `return`.

```python
def cuadrado(numero):
    return numero * numero

resultado = cuadrado(5)
print(resultado)  # Salida: 25
```

---

## 🔢 Múltiples parámetros

```python
def sumar(a, b):
    return a + b

print(sumar(3, 7))  # Salida: 10
```

---

## 🧮 Funciones con valores por defecto

```python
def saludar(nombre="invitado"):
    print(f"¡Hola, {nombre}!")

saludar()            # Salida: ¡Hola, invitado!
saludar("Paolo")     # Salida: ¡Hola, Paolo!
```

---

## 🌟 Funciones con número variable de argumentos

### *args — argumentos posicionales:

```python
def mostrar_numeros(*numeros):
    for numero in numeros:
        print(numero)

mostrar_numeros(1, 2, 3)
```

### **kwargs — argumentos con nombre:

```python
def mostrar_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Paolo", edad=30)
```

---

## 🧪 Funciones anidadas

```python
def exterior():
    def interior():
        print("Soy una función dentro de otra.")
    interior()

exterior()
```

---

## 🔄 Funciones recursivas

Una función que se llama a sí misma.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Salida: 120
```

---

## ✅ Conclusión

Las funciones te permiten dividir tu programa en piezas reutilizables y legibles. Entender cómo declararlas, llamarlas y usarlas correctamente es clave en tu camino como desarrollador.
