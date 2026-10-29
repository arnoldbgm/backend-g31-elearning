<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Python-logo-notext.svg?width=90" alt="Logo de Python" height="80">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Flask_logo.svg?width=240" alt="Logo de Flask" height="80">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Postman_%28software%29.png?width=240" alt="Logo de Postman" height="70">
</p>

# 🧠 Guía — Día 1 (Semana 3): Entornos virtuales, pip y Flask

Bienvenidos AL BACKEND. Sí, hoy dejamos de ser usuarios de Python y nos convertimos en desarrolladores que exponen servicios. Vamos a crear nuestro propio servidor, nuestra propia API, y la vamos a probar como Dios manda con **Postman**. Prepárense que esto cambia el juego.

Antes de escribir una sola línea, quiero que entiendan **por qué** existe todo esto. Porque si solo copian código sin entender el modelo mental, el día que algo falle van a estar perdidos. Así que vamos con calma al principio, y después sí, a codear.

---

## 0. El modelo cliente-servidor — la base de TODO lo que viene

Hasta ahora, cuando programaban en Python, ustedes escribían un script, lo ejecutaban, y ESE MISMO programa hacía todo: leía datos, los procesaba, mostraba resultados. Un solo actor.

En backend, la cosa cambia. Ahora hay **dos actores separados**:

- El **cliente**: es quien pide algo. Puede ser un navegador, una app de celular, Postman, otro programa. El cliente no sabe (ni le importa) cómo está hecho el servidor por dentro.
- El **servidor**: es quien escucha pedidos y responde. Nuestro `app.py` con Flask va a ser el servidor.

<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Client-server-model.svg?width=520" alt="Diagrama del modelo cliente-servidor: varios clientes conectados a un servidor a través de la red" width="520">
</p>
<p align="center"><sub><i>Varios clientes le hablan a UN servidor a través de la red. Imagen: Wikimedia Commons.</i></sub></p>

**Analogía (guárdensela, la van a usar todo el curso):** pensá en un restaurante. Vos (cliente) no entrás a la cocina a cocinar tu propio plato. Le pedís al mozo (la petición, el *request*) y la cocina (el servidor) te devuelve el plato (la respuesta, el *response*). No te importa cómo está organizada la cocina por dentro — te importa que el pedido llegue bien y rápido.

Eso es exactamente lo que va a pasar entre Postman (o cualquier app) y nuestro Flask:

```
Cliente (Postman)  --- pide algo -->  Servidor (Flask)
Cliente (Postman)  <-- responde ---  Servidor (Flask)
```

Cada "pedido" tiene una estructura: un **método** (¿qué querés hacer? leer, crear, borrar...), una **URL** (¿a dónde le pedís?), a veces un **body** (¿qué datos mandás?), y el servidor responde con **datos** + un **código de estado** (¿salió bien o mal?).

Con esto en la cabeza, ahora sí, empecemos a construir la cocina.

---

## 1. Entornos virtuales — la cajita mágica

Imaginate que tenés dos proyectos: uno usa Flask versión 2, el otro Flask versión 3. Sin entornos virtuales, es un caos — una cosa le gana a la otra, se te rompe todo y terminás formateando la compu (me pasó, y no está bueno).

Un entorno virtual es como una **caja aislada** para cada proyecto. Cada uno tiene su propio Flask, sus propias versiones, y no se pelean entre sí.

**Sin entorno virtual**: instalás Flask para el proyecto A, después el proyecto B necesita otra versión → conflicto, explosión, lágrimas.

**Con entorno virtual**: cada proyecto tiene su cajita. Una no toca a la otra. Paz mundial.

**Otra analogía, porque esta es importante:** pensá en un edificio de departamentos. Cada departamento (proyecto) tiene sus propios muebles (librerías) y nadie se mete a poner sus cosas en el departamento del vecino. Python "del sistema" sería como la calle — de ahí NO querés que dependa nada importante, porque ahí pasa cualquiera y desordena todo.

¿Por qué importa esto en un trabajo real? Porque cuando trabajes en una empresa, vas a tener 5, 10, 20 proyectos distintos en tu compu. Si todos comparten el mismo Python "pelado", el día que actualices una librería para el proyecto nuevo, le rompés el proyecto viejo sin darte cuenta. Los entornos virtuales evitan ESO.

---

### 1A — Demo: Crear y activar un entorno virtual

1. Abrí una terminal en la carpeta de tu proyecto
2. Ejecutá:

```bash
python -m venv venv
```

