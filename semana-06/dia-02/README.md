# 🧠 Guía — Día 2 (Semana 6): Creando endpoints con Flask-RESTful

<p align="center">
  <img src="https://flask.palletsprojects.com/en/stable/_static/flask-logo.png" alt="Logo de Flask" height="80">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://www.sqlalchemy.org/img/sqla_logo.png" alt="Logo de SQLAlchemy" height="60">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Postman_%28software%29.png?width=240" alt="Logo de Postman" height="70">
</p>

La clase pasada dejamos lista la cocina: tenemos las tablas `clientes`, `platos` y `pedidos`, y Flask-Migrate las creó por nosotros. Pero un restaurante con cocina y sin mozos no atiende a nadie. Hoy vamos a contratar a los mozos: los **endpoints**.

Hoy casi no hay teoría. Es un día de **escribir endpoints**: cada sección tiene una demo que hacemos juntos y un reto que ustedes resuelven solos. Empezamos con un CRUD sencillo y terminamos con endpoints que filtran, calculan totales y arman reportes.

El viaje de hoy: van a terminar el día con una API de Restaurante con **más de 15 endpoints** funcionando y probados en Postman. Al final van a poder decir "dame cualquier tabla y le armo su API".

---

## 0. Anatomía de un endpoint (15 min)

Un endpoint es la combinación de un **método HTTP** y una **ruta**. `GET /clientes` y `POST /clientes` comparten la ruta, pero son **dos endpoints distintos**.

**Analogía:** el endpoint es el mozo. El cliente del restaurante (Postman, una app, el frontend) le dice qué quiere (método), sobre qué (ruta) y con qué detalles (parámetros y body). El mozo va a la cocina (la BD) y vuelve con el plato (la respuesta) y una cara (el código de estado): sonriente si todo salió bien, preocupada si no hay ese plato.

```
   PUT  http://127.0.0.1:5000/clientes/3?notificar=si
   ───  ─────────────────────  ─────── ─ ────────────
    │            │                │    │      │
 método      servidor           ruta   │   query params (filtros opcionales)
                                       │
                          parámetro de ruta (¿cuál registro?)

   Body (JSON): { "telefono": "987654321" }   ← los datos que enviamos
```

**Las 3 formas de mandarle información a un endpoint:**

| Forma | Ejemplo | ¿Cómo se lee en Flask? | ¿Para qué se usa? |
|-------|---------|------------------------|-------------------|
| **Parámetro de ruta** | `/clientes/3` | Argumento del método: `def get(self, id_cliente)` | Identificar UN registro |
| **Query params** | `/platos?categoria=Postres` | `request.args.get("categoria")` | Filtrar, buscar, ordenar |
| **Body JSON** | `{"nombre": "Ana"}` | `request.get_json()` | Enviar datos para crear o actualizar |

**Los códigos de estado que vamos a usar hoy:**

| Código | Nombre | ¿Cuándo lo devolvemos? |
|--------|--------|------------------------|
| `200` | OK | Todo salió bien (GET, PUT, DELETE) |
| `201` | Created | Creamos un registro nuevo (POST) |
| `400` | Bad Request | El cliente mandó datos incompletos o inválidos |
| `404` | Not Found | El registro que pidió no existe |
| `409` | Conflict | La operación choca con otros datos (ej: borrar un cliente que tiene pedidos) |
| `500` | Internal Server Error | Nuestro código falló. **Nunca** lo devolvemos a propósito: si aparece, es un bug |

**La regla de oro de hoy:** un endpoint **nunca** debe devolver `500` porque el usuario mandó datos raros. Si el usuario se equivoca, le respondemos `400` con un mensaje que explique qué corregir.

---

## 1. Puesta a punto: corregir los modelos y segunda migración (25 min)

Antes de crear endpoints vamos a corregir tres detalles de los modelos de la clase pasada. Además nos sirve para ver **para qué existe Flask-Migrate**: cambiar tablas que ya existen sin perder datos.

**Los 3 detalles a corregir:**

| Problema | ¿Por qué es un problema? |
|----------|--------------------------|
| `telefono: Mapped[str]` sin `\| None` | En SQLAlchemy 2.0, `Mapped[str]` significa **obligatorio** (NOT NULL). Nuestra migración creó `telefono` y `direccion` como obligatorios aunque queríamos que fueran opcionales |
| `fecha: Mapped[str]` con `DateTime` | El tipo de Python no coincide con el tipo de la columna. Debe ser `Mapped[datetime]` |
| No hay `relationship` ni `to_dict()` | Sin `relationship` no podemos ir de un pedido a su cliente. Sin `to_dict()` no podemos devolver JSON |

> ⚠️ **Si clonaron el repo antes de la última actualización:** la migración `fcdc6ba66301` fue reemplazada por `3a308f4fc292`. Si `flask db upgrade` les dice `Can't locate revision`, borren el archivo `instance/project.db` y vuelvan a ejecutar `flask db upgrade`.

### 1A — Demo: Instalar Flask-RESTful y actualizar los modelos

Con el entorno virtual activado:

```bash
pip install flask-restful
```

Y regeneramos el `requirements.txt` **en UTF-8** (si usan `>` en PowerShell, el archivo sale en UTF-16 y Git lo trata como binario):

```powershell
pip freeze | Out-File -Encoding utf8 requirements.txt
```

Aprovechamos para crear un `.gitignore` en la carpeta `api/`, así dejamos de subir archivos basura al repo:

```
venv/
__pycache__/
instance/
.claude/
```

Ahora sí, los modelos. Borren `models/demo.py` (era solo una prueba) y actualicen los otros tres:

**`models/clientes.py`**

```python
from db import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ClientesModel(db.Model):
    __tablename__ = "clientes"

    id_cliente: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    telefono: Mapped[str | None] = mapped_column(String(9))
    direccion: Mapped[str | None] = mapped_column(String(200))

    # Un cliente tiene muchos pedidos (1:N)
    pedidos: Mapped[list["PedidosModel"]] = relationship(back_populates="cliente")

    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion
        }
```

**`models/platos.py`**

```python
from db import db
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship


class PlatosModel(db.Model):
    __tablename__ = "platos"

    id_plato: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    categoria: Mapped[str] = mapped_column(String(50))
    precio: Mapped[float] = mapped_column(Float)

    # Un plato aparece en muchos pedidos (1:N)
    pedidos: Mapped[list["PedidosModel"]] = relationship(back_populates="plato")

    def to_dict(self):
        return {
            "id_plato": self.id_plato,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }
```

**`models/pedidos.py`**

