# 🧠 Guía — Día 2 (Semana 3): CRUD completo + Frontend

<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/HTML5_logo_and_wordmark.svg?width=100" alt="Logo de HTML5" height="80">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/JavaScript-logo.png?width=100" alt="Logo de JavaScript" height="80">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Flask_logo.svg?width=240" alt="Logo de Flask" height="80">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Postman_%28software%29.png?width=240" alt="Logo de Postman" height="70">
</p>

Bienvenidos al día en que TODO cobra sentido. Ayer aprendimos a crear un servidor con Flask, a devolver datos, a recibir JSON. Hoy no solo vamos a leer datos — vamos a **Crear, Leer, Actualizar y Eliminar** jugadores como si fuéramos dueños de la base de datos del Mundial. Y después... ¡conectamos todo con un frontend! HTML, JavaScript, fetch, la combinación letal. Todo validado con Postman, obvio.

Antes de escribir código, tenemos que entender **qué es CRUD** y **por qué** esto es el 90% de todas las APIs que existen. Porque si entendés CRUD, entendés cómo funciona internet.

---

## 0. ¿Qué es CRUD y por qué cambia todo?

CRUD no es una mala palabra, son las **4 operaciones básicas** que cualquier sistema necesita para manejar datos. Literalmente, el 90% de las APIs del mundo solo hacen esto.

<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Client-server-model.svg?width=520" alt="Diagrama del modelo cliente-servidor" width="520">
</p>
<p align="center"><sub><i>Cada pedido del cliente es una operación CRUD. Imagen: Wikimedia Commons.</i></sub></p>

| Operación | Método HTTP | ¿Qué hace? | Ejemplo real |
|-----------|------------|------------|-------------|
| **C**reate | POST | Crear un recurso nuevo | Dar de alta un jugador |
| **R**ead | GET | Obtener uno o varios | Listar todos los jugadores |
| **U**pdate | PUT / PATCH | Actualizar uno existente | Cambiar la edad de un jugador |
| **D**elete | DELETE | Borrar un recurso | Eliminar un jugador |

**Analogía (retenela, te va a salvar en entrevistas laborales):** pensá en un restobar. POST es hacer un pedido nuevo (creás algo que no existía antes). GET es mirar la carta de tragos (leés). PUT/PATCH es pedirle al mozo que le ponga más hielo a tu trago (actualizás). DELETE es pedir que se lleven el plato vacío (borrás).

Cada operación tiene su método HTTP, su propósito, y su código de respuesta. Mezclarlos es como pedir un trago en la ventanilla de los pedidos para llevar — puede funcionar, pero no es la forma correcta.

---

## 1. READ — Leer datos (esto ya lo saben, pero lo repasamos como desafío)

**Profe dice:** "A ver, equipo. Necesito que me muestren todos los jugadores que tenemos en la lista. ¿Qué endpoint necesitamos? ¿Qué método HTTP?"

### 1A — Demo: GET /jugadores (listar todos)

Armamos el endpoint que devuelve la lista completa:

```python
from flask import Flask

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


@app.route("/jugadores")
def listar_jugadores():
    return jugadores
```

**Probá en Postman:** `GET /jugadores` → código 200, te devuelve los 5 jugadores

---

### 1B — Reto: GET /jugador/<id> (buscar uno solo)

**Profe dice:** "Ahora quiero poder preguntar por UN solo jugador. Por ejemplo, `GET /jugador/3` debería traerme solo a Renato Tapia. ¿Y si pregunto por uno que no existe, como el 99? Ahí debería responder con un 404."

Implementalo. Usá un `for` para recorrer la lista y comparar `id` por `id`.

<details>
<summary><b>Solución (reto)</b></summary>

```python
@app.route("/jugador/<int:id>")
def obtener_jugador(id):
    for j in jugadores:
        if j["id"] == id:
            return j
    return {"error": "Jugador no encontrado"}, 404
```

**Probá en Postman:**
- `GET /jugador/3` → datos de Renato Tapia, código 200
- `GET /jugador/99` → `{"error": "Jugador no encontrado"}`, código 404

</details>

---

## 2. CREATE — Crear jugadores (recibir datos del cliente)

**Profe dice:** "Bien, ya sabemos leer. Ahora: ¿cómo hacemos para AGREGAR un jugador nuevo? El usuario tiene que mandarnos los datos. ¿Por dónde los recibe Flask? Por el body de la petición. ¿Y qué método se usa para crear algo nuevo? POST."

### 2A — Demo: POST /jugador con JSON

La ruta POST recibe un JSON desde Postman, lo procesa, y agrega el jugador a la lista:

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


