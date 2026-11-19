# 🧠 Guía — Día 1 (Semana 6): Flask-Migrate + SQLAlchemy 2.0 + Flask-RESTful

<p align="center">
  <img src="https://flask.palletsprojects.com/en/stable/_static/flask-logo.png" alt="Logo de Flask" height="80">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://www.sqlalchemy.org/img/sqla_logo.png" alt="Logo de SQLAlchemy" height="60">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Postgresql_elephant.svg?width=120" alt="Logo de PostgreSQL" height="100">
</p>

Hasta ahora, toda la API que construían vivía en un solo archivo `app.py` con decorators sueltos por todos lados. Cada endpoint era una función independiente, sin orden, sin estructura. Eso funciona para una API de 5 endpoints... pero ¿y cuando tienen 30? Hoy eso se acabó.

Vamos a aprender **Flask-Migrate** para manejar cambios en la base de datos sin perder nada, la **nueva sintaxis de SQLAlchemy 2.0** (la que usa la industria ahora), y **Flask-RESTful** para organizar nuestros endpoints como profesionales.

El viaje de hoy: van a crear una API completa de un **Restaurante** con 3 tablas (Clientes, Platos, Pedidos). Al final del día, van a poder decir "yo sé organizar una API como se hace en el mundo real".

---

## 0. ¿Por qué Flask-RESTful? — el problema con decorators sueltos (15 min)

Hasta ahora, cuando querían crear endpoints para "artistas", hacían esto:

```python
@app.route("/artistas", methods=["GET"])
def get_artistas():
    # ... 20 lineas de logica
    return jsonify(resultado)

@app.route("/artistas/<int:id>", methods=["GET"])
def get_artista(id):
    # ... 15 lineas de logica
    return jsonify(artista)

@app.route("/artistas", methods=["POST"])
def crear_artista():
    # ... 25 lineas de validacion + insercion
    return jsonify(nuevo), 201

@app.route("/artistas/<int:id>", methods=["PUT"])
def actualizar_artista(id):
    # ... 20 lineas
    return jsonify(act)

@app.route("/artistas/<int:id>", methods=["DELETE"])
def eliminar_artista(id):
    # ... 15 lineas
    return jsonify(msg), 200
```

**Analogía:** es como tener una cocina donde los platos están por todos lados. El lomo saltado está en la estufa, el ceviche en el piso, la arroz con leche en la ventana. ¿Funciona? Sí. ¿Es organizado? Para nada. Cuando el restaurante crece y tenés 30 platos, es un caos total.

**Los problemas con decorators sueltos:**

| Problema | ¿Por qué importa? |
|----------|-------------------|
| **Código disperso** | 5 funciones sueltas para una sola entidad. Tenés que buscar por todo el archivo |
| **Naming inconsistente** | ¿`get_artistas` o `obtener_artistas`? Cada uno nombra como quiere |
| **Sin agrupación** | ¿Qué endpoints son de artistas? No lo sabés a simple vista |
| **Difícil de mantener** | Si hay 20 endpoints, es un desastre finding the logica de cada uno |

### La solución: Flask-RESTful con Resources

```python
class ArtistaResource(Resource):
    def get(self, id):      # GET /artistas/1
        ...

    def put(self, id):      # PUT /artistas/1
        ...

    def delete(self, id):   # DELETE /artistas/1
        ...

class ArtistaListResource(Resource):
    def get(self):          # GET /artistas
        ...

    def post(self):         # POST /artistas
        ...
```

**Analogía:** ahora la cocina está organizada. Todo lo que es "entradas" está en una estación, todo lo de "platos fuertes" en otra, y todo lo de "postres" en otra. Cada estación tiene sus herramientas y su orden. Cuando crece el restaurante, solo agregás una estación nueva sin desorganizar las que ya existen.

**¿Qué ganamos con Flask-RESTful?**

| Ventaja | ¿Qué significa en la práctica? |
|---------|-------------------------------|
| **Agrupación lógica** | Todo lo de clientes está EN UNA CLASE |
| **Naming automático** | `get()`, `post()`, `put()`, `delete()` — no hay que pensar nombres |
| **Estándar industrial** | Así trabajan todos los proyectos reales de Python |
| **Fácil de escalar** | Agregar un endpoint es agregar un método a la clase |

**¿Y cuándo usar decorators sueltos?** Para APIs muy pequeñas (2-3 endpoints) o para rutas puntuales que no encajan en una entidad. Pero cuando tu API crece, Flask-RESTful es la forma profesional de hacerlo.

---

## 1. Setup del proyecto (10 min)

### 1A — Demo: Crear entorno virtual e instalar dependencias

Abran una terminal en la carpeta donde quieran crear su proyecto:

```bash
mkdir restaurante_api
cd restaurante_api
python -m venv venv
venv\Scripts\activate
```

