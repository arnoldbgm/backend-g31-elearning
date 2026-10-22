# 🎰 Reto Integrador: Tragamonedas

Vamos a construir un sistema de **máquinas tragamonedas** paso a paso, desde una clase vacía hasta un sistema completo con múltiples máquinas, apuestas y estadísticas.

Cada parte tiene un **Demo** (el profe explica el requerimiento y codea en vivo la solución) y un **Reto** (los alumnos resuelven sobre lo que ya construyeron).

Al final tendrán un programa funcional con POO de verdad.

---

## Parte 1: La clase `Tragamonedas` — Nace la máquina

### 1A — Demo: La máquina más básica

**Requerimiento**: Necesito una clase `Tragamonedas` que me permita crear máquinas con un nombre y una cantidad de créditos. Quiero poder crear varias máquinas fácilmente, sin tener que asignar atributos una por una.

👉 El profe lo codea en vivo.

<details>
<summary><b>Solución</b></summary>

```python
class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

maquina = Tragamonedas("La Siete", 100)
```
</details>

### 1B — Reto: Muestra los datos

Agrega un método `mostrar()` a la clase `Tragamonedas` que imprima algo como:

```
🎰 La Siete — Créditos: S/ 100
```

Crea 3 máquinas distintas:
- `"La Siete"` con 100 créditos
- `"La Frutal"` con 250 créditos
- `"Jackpot City"` con 500 créditos

Llama a `mostrar()` para cada una.

<details>
<summary><b>Solución</b></summary>

```python
class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    def mostrar(self):
        print(f"🎰 {self.nombre} — Créditos: S/ {self.creditos}")

m1 = Tragamonedas("La Siete", 100)
m2 = Tragamonedas("La Frutal", 250)
m3 = Tragamonedas("Jackpot City", 500)

m1.mostrar()
m2.mostrar()
m3.mostrar()
```
</details>

---

## Parte 2: ¡A girar! — Números aleatorios

### 2A — Demo: Primer giro

**Requerimiento**: Quiero que la máquina tragamonedas pueda **girar** y mostrar 3 números aleatorios. Cuando el usuario juegue, debe ver los números en pantalla y saber si ganó o perdió.

👉 El profe lo codea en vivo.

<details>
<summary><b>Solución</b></summary>

```python
import random

class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    def mostrar(self):
        print(f"🎰 {self.nombre} — Créditos: S/ {self.creditos}")

    def girar(self):
        resultado = []
        for _ in range(3):
            resultado.append(random.randint(1, 9))
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

maquina = Tragamonedas("La Siete", 100)
resultado = maquina.girar()
```
</details>

### 2B — Reto: Símbolos con emojis

Cambia los números por emojis de tragamonedas. Crea una lista de símbolos:

```python
simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
```

Modifica `girar()` para que genere 3 símbolos aleatorios de esa lista y los muestre así:

```
🎰 La Siete — Créditos: S/ 100
[ 🍒  💎  ⭐ ]
```

<details>
<summary><b>Solución</b></summary>

```python
import random

class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    def mostrar(self):
        print(f"🎰 {self.nombre} — Créditos: S/ {self.creditos}")

    def girar(self):
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

maquina = Tragamonedas("La Siete", 100)
maquina.mostrar()
maquina.girar()
```
</details>

---

## Parte 3: Apuestas y premios — El negocio

### 3A — Demo: Apostar y ganar

**Requerimiento**: Necesito un método `jugar(apuesta)` que:
1. Verifique si hay créditos suficientes
2. Reste la apuesta de los créditos
3. Llame a `girar()`
4. Revise si ganó:
   - **3 símbolos iguales**: jackpot (apuesta x10)
   - **2 iguales**: premio chico (apuesta x2)
   - **0 iguales**: pierde todo

👉 El profe lo codea en vivo.

<details>
<summary><b>Solución</b></summary>