@app.route("/jugador", methods=["POST"])
def crear_jugador():
    datos = request.json

    nuevo_id = 0
    for j in jugadores:
        if j["id"] > nuevo_id:
            nuevo_id = j["id"]
    nuevo_id += 1

    nuevo_jugador = {
        "id": nuevo_id,
        "nombre": datos.get("nombre", ""),
        "edad": datos.get("edad", 0),
        "posicion": datos.get("posicion", ""),
        "equipo": datos.get("equipo", ""),
        "seleccion": datos.get("seleccion", ""),
    }

    jugadores.append(nuevo_jugador)
    return nuevo_jugador, 201
```

**En Postman:**
- Método: POST
- URL: `http://127.0.0.1:5000/jugador`
- Body → raw → JSON:
```json
{
    "nombre": "Alisson Becker",
    "edad": 33,
    "posicion": "Arquero",
    "equipo": "Liverpool",
    "seleccion": "Brasil"
}
```

**Respuesta esperada:** código 201, el servidor devuelve el jugador creado.

---

### 2B — Reto: Validá los datos antes de crear

**Profe dice:** "Está bien, creamos jugadores... pero mirá esto: ¿qué pasa si mandamos un POST sin nombre? ¿O sin posición? Se va a crear un jugador con datos vacíos. Eso no tiene sentido. Tenemos que VALIDAR que el cliente nos mande lo obligatorio antes de guardar."

Agregá estas validaciones:
- Si no mandó JSON (`request.json` es `None` o vacío) → devolvé `{"error": "Debes enviar datos en formato JSON"}` con código **400**
- Si falta el campo `nombre` o está vacío → devolvé `{"error": "Falta el campo: nombre"}` con código **400**
- Si falta `posicion` o está vacío → devolvé **400**
- Si falta `seleccion` o está vacío → devolvé **400**

<details>
<summary><b>Solución (reto)</b></summary>

```python
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

**Probá en Postman:**

| Body | Código esperado |
|------|-----------------|
| `{"nombre": "James", "posicion": "MED", "seleccion": "COL"}` | **201** |
| `{"nombre": ""}` | **400** — falta nombre |
| `{"posicion": "Arquero"}` | **400** — falta nombre |
| Body vacío | **400** — debe enviar JSON |

</details>

---

## 3. UPDATE — Modificar jugadores existentes

**Profe dice:** "Ya tenemos READ y CREATE. Ahora: un jugador se cambia de equipo, se pone más viejo... necesitamos ACTUALIZAR sus datos. ¿Qué método HTTP usamos cuando queremos modificar algo que ya existe?"

Algunos dirán PUT, otros PATCH. Vamos a ver la diferencia porque es una de las preguntas clásicas de entrevista.

### PUT vs PATCH — la confusión más común

<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/JSON_vector_logo.svg?width=130" alt="Logo de JSON" width="130">
</p>
<p align="center"><sub><i>JSON es el idioma en que hablamos con PUT y PATCH. Imagen: Wikimedia Commons.</i></sub></p>

| Método | Qué hace | ¿Qué pasa con los campos que no mandaste? |
|--------|----------|-------------------------------------------|
| **PUT** | Reemplaza TODO el recurso | Se pierden. Adiós. Se fueron. |
| **PATCH** | Actualiza SOLO los campos que llegan | Los que no mandaste se quedan como están |

**Analogía:** PUT es como pedir un plato nuevo desde cero cambiando todo. PATCH es como pedir "sin cebolla" para el plato que ya tenés. Con PUT devolvés el plato completo a la cocina y te mandan uno nuevo. Con PATCH el mozo anota una nota al costado y el plato vuelve con ese cambio apenas.

Nosotros vamos a usar PATCH porque es más seguro: solo tocamos lo que nos mandan.

### 3A — Demo: PATCH /jugador/<id>

Implementamos el endpoint para actualizar SOLO los campos que lleguen:

```python
@app.route("/jugador/<int:id>", methods=["PATCH"])
def actualizar_jugador(id):
    for j in jugadores:
        if j["id"] == id:
            datos = request.json

            if not datos:
                return {"error": "Debes enviar datos en formato JSON"}, 400

            for campo in datos:
                if campo in j:
                    j[campo] = datos[campo]

            return j, 200

    return {"error": "Jugador no encontrado"}, 404
