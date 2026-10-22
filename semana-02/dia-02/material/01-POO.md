# ⚽ Programación Orientada a Objetos con Python

Aprender POO con ejemplos del fútbol. Porque si entiendes cómo se arma un equipo, entiendes cómo se arma una clase.

---

## 📋 ¿Por qué clases? El problema antes de las clases

Imagina que quieres guardar información de jugadores para el Mundial:

```python
# Sin clases — datos sueltos
nombre1 = "Lionel Messi"
edad1 = 37
posicion1 = "Delantero"
equipo1 = "Argentina"

nombre2 = "Kylian Mbappé"
edad2 = 27
posicion2 = "Delantero"
equipo2 = "Francia"
```

Esto funciona para 2 jugadores. ¿Y para 26? Olvídate. Tienes 104 variables sueltas, sin relación entre ellas. Si quieres agregar un método (`celebrar`, `correr`), no hay dónde ponerlo.

**Las clases resuelven esto**: agrupan datos (atributos) y comportamiento (métodos) en un solo lugar.

```python
# Con una clase — todo organizado
class Jugador:
    pass

messi = Jugador()
messi.nombre = "Lionel Messi"
messi.edad = 37

mbappe = Jugador()
mbappe.nombre = "Kylian Mbappé"
mbappe.edad = 27
```

Ya estamos agrupando, pero aún toca asignar atributo por atributo afuera. Ahí entra el constructor.

---

## ⚙️ El constructor `__init__`

Cuando creas un jugador, sabes de entrada su nombre, edad y posición. El constructor te permite recibir esos datos al **momento de crear el objeto**.

```python
class Jugador:
    def __init__(self, nombre, edad, posicion, equipo):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo

messi = Jugador("Lionel Messi", 37, "Delantero", "Argentina")
mbappe = Jugador("Kylian Mbappé", 27, "Delantero", "Francia")
```

Ahora cada `Jugador` **nace con sus datos puestos**. No olvidas ninguno porque el constructor te obliga a pasarlos.

- `self` es una referencia al **propio objeto**. Piensa en él como "este jugador en específico".
- Los parámetros del `__init__` son los datos que cada jugador necesita para existir.

---

## 🎯 Métodos: dale comportamiento

Un jugador no solo tiene datos, también **hace cosas**: correr, celebrar, patear. En POO eso son los métodos.

```python
class Jugador:
    def __init__(self, nombre, edad, posicion, equipo):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo

    def celebrar(self):
        print(f"¡{self.nombre} celebra el gol! ¡GOOOOOOL!")

    def correr(self):
        print(f"{self.nombre} está corriendo por la banda.")

    def mostrar_info(self):
        print(f"{self.nombre} | {self.edad} años | {self.posicion} | {self.equipo}")

messi = Jugador("Lionel Messi", 37, "Delantero", "Argentina")
messi.mostrar_info()
messi.celebrar()
```

Los métodos trabajan con los datos del propio objeto a través de `self`.

---

## 🧩 Abstracción

**Abstracción** significa modelar un objeto del mundo real solo con los detalles que nos interesan, ignorando el resto.

Cuando creamos la clase `Jugador`, no nos importa su tipo de sangre, su color de ojos ni cómo duerme. Nos importa su **nombre, edad, posición y equipo** porque eso es lo relevante para un sistema de fútbol.

La abstracción te permite:
- Enfocarte en **qué hace** algo, no en **cómo lo hace** por dentro.
- Reducir la complejidad: modelas solo lo necesario.

```python
class Equipo:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        print(f"{jugador.nombre} se ha unido a {self.nombre}")

argentina = Equipo("Selección Argentina", "Argentina")
argentina.agregar_jugador(messi)
```

No necesitas saber cómo funciona internamente `agregar_jugador`. Solo usas el método. Eso es abstracción.

---

## 🧬 Herencia

En un equipo hay jugadores de diferentes posiciones, y cada posición tiene comportamientos específicos. La herencia permite crear clases **hijas** que heredan todo de una clase **padre** y añaden lo suyo.

