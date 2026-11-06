# 🧠 Guía — Día 1 (Semana 5): Flask + PostgreSQL + SQLAlchemy

<p align="center">
  <img src="https://flask.palletsprojects.com/en/stable/_static/flask-logo.png" alt="Logo de Flask" height="80">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg" alt="Logo de PostgreSQL" height="100">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Logo de Python" height="80">
</p>

<p align="center">
  <img src="https://www.sqlalchemy.org/img/sqla_logo.png" alt="Logo de SQLAlchemy" height="60">
</p>

Bienvenidos al día más importante del curso hasta ahora. Hasta ahora todo lo que construían en Python vivía en listas de diccionarios que desaparecían al apagar el servidor. Eso se acabó. Hoy aprendemos a **construir una API real** que conecta con una base de datos PostgreSQL.

Vamos a construir una **API de Música Peruana** — artistas, canciones, géneros. Cumbia, rock, música criolla. Datos de verdad, de artistas que ustedes conocen. Nada de tablas de ejemplo sin sentido.

El viaje de hoy: van a crear una API completa con Flask que se conecta a PostgreSQL. Primero con **psycopg2** (conexión directa, SQL manual) para entender cómo funciona por debajo. Después con **SQLAlchemy** (ORM) para ver lo fácil que puede ser. Al final del día, ustedes van a poder decir "yo sé construir APIs con base de datos".

---

## 0. El modelo cliente-servidor — la base de TODO lo que viene (15 min)

Hasta ahora, cuando programaban en Python, ustedes escribían un script, lo ejecutaban, y ESE MISMO programa hacía todo: leía datos, los procesaba, mostraba resultados. Un solo actor.

En backend, la cosa cambia. Ahora hay **dos actores separados**:

- El **cliente**: es quien pide algo. Puede ser un navegador, una app de celular, Postman, otro programa. El cliente no sabe (ni le importa) cómo está hecho el servidor por dentro.
- El **servidor**: es quien escucha pedidos y responde. Nuestro `app.py` con Flask va a ser el servidor.

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*OAUeCxrFGR2c0MPWQz8bAg.png" alt="Diagrama Cliente-Servidor" width="600">
</p>

**Analogía (guárdensela, la van a usar todo el curso):** pensá en un restaurante. Vos (cliente) no entrás a la cocina a cocinar tu propio plato. Le pedís al mozo (la petición, el *request*) y la cocina (el servidor) te devuelve el plato (la respuesta, el *response*). No te importa cómo está organizada la cocina por dentro — te importa que el pedido llegue bien y rápido.

Eso es exactamente lo que va a pasar entre Postman (o cualquier app) y nuestro Flask:

```
Cliente (Postman)  --- pide algo -->  Servidor (Flask)  --- consulta -->  PostgreSQL
Cliente (Postman)  <-- responde ---  Servidor (Flask)  <-- resultado --  PostgreSQL
```

**Pero hay un problema:** ¿y si el servidor se apaga? ¡Adiós datos! Por eso necesitamos una **base de datos**. Flask se conecta a PostgreSQL, y ahí los datos viven permanentemente.

### ¿Qué es una base de datos?

Una **base de datos** es como un archivero profesional donde guardamos información de forma estructurada. A diferencia de una lista de Python:

| Lista de Python | Base de datos PostgreSQL |
|----------------|--------------------------|
| Se borra al apagar | Vive en disco, siempre está |
| Solo funciona en tu compu | Varios la pueden usar al mismo tiempo |
| Sin reglas de seguridad | Garantiza integridad de datos |
| Buscar es lento con `for` | Búsquedas rápidas con índices |

**¿Y Flask?** Flask es el **cocinero** que conecta al cliente con la base de datos. Recibe el pedido (request), consulta la BD, y devuelve la respuesta (response).

```
┌─────────────┐      ┌─────────────┐      ┌─────────────────┐
│   Cliente   │ ───► │    Flask    │ ───► │   PostgreSQL    │
│  (Postman)  │ ◄─── │  (Servidor) │ ◄─── │ (Base de Datos) │
└─────────────┘      └─────────────┘      └─────────────────┘
     Request              psycopg2              Query SQL
     Response             jsonify               Resultado
```

---

## 1. Preparación del entorno — las bases (20 min)

Antes de escribir una sola línea de código, necesitamos preparar nuestro entorno de desarrollo. Esto es como preparar la cocina antes de cocinar: sin las herramientas correctas, no se puede trabajar.

### 1A — Demo: Crear el proyecto y el entorno virtual

1. Abrí una terminal en la carpeta de tu proyecto
2. Creá la carpeta del proyecto:

```bash
mkdir musica_peruana_api
cd musica_peruana_api
```

3. Creá el entorno virtual:

```bash
python -m venv venv
```