Esto crea una carpeta `venv/` con una copia aislada de Python. Como vimos en la semana 5, es como ponerse una casaca que dice "todo lo que instale ahora es solo para este proyecto".

Ahora instalamos las dependencias:

```bash
pip install flask flask-restful flask-sqlalchemy flask-migrate psycopg2-binary
```

**¿Qué instalamos?**

| Paquete | ¿Para qué? |
|---------|------------|
| `flask` | El microframework para crear APIs web |
| `flask-restful` | Organizar endpoints en clases Resource |
| `flask-sqlalchemy` | Integrar SQLAlchemy con Flask |
| `flask-migrate` | Manejar cambios en la BD sin perder datos |
| `psycopg2-binary` | Driver para conectarse a PostgreSQL |

Crear el archivo `requirements.txt`:

```
flask
flask-restful
flask-sqlalchemy
flask-migrate
psycopg2-binary
```

**Probá en terminal:**

```bash
pip install -r requirements.txt
```

Si no da error, todo está perfecto.

---

### 1B — Reto: Verificar la instalación

**Profe dice:** "Antes de seguir, verifiquen que todo quedó bien."

1. Ejecuten `pip list` en la terminal
2. Verifiquen que aparezcan: `Flask`, `flask-restful`, `flask-sqlalchemy`, `flask-migrate`, `psycopg2-binary`
3. Respondan: ¿cuál es la versión de Flask que instalaron?

<details>
<summary><b>Solución (reto)</b></summary>

```bash
pip list
```

Deberían ver algo como:

```
Flask                   3.1.1
flask-migrate           4.1.0
flask-restful           0.3.10
flask-sqlalchemy        3.1.1
psycopg2-binary         2.9.10
```

La versión de Flask puede variar, pero debe ser 3.x. Si no aparece alguno, reinstalen con `pip install` el paquete faltante.

</details>

---

## 2. SQLAlchemy 2.0 — La nueva sintaxis (25 min)

### El problema con la sintaxis vieja

En la semana 5 aprendieron a definir modelos así:

```python
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Artista(db.Model):
    __tablename__ = "artistas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
```

¿Funciona? Sí. Pero tiene problemas:

**Analogía:** es como escribir una receta donde dice "ingrediente 1: ingrediente 2: ingrediente 3". No sabés qué es cada ingrediente hasta que lees la receta completa. La sintaxis nueva es como escribir "harina: 2 tazas, azúcar: 1 taza, huevos: 3 unidades". SABÉS qué es cada cosa solo con mirar.

| Problema | Ejemplo |
|----------|---------|
| **Sin type hints** | Tu IDE no sabe que `id` es un `int` |
| **Ambigüedad** | `Column()` parece una función de Python pero es una columna de BD |
| **Errores tardíos** | Si ponés `Column(Integer)` pero debería ser `String`, lo descubrís recién al ejecutar |

### La solución: SQLAlchemy 2.0 con Mapped[]

La nueva sintaxis usa **type hints** de Python (lo estándar desde 2021):

```python
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, ForeignKey

class Artista(db.Model):
    __tablename__ = "artistas"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(150))
```

### Comparación lado a lado

| Concepto | Vieja (Column) | Nueva (Mapped) |
|----------|----------------|----------------|
| PK | `id = Column(Integer, primary_key=True)` | `id: Mapped[int] = mapped_column(primary_key=True)` |
| String | `nombre = Column(String(100))` | `nombre: Mapped[str] = mapped_column(String(100))` |
| Nullable | `Column(String, nullable=True)` | `nombre: Mapped[str \| None]` |
| FK | `cat_id = Column(Integer, ForeignKey('cats.id'))` | `cat_id: Mapped[int] = mapped_column(ForeignKey('cats.id'))` |
| Default | `Column(Boolean, default=True)` | `activo: Mapped[bool] = mapped_column(default=True)` |

### ¿Qué ganamos con la nueva sintaxis?

| Ganancia | ¿Por qué importa? |
|----------|-------------------|
| **Type hints** | Tu IDE sabe que tipo es cada campo. Si escribís `precio: Mapped[str]` en vez de `Mapped[float]`, te avisa al instante |
| **Legibilidad** | `Mapped[str]` es más claro que `Column(String)` |
| **Seguridad** | Python te avisa si te equivocás de tipo ANTES de ejecutar |
| **Estándar** | Es lo que usa la industria desde 2021. Si buscás trabajo, esto es lo que vas a ver en los proyectos reales |

### 2A — Demo: Configurar db.py

Crear el archivo `db.py`:

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

**Desglose línea por línea:**