```

**Punto clave:** ese `for campo in datos` recorre SOLO los campos que el cliente mandó. Si mandó solo `{"edad": 42}`, solo actualiza `edad`. El resto se queda igual.

**Probá en Postman:**

```
PATCH /jugador/3
Body: {"edad": 30, "equipo": "Celta de Vigo"}
```
→ Renato Tapia con edad 30 y nuevo equipo, código 200

```
PATCH /jugador/99
Body: {"edad": 25}
```
→ `{"error": "Jugador no encontrado"}`, código 404

---

### 3B — Reto: Validaciones en PATCH

**Profe dice:** "Ahora, del mismo modo que validamos en POST, tenemos que validar en PATCH. ¿Qué pasa si alguien manda `{"edad": -5}`? O `{"posicion": ""}`? Eso no debe pasar."

Agregale validaciones al endpoint PATCH:
- `edad`: si se envía, debe ser un número entre 0 y 100
- `posicion`: si se envía, no puede estar vacía
- `nombre`: si se envía, no puede estar vacío
- `seleccion`: si se envía, no puede estar vacía
- Si alguna validación falla, devolvé **400** con mensaje específico

<details>
<summary><b>Solución (reto)</b></summary>

```python
@app.route("/jugador/<int:id>", methods=["PATCH"])
def actualizar_jugador(id):
    for j in jugadores:
        if j["id"] == id:
            datos = request.json

            if not datos:
                return {"error": "Debes enviar datos en formato JSON"}, 400

            if "edad" in datos:
                try:
                    edad = int(datos["edad"])
                    if edad < 0 or edad > 100:
                        return {"error": "La edad debe estar entre 0 y 100"}, 400
                except (ValueError, TypeError):
                    return {"error": "La edad debe ser un número válido"}, 400

            if "posicion" in datos and not str(datos["posicion"]).strip():
                return {"error": "La posición no puede estar vacía"}, 400

            if "nombre" in datos and not str(datos["nombre"]).strip():
                return {"error": "El nombre no puede estar vacío"}, 400

            if "seleccion" in datos and not str(datos["seleccion"]).strip():
                return {"error": "La selección no puede estar vacía"}, 400

            for campo in datos:
                if campo in j:
                    j[campo] = datos[campo]

            return j, 200

    return {"error": "Jugador no encontrado"}, 404
```

**Probá en Postman:**

```
PATCH /jugador/1
Body: {"edad": 42}
```
→ 200, edad actualizada

```
PATCH /jugador/1
Body: {"edad": -5}
```
→ 400, "La edad debe estar entre 0 y 100"

```
PATCH /jugador/1
Body: {"posicion": ""}
```
→ 400, "La posición no puede estar vacía"

</details>

---

## 4. DELETE — Eliminar jugadores

**Profe dice:** "Última operación del CRUD. ¿Qué método usamos cuando queremos BORRAR algo? DELETE. No lleva body, solo la URL con el ID."

### 4A — Demo: DELETE /jugador/<id>

```python
@app.route("/jugador/<int:id>", methods=["DELETE"])
def eliminar_jugador(id):
    for j in jugadores:
        if j["id"] == id:
            jugadores.remove(j)
            return {"mensaje": "Jugador eliminado"}, 200

    return {"error": "Jugador no encontrado"}, 404
```

**Probá en Postman:**
- `DELETE /jugador/5` → `{"mensaje": "Jugador eliminado"}`, código 200
- `GET /jugadores` → la lista ya no tiene a Vinícius Jr
- `DELETE /jugador/99` → `{"error": "Jugador no encontrado"}`, código 404

---

### 4B — Reto: Armá el CRUD completo y probalo

**Profe dice:** "Ahora juntamos TODO. Con los endpoints que hicieron (GET todos, GET por ID, POST, PATCH, DELETE), armen un solo `app.py` con el CRUD completo y verifiquen que funciona."

Armá un solo archivo `app.py` con:
1. `GET /` → bienvenida
2. `GET /jugadores` → lista completa
3. `GET /jugador/<id>` → uno solo o 404
4. `POST /jugador` → crear con validaciones, código 201
5. `PATCH /jugador/<id>` → actualizar con validaciones, código 200
6. `DELETE /jugador/<id>` → eliminar o 404

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


@app.route("/jugadores")
def listar_jugadores():
    return jugadores


@app.route("/jugador/<int:id>")
def obtener_jugador(id):
    for j in jugadores:
        if j["id"] == id:
            return j
    return {"error": "Jugador no encontrado"}, 404


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


@app.route("/jugador/<int:id>", methods=["PATCH"])
def actualizar_jugador(id):
    for j in jugadores:
        if j["id"] == id:
            datos = request.json

            if not datos:
                return {"error": "Debes enviar datos en formato JSON"}, 400

            if "edad" in datos:
                try:
                    edad = int(datos["edad"])
                    if edad < 0 or edad > 100:
                        return {"error": "La edad debe estar entre 0 y 100"}, 400
                except (ValueError, TypeError):
                    return {"error": "La edad debe ser un número válido"}, 400

            if "posicion" in datos and not str(datos["posicion"]).strip():
                return {"error": "La posición no puede estar vacía"}, 400

            if "nombre" in datos and not str(datos["nombre"]).strip():
                return {"error": "El nombre no puede estar vacío"}, 400

            if "seleccion" in datos and not str(datos["seleccion"]).strip():
                return {"error": "La selección no puede estar vacía"}, 400

            for campo in datos:
                if campo in j:
                    j[campo] = datos[campo]

            return j, 200

    return {"error": "Jugador no encontrado"}, 404


@app.route("/jugador/<int:id>", methods=["DELETE"])
def eliminar_jugador(id):
    for j in jugadores:
        if j["id"] == id:
            jugadores.remove(j)
            return {"mensaje": "Jugador eliminado"}, 200

    return {"error": "Jugador no encontrado"}, 404
```