```python
class Jugador:
    def __init__(self, nombre, edad, equipo):
        self.nombre = nombre
        self.edad = edad
        self.equipo = equipo

    def entrenar(self):
        print(f"{self.nombre} está entrenando.")

class Arquero(Jugador):
    def __init__(self, nombre, edad, equipo):
        super().__init__(nombre, edad, equipo)
        self.posicion = "Arquero"

    def atajar(self):
        print(f"{self.nombre} vuela y ataja el penal! ❄️")

class Delantero(Jugador):
    def __init__(self, nombre, edad, equipo, dorsal):
        super().__init__(nombre, edad, equipo)
        self.posicion = "Delantero"
        self.dorsal = dorsal

    def definir(self):
        print(f"{self.nombre} (camiseta {self.dorsal}) define con clase y GOL.")

dibu = Arquero("Emiliano Martínez", 32, "Argentina")
dibu.entrenar()   # ✅ Heredado de Jugador
dibu.atajar()     # ✅ Propio de Arquero

juli = Delantero("Julián Álvarez", 26, "Argentina", 19)
juli.entrenar()   # ✅ Heredado
juli.definir()    # ✅ Propio de Delantero
```

`super().__init__()` llama al constructor de la clase padre. Así no repites código: el nombre, edad y equipo los inicializa `Jugador`.

---

## 🔄 Polimorfismo

**Polimorfismo** significa "muchas formas". La misma acción se comporta diferente según el tipo de objeto.

```python
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

    def celebrar(self):
        print(f"{self.nombre} celebra.")

class Arquero(Jugador):
    def celebrar(self):
        print(f"{self.nombre} grita: ¡ATAJÉ, NO ME LA COMO!")

class Delantero(Jugador):
    def celebrar(self):
        print(f"{self.nombre} corre y se desliza de rodillas.")

# Polimorfismo en acción
jugadores = [
    Arquero("Emiliano Martínez"),
    Delantero("Lionel Messi"),
    Delantero("Kylian Mbappé"),
]

for jugador in jugadores:
    jugador.celebrar()
# Cada uno celebra a su manera, con el mismo método.
```

Cada clase **sobrescribe** el método `celebrar()` con su propia implementación. El código que los llama no necesita saber qué tipo de jugador es — solo llama a `.celebrar()` y cada uno responde como corresponde.

---

## 🔐 Encapsulación

La encapsulación protege los datos de un objeto para que no sean modificados accidentalmente desde fuera.

En Python usamos convención: un guion bajo `_` significa "esto es privado, no lo toques desde afuera".

```python
class Contrato:
    def __init__(self, jugador, salario):
        self.jugador = jugador
        self._salario = salario   # Privado por convención

    def mostrar_salario(self):
        print(f"{self.jugador} gana ${self._salario:,} por temporada.")

    def aumentar_salario(self, bono):
        self._salario += bono
        print(f"✅ Bono aplicado. Nuevo salario: ${self._salario:,}")

c = Contrato("Lionel Messi", 40_000_000)
c.mostrar_salario()
c.aumentar_salario(5_000_000)
```

El salario **no se modifica directamente** (`c._salario = ...` es mala práctica). Lo cambias a través de métodos que pueden validar, registrar, o hacer lo que necesites.

---

## ✨ Métodos mágicos: `__str__`

Los métodos mágicos personalizan cómo se comporta tu clase con operaciones de Python. El más útil para empezar es `__str__`, que define cómo se ve tu objeto cuando lo imprimes.

```python
class Jugador:
    def __init__(self, nombre, edad, posicion, equipo):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo

    def __str__(self):
        return f"⚽ {self.nombre} ({self.edad}) | {self.posicion} — {self.equipo}"

messi = Jugador("Lionel Messi", 37, "Delantero", "Argentina")
print(messi)  # ⚽ Lionel Messi (37) | Delantero — Argentina
```

Sin `__str__`, `print(messi)` mostraría algo como `<__main__.Jugador object at 0x...>`. Con `__str__` muestras justo lo que importa.

---

## 🧪 Ejercicios progresivos

### 1. Tu primera clase — `Jugador`

Crea una clase `Jugador` con:
- Un constructor que reciba `nombre` y `posicion`
- Un método `mostrar()` que imprima `"Jugador: [nombre] - [posicion]"`

Crea un jugador y llama a `mostrar()`.

<details>
<summary><b>Solución</b></summary>

```python
class Jugador:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

    def mostrar(self):
        print(f"Jugador: {self.nombre} - {self.posicion}")

j = Jugador("Paolo Guerrero", "Delantero")
j.mostrar()
```
</details>

---

### 2. Agregar edad y equipo

Partiendo de la clase `Jugador`, agrégale los atributos `edad` y `equipo`. Modifica `mostrar()` para que imprima todo.

Crea 3 jugadores de distintas selecciones y llama a `mostrar()` para cada uno.

<details>
<summary><b>Solución</b></summary>