```python
from datetime import datetime
from db import db
from sqlalchemy import Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class PedidosModel(db.Model):
    __tablename__ = "pedidos"

    id_pedido: Mapped[int] = mapped_column(Integer, primary_key=True)
    cantidad: Mapped[int] = mapped_column(Integer)
    fecha: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    total: Mapped[float] = mapped_column(Float)

    # Llaves foráneas
    id_cliente: Mapped[int] = mapped_column(ForeignKey("clientes.id_cliente"))
    id_plato: Mapped[int] = mapped_column(ForeignKey("platos.id_plato"))

    # Cada pedido pertenece a UN cliente y a UN plato (N:1)
    cliente: Mapped["ClientesModel"] = relationship(back_populates="pedidos")
    plato: Mapped["PlatosModel"] = relationship(back_populates="pedidos")

    def to_dict(self):
        return {
            "id_pedido": self.id_pedido,
            "id_cliente": self.id_cliente,
            "cliente": self.cliente.nombre,
            "id_plato": self.id_plato,
            "plato": self.plato.nombre,
            "cantidad": self.cantidad,
            "total": self.total,
            "fecha": self.fecha.isoformat()
        }
```

**`models/__init__.py`**

```python
from models.clientes import ClientesModel
from models.platos import PlatosModel
from models.pedidos import PedidosModel
```

**Desglose de lo nuevo:**

| Línea | Significado |
|-------|-------------|
| `Mapped[str \| None]` | La columna acepta `NULL`: el teléfono es opcional |
| `Mapped[list["PedidosModel"]]` | Desde un cliente obtengo **una lista** de pedidos |
| `Mapped["ClientesModel"]` | Desde un pedido obtengo **un** cliente |
| `back_populates="cliente"` | Conecta las dos puntas de la relación. Si no lo ponemos, SQLAlchemy crea dos relaciones separadas y muestra un warning |
| `"PedidosModel"` entre comillas | Esa clase está en otro archivo. Con comillas, SQLAlchemy la busca cuando ya están todas cargadas |
| `self.fecha.isoformat()` | Convierte la fecha a texto (`"2026-11-20T19:30:00"`), porque JSON no entiende objetos `datetime` |

> 💡 **¿Y `nullable=False`?** Ya no hace falta: `nombre: Mapped[str]` ya es obligatorio. Lo único que define si una columna acepta nulos es el `| None`.

---

### 1B — Demo: Segunda migración

Hay un detalle: **SQLite no sabe modificar columnas** (`ALTER COLUMN`). Para cambiar `telefono` de obligatorio a opcional, Alembic usa un truco: crea una tabla nueva, copia los datos y reemplaza la vieja. Eso se llama **batch mode** y se activa en `app.py`:

```python
migrate = Migrate(app, db, render_as_batch=True)
```

Y quiten la línea `from models.demo import DemoModel` de `app.py`.

Ahora generamos y aplicamos la migración:

```bash
flask db migrate -m "Telefono y direccion opcionales, relaciones, quitar demotabla"
flask db upgrade
```

Abran el archivo nuevo en `migrations/versions/` y lean lo que generó Alembic. Deberían ver algo así:

```python
def upgrade():
    op.drop_table('demotabla')
    with op.batch_alter_table('clientes', schema=None) as batch_op:
        batch_op.alter_column('telefono', existing_type=sa.VARCHAR(length=9), nullable=True)
        batch_op.alter_column('direccion', existing_type=sa.VARCHAR(length=200), nullable=True)
    ...
```

**¿Qué pasó?**

| Cambio en el modelo | Lo que generó Alembic |
|---------------------|-----------------------|
| Borramos `DemoModel` | `op.drop_table('demotabla')` |
| `telefono: Mapped[str \| None]` | `alter_column('telefono', nullable=True)` |
| `categoria: String(50)` | **Nada.** En SQLite, Alembic no detecta el cambio de `VARCHAR` a `VARCHAR(50)` |
| `relationship(...)` | **Nada.** Las relaciones viven solo en Python, no cambian la tabla |

> 💡 **Siempre revisen la migración antes del `upgrade`.** Alembic adivina los cambios y a veces se equivoca, sobre todo con columnas renombradas, que interpreta como "borrar una y crear otra".

---

### 1C — Reto: Verificar la migración y cargar datos de prueba

**Profe dice:** "Antes de escribir endpoints, necesitamos datos. Creen este script y ejecútenlo."

Crear `seed.py` en la carpeta `api/`:

```python
from app import app
from db import db
from models import ClientesModel, PlatosModel, PedidosModel

with app.app_context():
    ya_hay_datos = db.session.execute(db.select(ClientesModel)).first()

    if ya_hay_datos:
        print("La BD ya tiene datos, no se insertó nada")
    else:
        juan = ClientesModel(nombre="Juan Perez", telefono="999111222", direccion="Av. Lima 123")
        maria = ClientesModel(nombre="Maria Garcia", telefono="988222333", direccion="Jr. Union 456")
        carlos = ClientesModel(nombre="Carlos Lopez", telefono=None, direccion="Av. Arequipa 789")

        lomo = PlatosModel(nombre="Lomo Saltado", categoria="Platos Fuertes", precio=25.00)
        aji = PlatosModel(nombre="Aji de Gallina", categoria="Platos Fuertes", precio=20.00)
        ceviche = PlatosModel(nombre="Ceviche", categoria="Entradas", precio=30.00)
        inca = PlatosModel(nombre="Inca Kola", categoria="Bebidas", precio=5.00)
        arroz = PlatosModel(nombre="Arroz con Leche", categoria="Postres", precio=12.00)

        db.session.add_all([juan, maria, carlos, lomo, aji, ceviche, inca, arroz])

        db.session.add_all([
            PedidosModel(cliente=juan, plato=lomo, cantidad=2, total=50.00),
            PedidosModel(cliente=juan, plato=inca, cantidad=3, total=15.00),
            PedidosModel(cliente=maria, plato=ceviche, cantidad=1, total=30.00),
            PedidosModel(cliente=carlos, plato=aji, cantidad=1, total=20.00)
        ])

        db.session.commit()
        print("Datos de prueba insertados ✅")
```

```bash
python seed.py
```

Después, abran `instance/project.db` con la extensión **SQLite Viewer** y respondan:

1. ¿Sigue existiendo la tabla `demotabla`?
2. Carlos no tiene teléfono. ¿Qué valor aparece en esa celda?
3. ¿Qué valor tiene la tabla `alembic_version`? ¿Coincide con el nombre de algún archivo de `migrations/versions/`?
4. Fíjense en `PedidosModel(cliente=juan, ...)`: no pusimos `id_cliente`. ¿Cómo supo SQLAlchemy qué ID guardar?

<details>
<summary><b>Solución (reto)</b></summary>