```python
def jugar(self, apuesta):
    if apuesta > self.creditos:
        print(f"❌ No tienes suficiente saldo. Créditos: {self.creditos}")
        return

    self.creditos -= apuesta
    resultado = self.girar()

    if resultado[0] == resultado[1] == resultado[2]:
        premio = apuesta * 10
        print(f"🎉 ¡JACKPOT! Ganaste S/ {premio}")
        self.creditos += premio
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        premio = apuesta * 2
        print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")
        self.creditos += premio
    else:
        print(f"😢 Perdiste S/ {apuesta}")
```
</details>

### 3B — Reto: Bucle de juego

Crea un bucle donde el usuario pueda jugar varias veces:

```
🎰 La Siete — Créditos: S/ 100

¿Cuánto apuestas? (0 para salir): 10
[ 🍒  💎  ⭐ ]
😢 Perdiste S/ 10

¿Cuánto apuestas? (0 para salir): 5
[ 🍒  🍒  💎 ]
✨ ¡Dos iguales! Ganaste S/ 10

¿Cuánto apuestas? (0 para salir): 0
💰 Saliste con S/ 95. ¡Vuelve pronto!
```

El programa debe:
- Mostrar el estado actual antes de cada jugada
- Pedir cuánto apostar
- Llamar a `jugar(apuesta)`
- Salir cuando el usuario ponga 0
- Si el usuario se queda sin créditos, terminar el juego automáticamente

<details>
<summary><b>Solución</b></summary>

```python
import random

class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    def mostrar(self):
        print(f"🎰 {self.nombre} — Créditos: S/ {self.creditos}")

    def girar(self):
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        if apuesta > self.creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: {self.creditos}")
            return

        self.creditos -= apuesta
        resultado = self.girar()

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 10
            print(f"🎉 ¡JACKPOT! Ganaste S/ {premio}")
            self.creditos += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")
            self.creditos += premio
        else:
            print(f"😢 Perdiste S/ {apuesta}")

maquina = Tragamonedas("La Siete", 100)

while maquina.creditos > 0:
    maquina.mostrar()
    try:
        apuesta = int(input("¿Cuánto apuestas? (0 para salir): "))
    except ValueError:
        print("Ingresa un número válido.")
        continue

    if apuesta == 0:
        print(f"💰 Saliste con S/ {maquina.creditos}. ¡Vuelve pronto!")
        break

    maquina.jugar(apuesta)
else:
    print("💸 Te quedaste sin créditos. ¡GAME OVER!")
```
</details>

---

## Parte 4: Herencia — Diferentes tipos de máquinas

### 4A — Demo: Máquina de Frutas

**Requerimiento**: Quiero crear diferentes **tipos de máquinas** con sus propios símbolos. Una máquina de frutas (🍒🍋🍊), una máquina clásica de casino (7️⃣💎🔔). Todas deben compartir la lógica de `jugar()` y `mostrar()`, pero cada una debe girar con sus propios símbolos.

👉 El profe lo codea en vivo.

<details>
<summary><b>Solución</b></summary>

```python
class TragamonedasFrutas(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍓"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

class TragamonedasClasico(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["7️⃣", "💎", "🔔", "⭐", "💲", "🎰"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

m1 = TragamonedasFrutas("La Frutal", 200)
m2 = TragamonedasClasico("La Clásica", 300)

m1.mostrar()
m1.jugar(10)

m2.mostrar()
m2.jugar(20)
```
</details>

### 4B — Reto: Crea tu propia máquina

Crea una nueva clase que herede de `Tragamonedas`. Dale tu propio tema:

- `TragamonedasMundial` — símbolos de selecciones: 🇵🇪 🇦🇷 🇫🇷 🇧🇷
- `TragamonedasAnimales` — 🐶 🐱 🐼 🦁 🐸
- `TragamonedasEmojis` — el que se les ocurra

Además, **sobrescribe el método `jugar()`** para que la máquina tenga reglas diferentes. Por ejemplo:

- En tu máquina, **3 símbolos iguales** pagan x15 en lugar de x10
- O si sale un símbolo especial, hay premio extra

Ponle un nombre creativo y pruébala con varias jugadas.

<details>
<summary><b>Solución</b></summary>

```python
class TragamonedasMundial(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷", "🇪🇸", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        if apuesta > self.creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: {self.creditos}")
            return

        self.creditos -= apuesta
        resultado = self.girar()
        tiene_peru = "🇵🇪" in resultado

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 15
            print(f"🏆 ¡TRIPLETE! Ganaste S/ {premio}")
            self.creditos += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"⚽ ¡Dos iguales! Ganaste S/ {premio}")
            self.creditos += premio
        elif tiene_peru:
            premio = apuesta
            print(f"🇵🇪 ¡Perú apareció! Recuperas S/ {premio}")
            self.creditos += premio
        else:
            print(f"😢 Perdiste S/ {apuesta}")

mondial = TragamonedasMundial("Mundial 2026", 200)
mondial.mostrar()
for _ in range(5):
    mondial.jugar(10)
    print()
```
</details>

---

## Parte 5: Encapsulación y estadísticas — Versión profesional

### 5A — Demo: Protegiendo los créditos

**Requerimiento**: Hasta ahora cualquiera podría hacer `maquina.creditos = 999999` desde fuera y alterar el saldo. Eso no debería pasar. Necesito proteger los créditos para que solo se modifiquen a través de `jugar()`. Además, quiero llevar estadísticas de cuánto se ha apostado y ganado en total.

👉 El profe lo codea en vivo.

<details>
<summary><b>Solución</b></summary>

```python
class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self._creditos = creditos
        self._total_jugado = 0
        self._total_ganado = 0

    def mostrar(self):
        print(f"🎰 {self.nombre} — Créditos: S/ {self._creditos}")

    def girar(self):
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: {self._creditos}")
            return

        self._creditos -= apuesta
        self._total_jugado += apuesta
        resultado = self.girar()

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 10
            print(f"🎉 ¡JACKPOT! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        else:
            print(f"😢 Perdiste S/ {apuesta}")

    def mostrar_estadisticas(self):
        print(f"\n📊 Estadísticas de {self.nombre}")
        print(f"   Total apostado: S/ {self._total_jugado}")
        print(f"   Total ganado:  S/ {self._total_ganado}")
        balance = self._total_ganado - self._total_jugado
        signo = "+" if balance >= 0 else ""
        print(f"   Balance:       S/ {signo}{balance}")
```

Ahora `_creditos` es privado por convención. El guion bajo es una advertencia: "no toques esto directamente, usa los métodos de la clase".
</details>

### 5B — Reto: Sistema multi-máquina

Crea un programa que gestione **varias máquinas** a la vez:

1. Crea 3 máquinas de distintos tipos: una `TragamonedasFrutas`, una `TragamonedasClasico` y tu máquina personalizada
2. Muestra un menú para elegir máquina:

```
🎰 CASINO ROYALE 🎰

1. La Frutal (S/ 200)
2. La Clásica (S/ 300)
3. Mundial 2026 (S/ 150)
4. Mostrar estadísticas de todas
5. Salir

Elige una máquina: 1
```

3. Al elegir una máquina, entra al bucle de juego de esa máquina
4. La opción 4 muestra estadísticas de todas las máquinas
5. Si una máquina se queda en 0 créditos, muéstrala como "SIN CRÉDITOS" en el menú
6. Al salir, muestra un resumen general del casino

<details>
<summary><b>Solución</b></summary>