```python
class Jugador:
    def __init__(self, nombre, edad, posicion, equipo):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo

    def mostrar(self):
        print(f"{self.nombre} | {self.edad} años | {self.posicion} | {self.equipo}")

p1 = Jugador("Paolo Guerrero", 41, "Delantero", "Perú")
p2 = Jugador("Luis Díaz", 29, "Extremo", "Colombia")
p3 = Jugador("Vinícius Jr.", 25, "Extremo", "Brasil")

p1.mostrar()
p2.mostrar()
p3.mostrar()
```
</details>

---

### 3. Métodos de acción

Agrega a la clase `Jugador` los métodos:
- `correr()` — imprime `"[nombre] está corriendo..."`.
- `patear()` — imprime `"[nombre] patea con fuerza!"`.

Crea un jugador y haz que corra y patee.

<details>
<summary><b>Solución</b></summary>

```python
class Jugador:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

    def correr(self):
        print(f"{self.nombre} está corriendo...")

    def patear(self):
        print(f"{self.nombre} patea con fuerza!")

p = Jugador("André Carrillo", "Extremo")
p.correr()
p.patear()
```
</details>

---

### 4. Abstracción — Clase `Equipo`

Crea una clase `Equipo` con:
- Atributos: `nombre`, `pais`, `jugadores` (lista vacía al inicio)
- Método `agregar(jugador)` que agregue un jugador a la lista
- Método `mostrar_plantilla()` que imprima todos los jugadores del equipo

Usa la clase `Jugador` del ejercicio 2.

<details>
<summary><b>Solución</b></summary>

```python
class Equipo:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.jugadores = []

    def agregar(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_plantilla(self):
        print(f"📋 {self.nombre} ({self.pais})")
        for j in self.jugadores:
            print(f"  - {j.nombre} ({j.posicion})")

peru = Equipo("Selección Peruana", "Perú")
peru.agregar(Jugador("Paolo Guerrero", 41, "Delantero", "Perú"))
peru.agregar(Jugador("André Carrillo", 33, "Extremo", "Perú"))
peru.mostrar_plantilla()
```
</details>

---

### 5. Herencia — `Arquero` y `Delantero`

Crea una clase base `Jugador` con `nombre` y `edad`.

Crea dos clases hijas:
- `Arquero` — método `atajar()` que imprima `"[nombre] ataja el disparo!"`
- `Delantero` — método `gol()` que imprima `"[nombre] define y GOL!"`

Ambas deben heredar el constructor de `Jugador`.

<details>
<summary><b>Solución</b></summary>

```python
class Jugador:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Arquero(Jugador):
    def atajar(self):
        print(f"{self.nombre} ataja el disparo!")

class Delantero(Jugador):
    def gol(self):
        print(f"{self.nombre} define y GOL!")

dibu = Arquero("Emiliano Martínez", 32)
dibu.atajar()

messi = Delantero("Lionel Messi", 37)
messi.gol()
```
</details>

---

### 6. Polimorfismo — Todos celebran diferente

Partiendo de las clases del ejercicio 5, agrega un método `celebrar()` a cada una:
- `Jugador`: `"[nombre] celebra."`
- `Arquero`: `"[nombre] grita: ATAJÉ!"`
- `Delantero`: `"[nombre] corre y se desliza de rodillas!"`

Crea una lista con jugadores de distintos tipos y recórrela llamando a `celebrar()`.

<details>
<summary><b>Solución</b></summary>

```python
class Jugador:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def celebrar(self):
        print(f"{self.nombre} celebra.")

class Arquero(Jugador):
    def celebrar(self):
        print(f"{self.nombre} grita: ATAJÉ!")

class Delantero(Jugador):
    def celebrar(self):
        print(f"{self.nombre} corre y se desliza de rodillas!")

jugadores = [
    Arquero("Emiliano Martínez", 32),
    Delantero("Lionel Messi", 37),
    Delantero("Kylian Mbappé", 27),
]

for j in jugadores:
    j.celebrar()
```
</details>

---

### 7. Encapsulación — `Contrato`

Crea una clase `Contrato` con:
- Atributo privado `_salario`
- Método `mostrar_salario()` que lo imprima
- Método `aplicar_bono(monto)` que aumente el salario

Crea un contrato para un jugador, muestra el salario, aplica un bono y muéstralo otra vez.

<details>
<summary><b>Solución</b></summary>

