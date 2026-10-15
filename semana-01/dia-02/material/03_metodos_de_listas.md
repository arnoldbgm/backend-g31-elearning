# 🛠️ Métodos de Listas en Python

Los **métodos de lista** permiten **modificar**, **ordenar** y **consultar** listas de manera eficiente. A continuación encontrarás una selección de los más importantes.

---

## 📥 Añadir Elementos

- **`append(x)`**: Añade el elemento `x` al final de la lista.

  ```python
  lista.append('e')
  ```

- **`insert(i, x)`**: Inserta el elemento `x` en la posición `i`.

  ```python
  lista.insert(1, '@')
  ```

- **`extend(iterable)`**: Extiende la lista agregando todos los elementos del iterable.

  ```python
  lista.extend(['😃', '😍'])
  ```

---

## 📤 Eliminar Elementos

- **`remove(x)`**: Elimina la **primera** aparición de `x`. Lanza `ValueError` si no existe.

  ```python
  lista.remove('@')
  ```

- **`pop([i])`**: Elimina y devuelve el elemento en la posición `i`. Por defecto, el último.

  ```python
  ultimo = lista.pop()   # Elimina y devuelve el último
  segundo = lista.pop(1) # Elimina el elemento en índice 1
  ```

- **`del lista[i]`**: Elimina el elemento en el índice `i` sin devolverlo.

  ```python
  del lista[-1]
  ```

- **`clear()`**: Elimina **todos** los elementos de la lista.

  ```python
  lista.clear()
  ```

- **`del lista[start:stop]`**: Elimina un **rango** de elementos por slicing.

  ```python
  del lista[1:3]
  ```

---

## 🔄 Ordenar Listas

- **`sort()`**: Ordena la lista **in-place** (modifica la lista original).

  ```python
  numbers.sort()
  ```

- **`sorted(iterable)`**: Devuelve una **nueva lista** ordenada, sin modificar la original.

  ```python
  sorted_numbers = sorted(numbers)
  ```

- **`sort(key=func, reverse=True|False)`**: Ordena usando una función clave y permite orden inverso.

  ```python
  frutas.sort(key=str.lower)
  frutas.sort(reverse=True)
  ```

---

## 🔍 Consultar Listas

- **`len(lista)`**: Devuelve la longitud de la lista.
- **`lista.count(x)`**: Cuenta cuántas veces aparece `x`.
- **`x in lista`**: Devuelve `True` si `x` está en la lista.
- **`lista.index(x)`**: Devuelve el primer índice de `x` (lanza `ValueError` si no está).

```python
count_perros = animals.count('🐶')
esta_panda = '🐼' in animals
indice_limón = frutas.index('limón')
```

---

## 📑 Resumen de Métodos

| Método                     | Descripción                                    |
|----------------------------|------------------------------------------------|
| `append(x)`                | Añade `x` al final                             |
| `insert(i, x)`             | Inserta `x` en posición `i`                    |
| `extend(iterable)`         | Extiende con elementos del iterable            |
| `remove(x)`                | Quita la primera aparición de `x`              |
| `pop([i])`                 | Quita y devuelve elemento en índice `i`        |
| `del lista[i]`             | Elimina elemento en índice `i`                 |
| `clear()`                  | Elimina todos los elementos                    |
| `del lista[start:stop]`    | Elimina un rango de elementos                  |
| `sort()`                   | Ordena in-place                                |
| `sorted(iterable)`         | Devuelve nueva lista ordenada                  |
| `sort(key=func, reverse)`  | Ordena in-place con clave y orden inverso      |
| `len(lista)`               | Devuelve la longitud                           |
| `lista.count(x)`           | Cuenta apariciones de `x`                      |
| `x in lista`               | Comprueba si `x` está en la lista              |
| `lista.index(x)`           | Primer índice de aparición de `x`              |

---

# 🧩 Ejercicios

## Ejercicio 1: Añadir y Modificar Elementos
- Crea una lista con números del 1 al 5.  
- Añade `6` al final con `append()`.  
- Inserta `10` en la posición `2` con `insert()`.  
- Modifica el primer elemento para que sea `0`.

```python
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.insert(2, 10)
lista[0] = 0
print(lista)  # [0, 1, 10, 2, 3, 4, 5, 6]
```

## Ejercicio 2: Combinar y Limpiar Listas
- `lista_a = [1, 2, 3]`  
- `lista_b = [4, 5, 6, 1, 2]`  
- Extiende `lista_a` con `lista_b`.  
- Elimina la primera aparición de `1` en `lista_a`.  
- Elimina el elemento en índice `3` de `lista_a` con `pop()`.  
- Limpia completamente `lista_b` con `clear()`.

```python
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
lista_a.remove(1)
lista_a.pop(3)
lista_b.clear()
print(lista_a)  # [2, 3, 4, 6, 1, 2]
print(lista_b)  # []
```

## Ejercicio 3: Slicing y Eliminación con `del`
- Crea `lista = [1,2,3,4,5,6,7,8,9,10]`.  
- Usa `del` y slicing para eliminar índices `2` a `4` (sin incluir `4`).  
- Imprime la lista resultante.

```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista[2:4]
print(lista)  # [1, 2, 5, 6, 7, 8, 9, 10]
```

## Ejercicio 4: Ordenar y Contar
- Crea `nums = [5, 2, 8, 1, 9, 4, 2]`.  
- Ordena con `sort()`.  
- Cuenta cuántas veces aparece `2` con `count()`.  
- Comprueba si `7` está en la lista con `in`.

```python
nums = [5, 2, 8, 1, 9, 4, 2]
nums.sort()
count_2 = nums.count(2)
is_7_in_list = 7 in nums
print(nums)  # [1, 2, 2, 4, 5, 8, 9]
print(count_2)  # 2
print(is_7_in_list)  # False
```

## Ejercicio 5: Copia vs Referencia
- `original = [1,2,3]`  
- `copia_1 = original[:]`  
- `copia_2 = original.copy()`  
- `referencia = original`  
- Cambia `referencia[0] = 10`.  
- Imprime las cuatro listas para observar diferencias.

```python
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print(original)   # [10, 2, 3]
print(copia_1)    # [1, 2, 3]
print(copia_2)    # [1, 2, 3]
print(referencia) # [10, 2, 3]
```

## Ejercicio 6: Ordenar Strings Insensible a Mayúsculas
- `frutas = ["Manzana", "pera", "BANANA", "naranja"]`  
- Ordena sin diferenciar mayúsculas usando `sort(key=str.lower)`.

```python
frutas = ["Manzana", "pera", "BANANA", "naranja"]
frutas.sort(key=str.lower)
print(frutas)  # ['BANANA', 'Manzana', 'naranja', 'pera']   
```