1. **No.** La migración ejecutó `op.drop_table('demotabla')`.
2. **`NULL`.** Antes de la migración, este insert habría fallado con `NOT NULL constraint failed: clientes.telefono`.
3. Tiene el ID de la **última migración aplicada** (el que acaban de generar). Así Alembic sabe en qué versión está la BD y qué migraciones le faltan.
4. Gracias a la `relationship`. Al asignar `cliente=juan`, SQLAlchemy guarda primero a Juan, obtiene su `id_cliente` y lo copia en el pedido. Trabajamos con **objetos**, no con IDs.

</details>

---

## 2. Primer Resource: listar y crear clientes (25 min)

### 2A — Demo: `GET /clientes` y `POST /clientes`

Crear la carpeta `resources/` con un archivo vacío `resources/__init__.py`, y el archivo `resources/clientes_resource.py`:

```python
from flask import request
from flask_restful import Resource
from db import db
from models import ClientesModel


class ClientesListResource(Resource):

    # GET /clientes → listar todos
    def get(self):
        consulta = db.select(ClientesModel).order_by(ClientesModel.id_cliente)
        clientes = db.session.execute(consulta).scalars().all()

        resultado = []
        for cliente in clientes:
            resultado.append(cliente.to_dict())

        return resultado, 200

    # POST /clientes → crear uno nuevo
    def post(self):
        data = request.get_json(silent=True)

        if not data:
            return {"msg": "Debes enviar un JSON en el body"}, 400

        nombre = data.get("nombre")
        if not isinstance(nombre, str) or not nombre.strip():
            return {"msg": "El campo 'nombre' es obligatorio"}, 400

        nuevo = ClientesModel(
            nombre=nombre.strip(),
            telefono=data.get("telefono"),
            direccion=data.get("direccion")
        )

        db.session.add(nuevo)
        db.session.commit()

        return nuevo.to_dict(), 201
```

**Desglose de `get()`:**

| Línea | Significado |
|-------|-------------|
| `db.select(ClientesModel)` | Arma la consulta `SELECT * FROM clientes` (todavía no la ejecuta) |
| `.order_by(ClientesModel.id_cliente)` | Le agrega `ORDER BY id_cliente` |
| `db.session.execute(consulta)` | **Ahora sí** la ejecuta en la BD |
| `.scalars().all()` | Devuelve una lista de objetos `ClientesModel` |
| `return resultado, 200` | Flask-RESTful convierte la lista a JSON automáticamente |

**Desglose de `post()`:**

| Línea | Significado |
|-------|-------------|
| `request.get_json(silent=True)` | Lee el body. Con `silent=True`, si el JSON viene mal formado devuelve `None` en vez de reventar |
| `isinstance(nombre, str)` | Verifica que sea texto. Si alguien manda `"nombre": 123`, `.strip()` fallaría con un `500` |
| `not nombre.strip()` | Rechaza nombres vacíos o con solo espacios: `"   "` |
| `data.get("telefono")` | Si no lo envían, queda `None`. Ahora sí está permitido |
| `return ..., 201` | `201 Created`: le avisamos al cliente que se creó algo nuevo |

> 💡 **¿Por qué `db.select()` y no `ClientesModel.query.all()`?** `Model.query` es la API antigua. Todavía funciona, pero SQLAlchemy 2.0 la marca como *legacy*. Si estamos usando la sintaxis nueva en los modelos, usemos también la forma nueva de consultar.

### Registro en `app.py`

```python
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from db import db
from models import ClientesModel, PlatosModel, PedidosModel
from resources.clientes_resource import ClientesListResource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)
api = Api(app)

# Rutas
api.add_resource(ClientesListResource, "/clientes")

if __name__ == "__main__":
    app.run(debug=True)
```

| Línea | Significado |
|-------|-------------|
| `api = Api(app)` | Activa Flask-RESTful en nuestra app |
| `api.add_resource(Clase, "/ruta")` | Conecta la clase con la ruta. Cada método (`get`, `post`...) responde a su verbo HTTP |
| `from models import ...` | Importar los modelos sigue siendo necesario para que Flask-Migrate los detecte |

**Prueba en Postman:**

| Método | URL | Body | Resultado esperado |
|--------|-----|------|--------------------|
| GET | `/clientes` | — | `200` con los 3 clientes del seed |
| POST | `/clientes` | `{"nombre": "Ana Torres", "telefono": "966555444"}` | `201` con Ana creada (`direccion: null`) |
| POST | `/clientes` | `{"telefono": "966555444"}` | `400` falta el nombre |
| POST | `/clientes` | `{"nombre": "   "}` | `400` nombre vacío |
| POST | `/clientes` | *(sin body)* | `400` debes enviar un JSON |

---

### 2B — Reto: Validar el teléfono

**Profe dice:** "Me acaban de crear un cliente con teléfono `'hola'`. Eso no puede pasar. El teléfono es opcional, pero si lo mandan tiene que ser un celular peruano válido."

Agreguen al `post()` esta validación:
- Si **no** envían `telefono`, se permite (queda `None`)
- Si lo envían, debe ser texto de **exactamente 9 dígitos** que **empiece con 9**
- Si no cumple, responder `400` con `{"msg": "El teléfono debe tener 9 dígitos y empezar con 9"}`

**Pista:** los strings tienen el método `.isdigit()` y `.startswith()`.

<details>
<summary><b>Solución (reto)</b></summary>

Agregar después de validar el nombre:

```python
        telefono = data.get("telefono")
        if telefono is not None:
            if not isinstance(telefono, str) or len(telefono) != 9 or not telefono.isdigit() or not telefono.startswith("9"):
                return {"msg": "El teléfono debe tener 9 dígitos y empezar con 9"}, 400
```

Y en la creación usar la variable:

```python
        nuevo = ClientesModel(
            nombre=nombre.strip(),
            telefono=telefono,
            direccion=data.get("direccion")
        )
```

**¿Por qué `is not None` y no `if telefono:`?** Porque `if telefono:` también sería falso para `""` (texto vacío), y dejaríamos pasar un teléfono vacío. Con `is not None`, solo nos saltamos la validación cuando de verdad no lo enviaron.

**Pruebas:**

| Body | Resultado |
|------|-----------|
| `{"nombre": "Luis"}` | `201` (sin teléfono, permitido) |
| `{"nombre": "Luis", "telefono": "987654321"}` | `201` |
| `{"nombre": "Luis", "telefono": "hola"}` | `400` |
| `{"nombre": "Luis", "telefono": "887654321"}` | `400` (no empieza con 9) |
| `{"nombre": "Luis", "telefono": 987654321}` | `400` (es número, no texto) |

</details>

---

## 3. Endpoints con parámetro de ruta: uno, editar y eliminar (25 min)

### 3A — Demo: `GET`, `PUT` y `DELETE /clientes/<id>`

En el mismo `resources/clientes_resource.py`, agregar una segunda clase:

```python
class ClienteResource(Resource):

    # GET /clientes/3 → obtener uno
    def get(self, id_cliente):
        cliente = db.session.get(ClientesModel, id_cliente)

        if not cliente:
            return {"msg": f"No existe el cliente con id {id_cliente}"}, 404

        return cliente.to_dict(), 200

    # PUT /clientes/3 → actualizar (solo los campos que envíen)
    def put(self, id_cliente):
        cliente = db.session.get(ClientesModel, id_cliente)

        if not cliente:
            return {"msg": f"No existe el cliente con id {id_cliente}"}, 404

        data = request.get_json(silent=True)
        if not data:
            return {"msg": "Debes enviar un JSON en el body"}, 400

        if "nombre" in data:
            nombre = data["nombre"]
            if not isinstance(nombre, str) or not nombre.strip():
                return {"msg": "El campo 'nombre' no puede estar vacío"}, 400
            cliente.nombre = nombre.strip()

        if "telefono" in data:
            cliente.telefono = data["telefono"]

        if "direccion" in data:
            cliente.direccion = data["direccion"]

        db.session.commit()
        return cliente.to_dict(), 200

    # DELETE /clientes/3 → eliminar
    def delete(self, id_cliente):
        cliente = db.session.get(ClientesModel, id_cliente)

        if not cliente:
            return {"msg": f"No existe el cliente con id {id_cliente}"}, 404

        nombre = cliente.nombre
        db.session.delete(cliente)
        db.session.commit()

        return {"msg": f"Cliente '{nombre}' eliminado"}, 200
```

Registrar en `app.py`:

```python
from resources.clientes_resource import ClientesListResource, ClienteResource

api.add_resource(ClienteResource, "/clientes/<int:id_cliente>")
```

**Desglose:**

| Línea | Significado |
|-------|-------------|
| `"/clientes/<int:id_cliente>"` | La parte `<int:id_cliente>` se captura y llega como argumento al método. Si alguien pide `/clientes/abc`, Flask responde `404` solo, porque `abc` no es `int` |
| `def get(self, id_cliente)` | El nombre del argumento **debe ser igual** al de la ruta |
| `db.session.get(ClientesModel, id_cliente)` | Busca por llave primaria. Devuelve el objeto o `None` |
| `if "nombre" in data:` | Solo actualizamos lo que nos mandaron. Si no mandan `direccion`, se queda como estaba |
| `nombre = cliente.nombre` | Guardamos el nombre **antes** de borrar, para usarlo en el mensaje |

**¿Por qué dos clases?** Porque tienen rutas distintas:

| Clase | Ruta | Métodos |
|-------|------|---------|
| `ClientesListResource` | `/clientes` | `GET` (todos), `POST` (crear) |
| `ClienteResource` | `/clientes/<id>` | `GET` (uno), `PUT` (editar), `DELETE` (borrar) |

> 💡 **PUT vs PATCH:** estrictamente, `PUT` reemplaza el registro completo y `PATCH` actualiza solo algunos campos. Nuestro `put()` en realidad se comporta como un `PATCH`. Muchas APIs lo hacen así; lo importante es que el equipo sea consistente.

---

### 3B — Reto: No borrar clientes con pedidos

**Profe dice:** "Prueben `DELETE /clientes/1`. Juan tiene 2 pedidos. ¿Qué pasa con esos pedidos?"

Lo que pasa es que SQLite, por defecto, **no revisa las llaves foráneas**. Juan se borra y sus pedidos quedan apuntando a un cliente que ya no existe. Y después, `GET /pedidos` revienta con `500`, porque `self.cliente.nombre` intenta leer el nombre de un cliente que es `None`.

Modifiquen el `delete()` para que:
- Si el cliente **tiene pedidos**, responda `409` con `{"msg": "No se puede eliminar a Juan Perez: tiene 2 pedido(s)"}`
- Si **no tiene pedidos**, lo borre normalmente

**Pista:** gracias a la `relationship`, `cliente.pedidos` es una lista.

<details>
<summary><b>Solución (reto)</b></summary>

```python
    def delete(self, id_cliente):
        cliente = db.session.get(ClientesModel, id_cliente)

        if not cliente:
            return {"msg": f"No existe el cliente con id {id_cliente}"}, 404

        if len(cliente.pedidos) > 0:
            return {"msg": f"No se puede eliminar a {cliente.nombre}: tiene {len(cliente.pedidos)} pedido(s)"}, 409

        nombre = cliente.nombre
        db.session.delete(cliente)
        db.session.commit()

        return {"msg": f"Cliente '{nombre}' eliminado"}, 200
```

**¿Por qué `409` y no `400`?** El request está bien formado (`400` sería "mandaste algo mal"). El problema es que la operación **choca con el estado actual de los datos**. Para eso existe `409 Conflict`.

**Pruebas:**
- `DELETE /clientes/1` → `409` (Juan tiene pedidos)
- `DELETE /clientes/4` → `200` (Ana, creada en la demo, no tiene pedidos)

> Si ya borraron a Juan en la demo, vuelvan a empezar: borren `instance/project.db`, ejecuten `flask db upgrade` y `python seed.py`.

</details>

---

## 4. Reto: CRUD completo de Platos (25 min)

**Profe dice:** "Ya vieron el patrón completo con Clientes. Ahora háganlo solos para Platos, con estas reglas de negocio."

Crear `resources/platos_resource.py` con `PlatosListResource` y `PlatoResource`:

| Endpoint | Regla |
|----------|-------|
| `GET /platos` | Lista todos, ordenados por `id_plato` |
| `POST /platos` | `nombre` obligatorio. `precio` obligatorio, numérico y mayor a 0. `categoria` obligatoria y debe ser una de: `Entradas`, `Platos Fuertes`, `Bebidas`, `Postres` |
| `GET /platos/<id>` | `404` si no existe |
| `PUT /platos/<id>` | Actualiza solo lo que envíen, **aplicando las mismas validaciones** |
| `DELETE /platos/<id>` | `409` si el plato tiene pedidos |

**Pista:** para validar un número, `isinstance(precio, (int, float))` acepta tanto `25` como `25.50`.

<details>
<summary><b>Solución (reto)</b></summary>