Esto crea una carpeta `venv/` con una copia aislada de Python. Fijate que aparece una carpeta nueva en tu proyecto — ábrela y vas a ver que tiene su propio `python.exe`, su propio `pip`, todo aparte.

3. Activá el entorno:

- Windows
```bash

venv\Scripts\activate
```
- En gitbash:
```bash
    source venv/Scripts/activate
```
- En macOS y Linux:
```bash
    source venv/bin/activate
```
Vas a ver que aparece `(venv)` al inicio de la línea. Eso significa que estás dentro del entorno virtual. Es como si te hubieras puesto una casaca que dice "todo lo que instale ahora es solo para este proyecto".

Para desactivarlo:

```bash
deactivate
```

Cuando está activo, todo `pip install` va a parar **dentro de esta caja**, no al sistema.

---

### 1B — Reto: Verificá que funciona

1. Creá un entorno virtual llamado `mundo-python`
2. Activarlo
3. Ejecutá `python --version` y `pip --version` para confirmar
4. Desactivarlo
5. Volvé a ejecutar `python --version` (sin el entorno activado) — todo sigue igual, el entorno no afecta al sistema

<details>
<summary><b>Solución (reto)</b></summary>

```bash
python -m venv mundo-python
mundo-python\Scripts\activate
python --version
pip --version
deactivate
python --version
```

</details>

---

## 2. pip — el dealer de paquetes

`pip` es el programa que usamos para instalar librerías externas. ¿Querés Flask? `pip install flask`. ¿Querés pandas? `pip install pandas`. ¿Querés hacer una API y que funcione? `pip install` todo lo que necesités.

Flask NO viene con Python. Nadie nace sabiendo, hay que instalarlo. Y para eso está pip.

**Analogía:** pip es como el mercado central de Python. Python trae lo básico en la "despensa" (la librería estándar: `os`, `math`, `random`, etc.), pero para lo especializado — hacer un servidor web, procesar Excel, entrenar un modelo de IA — tenés que ir al mercado (PyPI, el repositorio oficial de paquetes) y traerlo con `pip install`.

Cuando hacés `pip install flask` dentro de tu entorno virtual, pip va a **PyPI.org**, descarga el paquete y lo instala SOLO en la cajita de ese proyecto. Por eso el orden importa: primero creás y activás el entorno, DESPUÉS instalás.

### Comandos esenciales

| Comando | Qué hace |
|---------|----------|
| `pip install colorama` | Instala el paquete Colorama |
| `pip list` | Muestra los paquetes instalados |
| `pip freeze` | Lista los paquetes en formato `paquete==version` |
| `pip uninstall colorama` | Desinstala Colorama |

**¿Por qué `pip freeze` es tan importante?** Porque cuando trabajes en equipo (o subas tu proyecto a producción), nadie va a instalar paquete por paquete a mano. Generás un `requirements.txt` con las versiones EXACTAS que vos usaste, y cualquier otra persona (o servidor) puede recrear tu mismo entorno con un solo comando. Esto evita el clásico "en mi compu funciona" — chiste recontra viejo en programación, pero real como la vida misma.

---

### 2A — Demo: Instalar Colorama y ver magia en la terminal

Primero lo primero: instalemos algo **que se vea**. Nada de instalar una librería y no pasar nada — con Colorama ves colores al toque.

Con el entorno virtual activado:

```bash
pip install colorama
```

Después ejecutá:

```bash
python
```

Y dentro de Python:

```python
from colorama import init, Fore
init()
print(Fore.RED + "ROJO" + Fore.RESET)
print(Fore.GREEN + "VERDE" + Fore.RESET)
print(Fore.BLUE + "AZUL" + Fore.RESET)
print(Fore.YELLOW + "AMARILLO" + Fore.RESET)
```

Salí con `exit()`. **Colorama en acción.** La terminal se viste de gala.

Ahora guardá la lista de dependencias:

```bash
pip freeze > requirements.txt
```

Esto crea un archivo que después cualquier otro puede usar para instalar exactamente las mismas versiones:

```bash
pip install -r requirements.txt
```

---

### 2B — Reto: Tu propio cartel luminoso

1. Con el entorno activado, asegurate de tener Colorama instalado
2. Escribí un archivo `cartel.py` que muestre un mensaje como este usando colores:

```
=== BIENVENIDO AL MUNDIAL 2026 ===
```

- El borde y el texto deben ser de distintos colores
- Usá `Fore.CYAN`, `Fore.MAGENTA`, `Fore.GREEN`, etc.
- Probalo varias veces cambiando colores

<details>
<summary><b>Solución (reto)</b></summary>