| Línea | Significado |
|-------|-------------|
| `from flask_sqlalchemy import SQLAlchemy` | Importamos la herramienta de Flask para conectarse a BD |
| `db = SQLAlchemy()` | Creamos la instancia de SQLAlchemy que vamos a usar en todos los modelos |

Es igual a lo que ya conocemos — solo necesitamos `db = SQLAlchemy()` y listo.

---

### 2B — Reto: Identificar las diferencias

**Profe dice:** "Les muestro dos versiones del mismo modelo. Ustedes me dicen qué cambió y por qué es mejor."

Versión vieja:
```python
class Cliente(db.Model):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(20))
```

Versión nueva:
```python
class Cliente(db.Model):
    __tablename__ = "clientes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    telefono: Mapped[str] = mapped_column(String(20))
```

Respondan:
1. ¿Qué le falta a la versión nueva que sí tiene la vieja? (`nullable=False`)
2. ¿Dónde se especifica que `nombre` es obligatorio en la versión nueva?
3. ¿Qué tipo de dato es `telefono` en ambas versiones?

<details>
<summary><b>Solución (reto)</b></summary>

1. La versión nueva **no tiene `nullable=False`** en `nombre`. En la sintaxis nueva, si escribís `Mapped[str]` (sin `| None`), SQLAlchemy asume que es obligatorio automáticamente. No necesita `nullable=False`.

2. En la versión nueva, `nombre: Mapped[str]` significa que es un string **obligatorio**. Si fuera opcional, escribiríamos `Mapped[str | None]`.

3. `telefono` es un `String(20)` en ambas versiones. La diferencia es que en la nueva sabemos que es un string solo con mirar `Mapped[str]`.

</details>

---

## 3. Los 3 modelos (25 min)

Nuestra API de Restaurante tiene 3 tablas con relaciones 1:N:

```
┌──────────────────┐       ┌──────────────────┐
│    clientes      │       │     platos       │
├──────────────────┤       ├──────────────────┤
│ id_cliente (PK)  │       │ id_plato (PK)    │
│ nombre           │       │ nombre           │
│ telefono         │       │ categoria        │
│ direccion        │       │ precio           │
└────────┬─────────┘       └────────┬─────────┘
         │                          │
         │    ┌──────────────────┐  │
         └───►│     pedidos      │◄─┘
              ├──────────────────┤
              │ id_pedido (PK)   │
              │ id_cliente (FK)  │
              │ id_plato (FK)    │
              │ cantidad         │
              │ fecha            │
              │ total            │
              └──────────────────┘
```

**Relaciones:**
- Un **cliente** puede tener **muchos pedidos** (1:N)
- Un **plato** puede estar en **muchos pedidos** (1:N)
- Cada **pedido** tiene **un cliente** y **un plato**

### 3A — Demo: Modelo Cliente

Crear la carpeta `models/` y el archivo `models/cliente.py`:

```python
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from db import db


class Cliente(db.Model):
    __tablename__ = "clientes"

    id_cliente: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    telefono: Mapped[str] = mapped_column(String(20))
    direccion: Mapped[str] = mapped_column(String(200))

    # Relacion 1:N — Un cliente tiene muchos pedidos
    pedidos = relationship('Pedido')

    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion
        }
```

**Desglose línea por línea:**

| Línea | Significado |
|-------|-------------|
| `from sqlalchemy.orm import Mapped, mapped_column` | Importamos las herramientas de la sintaxis nueva |
| `from db import db` | Importamos nuestra instancia de SQLAlchemy |
| `class Cliente(db.Model)` | Esta clase es una tabla en la BD |
| `__tablename__ = "clientes"` | Nombre de la tabla en PostgreSQL |
| `id_cliente: Mapped[int]` | Columna entera, obligatoria |
| `mapped_column(primary_key=True)` | Es la llave primaria |
| `nombre: Mapped[str]` | Columna de texto, obligatoria |
| `String(100)` | Máximo 100 caracteres |
| `pedidos = relationship('Pedido')` | Relación 1:N — un cliente tiene muchos pedidos |
| `def to_dict(self)` | Convierte el objeto a diccionario para devolverlo como JSON |

**¿Por qué `to_dict()`?** Porque Flask no puede convertir un objeto de Python a JSON directamente. Necesitamos un diccionario. `to_dict()` hace esa conversión.

---

### 3B — Demo: Modelo Plato

Crear `models/plato.py`:

```python
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Float
from db import db


class Plato(db.Model):
    __tablename__ = "platos"

    id_plato: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    categoria: Mapped[str] = mapped_column(String(50))
    precio: Mapped[float] = mapped_column(Float)

    # Relacion 1:N — Un plato tiene muchos pedidos
    pedidos = relationship('Pedido')

    def to_dict(self):
        return {
            "id_plato": self.id_plato,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }
```

