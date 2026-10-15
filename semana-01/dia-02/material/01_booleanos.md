# 🔘 Booleanos en Python

Los **booleanos** son valores lógicos fundamentales en programación, representando **Verdadero** (`True`) o **Falso** (`False`). Son esenciales para el **control de flujo**, la **toma de decisiones** y la **lógica de tus programas**.

> 💡 **Dato útil**: En Python, los booleanos son una subclase de los enteros (`int`), donde `True` equivale a `1` y `False` a `0`, pero siempre deben usarse para representar condiciones lógicas.

---

## 📊 Valores Booleanos Básicos

```python
print(True)   # Salida: True
print(False)  # Salida: False
```

---

## ⚖️ Operadores de Comparación

Los operadores de comparación comparan valores y devuelven un booleano:

| Operador | Descripción                  | Ejemplo          | Resultado |
|----------|------------------------------|------------------|-----------|
| `>`      | Mayor que                    | `5 > 3`          | True      |
| `<`      | Menor que                    | `5 < 3`          | False     |
| `==`     | Igualdad                     | `5 == 5`         | True      |
| `!=`     | Desigualdad                  | `5 != 3`         | True      |
| `>=`     | Mayor o igual que            | `5 >= 5`         | True      |
| `<=`     | Menor o igual que            | `5 <= 3`         | False     |

**Comparación de cadenas**:

```python
print("manzana" < "pera")  # True (orden alfabético)
print("Hola" == "hola")    # False (distinción entre mayúsculas)
```

---

## 🔗 Operadores Lógicos

Combina booleanos para crear expresiones más complejas:

- `and`: True si **ambos** operandos son verdaderos.
- `or`: True si **al menos uno** de los operandos es verdadero.
- `not`: Invierte el valor de un booleano.

```python
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

---

## 📋 Tablas de Verdad

### `and`

| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

### `or`

| A     | B     | A or B  |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |

### `not`

| A     | not A |
|-------|-------|
| True  | False |
| False | True  |

---

## ✅ Buenas Prácticas

1. **Evita** usar valores no booleanos en condiciones (`0`, `""`, `None`). Es más claro usar comparaciones explícitas.
2. **Parentiza** expresiones lógicas complejas para mejorar la legibilidad:
   ```python
   if (a > b and not c) or d:
       # ...
   ```
3. **Documenta** tus condiciones si son complejas, con comentarios que expliquen la lógica.

---

## ✅ Conclusión

Los booleanos y sus operadores son la base de la lógica de tus programas en Python. Comprender cómo combinarlos y usarlos correctamente te permitirá controlar el flujo de ejecución y tomar decisiones en tu código de forma clara y eficiente.