```python
from colorama import init, Fore

init()

print(Fore.CYAN + "=" * 35 + Fore.RESET)
print(Fore.YELLOW + "   BIENVENIDO AL MUNDIAL 2026" + Fore.RESET)
print(Fore.CYAN + "=" * 35 + Fore.RESET)
```

**Probá también:**
```python
print(Fore.MAGENTA + "Perú" + Fore.GREEN + " campeón" + Fore.RESET)
```

</details>

---

## 3. Postman — la herramienta con la que vamos a vivir todo el curso

<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Postman_%28software%29.png?width=330" alt="Logo de Postman" width="330">
</p>

Antes de Flask, un momento para esto: **Postman va a ser tu compañero de todos los días de acá en adelante**. No es opcional, no es "para después". Cada endpoint que hagamos se prueba en Postman AL TOQUE, apenas está escrito. No hay excusas de "ya lo probaré después".

**¿Por qué no usar el navegador y ya?** Porque el navegador solo sabe hacer GET fácilmente. No podés mandar un body en JSON con un click, no podés guardar tus peticiones, no podés armar una colección ordenada de todos tus endpoints. Postman te da control total sobre el método, la URL, los headers y el body — que es exactamente lo que necesitás para probar una API de verdad.

### 3.1 — Instalación

1. Andá a **postman.com/downloads** y descargá la versión para tu sistema operativo.

> 📸 **Captura sugerida (tomala vos):** pantalla de descarga de Postman (postman.com/downloads), mostrando los botones de descarga para Windows/Mac/Linux.

2. Instalá como cualquier programa (siguiente, siguiente, finalizar).
3. Abrí Postman y creá una cuenta gratuita (o entrá como invitado, para lo que vamos a hacer alcanza).

### 3.2 — Conociendo la interfaz

Cuando abras Postman por primera vez, prestá atención a estas zonas:

- **Botón "New" / "+"** → para crear una petición nueva.
- **Selector de método** (GET, POST, PATCH, DELETE...) → arriba a la izquierda del campo de URL.
- **Campo de URL** → donde escribís, por ejemplo, `http://127.0.0.1:5000/jugadores`.
- **Pestaña "Body"** → donde vas a mandar JSON cuando hagamos POST o PATCH.
- **Botón "Send"** → dispara la petición.
- **Zona de respuesta** (abajo) → acá aparece lo que el servidor te devolvió, y el código de estado bien grande arriba a la derecha.

> 📸 **Captura sugerida (tomala vos):** interfaz principal de Postman con una petición GET armada, señalando el selector de método, la barra de URL y el botón "Send".

> 📸 **Captura sugerida (tomala vos):** pestaña "Body" → "raw" → "JSON" seleccionada, con un JSON de ejemplo escrito.

**Regla de oro del curso:** cada vez que creemos un endpoint nuevo en Flask, el siguiente paso — SIEMPRE — es abrir Postman y probarlo. No seguimos al próximo endpoint sin haber confirmado que el anterior responde bien.

---

## 4. Flask — tu primer servidor (y te juro que no es brujería)

<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Flask_logo.svg?width=320" alt="Logo de Flask" width="320">
</p>

Flask es un **microframework**. ¿Qué significa "micro"? Que te da lo mínimo para construir un servidor web sin imponerte cómo ordenar tu código. No trae ORM, no trae autenticación, no trae un montón de cosas que no necesitás hoy. Cuando las necesites, las agregás.

**Analogía:** si Django (otro framework de Python) es como comprar un departamento amoblado — ya viene con todo puesto, pero tenés que acomodarte a como está armado — Flask es como comprar un departamento vacío. Vos decidís dónde va cada mueble. Al principio da un poco más de trabajo, pero para aprender backend desde cero es IDEAL, porque entendés qué hace cada pieza en vez de que la magia te la esconda.

Pero lo importante: **con 4 líneas de código ya tenés un servidor funcionando**. ¿A que no sabías que era tan fácil?

### 3A — Demo: Hola Mundo en Flask

Creá un archivo `app.py`:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Hola, mundo Flask!"
```

Ahora ejecutalo:

```bash
python app.py
```

Abrí el navegador en `http://127.0.0.1:5000`. Vas a ver "Hola, mundo Flask!" en la pantalla. **Ya tenés un servidor web, loco. FELICITACIONES.**