**¿Qué cambia respecto al Cliente?**
- `precio: Mapped[float] = mapped_column(Float)` — usa `Float` en vez de `String` porque es un número decimal
- `categoria: Mapped[str]` — texto para guardar "Platos Fuertes", "Entradas", "Bebidas", "Postres"
- La relación `pedidos` apunta a la misma tabla que en Cliente

---

### 3C — Demo: Modelo Pedido

Crear `models/pedido.py`:

```python
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Float, Integer, DateTime, ForeignKey
from datetime import datetime
from db import db


class Pedido(db.Model):
    __tablename__ = "pedidos"

    id_pedido: Mapped[int] = mapped_column(primary_key=True)
    id_cliente: Mapped[int] = mapped_column(ForeignKey("clientes.id_cliente"))
    id_plato: Mapped[int] = mapped_column(ForeignKey("platos.id_plato"))
    cantidad: Mapped[int] = mapped_column(Integer)
    fecha: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    total: Mapped[float] = mapped_column(Float)

    # Relaciones N:1
    cliente = relationship('Cliente')
    plato = relationship('Plato')

    def to_dict(self):
        return {
            "id_pedido": self.id_pedido,
            "id_cliente": self.id_cliente,
            "id_plato": self.id_plato,
            "cantidad": self.cantidad,
            "fecha": str(self.fecha),
            "total": self.total,
            "cliente": self.cliente.nombre if self.cliente else None,
            "plato": self.plato.nombre if self.plato else None
        }
```

**Desglose de lasForeign Keys:**

| Línea | Significado |
|-------|-------------|
| `id_cliente: Mapped[int] = mapped_column(ForeignKey("clientes.id_cliente"))` | FK a la tabla clientes |
| `id_plato: Mapped[int] = mapped_column(ForeignKey("platos.id_plato"))` | FK a la tabla platos |
| `cliente = relationship('Cliente')` | Relación inversa — accedemos al objeto Cliente |
| `plato = relationship('Plato')` | Relación inversa — accedemos al objeto Plato |

**¿Por qué en `to_dict()` ponemos `self.cliente.nombre`?** Porque gracias a la relación, podemos acceder al objeto `Cliente` directamente desde el `Pedido`. No necesitamos hacer una consulta separada.

---

### models/__init__.py

Crear `models/__init__.py` para importar todos los modelos:

```python
from models.cliente import Cliente
from models.plato import Plato
from models.pedido import Pedido
```

**¿Para qué sirve este archivo?** Para que cuando hagamos `from models import Cliente`, Python sepa dónde buscarlo. Sin este archivo, tendríamos que hacer `from models.cliente import Cliente` cada vez.

---

## 4. Flask-Migrate — Crear y aplicar migraciones (30 min)

### ¿Qué es y por qué?

**Problema:** sin migraciones, cada cambio de modelo requiere:
1. Borrar la BD manualmente
2. Volver a crear todo
3. **Perder todos los datos**

**Analogía:** imaginen que están construyendo una casa. Sin migraciones, cada vez que quieren agregar una pared, tienen que demoler la casa y reconstruirla desde cero. Con migraciones, tienen un **plano que se actualiza** — el arquitecto anota "agregar pared en el cuarto 3", y ustedes ejecutan ese plano sin demoler nada.

**Solución:** Flask-Migrate (Alembic por debajo) genera scripts de migración:
- Detecta cambios en los modelos
- Crea archivos de migración versionados
- Aplica los cambios **sin perder datos**

**Flujo:**

```
Modelos (Python) --> flask db migrate --> Archivos SQL --> flask db upgrade --> BD actualizada
```

### 4A — Demo: Configurar y crear migración

Primero, crear la base de datos en pgAdmin:
1. Click derecho en **Databases** → **Create** → **Database...**
2. Nombre: `restaurante`
3. Owner: `postgres`

Ahora, crear `app.py` con la configuración inicial:

```python
from flask import Flask
from db import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/restaurante"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# Importar modelos para que Migrate los detecte
from models.cliente import Cliente
from models.plato import Plato
from models.pedido import Pedido

if __name__ == "__main__":
    app.run(debug=True)
```

**Desglose:**

| Línea | Significado |
|-------|-------------|
| `from flask_migrate import Migrate` | Importamos la herramienta de migraciones |
| `migrate = Migrate(app, db)` | Conectamos Flask-Migrate con nuestra app y nuestra BD |
| `from models.cliente import Cliente` | Importamos los modelos para que Migrate los detecte |

Ahora, ejecutar en terminal (asegurarse de estar en la carpeta del proyecto):

```bash
# 1. Crear la carpeta migrations/
flask db init

# 2. Generar la migracion (detecta los modelos)
flask db migrate -m "Crear tablas clientes, platos, pedidos"

# 3. Aplicar a la BD
flask db upgrade
```