```python
from flask import request
from flask_restful import Resource
from db import db
from models import PlatosModel

CATEGORIAS = ["Entradas", "Platos Fuertes", "Bebidas", "Postres"]


class PlatosListResource(Resource):

    def get(self):
        consulta = db.select(PlatosModel).order_by(PlatosModel.id_plato)
        platos = db.session.execute(consulta).scalars().all()

        resultado = []
        for plato in platos:
            resultado.append(plato.to_dict())

        return resultado, 200

    def post(self):
        data = request.get_json(silent=True)

        if not data:
            return {"msg": "Debes enviar un JSON en el body"}, 400

        nombre = data.get("nombre")
        if not isinstance(nombre, str) or not nombre.strip():
            return {"msg": "El campo 'nombre' es obligatorio"}, 400

        precio = data.get("precio")
        if not isinstance(precio, (int, float)) or precio <= 0:
            return {"msg": "El precio debe ser un número mayor a 0"}, 400

        categoria = data.get("categoria")
        if categoria not in CATEGORIAS:
            return {"msg": f"La categoría debe ser una de: {', '.join(CATEGORIAS)}"}, 400

        nuevo = PlatosModel(nombre=nombre.strip(), categoria=categoria, precio=precio)

        db.session.add(nuevo)
        db.session.commit()

        return nuevo.to_dict(), 201


class PlatoResource(Resource):

    def get(self, id_plato):
        plato = db.session.get(PlatosModel, id_plato)

        if not plato:
            return {"msg": f"No existe el plato con id {id_plato}"}, 404

        return plato.to_dict(), 200

    def put(self, id_plato):
        plato = db.session.get(PlatosModel, id_plato)

        if not plato:
            return {"msg": f"No existe el plato con id {id_plato}"}, 404

        data = request.get_json(silent=True)
        if not data:
            return {"msg": "Debes enviar un JSON en el body"}, 400

        if "nombre" in data:
            nombre = data["nombre"]
            if not isinstance(nombre, str) or not nombre.strip():
                return {"msg": "El campo 'nombre' no puede estar vacío"}, 400
            plato.nombre = nombre.strip()

        if "precio" in data:
            precio = data["precio"]
            if not isinstance(precio, (int, float)) or precio <= 0:
                return {"msg": "El precio debe ser un número mayor a 0"}, 400
            plato.precio = precio

        if "categoria" in data:
            if data["categoria"] not in CATEGORIAS:
                return {"msg": f"La categoría debe ser una de: {', '.join(CATEGORIAS)}"}, 400
            plato.categoria = data["categoria"]

        db.session.commit()
        return plato.to_dict(), 200

    def delete(self, id_plato):
        plato = db.session.get(PlatosModel, id_plato)

        if not plato:
            return {"msg": f"No existe el plato con id {id_plato}"}, 404

        if len(plato.pedidos) > 0:
            return {"msg": f"No se puede eliminar '{plato.nombre}': aparece en {len(plato.pedidos)} pedido(s)"}, 409

        nombre = plato.nombre
        db.session.delete(plato)
        db.session.commit()

        return {"msg": f"Plato '{nombre}' eliminado"}, 200
```

**Registro en `app.py`:**

```python
from resources.platos_resource import PlatosListResource, PlatoResource

api.add_resource(PlatosListResource, "/platos")
api.add_resource(PlatoResource, "/platos/<int:id_plato>")
```

**¿Qué cambia respecto a Clientes?**
- `CATEGORIAS` es una constante: la lista de valores permitidos se escribe **una sola vez** y la usan `post()` y `put()`
- `categoria not in CATEGORIAS` también rechaza `None`, así que cubre el caso "no la enviaron"
- Validamos **también en el `put()`**. Si no, alguien crea un plato válido y después le cambia el precio a `-10`

</details>

---

## 5. Query params: filtrar y buscar (25 min)

Hasta ahora `GET /platos` devuelve **todo**. Pero el mozo no le recita la carta completa a un cliente que solo quiere postres. Para eso existen los **query params**: todo lo que va después del `?` en la URL.

```
GET /platos?categoria=Postres&precio_max=15
            ─────────────────  ────────────
               parámetro 1      parámetro 2   (se separan con &)
```

### 5A — Demo: Filtrar platos por categoría y precio

Reemplazar el `get()` de `PlatosListResource`:

```python
    def get(self):
        categoria = request.args.get("categoria")
        precio_max = request.args.get("precio_max", type=float)

        consulta = db.select(PlatosModel)

        if categoria:
            consulta = consulta.where(PlatosModel.categoria == categoria)

        if precio_max is not None:
            consulta = consulta.where(PlatosModel.precio <= precio_max)

        consulta = consulta.order_by(PlatosModel.precio)
        platos = db.session.execute(consulta).scalars().all()

        resultado = []
        for plato in platos:
            resultado.append(plato.to_dict())

        return resultado, 200
```

**Desglose:**

| Línea | Significado |
|-------|-------------|
| `request.args.get("categoria")` | Lee `?categoria=...`. Si no viene, devuelve `None` |
| `request.args.get("precio_max", type=float)` | Lo convierte a `float`. Si viene algo que no es número (`?precio_max=caro`), devuelve `None` en vez de reventar |
| `consulta = consulta.where(...)` | Le **agregamos** una condición a la consulta. Es como armar el SQL por partes |
| `PlatosModel.precio <= precio_max` | Se traduce a `WHERE precio <= 15.0` |

**La idea clave:** la consulta se construye **paso a paso** y solo se ejecuta al final con `db.session.execute()`. Cada filtro es opcional: si no lo mandan, no se agrega.

**Prueba en Postman** (en la pestaña **Params** pueden escribirlos como tabla):

| URL | Resultado |
|-----|-----------|
| `/platos` | Los 5 platos, del más barato al más caro |
| `/platos?categoria=Platos Fuertes` | Aji de Gallina y Lomo Saltado |
| `/platos?precio_max=15` | Inca Kola y Arroz con Leche |
| `/platos?categoria=Platos Fuertes&precio_max=22` | Solo Aji de Gallina |
| `/platos?precio_max=caro` | Los 5 (el filtro se ignora) |

---

### 5B — Reto: Buscador de clientes

**Profe dice:** "La cajera quiere escribir 'gar' y que le aparezca Maria Garcia. No sabe si escribió con mayúscula o minúscula."

Modifiquen `GET /clientes` para que acepte:
- `?buscar=texto` → clientes cuyo **nombre contenga** ese texto, sin importar mayúsculas
- `?orden=desc` → ordenar por nombre de Z a A. Si no lo mandan (o mandan otra cosa), de A a Z

**Pista:** `ClientesModel.nombre.ilike("%gar%")` se traduce a `WHERE nombre LIKE '%gar%'` sin distinguir mayúsculas. Y para ordenar al revés: `ClientesModel.nombre.desc()`.

<details>
<summary><b>Solución (reto)</b></summary>

```python
    def get(self):
        buscar = request.args.get("buscar")
        orden = request.args.get("orden")

        consulta = db.select(ClientesModel)

        if buscar:
            consulta = consulta.where(ClientesModel.nombre.ilike(f"%{buscar}%"))

        if orden == "desc":
            consulta = consulta.order_by(ClientesModel.nombre.desc())
        else:
            consulta = consulta.order_by(ClientesModel.nombre)

        clientes = db.session.execute(consulta).scalars().all()

        resultado = []
        for cliente in clientes:
            resultado.append(cliente.to_dict())

        return resultado, 200
```

**Pruebas:**