Esto crea una carpeta `venv/` con una copia aislada de Python. Fijate que aparece una carpeta nueva en tu proyecto — ábrela y vas a ver que tiene su propio `python.exe`, su propio `pip`, todo aparte.

4. Activá el entorno:

```bash
# Windows (PowerShell)
venv\Scripts\activate

# Windows (CMD)
venv\Scripts\activate.bat

# Mac/Linux
source venv/bin/activate
```

Vas a ver que aparece `(venv)` al inicio de la línea. Eso significa que estás dentro del entorno virtual. Es como si te hubieras puesto una casaca que dice "todo lo que instale ahora es solo para este proyecto".

5. Instalá las dependencias:

```bash
pip install flask psycopg2-binary sqlalchemy flask-sqlalchemy
```

**¿Qué instalamos?**

| Paquete | ¿Para qué? |
|---------|------------|
| `flask` | El microframework para crear APIs web |
| `psycopg2-binary` | Driver para conectarse a PostgreSQL desde Python |
| `sqlalchemy` | ORM (Object-Relational Mapper) |
| `flask-sqlalchemy` | Integra SQLAlchemy con Flask |

---

## 2. PostgreSQL — Crear la base de datos (15 min)

Ahora necesitamos crear la base de datos donde vivirán nuestros datos de música peruana.

### 2A — Demo: Crear la BD y el schema

1. Abran **pgAdmin** y conéctense a su servidor PostgreSQL
2. Click derecho en **Databases** → **Create** → **Database...**
3. Nombre: `musica_peruana`
4. Owner: `postgres`
5. Save

Ahora, abran la Query Tool de `musica_peruana` (click derecho → Query Tool).

Andá al archivo **`schema.sql`** que está en esta carpeta y copiá TODO el contenido. Pegalo en la Query Tool y ejecutalo.

<p align="center">
  <img src="https://www.pgadmin.org/static/docs/pgadmin4-8.x/en_US/images/property-dialog.png" alt="pgAdmin Query Tool" width="500">
</p>

**¿Qué creó ese SQL?**
- Una tabla `artistas` con 10 artistas (Grupo 5, Agua Marina, Libido, Chabuca Granda, etc.)
- Una tabla `canciones` con 25 canciones de ejemplo
- Una relación 1:N: un artista tiene muchas canciones

Verificá que todo esté bien ejecutando estas consultas:

```sql
-- Ver todos los artistas
SELECT * FROM artistas;

-- Ver todos las canciones
SELECT * FROM canciones;
```

Si ves los 10 artistas y 25 canciones, todo está perfecto.

---

### 2B — Reto: Explorá la base de datos

Respondé estas preguntas ejecutando SQL en pgAdmin:

1. ¿Cuántos artistas hay por cada género?
2. ¿Cuáles son las canciones de Grupo 5?

<details>
<summary><b>Solución (reto)</b></summary>

```sql
-- 1. Artistas por género
SELECT genero, COUNT(*) AS cantidad
FROM artistas
GROUP BY genero;

-- 2. Canciones de Grupo 5
SELECT c.titulo, c.album, c.anio_lanzamiento
FROM canciones c
INNER JOIN artistas a ON c.artista_id = a.id
WHERE a.nombre = 'Grupo 5';
```

</details>

---

## 3. psycopg2 + Flask — La API manual (90 min)

Ahora viene lo emocionante: construir la API. Primero con **psycopg2** para entender exactamente qué pasa por debajo. Cada query SQL la escribimos nosotros.

<p align="center">
  <img src="https://flask.palletsprojects.com/en/stable/_static/flask-logo.png" alt="Logo de Flask" height="60">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://www.psycopg.org/static/img/psycopg2-binary.png" alt="Logo de psycopg2" height="60">
</p>

### 3A — Demo: La conexión a la base de datos

Creá un archivo `app.py` con el siguiente contenido:

```python
from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# =============================================================
# CONFIGURACIÓN DE LA BASE DE DATOS
# =============================================================
DB_CONFIG = {
    "host": "localhost",
    "database": "musica_peruana",
    "user": "postgres",
    "password": "postgres",  # Cambiar por su contraseña
    "port": 5432
}

# Columnas de cada tabla (para convertir tuplas a diccionarios)
COLUMNAS_ARTISTAS = ["id", "nombre", "genero", "pais_origen", "activo", "fecha_creacion"]
COLUMNAS_CANCIONES = ["id", "titulo", "album", "duracion_segundos", "anio_lanzamiento", "artista_id"]


def get_db_connection():
    """Crear una conexión a la base de datos."""
    conn = psycopg2.connect(**DB_CONFIG)
    return conn


def tupla_a_diccionario(tupla, columnas):
    """Convertir una tupla de la BD a un diccionario."""
    return dict(zip(columnas, tupla))


if __name__ == "__main__":
    app.run(debug=True)
```

**Explicación línea por línea:**