```python
class Contrato:
    def __init__(self, jugador, salario):
        self.jugador = jugador
        self._salario = salario

    def mostrar_salario(self):
        print(f"{self.jugador} gana ${self._salario:,}")

    def aplicar_bono(self, monto):
        self._salario += monto
        print(f"Bono de ${monto:,} aplicado.")

c = Contrato("Lionel Messi", 40_000_000)
c.mostrar_salario()
c.aplicar_bono(5_000_000)
c.mostrar_salario()
```
</details>

---

### 8. Todo junto — Sistema de Mundial

Crea un sistema que modele un Mundial usando las clases que ya conoces:

- Clase `Jugador` con nombre, edad, posicion, equipo
- Clase `Equipo` con nombre, pais, lista de jugadores, y método `agregar()` y `mostrar_plantilla()`
- Clase `Partido` con equipo_local, equipo_visitante, marcador_local=0, marcador_visitante=0
  - Método `gol_local()` que incremente el marcador local
  - Método `gol_visitante()` que incremente el marcador visitante
  - Método `mostrar_resultado()` que imprima el marcador

Crea 2 equipos con 3 jugadores cada uno, simula un partido con 2 goles y muestra el resultado final.

<details>
<summary><b>Solución</b></summary>

```python
class Jugador:
    def __init__(self, nombre, edad, posicion, equipo):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo

    def __str__(self):
        return f"{self.nombre} ({self.posicion})"

class Equipo:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.jugadores = []

    def agregar(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_plantilla(self):
        print(f"\n📋 {self.nombre} ({self.pais})")
        for j in self.jugadores:
            print(f"   ⚽ {j}")

class Partido:
    def __init__(self, local, visitante):
        self.local = local
        self.visitante = visitante
        self.goles_local = 0
        self.goles_visitante = 0

    def gol_local(self):
        self.goles_local += 1
        print(f"⚽ ¡GOL de {self.local.nombre}!")

    def gol_visitante(self):
        self.goles_visitante += 1
        print(f"⚽ ¡GOL de {self.visitante.nombre}!")

    def mostrar_resultado(self):
        print(f"\n🏆 FINAL: {self.local.nombre} {self.goles_local} - {self.goles_visitante} {self.visitante.nombre}")

# Crear jugadores
p1 = Jugador("Paolo Guerrero", 41, "Delantero", "Perú")
p2 = Jugador("André Carrillo", 33, "Extremo", "Perú")
p3 = Jugador("Renato Tapia", 29, "Volante", "Perú")

p4 = Jugador("Luis Díaz", 29, "Extremo", "Colombia")
p5 = Jugador("James Rodríguez", 33, "Volante", "Colombia")
p6 = Jugador("Davinson Sánchez", 28, "Defensa", "Colombia")

# Armar equipos
peru = Equipo("Selección Peruana", "Perú")
for j in [p1, p2, p3]:
    peru.agregar(j)

colombia = Equipo("Selección Colombiana", "Colombia")
for j in [p4, p5, p6]:
    colombia.agregar(j)

# Mostrar plantillas
peru.mostrar_plantilla()
colombia.mostrar_plantilla()

# Simular partido
partido = Partido(peru, colombia)
partido.gol_local()
partido.gol_visitante()
partido.gol_local()
partido.mostrar_resultado()
```
</details>

---

## 📊 Resumen de conceptos

| Concepto | Explicación | Ejemplo |
|----------|-------------|---------|
| **Clase** | Plantilla para crear objetos | `class Jugador:` |
| **Objeto** | Instancia de una clase | `messi = Jugador(...)` |
| **Constructor** | Inicializa el objeto al crearlo | `def __init__(self, ...)` |
| **Atributo** | Dato que pertenece al objeto | `self.nombre` |
| **Método** | Función que pertenece al objeto | `def celebrar(self)` |
| **Abstracción** | Modelar solo lo relevante | Ocultar lo que no importa |
| **Herencia** | Clase hija hereda de clase padre | `class Arquero(Jugador)` |
| **Polimorfismo** | Mismo método, comportamiento diferente | `celebrar()` en cada clase |
| **Encapsulación** | Proteger datos del objeto | `self._salario` |
| **`__str__`** | Cómo se imprime el objeto | `return f"{self.nombre}"` |

---

## ✅ Conclusión

Las clases te permiten organizar tu código como un **equipo de fútbol**: cada jugador (objeto) tiene sus datos y sabe lo que tiene que hacer. La herencia te permite especializar posiciones, el polimorfismo hace que cada uno responda a su manera, y la encapsulación protege lo que importa.

No escribas código desordenado con variables sueltas. Arma tu equipo con clases.