**Lo que pasó (prestá atención porque esto es la BASE de todo):**
- `from flask import Flask` → importamos la clase principal de Flask
- `app = Flask(__name__)` → creamos una instancia de la aplicación. Este objeto `app` es literalmente "tu restaurante": todo lo que agreguemos de acá en adelante (rutas, configuración) cuelga de él.
- `@app.route("/")` → esto es un **decorador**. Le decís a Flask: "Cuando alguien visite la raíz, ejecutá esta función". Es como poner un cartel en la puerta del restaurante: "acá se atiende el pedido de la mesa 1".
- `def inicio()` → la función que se ejecuta. Tiene que devolver algo (un string, un JSON, un HTML)
- cuando ejecutás `app.py`, Flask inicia un servidor en `http://127.0.0.1:5000` (`127.0.0.1` es tu propia computadora — se llama "localhost" — y `5000` es el puerto, como el número de mesa donde te vienen a atender)

**Ahora sí, probemos esto en Postman en vez de en el navegador** (recordá la regla de oro):

- Método: `GET`
- URL: `http://127.0.0.1:5000/`
- Send → deberías ver "Hola, mundo Flask!" en la zona de respuesta, con código **200**.

---

### 3B — Reto: Personalizá tu servidor

1. Creá un entorno virtual nuevo llamado `flask-crud`
2. Activarlo
3. Instalar Flask
4. Crear `app.py` con tu propio servidor que tenga:
   - Una ruta `/` que muestre "Bienvenido a la API de Jugadores del Mundial 2026"
   - Una ruta `/info` que devuelva `{"version": "1.0", "curso": "Backend con Flask"}`
   - **Probalo en Postman**: creá un GET a `http://127.0.0.1:5000/` y otro a `http://127.0.0.1:5000/info`

<details>
<summary><b>Solución (reto)</b></summary>

```bash
python -m venv flask-crud
flask-crud\Scripts\activate
pip install flask
```

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Bienvenido a la API de Jugadores del Mundial 2026"


@app.route("/info")
def info():
    return {"version": "1.0", "curso": "Backend con Flask"}
```

```bash
python app.py
```

En Postman:
- `GET http://127.0.0.1:5000/` → debe responder el string de bienvenida
- `GET http://127.0.0.1:5000/info` → debe responder el JSON

> **Nota:** Flask convierte automáticamente los diccionarios a JSON cuando los devolvés en una ruta.

</details>

---

## 5. Rutas dinámicas — cuando una URL vale más que mil palabras

Una API de verdad no tiene rutas fijas como `/jugador1`, `/jugador2`, `/jugador3`. Eso es una locura. Necesitás rutas que **cambien según lo que el cliente pida**. Algo como `/jugador/7` y que te devuelva al jugador con ID 7. Eso es una ruta dinámica, y es hermoso.

**Analogía:** pensá en las casillas de un correo. No existe una ventanilla distinta para cada paquete del mundo — existe UNA ventanilla que dice "casillero N°___", y vos completás el número. `/jugador/<int:id>` es exactamente eso: una sola ruta que sirve para CUALQUIER id que le pongas.

Hay dos formas de mandarle información extra a una ruta:

### Parámetros de ruta (`<tipo:nombre>`)

Van pegados a la URL, y normalmente identifican **un recurso específico**.

```python
@app.route("/jugador/<int:id>")
def obtener_jugador(id):
    return {"jugador_id": id, "nombre": "Ejemplo"}
```

### Parámetros de query (`request.args`)

Van después de un `?`, y normalmente sirven para **filtrar o buscar**, no para identificar un recurso puntual.

```python
@app.route("/buscar")
def buscar():
    nombre = request.args.get("nombre")
    return {"buscaste": nombre}
```

Esto responde a: `GET /buscar?nombre=Paolo`

**¿Cuándo uso cada uno?** Regla práctica: si estás pidiendo "ESE jugador puntual" → parámetro de ruta (`/jugador/3`). Si estás pidiendo "dame los que cumplan tal condición" → query params (`/buscar?posicion=Delantero`).

---

### 4A — Demo: Endpoint con jugadores hardcodeados

Fijate bien la estructura: **una lista de diccionarios**. Cada jugador tiene su propio `id` adentro, como debe ser. Esto es clave: como todavía no usamos base de datos, la lista `jugadores` vive en la memoria del programa mientras el servidor está corriendo — es nuestra "base de datos falsa" por ahora.