| Parte | Significado |
|-------|-------------|
| `from flask import Flask, jsonify, request` | Importamos las herramientas de Flask |
| `import psycopg2` | Importamos el driver de PostgreSQL |
| `DB_CONFIG` | Diccionario con los datos de conexión |
| `get_db_connection()` | Función que crea una nueva conexión |
| `@app.route("/")` | Decorador que define una ruta URL |
| `jsonify()` | Convierte un diccionario de Python a JSON |
| `app.run(debug=True)` | Inicia el servidor con modo desarrollo |

**Probá en Postman:**
- Ejecutá `python app.py`
- Abrí Postman y creá un GET a `http://127.0.0.1:5000/`
- Send → deberías ver el JSON con los endpoints

<p align="center">
  <img src="https://learning.postman.com/static/docs-hero-DYvJfQe0.svg" alt="Interfaz de Postman" width="500">
</p>

---

### ⚠️ IMPORTANTE: SQL Injection — ¡CUIDADO CON LOS STRINGS!

Antes de escribir queries, algo **muy importante** de seguridad:

```python
# ❌ ¡INSEGURO! — NUNCA hacer esto en producción
nombre = "Grupo 5"
cur.execute(f"SELECT * FROM artistas WHERE nombre = '{nombre}'")

# Si el usuario manda: nombre = "'; DROP TABLE artistas; --"
# El query se convierte en:
# SELECT * FROM artistas WHERE nombre = ''; DROP TABLE artistas; --'
# ¡Eliminan TODA la tabla!
```

```python
# ✅ SEGURO — Usar %s como placeholder
nombre = "Grupo 5"
cur.execute("SELECT * FROM artistas WHERE nombre = %s", (nombre,))
# PostgreSQL sabe que 'Grupo 5' es un DATO, no código SQL
```

**La regla de oro:** Los datos del usuario NUNCA se concatenan directo al SQL. psycopg2 se encarga de sanitizarlos con `%s`.

**¿Por qué en esta guía usamos f-strings?** Para que sea más fácil de entender para principiantes, pero recorden que en producción **siempre** usar `%s` con parámetros.

---

### 3B — Demo: GET todos los artistas

Agregar esta función a `app.py`:

```python
@app.route("/artistas", methods=["GET"])
def get_artistas():
    """Obtener todos los artistas."""
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM artistas ORDER BY nombre")
    filas = cur.fetchall()

    cur.close()
    conn.close()

    # Convertir cada tupla a diccionario
    artistas = []
    for fila in filas:
        artista = tupla_a_diccionario(fila, COLUMNAS_ARTISTAS)
        artistas.append(artista)

    return jsonify(artistas)
```

**¿Qué hace cada línea?**

| Línea | Significado |
|-------|-------------|
| `@app.route("/artistas", methods=["GET"])` | Esta función responde a GET /artistas |
| `conn = get_db_connection()` | Abro una conexión a PostgreSQL |
| `cur = conn.cursor()` | Creo un cursor (el que ejecuta SQL) |
| `cur.execute("SELECT * FROM artistas")` | Ejecuto el SQL |
| `cur.fetchall()` | Obtengo todos los resultados como tuplas |
| `tupla_a_diccionario(fila, COLUMNAS_ARTISTAS)` | Convierto cada tupla a diccionario |
| `cur.close()` | Cierro el cursor |
| `conn.close()` | Cierro la conexión |
| `return jsonify(artistas)` | Convierto a JSON y devuelvo |

**Probá en Postman:**
- GET `http://127.0.0.1:5000/artistas`
- Deberías ver los 10 artistas en JSON

---

### 3C — Demo: GET un artista por ID

```python
@app.route("/artistas/<int:id>", methods=["GET"])
def get_artista(id):
    """Obtener un artista por su ID."""
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM artistas WHERE id = %s", (id,))
    fila = cur.fetchone()

    cur.close()
    conn.close()

    if fila is None:
        return jsonify({"error": "Artista no encontrado"}), 404

    artista = tupla_a_diccionario(fila, COLUMNAS_ARTISTAS)
    return jsonify(artista)
```

**Concepto clave:** `<int:id>` en la ruta. Flask toma el número de la URL y lo pasa como parámetro `id` a la función. El `int:` asegura que solo acepte números.

**Probá en Postman:**
- GET `http://127.0.0.1:5000/artistas/1` → Grupo 5
- GET `http://127.0.0.1:5000/artistas/99` → Error 404

---

### 3D — Demo: GET canciones con el nombre del artista