| URL | Resultado |
|-----|-----------|
| `/clientes?buscar=gar` | Maria Garcia |
| `/clientes?buscar=PEREZ` | Juan Perez |
| `/clientes?buscar=lo` | Carlos Lopez |
| `/clientes?orden=desc` | Todos, de Z a A |
| `/clientes?buscar=xyz` | `[]` (lista vacía, **no** es un error) |

**¿Es peligroso meter `buscar` dentro del `f"%{buscar}%"`?** No: SQLAlchemy lo envía como **parámetro**, no lo pega dentro del SQL. Por eso no hay riesgo de SQL Injection, a diferencia de cuando armábamos el SQL con f-strings en psycopg2.

</details>

---

## 6. Pedidos: la lógica de negocio vive en el servidor (25 min)

Hasta ahora los endpoints guardaban lo que el cliente enviaba. Los pedidos son distintos: **el servidor calcula el total**. Si dejamos que el frontend envíe el total, cualquiera podría pedir 10 lomos saltados por S/ 1.

### 6A — Demo: `GET` y `POST /pedidos`, `GET` y `DELETE /pedidos/<id>`

Crear `resources/pedidos_resource.py`:

```python
from flask import request
from flask_restful import Resource
from db import db
from models import ClientesModel, PlatosModel, PedidosModel


class PedidosListResource(Resource):

    def get(self):
        consulta = db.select(PedidosModel).order_by(PedidosModel.fecha.desc())
        pedidos = db.session.execute(consulta).scalars().all()

        resultado = []
        for pedido in pedidos:
            resultado.append(pedido.to_dict())

        return resultado, 200

    def post(self):
        data = request.get_json(silent=True)

        if not data:
            return {"msg": "Debes enviar un JSON en el body"}, 400

        id_cliente = data.get("id_cliente")
        id_plato = data.get("id_plato")
        cantidad = data.get("cantidad", 1)

        if not isinstance(id_cliente, int) or not isinstance(id_plato, int):
            return {"msg": "'id_cliente' e 'id_plato' son obligatorios y deben ser números enteros"}, 400

        if not isinstance(cantidad, int) or cantidad <= 0:
            return {"msg": "La cantidad debe ser un número entero mayor a 0"}, 400

        cliente = db.session.get(ClientesModel, id_cliente)
        if not cliente:
            return {"msg": f"No existe el cliente con id {id_cliente}"}, 404

        plato = db.session.get(PlatosModel, id_plato)
        if not plato:
            return {"msg": f"No existe el plato con id {id_plato}"}, 404

        # El total lo calcula el SERVIDOR, nunca el cliente
        total = round(plato.precio * cantidad, 2)

        nuevo = PedidosModel(cliente=cliente, plato=plato, cantidad=cantidad, total=total)

        db.session.add(nuevo)
        db.session.commit()

        return nuevo.to_dict(), 201


class PedidoResource(Resource):

    def get(self, id_pedido):
        pedido = db.session.get(PedidosModel, id_pedido)

        if not pedido:
            return {"msg": f"No existe el pedido con id {id_pedido}"}, 404

        return pedido.to_dict(), 200

    def delete(self, id_pedido):
        pedido = db.session.get(PedidosModel, id_pedido)

        if not pedido:
            return {"msg": f"No existe el pedido con id {id_pedido}"}, 404

        db.session.delete(pedido)
        db.session.commit()

        return {"msg": f"Pedido {id_pedido} eliminado"}, 200
```

Registrar en `app.py`:

```python
from resources.pedidos_resource import PedidosListResource, PedidoResource

api.add_resource(PedidosListResource, "/pedidos")
api.add_resource(PedidoResource, "/pedidos/<int:id_pedido>")
```

**Desglose del `post()`:**

| Paso | ¿Qué hace? | Si falla... |
|------|-----------|-------------|
| 1. Validar formato | ¿Vienen los IDs? ¿Son enteros? ¿La cantidad es positiva? | `400` |
| 2. Validar existencia | ¿Existe ese cliente? ¿Existe ese plato? | `404` |
| 3. Calcular | `total = precio × cantidad` | — |
| 4. Guardar | `add` + `commit` | — |

**Ese orden importa:** primero lo barato (revisar el JSON) y después lo caro (consultar la BD). No tiene sentido ir a la BD si el JSON ya viene mal.

**Prueba en Postman:**

| Body de `POST /pedidos` | Resultado |
|-------------------------|-----------|
| `{"id_cliente": 2, "id_plato": 1, "cantidad": 2}` | `201` con `total: 50.0` y los nombres `Maria Garcia` / `Lomo Saltado` |
| `{"id_cliente": 2, "id_plato": 4}` | `201` con `cantidad: 1` y `total: 5.0` |
| `{"id_cliente": 2, "id_plato": 1, "total": 1}` | `201` con `total: 25.0`. El `total` enviado **se ignora** 😎 |
| `{"id_cliente": 99, "id_plato": 1}` | `404` cliente no existe |
| `{"id_cliente": 2, "id_plato": 1, "cantidad": 0}` | `400` |
| `{"id_cliente": "dos", "id_plato": 1}` | `400` |

---

### 6B — Reto: Editar la cantidad de un pedido

**Profe dice:** "Maria llamó: en vez de 2 lomos quiere 3. Necesito un `PUT /pedidos/<id>` que cambie la cantidad."

Reglas:
- Solo se puede cambiar `cantidad` (si mandan otra cosa, se ignora)
- `cantidad` es obligatoria, entera y mayor a 0
- El `total` se **recalcula** con el precio del plato
- `404` si el pedido no existe

**Pista:** desde el pedido llegan al precio con `pedido.plato.precio`.

<details>
<summary><b>Solución (reto)</b></summary>

Agregar a `PedidoResource`:

```python
    def put(self, id_pedido):
        pedido = db.session.get(PedidosModel, id_pedido)

        if not pedido:
            return {"msg": f"No existe el pedido con id {id_pedido}"}, 404

        data = request.get_json(silent=True)
        if not data:
            return {"msg": "Debes enviar un JSON en el body"}, 400

        cantidad = data.get("cantidad")
        if not isinstance(cantidad, int) or cantidad <= 0:
            return {"msg": "La cantidad debe ser un número entero mayor a 0"}, 400

        pedido.cantidad = cantidad
        pedido.total = round(pedido.plato.precio * cantidad, 2)

        db.session.commit()
        return pedido.to_dict(), 200
```

**Prueba:** `PUT /pedidos/5` con `{"cantidad": 3}` → `total: 75.0`.

**Para pensar:** si mañana el Lomo Saltado sube a S/ 28 y alguien edita un pedido de ayer, el total se recalcula con el precio **nuevo**. ¿Es correcto? En sistemas reales se guarda el `precio_unitario` dentro del pedido, al momento de crearlo. Ese es un buen cambio para practicar Flask-Migrate en casa.