```python
from flask import Flask, request

app = Flask(__name__)

jugadores = [
    {"id": 1, "nombre": "Paolo Guerrero", "edad": 41, "posicion": "Delantero", "equipo": "Alianza Lima", "seleccion": "Peru"},
    {"id": 2, "nombre": "Andre Carrillo", "edad": 33, "posicion": "Extremo", "equipo": "Al Hilal", "seleccion": "Peru"},
    {"id": 3, "nombre": "Renato Tapia", "edad": 29, "posicion": "Mediocampista", "equipo": "Leganes", "seleccion": "Peru"},
    {"id": 4, "nombre": "Lionel Messi", "edad": 38, "posicion": "Delantero", "equipo": "Inter Miami", "seleccion": "Argentina"},
    {"id": 5, "nombre": "Vinicius Jr", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
    {"id": 6, "nombre": "Luis Diaz", "edad": 28, "posicion": "Extremo", "equipo": "Liverpool", "seleccion": "Colombia"},
    {"id": 7, "nombre": "Federico Valverde", "edad": 27, "posicion": "Mediocampista", "equipo": "Real Madrid", "seleccion": "Uruguay"},
    {"id": 8, "nombre": "Rodrygo", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
    {"id": 9, "nombre": "Julian Alvarez", "edad": 26, "posicion": "Delantero", "equipo": "Manchester City", "seleccion": "Argentina"},
    {"id": 10, "nombre": "Christian Cueva", "edad": 33, "posicion": "Mediocampista", "equipo": "Cienciano", "seleccion": "Peru"},
]

@app.route("/")
def inicio():
    return "API de Jugadores del Mundial 2026"


@app.route("/jugador/<int:id>")
def obtener_jugador(id):
    for j in jugadores:
        if j["id"] == id:
            return j
    return {"error": "Jugador no encontrado"}, 404


@app.route("/jugadores")
def listar_jugadores():
    return jugadores
```

**Fijate cómo buscamos al jugador:** recorremos la lista entera con un `for`, comparamos `id` por `id`, y en el momento que coincide, devolvemos. Si el `for` termina y nunca encontró nada, cae en el `return` de abajo con el error 404. **Nada de acceso directo por índice o por clave mágica** — así es como se busca en una lista de diccionarios, y así lo vamos a hacer TODO el curso.

**Probalo en Postman:**
- `GET /` → bienvenida
- `GET /jugador/1` → datos de Paolo Guerrero
- `GET /jugador/99` → error 404
- `GET /jugadores` → lista de todos

---

### 4B — Reto: Endpoints de selecciones

Agregale al mismo `app.py`:

1. Una ruta `/seleccion/<nombre>` que devuelva todos los jugadores de esa selección. Ej: `GET /seleccion/Argentina` → solo Messi
2. Una ruta `/buscar` que acepte query params:
   - `?posicion=Delantero` → filtre por posición
   - `?edad_max=30` → jugadores menores o iguales a esa edad
   - **Combinables**: `?posicion=Delantero&edad_max=30`
3. Si no hay resultados, devolvé `{"mensaje": "No se encontraron jugadores"}` con código 200

> **Pista:** para `/seleccion/<nombre>`, el nombre llega como string, comparalo con `.title()` o `.lower()` según corresponda. Para `/buscar`, usá `request.args.get()` y verificate si cada filtro está presente.

<details>
<summary><b>Solución (reto)</b></summary>

```python
from flask import Flask, request

app = Flask(__name__)

jugadores = [
    {"id": 1, "nombre": "Paolo Guerrero", "edad": 41, "posicion": "Delantero", "equipo": "Alianza Lima", "seleccion": "Perú"},
    {"id": 2, "nombre": "André Carrillo", "edad": 33, "posicion": "Extremo", "equipo": "Al Hilal", "seleccion": "Perú"},
    {"id": 3, "nombre": "Renato Tapia", "edad": 29, "posicion": "Mediocampista", "equipo": "Leganés", "seleccion": "Perú"},
    {"id": 4, "nombre": "Lionel Messi", "edad": 38, "posicion": "Delantero", "equipo": "Inter Miami", "seleccion": "Argentina"},
    {"id": 5, "nombre": "Vinícius Jr", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
]


@app.route("/")
def inicio():
    return "API de Jugadores del Mundial 2026"


@app.route("/jugador/<int:id>")
def obtener_jugador(id):
    for j in jugadores:
        if j["id"] == id:
            return j
    return {"error": "Jugador no encontrado"}, 404


@app.route("/jugadores")
def listar_jugadores():
    return jugadores


@app.route("/seleccion/<nombre>")
def jugadores_por_seleccion(nombre):
    resultado = []
    for j in jugadores:
        if j["seleccion"].lower() == nombre.lower():
            resultado.append(j)

    if not resultado:
        return {"mensaje": "No se encontraron jugadores"}, 200
    return resultado


@app.route("/buscar")
def buscar_jugadores():
    resultado = jugadores.copy()

    posicion = request.args.get("posicion")
    if posicion:
        filtrados = []
        for j in resultado:
            if j["posicion"].lower() == posicion.lower():
                filtrados.append(j)
        resultado = filtrados

    edad_max = request.args.get("edad_max")
    if edad_max:
        try:
            edad_max_val = int(edad_max)
            filtrados = []
            for j in resultado:
                if j["edad"] <= edad_max_val:
                    filtrados.append(j)
            resultado = filtrados
        except ValueError:
            return {"error": "edad_max debe ser un número"}, 400

    if not resultado:
        return {"mensaje": "No se encontraron jugadores"}, 200

    return resultado
```