```python
@app.route("/canciones", methods=["GET"])
def get_canciones():
    """Obtener todas las canciones con el nombre del artista."""
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.titulo, c.album, c.duracion_segundos,
               c.anio_lanzamiento, a.nombre AS artista, a.genero
        FROM canciones c
        INNER JOIN artistas a ON c.artista_id = a.id
        ORDER BY a.nombre, c.titulo
    """)
    filas = cur.fetchall()

    cur.close()
    conn.close()

    # Columnas del resultado del JOIN
    columnas_canciones = ["id", "titulo", "album", "duracion_segundos", "anio_lanzamiento", "artista", "genero"]

    # Convertir cada tupla a diccionario
    canciones = []
    for fila in filas:
        cancion = tupla_a_diccionario(fila, columnas_canciones)
        canciones.append(cancion)

    return jsonify(canciones)
```

**¿Qué hace el JOIN?** Une la tabla `canciones` con `artistas` para traer el nombre del artista en lugar de solo el `artista_id`. Es exactamente el mismo JOIN que vimos en la semana 4.

**¿Por qué definimos `columnas_canciones`?** Porque el resultado del JOIN tiene columnas de AMBAS tablas, y necesitamos saber el orden exacto para la conversión.

**Probá en Postman:**
- GET `http://127.0.0.1:5000/canciones`
- Deberías ver 25 canciones con el nombre del artista

---

### 3E — Demo: POST crear un nuevo artista

```python
@app.route("/artistas", methods=["POST"])
def crear_artista():
    """Crear un nuevo artista."""
    datos = request.json

    if not datos:
        return jsonify({"error": "Debes enviar datos en formato JSON"}), 400

    if "nombre" not in datos or not str(datos.get("nombre", "")).strip():
        return jsonify({"error": "Falta el campo: nombre"}), 400

    if "genero" not in datos or not str(datos.get("genero", "")).strip():
        return jsonify({"error": "Falta el campo: genero"}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO artistas (nombre, genero, pais_origen)
        VALUES (%s, %s, %s)
    """, (
        datos["nombre"],
        datos["genero"],
        datos.get("pais_origen", "Perú")
    ))

    conn.commit()

    # Obtener el ID generado
    id_generado = cur.fetchone()[0]

    cur.close()
    conn.close()

    # Construir el artista devuelto
    nuevo_artista = {
        "id": id_generado,
        "nombre": datos["nombre"],
        "genero": datos["genero"],
        "pais_origen": datos.get("pais_origen", "Perú"),
        "activo": True
    }
    return jsonify(nuevo_artista), 201
```

**Explicación:**

| Parte | Significado |
|-------|-------------|
| `request.json` | Obtener el JSON enviado en el body del request |
| `conn.commit()` | Guardar los cambios (sin esto, no se guarda nada) |
| `cur.fetchone()[0]` | Obtener el ID generado automáticamente |
| `201` | Código HTTP de "Created" (éxito al crear) |

**Probá en Postman:**
- Método: POST
- URL: `http://127.0.0.1:5000/artistas`
- Body → raw → JSON:

```json
{
    "nombre": "Teresa Izquierdo",
    "genero": "Criolla",
    "pais_origen": "Perú"
}
```

- Send → Deberías ver el artista creado con código 201

<p align="center">
  <img src="https://learning.postman.com/static/docs-hero-DYvJfQe0.svg" alt="Postman POST" width="500">
</p>

---

### 3F — Demo: PUT actualizar un artista

```python
@app.route("/artistas/<int:id>", methods=["PUT"])
def actualizar_artista(id):
    """Actualizar un artista existente."""
    datos = request.json

    conn = get_db_connection()
    cur = conn.cursor()

    # Verificar que existe
    cur.execute("SELECT * FROM artistas WHERE id = %s", (id,))
    fila = cur.fetchone()

    if fila is None:
        cur.close()
        conn.close()
        return jsonify({"error": "Artista no encontrado"}), 404

    # Convertir a diccionario para obtener valores actuales
    artista = tupla_a_diccionario(fila, COLUMNAS_ARTISTAS)

    cur.execute("""
        UPDATE artistas
        SET nombre = %s, genero = %s, pais_origen = %s, activo = %s
        WHERE id = %s
        RETURNING *
    """, (
        datos.get("nombre", artista["nombre"]),
        datos.get("genero", artista["genero"]),
        datos.get("pais_origen", artista["pais_origen"]),
        datos.get("activo", artista["activo"]),
        id
    ))

    fila_actualizada = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    artista_actualizado = tupla_a_diccionario(fila_actualizada, COLUMNAS_ARTISTAS)
    return jsonify(artista_actualizado)
```

**Probá en Postman:**
- Método: PUT
- URL: `http://127.0.0.1:5000/artistas/1`
- Body → raw → JSON:

```json
{
    "genero": "Cumbia Marítima"
}
```

---

### 3G — Demo: DELETE eliminar un artista