**¿Qué hace cada comando?**

| Comando | ¿Qué hace? |
|---------|-----------|
| `flask db init` | Crea la carpeta `migrations/` con la configuración de Alembic |
| `flask db migrate -m "mensaje"` | Analiza los modelos y genera un archivo de migración |
| `flask db upgrade` | Ejecuta la migración en la BD — crea las tablas |

---

### 4B — Reto: Verificar en pgAdmin

**Profe dice:** "Después de ejecutar los 3 comandos, verifiquen que las tablas se crearon."

1. Abran pgAdmin y seleccionen la BD `restaurante`
2. Expandan **Schemas** → **public** → **Tables**
3. Deberían ver 3 tablas: `clientes`, `platos`, `pedidos`
4. También deberían ver `alembic_version` (es la tabla de control de migraciones)

Ejecuten esto en la Query Tool:

```sql
SELECT table_name FROM information_schema.tables 
WHERE table_schema = 'public';
```

<details>
<summary><b>Solución (reto)</b></summary>

El resultado debería ser:

```
table_name
----------------
alembic_version
clientes
platos
pedidos
```

Si `alembic_version` no aparece, significa que `flask db upgrade` no se ejecutó bien. Vuelvan a ejecutarlo.

Si alguna tabla falta, revisen que los modelos estén bien definidos y que `app.py` los importe.

</details>

---

## 5. Flask-RESTful — Resources (70 min)

### 5A — Demo: Resource de Clientes

Crear la carpeta `resources/` y el archivo `resources/cliente_resource.py`:

```python
from flask_restful import Resource
from flask import request
from db import db
from models.cliente import Cliente


class ClienteListResource(Resource):

    def get(self):
        clientes = Cliente.query.all()

        resultado = []
        for c in clientes:
            resultado.append(c.to_dict())

        return resultado

    def post(self):
        data = request.get_json()

        if not data:
            return {"msg": "Debes enviar datos"}, 400

        if "nombre" not in data or not data["nombre"].strip():
            return {"msg": "Falta el campo nombre"}, 400

        nuevo = Cliente(
            nombre=data["nombre"],
            telefono=data.get("telefono", ""),
            direccion=data.get("direccion", "")
        )

        db.session.add(nuevo)
        db.session.commit()

        return nuevo.to_dict(), 201


class ClienteResource(Resource):

    def get(self, id_cliente):
        cliente = Cliente.query.get(id_cliente)

        if not cliente:
            return {"msg": "Cliente no encontrado"}, 404

        return cliente.to_dict()

    def put(self, id_cliente):
        cliente = Cliente.query.get(id_cliente)

        if not cliente:
            return {"msg": "Cliente no encontrado"}, 404

        data = request.get_json()
        cliente.nombre = data.get("nombre", cliente.nombre)
        cliente.telefono = data.get("telefono", cliente.telefono)
        cliente.direccion = data.get("direccion", cliente.direccion)

        db.session.commit()
        return cliente.to_dict()

    def delete(self, id_cliente):
        cliente = Cliente.query.get(id_cliente)

        if not cliente:
            return {"msg": "Cliente no encontrado"}, 404

        nombre = cliente.nombre
        db.session.delete(cliente)
        db.session.commit()

        return {"msg": f"Cliente '{nombre}' eliminado"}
```

**¿Qué clase hace qué?**

| Clase | Endpoints | ¿Qué hace? |
|-------|-----------|-----------|
| `ClienteListResource` | GET /clientes, POST /clientes | Lista todos o crea uno nuevo |
| `ClienteResource` | GET /clientes/1, PUT /clientes/1, DELETE /clientes/1 | Obtiene, actualiza o elimina uno específico |

**Desglose de `ClienteListResource.get()`:**

| Línea | Significado |
|-------|-------------|
| `clientes = Cliente.query.all()` | Trae todos los clientes de la BD |
| `resultado = []` | Creo una lista vacía |
| `for c in clientes:` | Recorro cada cliente |
| `resultado.append(c.to_dict())` | Convierto a diccionario y agrego a la lista |
| `return resultado` | Devuelvo la lista completa |

**¿Por qué no usamos list comprehension?** Porque en este curso usamos `for` tradicional para que se vea cada paso. En la industria sí se usa list comprehension, pero acá queremos que se vea claro qué pasa.

---

### Registro en app.py

Agregar al final de `app.py` (antes del `if __name__`):

```python
from flask_restful import Api
from resources.cliente_resource import ClienteListResource, ClienteResource

api = Api(app)
api.add_resource(ClienteListResource, "/clientes")
api.add_resource(ClienteResource, "/clientes/<int:id_cliente>")
```

**Desglose:**