**Probalo en Postman:**
- `GET /seleccion/Peru` → 3 jugadores
- `GET /seleccion/brasil` → Vinícius Jr
- `GET /buscar?posicion=Delantero` → Guerrero y Messi
- `GET /buscar?edad_max=30` → Tapia, Vinícius Jr
- `GET /buscar?posicion=Delantero&edad_max=35` → solo Messi
- `GET /buscar?posicion=Arquero` → "No se encontraron jugadores"

</details>

---

## 6. Mandar datos desde Postman — ya no es solo leer, ahora escribimos

Hasta ahora solo hicimos GET: pedir datos. Pero una API de verdad necesita **crear** cosas. ¿Y cómo le mandás datos al servidor? Por el **body** de la petición.

Retomando la analogía del restaurante: GET es el menú (leer los platos), POST es hacer el pedido (crear algo nuevo). El mozo necesita saber QUÉ querés, y eso va en el body — no lo podés meter en la URL porque puede ser información compleja (nombre, edad, posición, todo junto).

### Tipos de body (el que manda es JSON)

<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/JSON_vector_logo.svg?width=130" alt="Logo de JSON" width="130">
</p>
<p align="center"><sub><i>JSON: el idioma universal de las APIs. Imagen: Wikimedia Commons.</i></sub></p>

| Tipo | Content-Type | Cómo se lee en Flask |
|------|-------------|----------------------|
| JSON | `application/json` | `request.json` → devuelve un diccionario |
| Formulario | `application/x-www-form-urlencoded` | `request.form` |
| Texto plano | `text/plain` | `request.data` |

Nosotros usamos **JSON**, porque es el estándar en APIs REST. Punto.

**¿Por qué JSON y no, no sé, Python puro?** Porque el cliente que le habla a tu API no siempre es Python. Puede ser una app en JavaScript, una app de Android, otro servidor en Java. JSON es un formato de texto que TODOS los lenguajes saben leer y escribir, así que es el idioma universal para que sistemas distintos se entiendan. Y fijate que su estructura es prácticamente igual a un diccionario de Python — por eso Flask lo convierte tan fácil.

### Cómo configurar Postman para mandar JSON

1. Elegí método **POST**
2. En la pestaña **Body** → **raw** → **JSON**
3. Escribí el JSON lindo y enviá

> 📸 **Captura sugerida (tomala vos):** Postman con método POST seleccionado, pestaña Body → raw → JSON activa, mostrando un JSON de ejemplo cargado y el botón Send resaltado.

---

### 5A — Demo: Endpoint POST que recibe JSON

```python
from flask import Flask, request

app = Flask(__name__)


@app.route("/saludar", methods=["POST"])
def saludar():
    datos = request.json
    nombre = datos.get("nombre", "invitado")
    return {"mensaje": f"Hola {nombre}, bienvenido a la API del Mundial"}
```

**En Postman:**
- Método: POST
- URL: `http://127.0.0.1:5000/saludar`
- Body → raw → JSON:
```json
{
    "nombre": "Carlos"
}
```

**Respuesta esperada:**
```json
{
    "mensaje": "Hola Carlos, bienvenido a la API del Mundial"
}
```

**Conceptos importantes:**
- `methods=["POST"]` → por defecto Flask solo acepta GET. Hay que decirle explícitamente qué métodos acepta. Si probás con GET en Postman sobre esta ruta, Flask te va a devolver un error 405 ("Method Not Allowed") — pruébalo, para que veas el error con tus propios ojos.
- `request.json` → Flask parsea automáticamente el JSON del body y lo convierte en un diccionario
- Si no se envió JSON, `request.json` es `None`, y si intentás hacer `.get()` sobre `None` te va a explotar el programa — por eso en el reto de abajo validamos antes de usar los datos.

---

### 5B — Reto: Validar datos recibidos

Creá un endpoint `POST /jugador` que reciba JSON con los datos de un nuevo jugador y lo agregue a la lista `jugadores`. Validá:

- `nombre`: obligatorio, no vacío
- `posicion`: obligatorio
- `seleccion`: obligatorio
- Si falta algún campo obligatorio, devolvé `{"error": "Falta el campo: nombre"}` con código **400**
- Si todo está bien, asignale un ID nuevo (el máximo + 1) y devolvé el jugador creado con código **201**

> **Pista:** para sacar el máximo ID tenés que recorrer la lista con un `for`, guardar el más grande, y sumarle 1. Nunca uses `len(jugadores) + 1` para el ID — si alguna vez borran un jugador del medio, te van a quedar IDs repetidos. El máximo + 1 es la forma correcta.

<details>
<summary><b>Solución (reto)</b></summary>

```python
from flask import Flask, request

app = Flask(__name__)

jugadores = [
    {"id": 1, "nombre": "Paolo Guerrero", "edad": 41, "posicion": "Delantero", "equipo": "Alianza Lima", "seleccion": "Perú"},
    {"id": 2, "nombre": "André Carrillo", "edad": 33, "posicion": "Extremo", "equipo": "Al Hilal", "seleccion": "Perú"},
    {"id": 3, "nombre": "Renato Tapia", "edad": 29, "posicion": "Mediocampista", "equipo": "Leganés", "seleccion": "Perú"},
    {"id": 4, "nombre": "Lionel Messi", "edad": 38, "posicion": "Delantero", "equipo": "Inter Miami", "seleccion": "Argentina"},
    {"id": 5, "nombre": "Vinícius Jr", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
]


@app.route("/")
def inicio():
    return "API de Jugadores del Mundial 2026"


@app.route("/jugador/<int:id>")
def obtener_jugador(id):
    for j in jugadores:
        if j["id"] == id:
            return j
    return {"error": "Jugador no encontrado"}, 404


@app.route("/jugadores")
def listar_jugadores():
    return jugadores


@app.route("/jugador", methods=["POST"])
def crear_jugador():
    datos = request.json

    if not datos:
        return {"error": "Debes enviar datos en formato JSON"}, 400

    if "nombre" not in datos or not str(datos.get("nombre", "")).strip():
        return {"error": "Falta el campo: nombre"}, 400

    if "posicion" not in datos or not str(datos.get("posicion", "")).strip():
        return {"error": "Falta el campo: posicion"}, 400

    if "seleccion" not in datos or not str(datos.get("seleccion", "")).strip():
        return {"error": "Falta el campo: seleccion"}, 400

    nuevo_id = 0
    for j in jugadores:
        if j["id"] > nuevo_id:
            nuevo_id = j["id"]
    nuevo_id += 1

    nuevo_jugador = {
        "id": nuevo_id,
        "nombre": datos["nombre"],
        "edad": datos.get("edad", 0),
        "posicion": datos["posicion"],
        "equipo": datos.get("equipo", ""),
        "seleccion": datos["seleccion"],
    }

    jugadores.append(nuevo_jugador)

    return nuevo_jugador, 201
```

**En Postman:**
- `POST /jugador` con body:
```json
{
    "nombre": "Alisson Becker",
    "edad": 33,
    "posicion": "Arquero",
    "equipo": "Liverpool",
    "seleccion": "Brasil"
}
```
→ Debe responder con los datos del jugador creado y código **201**

- `POST /jugador` con body:
```json
{
    "nombre": "James Rodríguez",
    "posicion": "Mediocampista",
    "seleccion": "Colombia"
}
```
→ Debe funcionar (edad y equipo son opcionales, toman valor por defecto)

- `POST /jugador` con body:
```json
{
    "nombre": ""
}
```
→ Debe responder `{"error": "Falta el campo: nombre"}` con código **400**

</details>

---

## 7. Códigos de estado HTTP — el servidor también tiene emociones

Cuando tu servidor responde, no solo manda datos. También manda un **código de estado** que es como su carita: le dice al cliente si todo salió bien, si se equivocó, si no encontró algo, o si explotó todo.

**Analogía:** pensá en un semáforo con muchos más colores que el normal. Verde total (200-201) significa "andá tranquilo, todo salió bien". Amarillo (400) significa "pará, algo mandaste mal, revisá tu pedido". Un cartel de "no existe" (404) significa "acá no hay nada, seguí buscando en otro lado". Y rojo total (500) significa "chocamos, algo se rompió del lado del servidor, y no es tu culpa".

