# 📘 Diccionarios en Python

Los diccionarios en Python son estructuras de datos que permiten almacenar **pares clave-valor**. Son muy útiles cuando queremos representar datos que están relacionados entre sí.

---

## 🔹 ¿Qué es un diccionario?

Un diccionario es una colección **desordenada**, **mutable** y **indexada** por claves. Se define usando llaves `{}`.

```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}
```

---

## 🧪 Acceder a los valores

Puedes acceder a un valor usando su clave:

```python
print(persona["nombre"])  # Ana
```

También puedes usar `get()` para evitar errores si la clave no existe:

```python
print(persona.get("altura", "No disponible"))
```

---

## ✏️ Modificar y agregar elementos

```python
persona["edad"] = 31  # Modificar valor existente
persona["profesión"] = "Ingeniera"  # Agregar nuevo par clave-valor
```

---

## ❌ Eliminar elementos

```python
del persona["ciudad"]
persona.pop("edad")
```

---

## 🛠️ Métodos útiles

```python
persona.keys()    # Devuelve las claves
persona.values()  # Devuelve los valores
persona.items()   # Devuelve claves y valores como tuplas
```

---

## 🔁 Recorrer un diccionario

```python
for clave in persona:
    print(clave, "->", persona[clave])

# o con items():
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

---

## 🧪 Diccionarios anidados

Puedes tener diccionarios dentro de diccionarios:

```python
estudiantes = {
    "001": {"nombre": "Carlos", "edad": 20},
    "002": {"nombre": "Lucía", "edad": 22}
}
print(estudiantes["001"]["nombre"])  # Carlos
```

---

## ✨ Ejercicios

### Ejercicio 1: Crear un diccionario

Crea un diccionario con información sobre un libro (título, autor, año) e imprímelo.

```python
libro = {
    "titulo": "El libro de las mil",
    "autor": "Juan Rulfo",
    "anio": 1994
}
```

---

### Ejercicio 2: Buscar clave

Pide al usuario una clave y verifica si existe en el diccionario. Si existe, imprime su valor.

```python
diccionario = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}
clave = input("Introduce la clave a buscar: ")
if clave in diccionario:
    print(diccionario[clave])
else:
    print("Clave no encontrada")
```

---

### Ejercicio 3: Contador de palabras

Pide al usuario una frase y muestra cuántas veces aparece cada palabra utilizando un diccionario como contador.

---

### Ejercicio 4: Agenda de contactos

Crea un programa que permita agregar contactos (nombre y teléfono) a un diccionario y luego mostrar todos los contactos guardados.

---

## ✅ Conclusión

Los diccionarios son fundamentales en Python. Te permiten estructurar la información de forma muy flexible y eficiente. ¡Son como pequeñas bases de datos en memoria!

---