| Línea | Significado |
|-------|-------------|
| `from flask_restful import Api` | Importamos la clase Api |
| `api = Api(app)` | Creamos la instancia de la API |
| `api.add_resource(ClienteListResource, "/clientes")` | Conectamos la clase con la URL |
| `"<int:id_cliente>"` | Flask captura el número de la URL y lo pasa como parámetro |

---

### Prueba en Postman

Ahora probemos que funcione. Ejecuten `python app.py` en la terminal.

**Crear un cliente (POST):**
- Método: POST
- URL: `http://127.0.0.1:5000/clientes`
- Body → raw → JSON:
```json
{
    "nombre": "Juan Perez",
    "telefono": "999999",
    "direccion": "Av. Lima 123"
}
```
- Send → Deberían ver el cliente creado con código 201

**Obtener todos (GET):**
- Método: GET
- URL: `http://127.0.0.1:5000/clientes`
- Send → Deberían ver una lista con el cliente creado

**Obtener uno (GET):**
- Método: GET
- URL: `http://127.0.0.1:5000/clientes/1`
- Send → Deberían ver solo Juan Perez

**Actualizar (PUT):**
- Método: PUT
- URL: `http://127.0.0.1:5000/clientes/1`
- Body → raw → JSON:
```json
{
    "nombre": "Juan Carlos Perez"
}
```
- Send → Deberían ver el nombre actualizado

**Eliminar (DELETE):**
- Método: DELETE
- URL: `http://127.0.0.1:5000/clientes/1`
- Send → Deberían ver mensaje de confirmación

---

### 5B — Reto: Resource de Platos

**Profe dice:** "Ahora creen el Resource de Platos siguiendo el mismo patrón de Clientes. Recuerden: un plato tiene nombre, categoría y precio."

Crear `resources/plato_resource.py`:

<details>
<summary><b>Solución (reto)</b></summary>

```python
from flask_restful import Resource
from flask import request
from db import db
from models.plato import Plato


class PlatoListResource(Resource):

    def get(self):
        platos = Plato.query.all()

        resultado = []
        for p in platos:
            resultado.append(p.to_dict())

        return resultado

    def post(self):
        data = request.get_json()

        if not data:
            return {"msg": "Debes enviar datos"}, 400

        if "nombre" not in data or not data["nombre"].strip():
            return {"msg": "Falta el campo nombre"}, 400

        if "precio" not in data or data["precio"] <= 0:
            return {"msg": "El precio debe ser mayor a 0"}, 400

        nuevo = Plato(
            nombre=data["nombre"],
            categoria=data.get("categoria", "General"),
            precio=data["precio"]
        )

        db.session.add(nuevo)
        db.session.commit()

        return nuevo.to_dict(), 201


class PlatoResource(Resource):

    def get(self, id_plato):
        plato = Plato.query.get(id_plato)

        if not plato:
            return {"msg": "Plato no encontrado"}, 404

        return plato.to_dict()

    def put(self, id_plato):
        plato = Plato.query.get(id_plato)

        if not plato:
            return {"msg": "Plato no encontrado"}, 404

        data = request.get_json()
        plato.nombre = data.get("nombre", plato.nombre)
        plato.categoria = data.get("categoria", plato.categoria)
        plato.precio = data.get("precio", plato.precio)

        db.session.commit()
        return plato.to_dict()

    def delete(self, id_plato):
        plato = Plato.query.get(id_plato)

        if not plato:
            return {"msg": "Plato no encontrado"}, 404

        nombre = plato.nombre
        db.session.delete(plato)
        db.session.commit()

        return {"msg": f"Plato '{nombre}' eliminado"}
```

**Registro en app.py:**
```python
from resources.plato_resource import PlatoListResource, PlatoResource

api.add_resource(PlatoListResource, "/platos")
api.add_resource(PlatoResource, "/platos/<int:id_plato>")
```

**¿Qué cambia respecto a Clientes?**
- Validación adicional: `if "precio" not in data or data["precio"] <= 0` — el precio debe ser positivo
- `categoria=data.get("categoria", "General")` — si no mandan categoría, usa "General" por defecto

</details>

---

### 5C — Demo: Resource de Pedidos

Crear `resources/pedido_resource.py`:

```python
from flask_restful import Resource
from flask import request
from db import db
from models.pedido import Pedido
from models.cliente import Cliente
from models.plato import Plato
from datetime import datetime


class PedidoListResource(Resource):

    def get(self):
        pedidos = Pedido.query.all()

        resultado = []
        for p in pedidos:
            resultado.append(p.to_dict())

        return resultado

    def post(self):
        data = request.get_json()

        if not data:
            return {"msg": "Debes enviar datos"}, 400

        # Validar que exista el cliente
        cliente = Cliente.query.get(data.get("id_cliente"))
        if not cliente:
            return {"msg": "Cliente no encontrado"}, 404

        # Validar que exista el plato
        plato = Plato.query.get(data.get("id_plato"))
        if not plato:
            return {"msg": "Plato no encontrado"}, 404

        cantidad = data.get("cantidad", 1)
        total = plato.precio * cantidad

        nuevo = Pedido(
            id_cliente=data["id_cliente"],
            id_plato=data["id_plato"],
            cantidad=cantidad,
            fecha=datetime.now(),
            total=total
        )

        db.session.add(nuevo)
        db.session.commit()

        return nuevo.to_dict(), 201


class PedidoResource(Resource):

    def get(self, id_pedido):
        pedido = Pedido.query.get(id_pedido)

        if not pedido:
            return {"msg": "Pedido no encontrado"}, 404

        return pedido.to_dict()

    def delete(self, id_pedido):
        pedido = Pedido.query.get(id_pedido)

        if not pedido:
            return {"msg": "Pedido no encontrado"}, 404

        db.session.delete(pedido)
        db.session.commit()

        return {"msg": "Pedido eliminado"}
```

**¿Qué tiene de diferente este Resource?**

| Diferencia | ¿Por qué? |
|-----------|-----------|
| Valida que el cliente exista | No puedes crear un pedido para un cliente que no existe |
| Valida que el plato exista | No puedes pedir un plato que no está en el menú |
| Calcula el total automáticamente | `total = plato.precio * cantidad` — no lo calcula el usuario |
| Usa `datetime.now()` | La fecha se asigna automáticamente al momento de crear el pedido |

**Registro en app.py:**

```python
from resources.pedido_resource import PedidoListResource, PedidoResource

api.add_resource(PedidoListResource, "/pedidos")
api.add_resource(PedidoResource, "/pedidos/<int:id_pedido>")
```

---

### Prueba en Postman

**Crear un pedido (POST):**
- Método: POST
- URL: `http://127.0.0.1:5000/pedidos`
- Body → raw → JSON:
```json
{
    "id_cliente": 1,
    "id_plato": 2,
    "cantidad": 3
}
```
- Send → Deberían ver el pedido con el total calculado automáticamente

**Obtener todos (GET):**
- Método: GET
- URL: `http://127.0.0.1:5000/pedidos`
- Send → Deberían ver los pedidos con el nombre del cliente y del plato (no los IDs)

---

## 6. Seed data y pruebas (15 min)

### Insertar datos de prueba

Ejecuten esto en la Query Tool de pgAdmin:

```sql
-- Clientes
INSERT INTO clientes (nombre, telefono, direccion) VALUES
    ('Juan Perez', '999111222', 'Av. Lima 123'),
    ('Maria Garcia', '988222333', 'Jr. Union 456'),
    ('Carlos Lopez', '977333444', 'Av. Arequipa 789');

-- Platos
INSERT INTO platos (nombre, categoria, precio) VALUES
    ('Lomo Saltado', 'Platos Fuertes', 25.00),
    ('Aji de Gallina', 'Platos Fuertes', 20.00),
    ('Ceviche', 'Entradas', 30.00),
    ('Inca Kola', 'Bebidas', 5.00),
    ('Arroz con Leche', 'Postres', 12.00);

-- Pedidos
INSERT INTO pedidos (id_cliente, id_plato, cantidad, fecha, total) VALUES
    (1, 1, 2, NOW(), 50.00),
    (1, 4, 3, NOW(), 15.00),
    (2, 3, 1, NOW(), 30.00),
    (3, 2, 1, NOW(), 20.00);
```

**¿Por qué usamos SQL directo en pgAdmin?** Porque es más rápido que crear cada registro por Postman. En la vida real, los datos de prueba se insertan con scripts SQL o con migraciones de seed data.

### Tabla de pruebas en Postman

| Método | URL | Body JSON |
|--------|-----|-----------|
| GET | `http://127.0.0.1:5000/clientes` | - |
| POST | `http://127.0.0.1:5000/clientes` | `{"nombre": "Ana", "telefono": "999888777", "direccion": "Av. Brasil 456"}` |
| GET | `http://127.0.0.1:5000/clientes/1` | - |
| PUT | `http://127.0.0.1:5000/clientes/1` | `{"nombre": "Juan Perez Modificado"}` |
| DELETE | `http://127.0.0.1:5000/clientes/1` | - |
| GET | `http://127.0.0.1:5000/platos` | - |
| POST | `http://127.0.0.1:5000/platos` | `{"nombre": "Tallarin Saltado", "categoria": "Platos Fuertes", "precio": 22.00}` |
| GET | `http://127.0.0.1:5000/pedidos` | - |
| POST | `http://127.0.0.1:5000/pedidos` | `{"id_cliente": 2, "id_plato": 1, "cantidad": 2}` |

---