Y esto es CLAVE: una API no es solo devolver datos, es devolverlos con el código correcto. Si no, el cliente (que puede ser una app hecha por OTRO equipo, que ni conocés) no tiene forma de saber automáticamente si su pedido salió bien o mal — tendría que "adivinar" leyendo el mensaje de texto, y eso rompe toda la lógica de una API bien hecha.

### Los códigos que más vas a usar (aprendételos, en serio):

| Código | Significado | Cuándo usarlo |
|--------|------------|---------------|
| **200** | OK | Todo bien, acá están tus datos |
| **201** | Created | Acabo de crear algo, tomá |
| **204** | No Content | Lo eliminé, no hay nada que devolver |
| **400** | Bad Request | Mandaste cualquier cosa, revisá |
| **404** | Not Found | Eso que buscás no existe, pe |
| **500** | Internal Server Error | Algo explotó del lado del servidor |

**Un dato que les va a servir toda la carrera:** los códigos están agrupados por familia según el primer dígito. Los que empiezan con **2** son éxito, los que empiezan con **4** son error DEL CLIENTE (mandaste algo mal vos), y los que empiezan con **5** son error DEL SERVIDOR (la rompió el backend, no vos). Cuando algo falle, mirá primero ese primer número — te dice para qué lado mirar.

En Flask, devolvés el código como segundo valor en el `return`:

```python
return {"error": "No encontrado"}, 404
return nuevo_jugador, 201
```

Sí, es así de simple. El primer valor son los datos, el segundo es el código. Si no ponés nada, Flask asume **200** por defecto — por eso en el Hola Mundo del principio nunca escribimos un código y todo funcionó igual.

---

### 6A — Demo: Probá los códigos en Postman como un profesional

Con tu `app.py` corriendo (el del reto anterior), probá esto en Postman y mirá el código que devuelve cada uno:

1. `GET /jugador/99` → código **404** — no existe, obvio
2. `POST /jugador` sin body o con body vacío → código **400** — mandaste mal los datos
3. `POST /jugador` con JSON válido → código **201** — se creó con éxito
4. `GET /jugador/6` → código **200** — acá está el jugador que creaste

En Postman, el código de estado aparece arriba a la derecha, bien grande, y viene coloreado (verde para éxito, naranja/rojo para error). No lo ignorés. Es tan importante como los datos.

> 📸 **Captura sugerida (tomala vos):** zona de respuesta de Postman resaltando el código de estado (ej. "200 OK" en verde) en la esquina superior derecha.

---

### 6B — Reto: Mejorá los códigos de estado

Tomá el `app.py` del reto 5B y asegurate de que **todas** las rutas devuelvan el código de estado correcto:

| Ruta | Caso | Código |
|------|------|--------|
| `GET /jugador/<id>` | Existe | 200 |
| `GET /jugador/<id>` | No existe | 404 |
| `GET /jugadores` | Siempre | 200 |
| `POST /jugador` | Datos válidos | 201 |
| `POST /jugador` | Faltan campos | 400 |
| `GET /seleccion/<nombre>` | Existe | 200 |
| `GET /seleccion/<nombre>` | No existe | 200 (con mensaje) |
| `GET /buscar` | Sin resultados | 200 (con mensaje) |

<details>
<summary><b>Solución (reto)</b></summary>

Revisá el código del reto 5B — ya tiene los códigos correctos. Verificá con Postman cada caso listado arriba y confirmá que el código que devuelve coincida.

Si algún endpoint no devuelve el código esperado, ajustalo.

</details>

---

## 🎯 Resumen de conceptos

| Tema | Demo | Reto | Conceptos clave |
|------|:----:|:----:|-----------------|
| 0. Cliente-servidor | — | — | request, response, modelo de comunicación |
| 1. Entorno virtual | ✅ | ✅ | `venv`, activación, aislamiento |
| 2. pip y dependencias | ✅ | ✅ | `pip install`, `freeze`, `requirements.txt` |
| 3. Postman | — | — | instalación, interfaz, método, URL, body |
| 4. Flask Hello World | ✅ | ✅ | `Flask`, `@app.route()`, servidor |
| 5. Rutas dinámicas | ✅ | ✅ | `<int:id>`, `request.args`, query params |
| 6. POST y request.json | ✅ | ✅ | `methods=["POST"]`, validación, código 201 |
| 7. Códigos HTTP | ✅ | ✅ | familias 2xx/4xx/5xx, 200, 201, 400, 404 |

---

<sub>Créditos de imágenes: logos de Python, Flask, Postman y JSON, y diagrama cliente-servidor, servidos desde Wikimedia Commons. Los logos son marcas de sus respectivos dueños y se usan solo con fines educativos de identificación.</sub>