**Tabla de verificación en Postman:**

| Método | URL | Body | Código esperado |
|--------|-----|------|:----------------:|
| `GET` | `/jugadores` | - | 200 |
| `GET` | `/jugador/3` | - | 200 |
| `GET` | `/jugador/99` | - | 404 |
| `POST` | `/jugador` | `{"nombre": "James", "posicion": "MED", "seleccion": "COL"}` | 201 |
| `POST` | `/jugador` | `{"nombre": ""}` | 400 |
| `PATCH` | `/jugador/3` | `{"edad": 30}` | 200 |
| `PATCH` | `/jugador/1` | `{"edad": -5}` | 400 |
| `DELETE` | `/jugador/5` | - | 200 |
| `DELETE` | `/jugador/99` | - | 404 |

</details>

---

## 5. Frontend — ahora sí, algo que se ve bonito

Hasta ahora todo lo probamos con Postman. Y está bien, Postman es el amigo fiel del backend. Pero una API no vive para Postman — vive para que **otros programas** la consuman.

Hoy creamos un frontend en HTML plano que se conecta a tu API usando `fetch`. Nada de React, nada de Vue, nada de frameworks — HTML, JavaScript y ganas. Porque antes de correr, hay que aprender a caminar: si no entendés cómo funciona `fetch` a pelo, después no vas a entender por qué React hace lo que hace.

### El problema del CORS (y por qué existe)

Cuando tu frontend corre en `file://` o en un puerto distinto al del backend, el navegador se pone nervioso y dice "eh, esto es sospechoso" y **bloquea la petición**. No es malo, es seguridad. Pero nosotros tenemos que decirle: "tranqui, confiá".

Hay dos formas de resolverlo:
1. **Servir el HTML desde Flask** → mismo origen, cero CORS (la que usamos hoy)
2. **Usar flask-cors** → permitir explícitamente que otro origen hable con tu API (la que usarías en producción)

Nosotros vamos con la primera porque es más simple y no agrega conceptos que hoy no necesitamos.

### 5A — Demo: Servir el frontend DESDE Flask (sin vueltas)

La solución más limpia: que Flask sirva el HTML. Mismo origen, cero CORS, cero problemas.

Primero, instalá Flask-CORS por si acaso:

```bash
pip install flask-cors
```

Después, actualizá `app.py` para que sirva el archivo HTML:

```python
from flask import Flask, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde cualquier origen (por si acaso)


@app.route("/")
def servir_frontend():
    return send_from_directory(".", "index.html")
```

Ahora creá un archivo `index.html` en la **misma carpeta** que `app.py`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Jugadores del Mundial 2026</title>
</head>
<body>
    <h1>Jugadores del Mundial 2026</h1>

    <button onclick="cargarJugadores()">Cargar Jugadores</button>

    <ul id="lista"></ul>

    <script>
        const API = "http://127.0.0.1:5000";

        async function cargarJugadores() {
            const respuesta = await fetch(`${API}/jugadores`);
            const jugadores = await respuesta.json();

            const lista = document.getElementById("lista");
            lista.innerHTML = "";

            jugadores.forEach(j => {
                const item = document.createElement("li");
                item.textContent = `${j.nombre} - ${j.posicion} - ${j.seleccion}`;
                lista.appendChild(item);
            });
        }
    </script>
</body>
</html>
```

Ahora andá a `http://127.0.0.1:5000/`. ¿Qué ves? **Tu frontend.** Servido por Flask. Mismo origen, cero configuraciones raras, cero dolores de cabeza.

Hacé click en "Cargar Jugadores" y los ves aparecer en la lista. Eso que acaba de pasar es exactamente lo mismo que cuando hacés `GET /jugadores` en Postman — solo que ahora lo hizo el navegador, y vos ves el resultado en una interfaz.

---

### 5B — Reto: Mejorá el frontend

Agregale al `index.html`:

1. Un campo de texto para buscar por **nombre** (input + botón). Cuando escribas y des click, llamá a un endpoint de búsqueda... esperá, no tenemos endpoint de búsqueda por nombre. Agregá uno en `app.py`:

```
GET /buscar-por-nombre?q=Paolo
```

2. Mostrá los resultados en una **tabla** (no en lista) con columnas: Nombre, Edad, Posición, Equipo, Selección
3. Si no hay resultados, mostrá "No se encontraron jugadores"

<details>
<summary><b>Solución (reto)</b></summary>

**En `app.py`**, agregá el endpoint de búsqueda:

```python
@app.route("/buscar-por-nombre")
def buscar_por_nombre():
    q = request.args.get("q", "").lower()
    resultado = []
    for j in jugadores:
        if q in j["nombre"].lower():
            resultado.append(j)

    if not resultado:
        return {"mensaje": "No se encontraron jugadores"}

    return resultado
```

**En `index.html`**, reemplazá todo el contenido con esto:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Jugadores del Mundial 2026</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; max-width: 900px; }
        input, button { padding: 8px; margin: 3px; }
        table { border-collapse: collapse; width: 100%; margin-top: 10px; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background: #1a3a5c; color: white; }
        .error { color: #999; font-style: italic; }
    </style>
</head>
<body>
    <h1>Jugadores del Mundial 2026</h1>

    <div>
        <input type="text" id="busqueda" placeholder="Buscar por nombre...">
        <button onclick="buscarJugador()">Buscar</button>
        <button onclick="cargarJugadores()">Ver todos</button>
    </div>

    <p id="mensaje"></p>
    <table>
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Edad</th>
                <th>Posición</th>
                <th>Equipo</th>
                <th>Selección</th>
            </tr>
        </thead>
        <tbody id="tabla-jugadores"></tbody>
    </table>

    <script>
        const API = "http://127.0.0.1:5000";

        async function cargarJugadores() {
            const respuesta = await fetch(`${API}/jugadores`);
            const jugadores = await respuesta.json();
            mostrarJugadores(jugadores);
        }

        async function buscarJugador() {
            const q = document.getElementById("busqueda").value.trim();
            if (!q) {
                cargarJugadores();
                return;
            }

            const respuesta = await fetch(`${API}/buscar-por-nombre?q=${q}`);
            const datos = await respuesta.json();
            mostrarJugadores(datos);
        }

        function mostrarJugadores(datos) {
            const tbody = document.getElementById("tabla-jugadores");
            const mensaje = document.getElementById("mensaje");

            tbody.innerHTML = "";
            mensaje.textContent = "";

            if (datos.mensaje || datos.length === 0) {
                mensaje.textContent = datos.mensaje || "No se encontraron jugadores";
                mensaje.className = "error";
                return;
            }

            datos.forEach(j => {
                const fila = document.createElement("tr");
                fila.innerHTML = `
                    <td>${j.nombre}</td>
                    <td>${j.edad}</td>
                    <td>${j.posicion}</td>
                    <td>${j.equipo}</td>
                    <td>${j.seleccion}</td>
                `;
                tbody.appendChild(fila);
            });
        }

        cargarJugadores();
    </script>
</body>
</html>
```

**Probá:**
- La página carga automáticamente todos los jugadores
- Buscá "Paolo" → solo Guerrero
- Buscá "zzz" → "No se encontraron jugadores"
- Click en "Ver todos" → vuelve la lista completa

</details>

<p align="center">
  <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='300' viewBox='0 0 600 300'%3E%3Crect width='600' height='300' fill='%23f0f0f0'/%3E%3Ctext x='200' y='50' font-family='monospace' font-size='16' fill='%23333' text-anchor='middle' font-weight='bold'%3EARQUITECTURA:%20Frontend%20+%20Backend%3C/text%3E%3Crect x='50' y='80' width='200' height='150' rx='10' fill='%233498db'/%3E%3Ctext x='150' y='130' font-family='monospace' font-size='14' fill='white' text-anchor='middle'%3ENavegador%3C/text%3E%3Ctext x='150' y='155' font-family='monospace' font-size='12' fill='%23d4e6f1' text-anchor='middle'%3Eindex.html%3C/text%3E%3Ctext x='150' y='180' font-family='monospace' font-size='12' fill='%23d4e6f1' text-anchor='middle'%3Efetch()%3C/text%3E%3Crect x='350' y='80' width='200' height='150' rx='10' fill='%2327ae60'/%3E%3Ctext x='450' y='130' font-family='monospace' font-size='14' fill='white' text-anchor='middle'%3EFlask%3C/text%3E%3Ctext x='450' y='155' font-family='monospace' font-size='12' fill='%23d5f5e3' text-anchor='middle'%3Eapp.py%3C/text%3E%3Ctext x='450' y='180' font-family='monospace' font-size='12' fill='%23d5f5e3' text-anchor='middle'%3E/%20jugador/%3C/text%3E%3Crect x='350' y='200' width='200' height='30' rx='5' fill='%231e8448'/%3E%3Ctext x='450' y='220' font-family='monospace' font-size='11' fill='white' text-anchor='middle'%3ELista%20jugadores%20(memoria)%3C/text%3E%3Cline x1='250' y1='155' x2='345' y2='155' stroke='%23e74c3c' stroke-width='3' marker-end='url(%23arrow)'/%3E%3Ctext x='298' y='145' font-family='monospace' font-size='10' fill='%23e74c3c' text-anchor='middle'%3EGET/POST%3C/text%3E%3Cdefs%3E%3Cmarker id='arrow' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='6' markerHeight='6' orient='auto'%3E%3Cpath d='M0,0 L10,5 L0,10 z' fill='%23e74c3c'/%3E%3C/marker%3E%3C/defs%3E%3C/svg%3E" alt="Diagrama de arquitectura Frontend + Backend" width="600">
</p>
<p align="center"><sub><i>El navegador (HTML + JS) le habla a Flask (Python). Flask responde con datos. Todo en el mismo puerto.</i></sub></p>

---

## 6. CRUD desde el navegador — el frontend completo

Ahora viene lo bueno. Ya tenemos la API que hace CRUD. Ya tenemos un frontend que muestra datos. Es hora de **unir todo** y crear, editar y eliminar jugadores directamente desde el navegador. Sin Postman, sin terminal — todo desde la interfaz.

Esto es lo que hace que un backend cobre vida. Porque una API que solo se prueba con Postman es como un motor fuera del auto — corre, hace ruido, pero no lleva a nadie a ningún lado. Cuando conectás el frontend, el auto empieza a andar.

### 6A — Demo: Agregar jugador desde el frontend

Agregá esto al `index.html` (después de la tabla):

```html
<h2>Agregar jugador</h2>
<form id="form-crear">
    <input type="text" name="nombre" placeholder="Nombre" required>
    <input type="number" name="edad" placeholder="Edad">
    <input type="text" name="posicion" placeholder="Posición" required>
    <input type="text" name="equipo" placeholder="Equipo">
    <input type="text" name="seleccion" placeholder="Selección" required>
    <button type="submit">Agregar</button>
</form>
```

Y esto al `script`:

```javascript
document.getElementById("form-crear").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const datos = Object.fromEntries(formData.entries());

    const respuesta = await fetch(`${API}/jugador`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(datos),
    });

    if (respuesta.ok) {
        e.target.reset();
        cargarJugadores();
    } else {
        const error = await respuesta.json();
        alert("Error: " + (error.error || "No se pudo crear"));
    }
});
```

Cuando creés un jugador desde el formulario, la tabla se actualiza automáticamente. Sin recargar la página. Sin magia — es `fetch()` con POST, y cuando el servidor responde 201, llamás a `cargarJugadores()` de nuevo.

---

### 6B — Reto: CRUD completo en frontend

Agregá al `index.html`:

1. **Botón "Eliminar"** en cada fila de la tabla. Al hacer click:
   - Confirmá con `confirm("¿Seguro que querés eliminar a X?")`
   - Hacé un `DELETE` a `{API}/jugador/{id}`
   - Si funciona, recargá la tabla

2. **Edición inline**: al hacer click en un nombre, convertí esa celda en un input para editar. Al perder el foco o presionar Enter, enviá un `PATCH` con el nuevo nombre.

3. Mostrá los **códigos de error** del servidor (400, 404) en la interfaz, no solo con `alert()`.

> **Pista:** para el botón eliminar, necesitás el ID de cada jugador. Modificá `mostrarJugadores()` para guardar el ID en un atributo `data-id` de la fila. Para la edición inline, cada celda editable necesita su propio `data-campo`.

<details>
<summary><b>Solución (reto)</b></summary>

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Jugadores del Mundial 2026</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; max-width: 900px; }
        input, button { padding: 8px; margin: 3px; }
        table { border-collapse: collapse; width: 100%; margin-top: 10px; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background: #1a3a5c; color: white; }
        .error { color: #999; font-style: italic; }
        .btn-eliminar { background: #d9534f; color: white; border: none; cursor: pointer; }
        .btn-eliminar:hover { background: #c9302c; }
        form { background: #f5f5f5; padding: 15px; border-radius: 5px; margin: 15px 0; }
        input { border: 1px solid #ccc; border-radius: 3px; }
        .mensaje-error { color: #d9534f; font-weight: bold; }
        .celda-editable { cursor: pointer; }
        .celda-editable:hover { background: #fff3cd; }
    </style>
</head>
<body>
    <h1>Jugadores del Mundial 2026</h1>

    <form id="form-crear">
        <h3>Agregar jugador</h3>
        <input type="text" name="nombre" placeholder="Nombre" required>
        <input type="number" name="edad" placeholder="Edad">
        <input type="text" name="posicion" placeholder="Posición" required>
        <input type="text" name="equipo" placeholder="Equipo">
        <input type="text" name="seleccion" placeholder="Selección" required>
        <button type="submit">Agregar</button>
    </form>

    <div>
        <input type="text" id="busqueda" placeholder="Buscar por nombre...">
        <button onclick="buscarJugador()">Buscar</button>
        <button onclick="cargarJugadores()">Ver todos</button>
    </div>

    <p id="mensaje-estado"></p>

    <table>
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Edad</th>
                <th>Posición</th>
                <th>Equipo</th>
                <th>Selección</th>
                <th>Acción</th>
            </tr>
        </thead>
        <tbody id="tabla-jugadores"></tbody>
    </table>

    <script>
        const API = "http://127.0.0.1:5000";

        async function cargarJugadores() {
            const respuesta = await fetch(`${API}/jugadores`);
            const jugadores = await respuesta.json();
            mostrarJugadores(jugadores);
        }

        async function buscarJugador() {
            const q = document.getElementById("busqueda").value.trim();
            if (!q) { cargarJugadores(); return; }

            const respuesta = await fetch(`${API}/buscar-por-nombre?q=${q}`);
            const datos = await respuesta.json();
            mostrarJugadores(datos);
        }

        function mostrarJugadores(datos) {
            const tbody = document.getElementById("tabla-jugadores");
            const estado = document.getElementById("mensaje-estado");
            tbody.innerHTML = "";
            estado.textContent = "";

            if (datos.mensaje || datos.length === 0) {
                estado.textContent = datos.mensaje || "No se encontraron jugadores";
                estado.className = "error";
                return;
            }

            datos.forEach(j => {
                const fila = document.createElement("tr");
                fila.dataset.id = j.id;
                fila.innerHTML = `
                    <td class="celda-editable" data-campo="nombre">${j.nombre}</td>
                    <td>${j.edad}</td>
                    <td>${j.posicion}</td>
                    <td>${j.equipo}</td>
                    <td>${j.seleccion}</td>
                    <td><button class="btn-eliminar" data-id="${j.id}" data-nombre="${j.nombre}">Eliminar</button></td>
                `;
                tbody.appendChild(fila);
            });

            document.querySelectorAll(".btn-eliminar").forEach(btn => {
                btn.addEventListener("click", eliminarJugador);
            });

            document.querySelectorAll(".celda-editable").forEach(celda => {
                celda.addEventListener("click", editarCelda);
            });
        }

        async function eliminarJugador(e) {
            const id = e.target.dataset.id;
            const nombre = e.target.dataset.nombre;

            if (!confirm(`¿Seguro que querés eliminar a ${nombre}?`)) return;

            const respuesta = await fetch(`${API}/jugador/${id}`, {
                method: "DELETE"
            });

            if (respuesta.ok) {
                cargarJugadores();
            } else {
                const error = await respuesta.json();
                document.getElementById("mensaje-estado").textContent = "Error: " + (error.error || "No se pudo eliminar");
                document.getElementById("mensaje-estado").className = "mensaje-error";
            }
        }

        function editarCelda(e) {
            const celda = e.target;
            const campo = celda.dataset.campo;
            const id = celda.closest("tr").dataset.id;
            const valorActual = celda.textContent;

            const input = document.createElement("input");
            input.type = "text";
            input.value = valorActual;
            celda.textContent = "";
            celda.appendChild(input);
            input.focus();

            async function guardar() {
                const nuevoValor = input.value.trim();
                if (nuevoValor && nuevoValor !== valorActual) {
                    const respuesta = await fetch(`${API}/jugador/${id}`, {
                        method: "PATCH",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({[campo]: nuevoValor}),
                    });

                    if (respuesta.ok) {
                        cargarJugadores();
                    } else {
                        const error = await respuesta.json();
                        document.getElementById("mensaje-estado").textContent = "Error: " + (error.error || "No se pudo actualizar");
                        document.getElementById("mensaje-estado").className = "mensaje-error";
                        celda.textContent = valorActual;
                    }
                } else {
                    celda.textContent = valorActual;
                }
            }

            input.addEventListener("blur", guardar);
            input.addEventListener("keydown", (e) => {
                if (e.key === "Enter") {
                    e.preventDefault();
                    input.blur();
                }
                if (e.key === "Escape") {
                    celda.textContent = valorActual;
                }
            });
        }

        document.getElementById("form-crear").addEventListener("submit", async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const datos = Object.fromEntries(formData.entries());

            if (datos.edad) datos.edad = parseInt(datos.edad);

            const respuesta = await fetch(`${API}/jugador`, {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(datos),
            });

            if (respuesta.ok) {
                e.target.reset();
                cargarJugadores();
            } else {
                const error = await respuesta.json();
                document.getElementById("mensaje-estado").textContent = "Error: " + (error.error || "No se pudo crear");
                document.getElementById("mensaje-estado").className = "mensaje-error";
            }
        });

        cargarJugadores();
    </script>
</body>
</html>
```