</details>

---

## 7. Endpoints anidados: navegar las relaciones (20 min)

Una ruta como `/clientes/1/pedidos` se lee: "los pedidos **del** cliente 1". Es la forma estándar de exponer una relación 1:N en una API.

### 7A — Demo: `GET /clientes/<id>/pedidos`

En `resources/clientes_resource.py`:

```python
class ClientePedidosResource(Resource):

    def get(self, id_cliente):
        cliente = db.session.get(ClientesModel, id_cliente)

        if not cliente:
            return {"msg": f"No existe el cliente con id {id_cliente}"}, 404

        pedidos = []
        total_gastado = 0

        for pedido in cliente.pedidos:
            pedidos.append(pedido.to_dict())
            total_gastado += pedido.total

        return {
            "cliente": cliente.nombre,
            "cantidad_pedidos": len(pedidos),
            "total_gastado": round(total_gastado, 2),
            "pedidos": pedidos
        }, 200
```

Registrar en `app.py`:

```python
from resources.clientes_resource import ClientesListResource, ClienteResource, ClientePedidosResource

api.add_resource(ClientePedidosResource, "/clientes/<int:id_cliente>/pedidos")
```

**Prueba:** `GET /clientes/1/pedidos`

```json
{
    "cliente": "Juan Perez",
    "cantidad_pedidos": 2,
    "total_gastado": 65.0,
    "pedidos": [ ... ]
}
```

**¿Qué ganamos con la `relationship`?** `cliente.pedidos` ya trae los pedidos. Sin la relación tendríamos que escribir la consulta a mano: `db.select(PedidosModel).where(PedidosModel.id_cliente == id_cliente)`.

---

### 7B — Reto: Estadísticas de un plato

**Profe dice:** "El chef quiere saber cómo le va a cada plato."

Crear `GET /platos/<id>/pedidos` que devuelva (ejemplo con los datos del `seed.py`):

```json
{
    "plato": "Lomo Saltado",
    "veces_pedido": 1,
    "unidades_vendidas": 2,
    "ingresos": 50.0
}
```

- `veces_pedido`: cuántos pedidos incluyen ese plato
- `unidades_vendidas`: la suma de las cantidades
- `ingresos`: la suma de los totales
- `404` si el plato no existe

<details>
<summary><b>Solución (reto)</b></summary>

En `resources/platos_resource.py`:

```python
class PlatoPedidosResource(Resource):

    def get(self, id_plato):
        plato = db.session.get(PlatosModel, id_plato)

        if not plato:
            return {"msg": f"No existe el plato con id {id_plato}"}, 404

        unidades = 0
        ingresos = 0

        for pedido in plato.pedidos:
            unidades += pedido.cantidad
            ingresos += pedido.total

        return {
            "plato": plato.nombre,
            "veces_pedido": len(plato.pedidos),
            "unidades_vendidas": unidades,
            "ingresos": round(ingresos, 2)
        }, 200
```

**Registro en `app.py`:**

```python
from resources.platos_resource import PlatosListResource, PlatoResource, PlatoPedidosResource

api.add_resource(PlatoPedidosResource, "/platos/<int:id_plato>/pedidos")
```

**Prueba:** `GET /platos/5/pedidos` (Arroz con Leche, nadie lo pidió) → `veces_pedido: 0`, `ingresos: 0`. Un plato sin ventas **no es un error**: es un `200` con ceros.

</details>

---

## 8. Ejercicio integrador: reporte de ventas (20 min)

### Reto: `GET /reporte/ventas`

**Profe dice:** "El dueño quiere ver en un solo endpoint cómo va el negocio. Y ojo: esta vez no quiero que recorran todos los pedidos con un `for` en Python. Que la BD haga las cuentas."

Crear `resources/reportes_resource.py` con `ReporteVentasResource` que devuelva:

```json
{
    "total_pedidos": 4,
    "total_ingresos": 115.0,
    "ventas_por_categoria": [
        {"categoria": "Platos Fuertes", "ingresos": 70.0},
        {"categoria": "Entradas", "ingresos": 30.0},
        {"categoria": "Bebidas", "ingresos": 15.0}
    ],
    "plato_mas_vendido": {"nombre": "Inca Kola", "unidades": 3}
}
```

*(Valores esperados si la BD solo tiene los datos del `seed.py`.)*

**Pistas:**
- `from sqlalchemy import func` trae `func.count()` y `func.sum()`
- `db.session.execute(db.select(func.sum(PedidosModel.total))).scalar()` devuelve **un solo valor**
- Para agrupar: `.select_from(PedidosModel).join(PlatosModel).group_by(...)`

<details>
<summary><b>Solución (reto)</b></summary>

```python
from flask_restful import Resource
from sqlalchemy import func
from db import db
from models import PlatosModel, PedidosModel


class ReporteVentasResource(Resource):

    def get(self):
        # 1. Totales generales
        total_pedidos = db.session.execute(
            db.select(func.count(PedidosModel.id_pedido))
        ).scalar()

        total_ingresos = db.session.execute(
            db.select(func.sum(PedidosModel.total))
        ).scalar()

        if total_ingresos is None:  # SUM de una tabla vacía devuelve NULL
            total_ingresos = 0

        # 2. Ingresos agrupados por categoría
        consulta_categorias = (
            db.select(PlatosModel.categoria, func.sum(PedidosModel.total))
            .select_from(PedidosModel)
            .join(PlatosModel)
            .group_by(PlatosModel.categoria)
            .order_by(func.sum(PedidosModel.total).desc())
        )

        ventas_por_categoria = []
        for categoria, ingresos in db.session.execute(consulta_categorias).all():
            ventas_por_categoria.append({
                "categoria": categoria,
                "ingresos": round(ingresos, 2)
            })

        # 3. Plato con más unidades vendidas
        consulta_top = (
            db.select(PlatosModel.nombre, func.sum(PedidosModel.cantidad))
            .select_from(PedidosModel)
            .join(PlatosModel)
            .group_by(PlatosModel.id_plato, PlatosModel.nombre)
            .order_by(func.sum(PedidosModel.cantidad).desc())
            .limit(1)
        )
        plato_top = db.session.execute(consulta_top).first()

        resultado = {
            "total_pedidos": total_pedidos,
            "total_ingresos": round(total_ingresos, 2),
            "ventas_por_categoria": ventas_por_categoria,
            "plato_mas_vendido": None
        }

        if plato_top:
            resultado["plato_mas_vendido"] = {
                "nombre": plato_top[0],
                "unidades": plato_top[1]
            }

        return resultado, 200
```

**Registro en `app.py`:**

```python
from resources.reportes_resource import ReporteVentasResource

api.add_resource(ReporteVentasResource, "/reporte/ventas")
```

**Desglose de la consulta por categoría:**