```python
@app.route("/artistas/<int:id>", methods=["DELETE"])
def eliminar_artista(id):
    """Eliminar un artista y todas sus canciones."""
    conn = get_db_connection()
    cur = conn.cursor()

    # Verificar que existe
    cur.execute("SELECT * FROM artistas WHERE id = %s", (id,))
    fila = cur.fetchone()

    if fila is None:
        cur.close()
        conn.close()
        return jsonify({"error": "Artista no encontrado"}), 404

    artista = tupla_a_diccionario(fila, COLUMNAS_ARTISTAS)

    # Eliminar canciones primero (por la FK)
    cur.execute("DELETE FROM canciones WHERE artista_id = %s", (id,))

    # Eliminar el artista
    cur.execute("DELETE FROM artistas WHERE id = %s", (id,))

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "mensaje": f"Artista '{artista['nombre']}' eliminado",
        "artista": artista
    })
```

**¿Por qué eliminar canciones primero?** Por la foreign key. Si intentamos eliminar un artista que tiene canciones, PostgreSQL nos dará error. Por eso primero borramos las canciones, luego el artista.

**Probá en Postman:**
- Método: DELETE
- URL: `http://127.0.0.1:5000/artistas/11`

---

### 3H — Reto: Creá el endpoint de artistas por género

**Profe dice:** "Necesito un endpoint que me devuelva todos los artistas de un género específico. Por ejemplo, GET /artistas/genero/Cumbia debería devolver solo los de cumbia."

Crear el endpoint `GET /artistas/genero/<genero>` que:
1. Reciba el género como parámetro de ruta
2. Devuelva los artistas de ese género
3. Si no hay artistas de ese género, devuelva `{"mensaje": "No hay artistas de ese género"}` con código 200
4. Sea case-insensitive (que funcione con "cumbia", "Cumbia", "CUMBIA")

<details>
<summary><b>Solución (reto)</b></summary>

```python
@app.route("/artistas/genero/<genero>", methods=["GET"])
def get_artistas_por_genero(genero):
    """Obtener artistas por género."""
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM artistas WHERE LOWER(genero) = LOWER(%s) ORDER BY nombre",
        (genero,)
    )
    filas = cur.fetchall()

    cur.close()
    conn.close()

    if not filas:
        return jsonify({"mensaje": "No hay artistas de ese género"}), 200

    artistas = []
    for fila in filas:
        artista = tupla_a_diccionario(fila, COLUMNAS_ARTISTAS)
        artistas.append(artista)

    return jsonify(artistas)
```

**Probá en Postman:**
- GET `http://127.0.0.1:5000/artistas/genero/Cumbia` → 3 artistas
- GET `http://127.0.0.1:5000/artistas/genero/rock` → 5 artistas
- GET `http://127.0.0.1:5000/artistas/genero/jazz` → "No hay artistas de ese género"

</details>

---

### 3I — Reto: Creá el endpoint de buscador

**Profe dice:** "Necesito un endpoint que me permita buscar artistas o canciones por nombre. Algo como /buscador?q=grupo que me devuelva todo lo que contenga 'grupo' en el nombre."

Crear el endpoint `GET /buscador?q=<texto>` que:
1. Reciba el texto de búsqueda como query param
2. Busque en artistas (nombre) y en canciones (título)
3. Devuelva los resultados de ambas tablas
4. Si no hay resultados, devuelva `{"mensaje": "No se encontraron resultados"}` con código 200

<details>
<summary><b>Solución (reto)</b></summary>

```python
@app.route("/buscador", methods=["GET"])
def buscador():
    """Buscar artistas o canciones por nombre."""
    texto = request.args.get("q", "")

    if not texto:
        return jsonify({"error": "Debes enviar un parámetro 'q'"}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    # Buscar artistas
    cur.execute(
        "SELECT * FROM artistas WHERE LOWER(nombre) LIKE LOWER(%s)",
        (f"%{texto}%",)
    )
    filas_artistas = cur.fetchall()

    # Buscar canciones
    cur.execute("""
        SELECT c.id, c.titulo, c.album, a.nombre AS artista
        FROM canciones c
        INNER JOIN artistas a ON c.artista_id = a.id
        WHERE LOWER(c.titulo) LIKE LOWER(%s)
    """, (f"%{texto}%",))
    filas_canciones = cur.fetchall()

    cur.close()
    conn.close()

    # Columnas para las canciones del JOIN
    columnas_canciones = ["id", "titulo", "album", "artista"]

    artistas = []
    for fila in filas_artistas:
        artista = tupla_a_diccionario(fila, COLUMNAS_ARTISTAS)
        artistas.append(artista)

    canciones = []
    for fila in filas_canciones:
        cancion = tupla_a_diccionario(fila, columnas_canciones)
        canciones.append(cancion)

    if not artistas and not canciones:
        return jsonify({"mensaje": "No se encontraron resultados"}), 200

    return jsonify({
        "artistas": artistas,
        "canciones": canciones
    })
```

**Probá en Postman:**
- GET `http://127.0.0.1:5000/buscador?q=grupo` → Grupo 5
- GET `http://127.0.0.1:5000/buscador?q=cariñito` → Canción "Cariñito"
- GET `http://127.0.0.1:5000/buscador?q=xyz` → "No se encontraron resultados"