```python
import random

class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self._creditos = creditos
        self._total_jugado = 0
        self._total_ganado = 0

    def mostrar(self):
        estado = f"S/ {self._creditos}" if self._creditos > 0 else "💀 SIN CRÉDITOS"
        print(f"🎰 {self.nombre} — {estado}")

    def girar(self):
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        if self._creditos == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False
        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: {self._creditos}")
            return False

        self._creditos -= apuesta
        self._total_jugado += apuesta
        resultado = self.girar()

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 10
            print(f"🎉 ¡JACKPOT! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        else:
            print(f"😢 Perdiste S/ {apuesta}")
        return True

    def mostrar_estadisticas(self):
        print(f"   {self.nombre}")
        print(f"   Apostado: S/ {self._total_jugado} | Ganado: S/ {self._total_ganado}")
        balance = self._total_ganado - self._total_jugado
        signo = "+" if balance >= 0 else ""
        print(f"   Balance: S/ {signo}{balance} | Créditos actuales: S/ {self._creditos}")
        print()

class TragamonedasFrutas(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍓"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

class TragamonedasClasico(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["7️⃣", "💎", "🔔", "⭐", "💲", "🎰"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

class TragamonedasMundial(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷", "🇪🇸", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        if self._creditos == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False
        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: {self._creditos}")
            return False

        self._creditos -= apuesta
        self._total_jugado += apuesta
        resultado = self.girar()
        tiene_peru = "🇵🇪" in resultado

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 15
            print(f"🏆 ¡TRIPLETE! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"⚽ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif tiene_peru:
            print(f"🇵🇪 ¡Perú apareció! Recuperas tu apuesta.")
            self._creditos += apuesta
        else:
            print(f"😢 Perdiste S/ {apuesta}")
        return True

def jugar_en_maquina(maquina):
    while maquina._creditos > 0:
        maquina.mostrar()
        try:
            apuesta = int(input("¿Cuánto apuestas? (0 para volver al casino): "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if apuesta == 0:
            break

        maquina.jugar(apuesta)
        print()

maquinas = [
    TragamonedasFrutas("La Frutal", 200),
    TragamonedasClasico("La Clásica", 300),
    TragamonedasMundial("Mundial 2026", 150),
]

while True:
    print("\n" + "=" * 35)
    print("  🎰 CASINO ROYALE 🎰")
    print("=" * 35)

    for i, m in enumerate(maquinas, 1):
        estado = f"S/ {m._creditos}" if m._creditos > 0 else "💀 SIN CRÉDITOS"
        print(f"  {i}. {m.nombre} ({estado})")

    print(f"  {len(maquinas) + 1}. Mostrar estadísticas")
    print(f"  {len(maquinas) + 2}. Salir")

    try:
        opcion = int(input("\nElige una opción: "))
    except ValueError:
        print("Opción inválida.")
        continue

    if 1 <= opcion <= len(maquinas):
        maquina = maquinas[opcion - 1]
        if maquina._creditos == 0:
            print("💀 Esta máquina está sin créditos. Elige otra.")
        else:
            jugar_en_maquina(maquina)

    elif opcion == len(maquinas) + 1:
        print("\n📊 ESTADÍSTICAS DEL CASINO")
        print("-" * 35)
        for m in maquinas:
            m.mostrar_estadisticas()

    elif opcion == len(maquinas) + 2:
        print("\n💰 Gracias por visitar el Casino Royale. ¡Vuelve pronto!")
        break

    else:
        print("Opción inválida.")
```
</details>

---

## 🎯 Resumen de conceptos aplicados

| Parte | Concepto | Lo hicieron |
|-------|----------|-------------|
| 1 | Clase y constructor | Crearon `Tragamonedas` con `__init__` |
| 2 | Métodos y `random` | Implementaron `girar()` con emojis |
| 3 | Lógica de negocio | Sistema de apuestas con condiciones de premio |
| 4 | Herencia | Crearon máquinas hijas con distintos temas |
| 5 | Encapsulación | Protegieron el saldo con `_creditos` y agregaron estadísticas |

Este reto integrador cubre **todos los pilares de POO**: abstracción (modelar una máquina), herencia (tipos de máquinas), polimorfismo (cada `girar()` se comporta distinto) y encapsulación (`_creditos` protegido por convención).
