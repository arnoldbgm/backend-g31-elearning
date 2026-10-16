# 🛡️ Manejo de Errores con `try-except`

Los errores pasan. Siempre. Un usuario ingresa texto donde esperabas un número, un archivo no existe, la conexión a internet falla. En vez de que tu programa explote con un mensaje críptico, Python te da herramientas para **anticipar y manejar** esos errores de forma elegante.

---

## ⚠️ ¿Qué es una excepción?

Una **excepción** es un error que ocurre mientras tu programa se ejecuta. Cuando ocurre, Python detiene el programa y muestra un **traceback**:

```python
numero = int(input("Ingresa un número: "))
# Si el usuario escribe "hola", Python lanza:
# ValueError: invalid literal for int() with base 10: 'hola'
```

En lugar de que el programa se caiga, nosotros podemos **capturar** esa excepción y manejarla.

---

## 🧱 Estructura básica: `try` / `except`

```python
try:
    numero = int(input("Ingresa un número: "))
    print(f"Tu número es {numero}")
except:
    print("Eso no fue un número válido.")
```

El bloque `try` ejecuta el código peligroso. Si algo sale mal, el bloque `except` atrapa el error y ejecuta su propio código.

---

## 🎯 Capturar excepciones específicas

Usar `except` sin especificar el tipo atrapa **cualquier error**, lo cual no es buena práctica. Siempre capturá la excepción específica que esperás:

```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"10 / {numero} = {resultado}")
except ValueError:
    print("Eso no era un número válido.")
except ZeroDivisionError:
    print("No se puede dividir entre cero, causa.")
```

Cada `except` captura un tipo distinto de error. Si ocurre un `ValueError`, salta al primer bloque; si es `ZeroDivisionError`, al segundo.

---

## 🔗 `else` y `finally`

### `else` — se ejecuta si NO hubo error

```python
try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("No es un número válido.")
else:
    print(f"El cuadrado de {numero} es {numero ** 2}")
```

### `finally` — se ejecuta SIEMPRE, haya error o no

```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Esto se ejecuta siempre.")
    archivo.close()
```

`finally` es ideal para liberar recursos (cerrar archivos, conexiones, etc.).

---

## 🧩 Varias excepciones en un solo `except`

Podés capturar múltiples excepciones en el mismo bloque usando una tupla:

```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 100 / numero
except (ValueError, ZeroDivisionError):
    print("Error: ingresa un número diferente de cero.")
```

---

## 🆘 `raise` — lanzar tus propias excepciones

A veces querés **crear** un error intencionalmente si algo no cumple las reglas de tu programa:

```python
def votar(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad >= 18:
        return "Puedes votar"
    return "No puedes votar"

print(votar(25))   # Puedes votar
print(votar(-5))   # ValueError: La edad no puede ser negativa.
```

Combinado con `try-except`:

```python
try:
    print(votar(-5))
except ValueError as error:
    print(f"Error: {error}")
```

La variable `error` captura el mensaje que le pasamos a `raise`.

---

## 📋 Excepciones comunes en Python

| Excepción | Cuándo ocurre |
|-----------|---------------|
| `ValueError` | Función recibe argumento del tipo correcto pero valor inapropiado (ej. `int("hola")`) |
| `ZeroDivisionError` | Dividir o módulo por cero |
| `TypeError` | Operación con tipo incorrecto (ej. `"texto" + 5`) |
| `IndexError` | Índice fuera de rango en una lista |
| `KeyError` | Clave que no existe en un diccionario |
| `FileNotFoundError` | Archivo que no existe al intentar abrirlo |
| `NameError` | Variable no definida |

---

## ✅ Buenas prácticas

1. **Sé específico**: capturá la excepción concreta, no uses `except` genérico
2. **No te comas el error**: si capturás una excepción, al menos mostrá un mensaje útil
3. **Usá `else`** para el código que solo debe ejecutarse si no hubo error
4. **Usá `finally`** para limpiar recursos (archivos, conexiones)
5. **No uses `try-except` para control de flujo normal**, solo para errores reales
6. **Capturá el error con `as`** si necesitás mostrar el mensaje original
7. **Validá antes de operar**: si podés evitar el error con un `if`, hacelo primero

---

## ✅ Conclusión

`try-except` no es para cubrir tus errores de lógica, sino para manejar situaciones que **no podés controlar**: input del usuario, archivos que faltan, conexiones que fallan. Es tu red de seguridad para que el programa no se caiga ante lo inesperado. Usalo con criterio y tu código será mucho más robusto.