## 7. Ejercicio integrador (15 min)

### Reto: Reporte de ventas

**Profe dice:** "El dueño del restaurante quiere saber cómo le va. Necesito un endpoint que le dé un resumen: cuántos pedidos tiene, cuánto ha ganado, quién es su mejor cliente, y cuál es el plato más popular."

Crear el endpoint `GET /reporte/ventas` que devuelva:
- Total de pedidos
- Total de ingresos
- Cliente que más gastó
- Plato más pedido

<details>
<summary><b>Solución (reto)</b></summary>

Agregar a `resources/pedido_resource.py`:

```python
from sqlalchemy import func


class ReporteResource(Resource):

    def get(self):
        # Total de pedidos
        total_pedidos = Pedido.query.count()

        # Total de ingresos
        total_ingresos = db.session.query(
            func.sum(Pedido.total)
        ).scalar()

        if total_ingresos is None:
            total_ingresos = 0

        # Cliente que mas gasto
        cliente_top = db.session.query(
            Cliente.nombre,
            func.sum(Pedido.total)
        ).join(Cliente).group_by(
            Cliente.nombre
        ).order_by(
            func.sum(Pedido.total).desc()
        ).first()

        # Plato mas pedido
        plato_top = db.session.query(
            Plato.nombre,
            func.sum(Pedido.cantidad)
        ).join(Plato).group_by(
            Plato.nombre
        ).order_by(
            func.sum(Pedido.cantidad).desc()
        ).first()

        resultado = {
            "total_pedidos": total_pedidos,
            "total_ingresos": float(total_ingresos)
        }

        if cliente_top:
            resultado["cliente_top"] = {
                "nombre": cliente_top[0],
                "total_gastado": float(cliente_top[1])
            }

        if plato_top:
            resultado["plato_top"] = {
                "nombre": plato_top[0],
                "total_vendido": int(plato_top[1])
            }

        return resultado
```

**Registro en app.py:**
```python
from resources.pedido_resource import ReporteResource
api.add_resource(ReporteResource, "/reporte/ventas")
```

**Prueba en Postman:**
- GET `http://127.0.0.1:5000/reporte/ventas`

**Resultado esperado:**
```json
{
    "total_pedidos": 4,
    "total_ingresos": 115.0,
    "cliente_top": {
        "nombre": "Juan Perez",
        "total_gastado": 65.0
    },
    "plato_top": {
        "nombre": "Inca Kola",
        "total_vendido": 3
    }
}
```

</details>

---

## app.py completo

```python
from flask import Flask
from db import db
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/restaurante"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# Importar modelos
from models.cliente import Cliente
from models.plato import Plato
from models.pedido import Pedido

# Importar resources
from resources.cliente_resource import ClienteListResource, ClienteResource
from resources.plato_resource import PlatoListResource, PlatoResource
from resources.pedido_resource import PedidoListResource, PedidoResource, ReporteResource

# Registrar rutas
api.add_resource(ClienteListResource, "/clientes")
api.add_resource(ClienteResource, "/clientes/<int:id_cliente>")

api.add_resource(PlatoListResource, "/platos")
api.add_resource(PlatoResource, "/platos/<int:id_plato>")

api.add_resource(PedidoListResource, "/pedidos")
api.add_resource(PedidoResource, "/pedidos/<int:id_pedido>")

api.add_resource(ReporteResource, "/reporte/ventas")

if __name__ == "__main__":
    app.run(debug=True)
```

---

## Resumen de conceptos

| Tema | Demo | Reto | Conceptos clave |
|------|:----:|:----:|-----------------|
| 0. ¿Por qué Flask-RESTful? | — | — | decorators sueltos vs Resources, agrupación lógica |
| 1. Setup del proyecto | ✅ | ✅ | venv, pip, requirements.txt |
| 2. SQLAlchemy 2.0 | ✅ | ✅ | Mapped[], mapped_column, type hints |
| 3. Los 3 modelos | ✅ | — | Relaciones 1:N, to_dict() |
| 4. Flask-Migrate | ✅ | ✅ | db init, migrate, upgrade, migrations |
| 5. Flask-RESTful Resources | ✅ | ✅ | Resource, add_resource, GET/POST/PUT/DELETE |
| 6. Seed data + pruebas | ✅ | — | SQL directo, Postman |
| 7. Ejercicio integrador | — | ✅ | func.sum, func.count, reporte |

---

## Estructura final del proyecto

```
restaurante_api/
├── app.py
├── db.py
├── requirements.txt
├── migrations/
├── models/
│   ├── __init__.py
│   ├── cliente.py
│   ├── plato.py
│   └── pedido.py
└── resources/
    ├── __init__.py
    ├── cliente_resource.py
    ├── plato_resource.py
    └── pedido_resource.py
```