**Eso es todo. Tenés un CRUD completo funcionando:**
- El backend sirve el frontend y expone la API
- El frontend consume la API con `fetch`
- Podés crear, leer, actualizar (editando inline) y eliminar jugadores

</details>

---

## 7. Proyecto final — el desafío que separa a los que entienden de los que solo copian

### 7A — Demo: La arquitectura completa (mirá TODO lo que construimos)

Pará un toque y mirá esto:

```
Navegador (index.html)
       │
       │ fetch()  ← GET, POST, PATCH, DELETE
       ▼
Flask (app.py) ──► jugadores (lista de diccionarios en memoria)
       │
       │ send_from_directory()
       ▼
   index.html servido por Flask
```

¿Te das cuenta? **Todo vive en una sola URL** (`http://127.0.0.1:5000`). Flask sirve el frontend Y expone la API. Sin CORS, sin configuraciones raras, sin magia. Solo código que vos escribiste.

Hiciste un backend completo, con frontend incluido, que hace CRUD. Eso no es poco, causa. En 2 días pasaste de "hola mundo" a tener una API funcional con interfaz gráfica. La mayoría de la gente paga cursos enteros para llegar a esto.

---

### 7B — Reto final: Extendé la API con equipos

Ahora que tenés el CRUD de jugadores funcionando como un campeón, agregá un nuevo recurso: **Equipos de fútbol**. Porque un jugador sin equipo es como un backend sin endpoints — no funciona.