| Parte | SQL equivalente |
|-------|-----------------|
| `db.select(PlatosModel.categoria, func.sum(PedidosModel.total))` | `SELECT platos.categoria, SUM(pedidos.total)` |
| `.select_from(PedidosModel)` | `FROM pedidos` |
| `.join(PlatosModel)` | `JOIN platos ON platos.id_plato = pedidos.id_plato` (lo deduce de la FK) |
| `.group_by(PlatosModel.categoria)` | `GROUP BY platos.categoria` |
| `.order_by(func.sum(...).desc())` | `ORDER BY SUM(pedidos.total) DESC` |

**¿Por qué "Postres" no aparece?** Porque nadie pidió Arroz con Leche: el `JOIN` solo incluye platos que tienen pedidos.

**¿Por qué en la BD y no con un `for`?** Con 4 pedidos da igual. Con 500 000, traer todo a Python para sumarlo es lentísimo. La BD está hecha para eso.

</details>

---

## `app.py` completo

```python
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from db import db
from models import ClientesModel, PlatosModel, PedidosModel
from resources.clientes_resource import ClientesListResource, ClienteResource, ClientePedidosResource
from resources.platos_resource import PlatosListResource, PlatoResource, PlatoPedidosResource
from resources.pedidos_resource import PedidosListResource, PedidoResource
from resources.reportes_resource import ReporteVentasResource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)
api = Api(app)

# Clientes
api.add_resource(ClientesListResource, "/clientes")
api.add_resource(ClienteResource, "/clientes/<int:id_cliente>")
api.add_resource(ClientePedidosResource, "/clientes/<int:id_cliente>/pedidos")

# Platos
api.add_resource(PlatosListResource, "/platos")
api.add_resource(PlatoResource, "/platos/<int:id_plato>")
api.add_resource(PlatoPedidosResource, "/platos/<int:id_plato>/pedidos")

# Pedidos
api.add_resource(PedidosListResource, "/pedidos")
api.add_resource(PedidoResource, "/pedidos/<int:id_pedido>")

# Reportes
api.add_resource(ReporteVentasResource, "/reporte/ventas")

if __name__ == "__main__":
    app.run(debug=True)
```

---

## Mapa de endpoints

| # | Método | Ruta | ¿Qué hace? | Sección |
|---|--------|------|-----------|:-------:|
| 1 | GET | `/clientes?buscar=&orden=` | Listar / buscar clientes | 2A, 5B |
| 2 | POST | `/clientes` | Crear cliente | 2A, 2B |
| 3 | GET | `/clientes/<id>` | Obtener un cliente | 3A |
| 4 | PUT | `/clientes/<id>` | Editar cliente | 3A |
| 5 | DELETE | `/clientes/<id>` | Eliminar cliente (409 si tiene pedidos) | 3A, 3B |
| 6 | GET | `/clientes/<id>/pedidos` | Pedidos y total gastado de un cliente | 7A |
| 7 | GET | `/platos?categoria=&precio_max=` | Listar / filtrar platos | 4, 5A |
| 8 | POST | `/platos` | Crear plato | 4 |
| 9 | GET | `/platos/<id>` | Obtener un plato | 4 |
| 10 | PUT | `/platos/<id>` | Editar plato | 4 |
| 11 | DELETE | `/platos/<id>` | Eliminar plato (409 si tiene pedidos) | 4 |
| 12 | GET | `/platos/<id>/pedidos` | Estadísticas de un plato | 7B |
| 13 | GET | `/pedidos` | Listar pedidos | 6A |
| 14 | POST | `/pedidos` | Crear pedido (total calculado) | 6A |
| 15 | GET | `/pedidos/<id>` | Obtener un pedido | 6A |
| 16 | PUT | `/pedidos/<id>` | Cambiar cantidad (recalcula total) | 6B |
| 17 | DELETE | `/pedidos/<id>` | Eliminar pedido | 6A |
| 18 | GET | `/reporte/ventas` | Reporte general | 8 |

> 💡 Guarden todas estas pruebas en una **colección de Postman** llamada `Restaurante API`, con una carpeta por recurso. La próxima clase la vamos a reutilizar.

---

## Resumen de conceptos

| Tema | Demo | Reto | Conceptos clave |
|------|:----:|:----:|-----------------|
| 0. Anatomía de un endpoint | — | — | Método + ruta, parámetros de ruta, query params, body, códigos de estado |
| 1. Puesta a punto | ✅ | ✅ | `Mapped[str \| None]`, `back_populates`, `render_as_batch`, segunda migración, seed |
| 2. Listar y crear | ✅ | ✅ | `Resource`, `add_resource`, `db.select()`, `get_json(silent=True)`, `isinstance`, `201` |
| 3. Uno, editar, eliminar | ✅ | ✅ | `<int:id>`, `db.session.get()`, actualización parcial, `404`, `409` |
| 4. CRUD de Platos | — | ✅ | Reglas de negocio, constantes, validar también en el `PUT` |
| 5. Query params | ✅ | ✅ | `request.args.get(type=)`, `.where()`, `.ilike()`, `.order_by().desc()` |
| 6. Pedidos | ✅ | ✅ | Validar → buscar → calcular → guardar; el servidor calcula el total |
| 7. Endpoints anidados | ✅ | ✅ | `/recurso/<id>/subrecurso`, navegar `relationship` |
| 8. Reporte de ventas | — | ✅ | `func.count`, `func.sum`, `join`, `group_by`, `.scalar()` |

---

## Estructura final del proyecto

```
api/
├── .gitignore
├── app.py
├── db.py
├── seed.py
├── requirements.txt
├── instance/
│   └── project.db
├── migrations/
│   └── versions/
│       ├── 3a308f4fc292_migracion_inicial.py
│       └── xxxxxxxxxxxx_telefono_y_direccion_opcionales_....py
├── models/
│   ├── __init__.py
│   ├── clientes.py
│   ├── platos.py
│   └── pedidos.py
└── resources/
    ├── __init__.py
    ├── clientes_resource.py
    ├── platos_resource.py
    ├── pedidos_resource.py
    └── reportes_resource.py
```

---

## 🏠 Para practicar en casa

1. **Precio histórico:** agreguen `precio_unitario: Mapped[float]` a `PedidosModel`, generen la migración y úsenlo en el `POST` y el `PUT` de pedidos (ver la reflexión del reto 6B).
2. **Filtro por fechas:** `GET /pedidos?desde=2026-11-01&hasta=2026-11-30`. Pista: `datetime.fromisoformat()`.
3. **Paginación:** `GET /clientes?pagina=2&por_pagina=10`. Pista: `.limit()` y `.offset()`.
4. **Código repetido:** el bloque "buscar por ID y si no existe devolver 404" aparece en casi todos los métodos. ¿Cómo lo convertirían en una función reutilizable?
