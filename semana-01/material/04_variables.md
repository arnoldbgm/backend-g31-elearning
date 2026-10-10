# 🧠 Variables en Python: Guía Completa

Las **variables** son fundamentales en cualquier lenguaje de programación. En Python, se utilizan para almacenar datos en memoria, lo que permite trabajar con ellos a lo largo de la ejecución de un programa.

> 💡 **Dato útil**: Python es un lenguaje con **tipado dinámico** y **tipado fuerte**, lo que implica que el tipo de una variable se determina en tiempo de ejecución, pero no puedes mezclar tipos incompatibles sin generar un error.

## ✍️ Asignación de Variables

En Python, asignar una variable es muy sencillo. Solo necesitas asignarle un valor, y Python se encargará de determinar su tipo:

```python
my_name = "John Doe"
print(my_name)  # Salida: John Doe

age = 32
print(age)  # Salida: 32
```

Puedes **reasignar valores** a las variables de manera flexible, sin necesidad de declarar el tipo previamente:

```python
age = 39
print(age)  # Salida: 39
```

---

## 🔄 Tipado Dinámico

Python es un lenguaje de **tipado dinámico**, lo que significa que no es necesario declarar el tipo de una variable al momento de crearla. El tipo se determina en tiempo de ejecución:

```python
name = "John Doe"
print(type(name))  # Salida: <class 'str'>

name = 32
print(type(name))  # Salida: <class 'int'>
```

---

## 🧱 Tipado Fuerte

Aunque Python es dinámico, es **fuertemente tipado**, lo que significa que no permite hacer conversiones automáticas entre tipos incompatibles. Esto puede generar errores si intentas operar con tipos no compatibles:

```python
# Esto generaría un error:
# print(10 + "2")  # ❌ TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

---

## 🧵 Cadenas Formateadas con f-strings (Python 3.6+)

Desde la versión 3.6 de Python, puedes usar **f-strings** (cadenas literales formateadas) para incluir variables dentro de cadenas de forma fácil y eficiente:

```python
print(f"Hola {my_name}, tengo {age + 5} años")
# Salida: Hola John Doe, tengo 49 años
```

---

## 🚫 Recomendaciones para la Declaración de Variables

Es recomendable seguir ciertas convenciones y buenas prácticas al declarar variables. Una forma de hacerlo es utilizando el estilo **snake_case**, en lugar de **camelCase** o **PascalCase**, ya que Python lo favorece por convención:

```python
# Estilo recomendado: snake_case
mi_nombre_de_variable = "ok"

# Estilos no recomendados
miNombreDeVariable = "no-recomendado"  # ❌ camelCase
MiNombreDeVariable = "no-recomendado"  # ❌ PascalCase
```

---

## 📏 Convenciones para Nombres de Variables

En Python, hay ciertas reglas que se deben seguir al nombrar variables:

- Las variables deben comenzar con una letra o un guion bajo (`_`), **no con un número**.
- No se pueden utilizar **palabras reservadas** como `True`, `False`, `None`, `if`, `else`, etc.
- Los nombres de variables deben seguir un **formato coherente** y preferentemente en **snake_case**.

Ejemplo de uso de constantes:

```python
MI_CONSTANTE = 3.14  # Se usa en mayúsculas para denotar constantes
```

---

## ❌ Nombres Inválidos para Variables

Hay ciertos patrones que no son válidos y generarán errores en Python. Aquí algunos ejemplos:

```python
# 123variable = "no"  # ❌ No puede comenzar con un número
# mi-variable = "no"  # ❌ No se pueden usar guiones (-)
# mi variable = "no"  # ❌ No se pueden usar espacios
# True = False  # ❌ No se pueden sobrescribir palabras reservadas
```

---

## 🔒 Palabras Reservadas en Python

Existen palabras clave en Python que tienen un significado especial y no pueden ser utilizadas como nombres de variables. Estas incluyen:

```python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

---

## ✍️ Anotaciones de Tipo (Opcional)

Aunque no son obligatorias, las **anotaciones de tipo** proporcionan claridad al código y mejoran la comprensión de los tipos de datos esperados en las variables:

```python
is_user_logged_in: bool = True  # Indica que es un valor booleano
name: str = "John Doe"  # Indica que es una cadena de texto
```

---

## ✅ Conclusión

Las **variables** en Python son esenciales para almacenar y manipular datos en tus programas. Comprender cómo asignarlas, cómo seguir las buenas prácticas de nombres y cómo trabajar con el tipado dinámico y fuerte te permitirá escribir código más limpio, claro y eficiente.

Con estos conceptos, ahora estás listo para continuar con el aprendizaje de Python y dominar su sintaxis y características.