1. Creá una lista `equipos` con data así:

```python
equipos = [
    {"id": 1, "nombre": "Real Madrid", "pais": "España", "liga": "La Liga", "copas": 15},
    {"id": 2, "nombre": "Liverpool", "pais": "Inglaterra", "liga": "Premier League", "copas": 6},
    {"id": 3, "nombre": "Alianza Lima", "pais": "Perú", "liga": "Liga 1", "copas": 25},
    {"id": 4, "nombre": "Inter Miami", "pais": "EE.UU.", "liga": "MLS", "copas": 0},
    {"id": 5, "nombre": "Al Hilal", "pais": "Arabia Saudita", "liga": "Saudi League", "copas": 18},
]
```

2. Implementá el CRUD completo para equipos (GET todos, GET por ID, POST, PATCH, DELETE)

3. Modificá `GET /jugadores` para que en lugar de mandar el nombre del equipo como texto, mande el objeto completo del equipo. O sea, si el jugador tiene `"equipo": "Real Madrid"`, que el endpoint devuelva los datos completos del Real Madrid.

4. Agregá en el frontend una sección para listar y crear equipos

5. **PLUS:** Hacé que al crear un jugador, el campo `equipo` sea un `<select>` que cargue los equipos desde la API. O sea, el frontend pide `GET /equipos` y llena el combo. Nivel dios.