</details>

---

## 4. SQLAlchemy ORM — El mismo CRUD pero más fácil (45 min)

Ahora viene la magia. Vamos a hacer **exactamente lo mismo** pero con SQLAlchemy ORM. Preparen los trapos porque esto es lo que van a usar en el bootcamp.

<p align="center">
  <img src="https://www.sqlalchemy.org/img/sqla_logo.png" alt="Logo de SQLAlchemy" height="80">
</p>

### 4A — ¿Qué es SQLAlchemy?

SQLAlchemy es un **ORM (Object-Relational Mapper)**. Significa que en lugar de escribir SQL manualmente, definimos **clases de Python** que representan las tablas, y SQLAlchemy se encarga de traducir nuestras operaciones de Python a SQL.

**Analogía:** psycopg2 es como hablar directamente con el arquitecto en su idioma (SQL). SQLAlchemy es como tener un traductor: vos le decís "quiero una casa de 3 ambientes" en español, y el traductor le dice al arquitecto en su idioma. Es más fácil para vos, y el resultado es el mismo.

**Comparación:**

| Operación | psycopg2 (SQL manual) | SQLAlchemy (ORM) |
|-----------|----------------------|------------------|
| Obtener todos | `SELECT * FROM artistas` | `Artista.query.all()` |
| Obtener uno | `SELECT * WHERE id = 1` | `Artista.query.get(1)` |
| Crear | `INSERT INTO artistas ...` | `db.session.add(artista)` |
| Actualizar | `UPDATE artistas SET ...` | `artista.nombre = "nuevo"` |
| Eliminar | `DELETE FROM artistas WHERE id = 1` | `db.session.delete(artista)` |

---

### 4B — Demo: Configurar SQLAlchemy en Flask

Reescribir `app.py` completamente:

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# =============================================================
# CONFIGURACIÓN
# =============================================================
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/musica_peruana"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# =============================================================
# MODELOS (las tablas de la BD)
# =============================================================
class Artista(db.Model):
    __tablename__ = "artistas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    pais_origen = db.Column(db.String(50), default="Perú")
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, server_default=db.func.now())

    # Relación 1:N - Un artista tiene muchas canciones
    canciones = db.relationship("Cancion", backref="artista", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "pais_origen": self.pais_origen,
            "activo": self.activo
        }