<details>
<summary><b>Pistas (no solución — este reto es tuyo)</b></summary>

No te voy a dar la solución completa porque este es el ejercicio que separa a los que entienden de los que copian y pegan. Pero te tiro unos tips:

- Los endpoints de equipos son IDÉNTICOS en estructura a los de jugadores. Literalmente podés copiar y pegar, cambiar "jugador" por "equipo", y funciona.
- Para el punto 3, vas a necesitar buscar el equipo por nombre dentro del bucle de jugadores. Cuando armás la respuesta, en vez de poner `j["equipo"]`, poné el objeto completo del equipo que encontraste.
- Para el `<select>`, hacé un `fetch` a la API de equipos cuando cargue la página y llená las opciones con un `forEach`.

Si te trabás, preguntá. Pero primero intentá. La diferencia entre un dev que sabe y uno que no, es que el primero **prueba antes de preguntar**.

</details>

---

## 🎯 Resumen de conceptos

| Tema | Demo | Reto | Conceptos clave |
|------|:----:|:----:|-----------------|
| 0. ¿Qué es CRUD? | — | — | POST=crear, GET=leer, PATCH=actualizar, DELETE=borrar |
| 1. READ | ✅ | ✅ | `@app.route()`, `GET`, ruta con `<int:id>`, 404 |
| 2. CREATE | ✅ | ✅ | `POST`, `request.json`, validación, código 201 |
| 3. UPDATE (PATCH) | ✅ | ✅ | Reemplazo vs actualización parcial, validar tipo/rango |
| 4. DELETE | ✅ | ✅ | `DELETE`, `jugadores.remove()`, 404 si no existe |
| 5. Frontend + fetch | ✅ | ✅ | `fetch()`, `send_from_directory()`, HTML dinámico |
| 6. CRUD desde frontend | ✅ | ✅ | POST/PATCH/DELETE con fetch, edición inline |
| 7. Proyecto integrador | ✅ | ✅ | CRUD completo frontend + backend + equipos |

---

<sub>Créditos de imágenes: logos de HTML5, JavaScript, Flask, Postman y JSON, y diagrama cliente-servidor, servidos desde Wikimedia Commons. Los logos son marcas de sus respectivos dueños y se usan solo con fines educativos de identificación. Diagrama de arquitectura generado a modo ilustrativo.</sub>