class Cancion(db.Model):
    __tablename__ = "canciones"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    album = db.Column(db.String(150))
    duracion_segundos = db.Column(db.Integer)
    anio_lanzamiento = db.Column(db.Integer)
    artista_id = db.Column(db.Integer, db.ForeignKey("artistas.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "album": self.album,
            "duracion_segundos": self.duracion_segundos,
            "anio_lanzamiento": self.anio_lanzamiento,
            "artista_id": self.artista_id
        }


# =============================================================
# RUTAS
# =============================================================
@app.route("/")
def home():
    return jsonify({"mensaje": "API de Música Peruana - SQLAlchemy"})


@app.route("/artistas", methods=["GET"])
def get_artistas():
    artistas = Artista.query.order_by(Artista.nombre).all()
    return jsonify([a.to_dict() for a in artistas])


@app.route("/artistas/<int:id>", methods=["GET"])
def get_artista(id):
    artista = Artista.query.get(id)
    if artista is None:
        return jsonify({"error": "Artista no encontrado"}), 404
    return jsonify(artista.to_dict())


@app.route("/canciones", methods=["GET"])
def get_canciones():
    canciones = Cancion.query.all()
    resultado = []
    for c in canciones:
        datos = c.to_dict()
        datos["artista"] = c.artista.nombre
        datos["genero"] = c.artista.genero
        resultado.append(datos)
    return jsonify(resultado)


@app.route("/artistas/<int:id>/canciones", methods=["GET"])
def get_canciones_artista(id):
    artista = Artista.query.get(id)
    if artista is None:
        return jsonify({"error": "Artista no encontrado"}), 404

    return jsonify({
        "artista": artista.nombre,
        "genero": artista.genero,
        "canciones": [c.to_dict() for c in artista.canciones]
    })


@app.route("/artistas", methods=["POST"])
def crear_artista():
    datos = request.json

    if not datos:
        return jsonify({"error": "Debes enviar datos en formato JSON"}), 400

    if "nombre" not in datos or not str(datos.get("nombre", "")).strip():
        return jsonify({"error": "Falta el campo: nombre"}), 400

    if "genero" not in datos or not str(datos.get("genero", "")).strip():
        return jsonify({"error": "Falta el campo: genero"}), 400

    nuevo_artista = Artista(
        nombre=datos["nombre"],
        genero=datos["genero"],
        pais_origen=datos.get("pais_origen", "Perú")
    )
    db.session.add(nuevo_artista)
    db.session.commit()

    return jsonify(nuevo_artista.to_dict()), 201


@app.route("/canciones", methods=["POST"])
def crear_cancion():
    datos = request.json

    if not datos:
        return jsonify({"error": "Debes enviar datos en formato JSON"}), 400

    if "titulo" not in datos or not str(datos.get("titulo", "")).strip():
        return jsonify({"error": "Falta el campo: titulo"}), 400

    if "artista_id" not in datos:
        return jsonify({"error": "Falta el campo: artista_id"}), 400

    artista = Artista.query.get(datos["artista_id"])
    if artista is None:
        return jsonify({"error": "Artista no encontrado"}), 404

    nueva_cancion = Cancion(
        titulo=datos["titulo"],
        album=datos.get("album"),
        duracion_segundos=datos.get("duracion_segundos"),
        anio_lanzamiento=datos.get("anio_lanzamiento"),
        artista_id=datos["artista_id"]
    )
    db.session.add(nueva_cancion)
    db.session.commit()

    return jsonify(nueva_cancion.to_dict()), 201


@app.route("/artistas/<int:id>", methods=["PUT"])
def actualizar_artista(id):
    artista = Artista.query.get(id)
    if artista is None:
        return jsonify({"error": "Artista no encontrado"}), 404

    datos = request.json
    artista.nombre = datos.get("nombre", artista.nombre)
    artista.genero = datos.get("genero", artista.genero)
    artista.pais_origen = datos.get("pais_origen", artista.pais_origen)
    artista.activo = datos.get("activo", artista.activo)

    db.session.commit()
    return jsonify(artista.to_dict())


@app.route("/artistas/<int:id>", methods=["DELETE"])
def eliminar_artista(id):
    artista = Artista.query.get(id)
    if artista is None:
        return jsonify({"error": "Artista no encontrado"}), 404

    db.session.delete(artista)
    db.session.commit()

    return jsonify({"mensaje": f"Artista '{artista.nombre}' eliminado"})


if __name__ == "__main__":
    app.run(debug=True)
```

**Explicación de los modelos:**

| Parte | Significado |
|-------|-------------|
| `class Artista(db.Model)` | Define una tabla llamada "artistas" |
| `__tablename__ = "artistas"` | Nombre de la tabla en la BD |
| `id = db.Column(db.Integer, primary_key=True)` | Columna id, entero, primary key |
| `nombre = db.Column(db.String(150), nullable=False)` | Columna nombre, texto de hasta 150 chars, obligatorio |
| `canciones = db.relationship(...)` | Relación 1:N con la tabla Cancion |
| `def to_dict(self)` | Método para convertir el objeto a diccionario |

**Probá en Postman:** todos los endpoints deben funcionar igual que antes.

---

### 4C — Demo: Comparación lado a lado

| Operación | psycopg2 (SQL manual) | SQLAlchemy (ORM) |
|-----------|----------------------|------------------|
| Conexión | `conn = psycopg2.connect(...)` | Automática con `db.session` |
| Obtener todos | `cur.execute("SELECT * FROM artistas")` | `Artista.query.all()` |
| Obtener uno | `cur.execute("SELECT * WHERE id = %s", (id,))` | `Artista.query.get(id)` |
| Crear | `cur.execute("INSERT INTO artistas ...")` | `db.session.add(artista)` |
| Actualizar | `cur.execute("UPDATE artistas SET ...")` | `artista.nombre = "nuevo"` |
| Eliminar | `cur.execute("DELETE FROM artistas WHERE id = %s", (id,))` | `db.session.delete(artista)` |
| Guardar | `conn.commit()` | `db.session.commit()` |
| Resultados | Tuplas o diccionarios (`RealDictCursor`) | Objetos de Python |

**¿Cuál usar?**

| Situación | Recomendación |
|-----------|---------------|
| **Bootcamp / Proyectos** | SQLAlchemy (más fácil, más seguro) |
| **Optimización extrema** | psycopg2 (más rápido) |
| **Queries complejas** | psycopg2 o `db.session.execute()` |
| **Desarrollo rápido** | SQLAlchemy |

**En el bootcamp usaremos SQLAlchemy** porque:
1. Es el estándar de la industria
2. Protege contra SQL injection automáticamente
3. El código es más legible y mantenible
4. Funciona con cualquier base de datos (PostgreSQL, MySQL, SQLite)

---

### 4D — Reto: Convertí un endpoint de psycopg2 a SQLAlchemy

**Profe dice:** "Tomá el endpoint `GET /artistas/genero/<genero>` que hicimos con psycopg2 y reescribalo con SQLAlchemy."

<details>
<summary><b>Solución (reto)</b></summary>

```python
@app.route("/artistas/genero/<genero>", methods=["GET"])
def get_artistas_por_genero(genero):
    """Obtener artistas por género con SQLAlchemy."""
    artistas = Artista.query.filter(
        db.func.lower(Artista.genero) == db.func.lower(genero)
    ).order_by(Artista.nombre).all()

    if not artistas:
        return jsonify({"mensaje": "No hay artistas de ese género"}), 200

    return jsonify([a.to_dict() for a in artistas])
```

**¿Qué cambió?**
- En vez de `cur.execute("SELECT * FROM artistas WHERE LOWER(genero) = LOWER(%s)", (genero,))`
- Usamos `Artista.query.filter(db.func.lower(Artista.genero) == db.func.lower(genero))`
- No necesitamos abrir/cerrar conexión manualmente
- No necesitamos `RealDictCursor` porque ya tenemos objetos Python

</details>

---

## 5. Ejercicios (15 min)

Ahora es su turno. Practiquen con estos ejercicios:

### Ejercicio 1: Agregar artistas de Cumbia Peruana

Crear los siguientes artistas usando POST `/artistas`:

1. **Pachuco y la Cubanacán** (Cumbia, Perú)
2. **Corazón Serrano** (Cumbia, Perú)
3. **Hermelinda Fuentes** (Cumbia, Perú)

### Ejercicio 2: Agregar canciones

Crear al menos 2 canciones para cada nuevo artista usando POST `/canciones`.

### Ejercicio 3: Endpoint de estadísticas

Crear el endpoint `GET /estadisticas` que devuelva:
- Total de artistas
- Total de canciones
- Artistas por género
- Artista con más canciones

<details>
<summary><b>Solución Ejercicio 1</b></summary>

```bash
# Pachuco y la Cubanacán
POST /artistas
{
    "nombre": "Pachuco y la Cubanacán",
    "genero": "Cumbia",
    "pais_origen": "Perú"
}

# Corazón Serrano
POST /artistas
{
    "nombre": "Corazón Serrano",
    "genero": "Cumbia",
    "pais_origen": "Perú"
}

# Hermelinda Fuentes
POST /artistas
{
    "nombre": "Hermelinda Fuentes",
    "genero": "Cumbia",
    "pais_origen": "Perú"
}
```

</details>

<details>
<summary><b>Solución Ejercicio 3</b></summary>

```python
@app.route("/estadisticas", methods=["GET"])
def get_estadisticas():
    """Obtener estadísticas de la API."""
    # Total de artistas
    total_artistas = Artista.query.count()

    # Total de canciones
    total_canciones = Cancion.query.count()

    # Artistas por género
    artistas_por_genero = db.session.query(
        Artista.genero,
        db.func.count(Artista.id)
    ).group_by(Artista.genero).all()

    # Artista con más canciones
    artista_top = db.session.query(
        Artista.nombre,
        db.func.count(Cancion.id)
    ).join(Cancion).group_by(Artista.nombre).order_by(
        db.func.count(Cancion.id).desc()
    ).first()

    return jsonify({
        "total_artistas": total_artistas,
        "total_canciones": total_canciones,
        "artistas_por_genero": [{"genero": g, "cantidad": c} for g, c in artistas_por_genero],
        "artista_mas_canciones": {"nombre": artista_top[0], "canciones": artista_top[1]} if artista_top else None
    })
```

</details>

---

## 🎯 Resumen de conceptos

| Tema | Demo | Reto | Conceptos clave |
|------|:----:|:----:|-----------------|
| 0. Cliente-servidor | — | — | request, response, modelo de comunicación, base de datos |
| 1. Preparación del entorno | ✅ | ✅ | venv, pip, requirements.txt, estructura |
| 2. PostgreSQL schema | ✅ | ✅ | CREATE DATABASE, schema.sql, pgAdmin |
| 3. psycopg2 + Flask | ✅ | ✅ | Conexión manual, SQL, cursor, commit, CRUD |
| 4. SQLAlchemy ORM | ✅ | ✅ | Modelos, relaciones, session, queries |
| 5. Ejercicios | — | ✅ | CRUD completo, filtros, estadísticas |

---

## Diagrama de la base de datos

```
┌──────────────────────┐
│      artistas        │
├──────────────────────┤
│ id (PK)              │
│ nombre               │
│ genero               │
│ pais_origen          │
│ activo               │
│ fecha_creacion       │
└──────────┬───────────┘
           │
           │ 1:N
           │
┌──────────▼───────────┐
│      canciones       │
├──────────────────────┤
│ id (PK)              │
│ titulo               │
│ album                │
│ duracion_segundos    │
│ anio_lanzamiento     │
│ artista_id (FK)      │
└──────────────────────┘
```

---

## ¿Qué sigue?

Mañana veremos:
- **Flask-Restful** — para organizar mejor los endpoints
- **Relaciones más complejas** — entre múltiples tablas
- **CRUD completo** — con validaciones y manejo de errores

¡Nos vemos mañana! 🎵
