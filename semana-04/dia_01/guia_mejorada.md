# 🧠 Guía — Día 1 (Semana 4): Bases de datos con PostgreSQL

<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Postgresql_elephant.svg?width=120" alt="Logo de PostgreSQL" height="100">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Python-logo-notext.svg?width=90" alt="Logo de Python" height="80">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Pgadmin-logo.svg?width=220" alt="Logo de pgAdmin" height="80">
</p>

Bienvenidos al día más importante del curso. Hasta ahora todo lo que construían en Python vivía en listas de diccionarios que desaparecían al apagar el servidor. Eso se acabó. Hoy aprendemos a **persistir datos como profesionales**.

Vamos a usar **PostgreSQL**, el motor de base de datos open source más potente del planeta. Y todo alrededor del **Mundial 2026** — selecciones (equipos), jugadores, partidos, goles, y tabla de posiciones. Nada de tablas de ejemplo sin sentido. Esto es datos de verdad.

El viaje de hoy: van a construir una base de datos completa desde cero. Van a crear tablas, llenarlas con datos del Mundial, consultar partidos, calcular posiciones, y entender cómo se relaciona todo. Al final del día, ustedes van a poder decir "yo sé SQL".

---

## 0. ¿Qué es una base de datos? — el modelo mental (15 min)

Hasta la semana pasada, ustedes guardaban datos así:

```python
equipos = [
    {"id": 1, "nombre": "Argentina", "grupo": "A", "ranking_fifa": 1},
    {"id": 2, "nombre": "Perú", "grupo": "A", "ranking_fifa": 31},
]

jugadores = [
    {"id": 1, "nombre": "Lionel Messi", "dorsal": 10, "posicion": "Delantero", "equipo_id": 1},
    {"id": 2, "nombre": "Paolo Guerrero", "dorsal": 9, "posicion": "Delantero", "equipo_id": 2},
]
```

Y eso funciona... hasta que apagan el servidor y todo se pierde. O hasta que tienen 50,000 jugadores y la lista vive en la memoria de una sola máquina. O hasta que dos personas intentan modificar los datos al mismo tiempo.

Una **base de datos** resuelve tres problemas que una lista de Python jamás va a poder resolver:

| Problema | Lista de Python | Base de datos |
|----------|----------------|---------------|
| **Persistencia** | Se borra al apagar | Vive en disco, siempre está |
| **Búsqueda rápida** | Tenés que recorrer todo con un `for` | Índices, consultas optimizadas al instante |
| **Concurrencia** | Un solo programa accede | Miles de usuarios al mismo tiempo, sin pisarse |
| **Relaciones** | Las FK las manejas a mano, si te acuerdas | El motor las garantiza, no permite datos inválidos |

**Analogía clave:** una lista de Python es como una hoja de papel donde anotas cosas. Rápida, práctica, pero si se moja o se pierde, chau datos. Una base de datos es como un archivero profesional con cajones etiquetados, donde cada cajón tiene sus reglas, y varias personas pueden sacar y guardar papeles al mismo tiempo sin que se pierda nada.

### ¿Cómo se organiza una base de datos?

```
Base de datos (mundial_futbol)
  ├── Tabla: equipos
  │     ├── Columnas: id, nombre, confederacion, grupo, ranking_fifa
  │     └── Filas: Argentina (A, rk1), Perú (A, rk31), Brasil (C, rk5)...
  ├── Tabla: jugadores
  │     ├── Columnas: id, nombre, posicion, dorsal, equipo_id
  │     └── Filas: Messi (equipo_id=1), Guerrero (equipo_id=2)...
  ├── Tabla: partidos
  │     ├── Columnas: id, local_id, visitante_id, goles_local, goles_visitante
  │     └── Filas: Argentina 2-0 Perú, Brasil 4-1 Uruguay...
  ├── Tabla: goles
  │     ├── Columnas: id, minuto, jugador_id, partido_id
  │     └── Filas: Messi 35' (ARG vs PER), Neymar 85' penal (BRA vs URU)...
  └── Tabla: posiciones_por_grupo
        ├── Columnas: equipo_id, pj, pg, pe, pp, gf, gc, puntos
        └── Filas: Argentina (3 pts, +2), Perú (0 pts, -2)...
```

Cada **tabla** es como una hoja de Excel con columnas fijas (los **campos**) y filas (cada fila es un **registro**). Pero a diferencia de Excel, la base de datos te garantiza que los datos sean consistentes: no se duplican IDs, no puedes tener un gol sin un partido, no puedes tener un jugador sin equipo.

**Y lo mejor de todo:** no importa qué lenguaje uses — Python, Java, JavaScript, Go — todos se comunican con la base de datos usando el mismo idioma: **SQL**. Lo que aprendan hoy les sirve para toda su carrera, sin importar el stack.

---

## 1. Conectarse a PostgreSQL — la puerta de entrada (10 min)

Para hablar con PostgreSQL necesitamos un **cliente**. Hay varias opciones:

- **pgAdmin** — interfaz gráfica (la más amigable para empezar)
- **psql** — terminal (la que usan los profesionales)
- **DBeaver, DataGrip** — otras herramientas

Hoy usamos **pgAdmin** porque viene con PostgreSQL y tiene interfaz visual. Es como tener el panel de control de la base de datos.

### 1A — Demo: Abrir pgAdmin y conectar al servidor

1. Abran pgAdmin desde el menú de inicio (busquen "pgAdmin 4" en su compu)
2. Les va a pedir una **contraseña maestra** — pongan una que recuerden (es solo para pgAdmin, no para la BD en sí)
3. En el panel izquierdo, busquen **Servers** y expandan:
   - Si PostgreSQL ya está instalado, deberían ver algo como **PostgreSQL 16** o **PostgreSQL 17**
   - Si no aparece, hagan click derecho en **Servers** → **Register** → **Server...**
4. En la ventana que aparece:
   - **Name:** `Local` (o el nombre que quieran)
   - Pestaña **Connection**:
     - Host: `localhost`
     - Port: `5432`
     - Username: `postgres`
     - Password: la que pusieron al instalar PostgreSQL
   - Click en **Save**

Si todo sale bien, ven el servidor en el panel izquierdo y pueden expandirlo para ver **Databases**, **Tablespaces**, etc.

**¿Qué pasó ahí?** pgAdmin es un cliente gráfico que se conecta al motor de PostgreSQL que está corriendo en su máquina. El motor escucha en el puerto `5432` (igual que Flask escuchaba en el `5000`). El usuario `postgres` es el administrador por defecto, como el `root` del sistema operativo.

---

### 1B — Reto: Explorar la interfaz

1. Conéctense al servidor PostgreSQL desde pgAdmin
2. Expandan **Databases** — van a ver una BD llamada `postgres` (es la base de datos por defecto del sistema)
3. Expandan **Schemas** → **public** → **Tables** (vacío, no hay tablas todavía)
4. Click derecho en `postgres` → **Properties** — miren las propiedades generales
5. Respondan: ¿qué versión de PostgreSQL tienen instalada?

<details>
<summary><b>Solución (reto)</b></summary>

Para ver la versión:
- En pgAdmin: click derecho en el servidor → **Properties** → pestaña **General** → **Version**
- O también pueden abrir una Query Tool (`Tools` → `Query Tool`) y ejecutar:

```sql
SELECT version();
```

La respuesta debería ser algo como `PostgreSQL 16.x` o la versión que tengan instalada.

</details>

---

## 2. CREATE DATABASE — el archivero nuevo (15 min)

Antes de crear tablas, necesitamos una base de datos donde guardar todo. En nuestro caso, vamos a crear la BD del Mundial 2026.

**Analogía:** una base de datos es como el edificio del archivero. Las tablas son los cajones adentro. No puedes tener cajones sin un edificio donde ponerlos.

### 2A — Demo: Crear la base de datos del Mundial

Desde pgAdmin:

1. Click derecho en **Databases** → **Create** → **Database...**
2. En la ventana, llenen:
   - **Database:** `mundial_futbol`
   - **Owner:** `postgres`
   - Lo demás déjenlo por defecto
3. Click en **Save**

O por SQL (abran una Query Tool primero: seleccionen el servidor → Tools → Query Tool):

```sql
CREATE DATABASE mundial_futbol;
```

Así de simple. Una línea y ya tienen su base de datos lista.

¿Dónde está físicamente? PostgreSQL la crea en disco, en la carpeta de datos del motor. Ustedes no necesitan saber la ruta exacta — el motor se encarga de todo. Solo le dicen "crea esto" y él lo gestiona.

Ahora, para trabajar dentro de `mundial_futbol`, tienen que seleccionarla. En pgAdmin:
- Hagan click derecho en `mundial_futbol` → **Query Tool**
- O simplemente expandan `mundial_futbol` y van a ver `Schemas` → `public`

La próxima vez que abran pgAdmin, `mundial_futbol` va a seguir ahí. **Los datos persisten.** Apaguen la compu, reinícienla, y la BD sigue viva.

---

### 2B — Reto: Crear una base de datos de respaldo

**Profe dice:** "Imagínense que son los DBA (Database Administrator) de la FIFA. Necesitan tener una BD de prueba aparte para no romper los datos reales. Créenla."

1. Creen una base de datos llamada `mundial_futbol_pruebas`
2. Verifiquen que aparece en la lista de Databases
3. Bórrenla con:

```sql
DROP DATABASE mundial_futbol_pruebas;
```

4. ¿Qué pasó? La BD desapareció. Así de fácil como se crea, se borra. Por eso hay que tener muchísimo cuidado con `DROP`.

<details>
<summary><b>Solución (reto)</b></summary>

```sql
CREATE DATABASE mundial_futbol_pruebas;
-- Verifiquen que aparece en pgAdmin
DROP DATABASE mundial_futbol_pruebas;
-- Ya no está
```

> **Importante:** no pueden borrar una BD mientras están conectados a ella. Si están en la Query Tool de `mundial_futbol_pruebas`, cámbiense a `postgres` y ejecuten el `DROP` desde ahí.

</details>

---

## 3. DDL Parte I — CREATE TABLE (30 min)

DDL significa **Data Definition Language**. Son los comandos que DEFINEN la estructura de los datos, no los datos en sí. `CREATE`, `ALTER`, `DROP`, `TRUNCATE` son DDL. Cambian el **molde**, no la masa.

**Analogía:** DDL es como construir los moldes de una fábrica. `CREATE` hace el molde, `ALTER` le cambia una pieza, `TRUNCATE` vacía lo que salió del molde, `DROP` rompe el molde y lo tira. Después, DML (que veremos más adelante) es lo que mete y saca masa de los moldes.

### ¿Qué es una tabla?

Una tabla tiene:

| Concepto SQL | Analogía | Ejemplo en Mundial 2026 |
|-------------|----------|------------------------|
| **Tabla** | Un cajón del archivero | `equipos` |
| **Columna** | Un campo del formulario | `nombre`, `confederacion`, `grupo` |
| **Fila** | Un registro lleno | Argentina, CONMEBOL, A |
| **Tipo de dato** | Qué tipo de valor admite | `VARCHAR`, `INTEGER`, `BOOLEAN`, `DATE` |

### Tipos de datos en PostgreSQL (los que más van a usar este curso):

| Tipo | Para qué | Ejemplo |
|------|----------|---------|
| `SERIAL` | ID autoincremental | 1, 2, 3... |
| `INTEGER` | Números enteros | 1, 31, 42 |
| `VARCHAR(n)` | Texto corto con límite | "Argentina", "Delantero" |
| `CHAR(1)` | Texto fijo de 1 carácter | 'A', 'B', 'C', 'D' |
| `BOOLEAN` | Verdadero / Falso | TRUE, FALSE |
| `DATE` | Fecha | '2026-06-14' |
| `TIMESTAMP` | Fecha y hora | '2026-06-14 15:00:00' |

### 3A — Demo: Crear la tabla equipos (sin FK)

Vamos a crear nuestra primera tabla. Abran la Query Tool de `mundial_futbol` y ejecuten:

```sql
CREATE TABLE equipos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    confederacion VARCHAR(50) NOT NULL,
    grupo CHAR(1) NOT NULL,
    ranking_fifa INTEGER NOT NULL,
    clasificado BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT NOW()
);
```

**Desglosemos línea por línea:**

| Parte | Significado |
|-------|-------------|
| `CREATE TABLE equipos` | Crea una tabla llamada equipos |
| `id SERIAL` | Columna id, autoincremental (PostgreSQL asigna 1, 2, 3...) |
| `PRIMARY KEY` | Esta columna identifica ÚNICAMENTE cada fila. No se repite, no es NULL |
| `nombre VARCHAR(100) NOT NULL` | Texto de hasta 100 caracteres, obligatorio |
| `confederacion VARCHAR(50) NOT NULL` | Texto, obligatorio |
| `grupo CHAR(1) NOT NULL` | Un solo carácter ('A', 'B', 'C', 'D'), obligatorio |
| `ranking_fifa INTEGER NOT NULL` | Número entero, obligatorio |
| `clasificado BOOLEAN DEFAULT TRUE` | TRUE o FALSE; si no se especifica, toma TRUE |
| `fecha_creacion TIMESTAMP DEFAULT NOW()` | Fecha y hora; si no se especifica, toma la actual |

Después de ejecutar, expandan `mundial_futbol` → **Schemas** → **public** → **Tables** → hagan click derecho en `equipos` → **Properties**. Van a ver las columnas, tipos y restricciones. **Lo que crearon con SQL ahora vive en la estructura de la BD.**

---

### 3B — Reto: Crear la tabla jugadores (con FK a equipos)

**Profe dice:** "Ya tenemos equipos. Ahora necesitamos los jugadores. Cada jugador pertenece a un equipo. ¿Qué columnas debería tener? Piénsenlo."

Crear la tabla `jugadores` con:
- `id`: SERIAL PRIMARY KEY
- `nombre`: VARCHAR, NOT NULL
- `posicion`: VARCHAR, NOT NULL
- `dorsal`: INTEGER, NOT NULL
- `activo`: BOOLEAN, DEFAULT TRUE
- `fecha_nacimiento`: DATE
- `equipo_id`: INTEGER, NOT NULL, REFERENCES equipos(id)

<details>
<summary><b>Solución (reto)</b></summary>

```sql
CREATE TABLE jugadores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    posicion VARCHAR(50) NOT NULL,
    dorsal INTEGER NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    fecha_nacimiento DATE,
    equipo_id INTEGER NOT NULL REFERENCES equipos(id)
);
```

**¿Qué hace la última línea?** `equipo_id INTEGER NOT NULL REFERENCES equipos(id)` significa:
- Cada jugador TIENE que tener un equipo (NOT NULL)
- Ese equipo debe EXISTIR en la tabla equipos (REFERENCES)
- Si intentan insertar un jugador con equipo_id = 999 y no hay equipo con ese ID, PostgreSQL les PARA la operación con error

**¡Pruébenlo!** Expandan Tables en pgAdmin y deberían ver `jugadores` al lado de `equipos`.

</details>

---

### 3C — Demo: Crear la tabla partidos (con 2 FK a equipos)

Ahora la tabla más interesante: los partidos. Cada partido tiene un equipo LOCAL y un equipo VISITANTE. Ambas son FK a la misma tabla `equipos`.

```sql
CREATE TABLE partidos (
    id SERIAL PRIMARY KEY,
    goles_local INTEGER DEFAULT 0,
    goles_visitante INTEGER DEFAULT 0,
    fase VARCHAR(50) NOT NULL,
    fecha TIMESTAMP,
    local_id INTEGER NOT NULL REFERENCES equipos(id),
    visitante_id INTEGER NOT NULL REFERENCES equipos(id)
);
```

**Dato clave:** una tabla puede tener VARIAS FK apuntando a la MISMA tabla. `local_id` y `visitante_id` son dos conceptos distintos, cada uno apunta a `equipos(id)`. PostgreSQL no se confunde porque las columnas tienen nombres distintos.

---

### 3D — Mencionar: goles y posiciones_por_grupo

Existen dos tablas más en nuestro esquema. No las vamos a crear ahora (las crearemos en los ejercicios o más adelante), pero es importante que sepan que existen:

- **goles** — registra cada gol de cada partido. Tiene FK a `partidos` y a `jugadores`.
- **posiciones_por_grupo** — registra las estadísticas de cada equipo en la fase de grupos. Tiene FK a `equipos`.

Ambas también usan FK, así que el concepto es el mismo que ya vieron.

---

## 4. Relaciones y cardinalidad — el verdadero poder de las BD (30 min)

Esto es lo que diferencia una base de datos relacional de un montón de archivos de Excel. Las tablas se **relacionan** entre sí. Y en este curso solo vamos a ver un tipo de relación: **1:N (uno a muchos)**. Así se evitan confusiones y se construye una base sólida.

### 4A — Demo: La FK y la relación 1:N

**Profe dice:** "Tenemos equipos y tenemos jugadores. Un equipo tiene MUCHOS jugadores. Un jugador pertenece a UN equipo. ¿Cómo representamos eso?"

Eso es una relación **1:N**. La forma de representarla es con una **foreign key (FK)** en la tabla del lado "muchos" (`jugadores`) que apunta a la primary key de la tabla del lado "uno" (`equipos`).

La línea clave que ya vimos:

```sql
equipo_id INTEGER NOT NULL REFERENCES equipos(id)
```

Eso significa:
- `equipo_id` solo puede contener valores que existan en `equipos.id`
- Si intentan insertar un jugador con `equipo_id = 999` y no hay equipo con ID 999, PostgreSQL les REVIENTA con error
- Si intentan borrar un equipo que tiene jugadores, PostgreSQL se los impide (a menos que usen `ON DELETE CASCADE`, que veremos después)

**Analogía:** la FK es como tu DNI. No puedes decir que vives en una dirección que no existe. La FK obliga a que tus datos tengan sentido — es la base de la **integridad referencial**.

### Las 6 relaciones 1:N de nuestro modelo

En nuestra base de datos del Mundial, TODAS las relaciones son 1:N. No hay ni una sola 1:1 ni N:M. Vean:

| Relación | Tabla "1" | Tabla "N" | FK |
|----------|-----------|-----------|----|
| Equipo → Jugadores | equipos | jugadores | jugadores.equipo_id |
| Equipo → Partidos (local) | equipos | partidos | partidos.local_id |
| Equipo → Partidos (visitante) | equipos | partidos | partidos.visitante_id |
| Equipo → Posiciones | equipos | posiciones_por_grupo | posiciones_por_grupo.equipo_id |
| Partido → Goles | partidos | goles | goles.partido_id |
| Jugador → Goles | jugadores | goles | goles.jugador_id |

**Ojo:** la tabla `goles` tiene DOS FK (`partido_id` y `jugador_id`), pero cada una es una relación 1:N separada. Eso NO es una relación N:M. Es simplemente que la tabla "goles" está en el lado "muchos" de dos relaciones distintas al mismo tiempo.

### Cardinalidad — la notación que los DBAs usan en la vida real

Cuando se diseñan bases de datos, no se escribe SQL directo. Primero se dibuja un **diagrama entidad-relación (DER)**. Y en ese diagrama, la **cardinalidad** define cuántos registros de una tabla se relacionan con cuántos de la otra.

La cardinalidad tiene DOS componentes:

| Componente | Significado | Ejemplo (equipo → jugador) |
|------------|-------------|---------------------------|
| **Máxima** | La cantidad máxima de relaciones | Un equipo tiene **muchos** jugadores → N |
| **Mínima** | ¿Es obligatorio? | Un jugador **debe** tener equipo → 1 (obligatorio) |

En notación de diagramas, se representa con la **notación de pata de cuervo** (crow's foot):

```
 equipos ───────╼<│── jugadores
     1               N
(obligatorio)   (obligatorio)
```

Los símbolos más comunes en crow's foot:

| Símbolo | Significado |
|---------|-------------|
| `│` | Exactamente uno |
| `╽` o `○` | Cero o uno (opcional) |
| `╼<` o `╾<` | Muchos (N) |
| `╿<` o `○<` | Cero o muchos |

Aplicado a nuestro modelo del Mundial 2026:

```
 equipos ───────╼<│── jugadores
     1                N (obligatorio)

 equipos ───────╼<│── partidos (como local)
     1                N (obligatorio)

 equipos ───────╼<│── partidos (como visitante)
     1                N (obligatorio)

 equipos ───────╼<│── posiciones_por_grupo
     1                N (obligatorio)

 partidos ──────╼<│── goles
     1                N (obligatorio)

 jugadores ─────╼<│── goles
     1                N (obligatorio)
```

¿Por qué importa esto en la vida real?

- **1 del lado de equipo** → cada jugador pertenece a EXACTAMENTE UN equipo. No puedes tener un jugador sin equipo ni en dos equipos.
- **N del lado de jugador** → un equipo puede tener 0, 1, 20 o 50 jugadores.
- La **mínima** define si la FK puede ser `NULL` o no. En nuestro modelo, casi todas las FK son `NOT NULL` porque la relación es obligatoria.

**Regla práctica para diseñar:**

> Si del lado "muchos" la relación es obligatoria, pon `NOT NULL` en la FK. Si es opcional, déjala nullable. En nuestro Mundial, todas las relaciones son obligatorias, así que todas las FK llevan `NOT NULL`.

---

### 4B — Reto: Identificar las relaciones

**Profe dice:** "Les muestro el esquema completo de la BD. Ustedes me dicen qué tipo de relación hay entre cada par de tablas."

Observen este diagrama de todas las tablas:

```
                    ┌──────────────┐
                    │   equipos    │
                    └──────┬───────┘
                  ┌────────┼──────────────────┐
                  │        │                  │
                  ▼        ▼                  ▼
           ┌──────────┐ ┌──────────┐ ┌──────────────────┐
           │ jugadores │ │ partidos │ │ posiciones_por_  │
           │          │ │          │ │ grupo             │
           └──────────┘ └────┬─────┘ └──────────────────┘
                             │
                             ▼
                      ┌──────────┐
                      │  goles   │
                      └──────────┘
```

Respondan:
1. ¿Cuántas tablas tiene el esquema?
2. ¿Cuántas relaciones 1:N hay en total?
3. La tabla `goles` está relacionada con dos tablas. ¿Cuáles son? ¿Eso hace una N:M?
4. ¿Por qué `partidos` aparece dos veces conectada a `equipos`?

<details>
<summary><b>Solución (reto)</b></summary>

1. El esquema tiene **5 tablas**: equipos, jugadores, partidos, goles, posiciones_por_grupo.
2. Hay **6 relaciones 1:N** (las que listamos arriba).
3. `goles` está relacionada con `partidos` (cada gol pertenece a un partido) y con `jugadores` (cada gol lo marcó un jugador). Eso NO es N:M — son **dos relaciones 1:N separadas**. Un gol pertenece a UN partido y lo marca UN jugador. La tabla goles simplemente está en el lado "muchos" de dos relaciones distintas.
4. `partidos` aparece conectada dos veces a `equipos` porque un partido tiene un equipo local y un equipo visitante. Son dos FK distintas, cada una es una relación 1:N independiente.

</details>

---

## 5. DDL Parte II — ALTER, TRUNCATE, DROP (20 min)

Ya creamos tablas. Ahora veamos cómo **modificarlas, vaciarlas y eliminarlas**. Esto es la cirugía de base de datos: hay que saber hacerlo, pero con muchísimo cuidado.

### 5A — Demo: ALTER TABLE sobre equipos

**Profe dice:** "Se me fue la luz. Me olvidé de ponerle el país de origen a los equipos. ¿Borramos la tabla y la creamos de nuevo?"

NO. Para eso existe `ALTER TABLE`. Nunca borren una tabla para cambiarle algo. Jamás.

```sql
-- Agregar una columna
ALTER TABLE equipos ADD COLUMN pais_origen VARCHAR(100);

-- Agregar columna con valor por defecto
ALTER TABLE equipos ADD COLUMN ultima_actualizacion TIMESTAMP DEFAULT NOW();
```

#### Otros comandos ALTER útiles:

```sql
-- Renombrar una columna
ALTER TABLE equipos RENAME COLUMN pais_origen TO pais_fundacion;

-- Cambiar el tipo de dato
ALTER TABLE equipos ALTER COLUMN ranking_fifa TYPE NUMERIC(4);

-- Eliminar una columna (CUIDADO: esto borra datos)
ALTER TABLE equipos DROP COLUMN pais_fundacion;

-- Agregar una restricción
ALTER TABLE equipos ADD CONSTRAINT ranking_positivo CHECK (ranking_fifa > 0);
```

#### TRUNCATE vs DELETE vs DROP

```sql
-- TRUNCATE: vacía la tabla pero la mantiene (borra todas las filas)
TRUNCATE TABLE equipos;

-- DELETE: borra filas una por una (con WHERE, borra específicas)
DELETE FROM equipos WHERE ranking_fifa > 50;

-- DROP: borra la tabla entera (estructura y datos)
DROP TABLE equipos;
```

Diferencia clave entre los tres:

| Comando | ¿Borra datos? | ¿Borra estructura? | ¿Se puede deshacer? |
|---------|:------------:|:------------------:|:-------------------:|
| `DELETE` (DML) | Sí | No | Con `ROLLBACK` |
| `TRUNCATE` | Sí (mucho más rápido) | No | No en la práctica |
| `DROP` | Sí | Sí | No |

**TRUNCATE** es como sacar todas las hojas de un cajón sin romper el cajón. La tabla sigue existiendo con sus columnas, tipos y FKs, pero vacía. Es mucho más rápido que `DELETE` porque no registra cada fila borrada, solo limpia todo de golpe.

**DROP** es agarrar el cajón y tirarlo a la basura con todo adentro. La tabla desaparece para siempre. Sin backup, no hay vuelta atrás.

---

### 5B — Reto: Modificar el esquema de equipos

**Profe dice:** "La tabla equipos está muy básica. Necesitamos más control de datos. En vez de borrarla y crearla de nuevo (que sería una locura), usen ALTER."

1. Agreguen una columna `codigo_fifa` de tipo `VARCHAR(3)` (ej: "ARG", "PER", "BRA")
2. Agreguen una restricción `UNIQUE` a `codigo_fifa`
3. Agreguen una columna `debut_mundial` de tipo `INTEGER` (año del primer mundial del equipo)
4. Cambien el nombre de la columna `clasificado` a `clasificado_mundial` (usen `RENAME COLUMN`)
5. Verifiquen los cambios: click derecho en `equipos` → **Properties** → **Columns**

<details>
<summary><b>Solución (reto)</b></summary>

```sql
ALTER TABLE equipos ADD COLUMN codigo_fifa VARCHAR(3);
ALTER TABLE equipos ADD CONSTRAINT codigo_fifa_unico UNIQUE (codigo_fifa);
ALTER TABLE equipos ADD COLUMN debut_mundial INTEGER;
ALTER TABLE equipos RENAME COLUMN clasificado TO clasificado_mundial;
```

Ahora la tabla `equipos` tiene:
- `id`, `nombre`, `confederacion`, `grupo`, `ranking_fifa`, `clasificado_mundial`, `fecha_creacion`, `codigo_fifa`, `debut_mundial`

Sin borrar nada. Sin perder datos (aunque todavía no tengamos datos). Los cambios quedaron grabados en la estructura de la BD.

</details>

---

## 6. DML Parte I — SELECT, INSERT, GROUP BY y JOINs (55 min)

DML significa **Data Manipulation Language**. Ya tenemos los moldes (tablas), ahora vamos a meter y sacar datos. `INSERT` mete, `SELECT` saca.

### 6A — Demo: Insertar equipos

Primero, llenemos la tabla `equipos` con los 16 equipos del Mundial 2026. Cuatro grupos de cuatro equipos cada uno.

**Grupo A:**

```sql
INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa) VALUES
    ('Argentina', 'CONMEBOL', 'A', 1),
    ('Perú', 'CONMEBOL', 'A', 31),
    ('Chile', 'CONMEBOL', 'A', 42),
    ('Canadá', 'CONCACAF', 'A', 48);
```

**Grupo B:**

```sql
INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa) VALUES
    ('España', 'UEFA', 'B', 8),
    ('Países Bajos', 'UEFA', 'B', 6),
    ('Japón', 'AFC', 'B', 17),
    ('Marruecos', 'CAF', 'B', 13);
```

**Grupo C:**

```sql
INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa) VALUES
    ('Brasil', 'CONMEBOL', 'C', 5),
    ('Uruguay', 'CONMEBOL', 'C', 14),
    ('Croacia', 'UEFA', 'C', 9),
    ('Camerún', 'CAF', 'C', 38);
```

**Grupo D:**

```sql
INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa) VALUES
    ('Francia', 'UEFA', 'D', 2),
    ('Inglaterra', 'UEFA', 'D', 4),
    ('EE.UU.', 'CONCACAF', 'D', 11),
    ('Australia', 'AFC', 'D', 39);
```

**¿Notaron que NO pusimos `id`?** Porque es `SERIAL`. PostgreSQL lo asigna automáticamente: 1, 2, 3... en el orden que insertaron.

Ahora, consultas básicas para VER los datos:

```sql
-- Todas las columnas de todos los equipos
SELECT * FROM equipos;

-- Solo algunas columnas específicas
SELECT nombre, grupo, ranking_fifa FROM equipos;

-- Con filtro (WHERE)
SELECT * FROM equipos WHERE confederacion = 'CONMEBOL';
SELECT * FROM equipos WHERE grupo = 'A';
SELECT * FROM equipos WHERE ranking_fifa < 10;

-- Con operadores lógicos
SELECT * FROM equipos WHERE confederacion = 'UEFA' AND ranking_fifa < 10;
SELECT * FROM equipos WHERE grupo = 'A' OR grupo = 'B';

-- Con orden
SELECT * FROM equipos ORDER BY ranking_fifa;
SELECT * FROM equipos ORDER BY ranking_fifa DESC;

-- Con límite
SELECT * FROM equipos ORDER BY ranking_fifa ASC LIMIT 3;

-- Contar registros
SELECT COUNT(*) FROM equipos;
SELECT COUNT(*) FROM equipos WHERE confederacion = 'CONMEBOL';
```

**Lo que aprendieron:**
- `INSERT INTO ... VALUES` para crear registros
- `SELECT * FROM` para ver todo
- `WHERE` para filtrar
- `ORDER BY` para ordenar (ASC por defecto, DESC para invertir)
- `LIMIT` para limitar resultados
- `COUNT(*)` para contar

---

### 6B — Reto: Insertar jugadores y consultarlos

**Profe dice:** "Los equipos están listos. Ahora necesitamos los 48 jugadores, 3 por equipo. Van a insertarlos y después hacer consultas."

Primero, averigüen los IDs de los equipos ejecutando:

```sql
SELECT id, nombre FROM equipos ORDER BY id;
```

Ahora inserten los jugadores del Grupo A:

```sql
INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id) VALUES
    ('Lionel Messi', 'Delantero', 10, 1),
    ('Julián Álvarez', 'Delantero', 9, 1),
    ('Enzo Fernández', 'Mediocampista', 8, 1),
    ('Paolo Guerrero', 'Delantero', 9, 2),
    ('André Carrillo', 'Extremo', 18, 2),
    ('Renato Tapia', 'Mediocampista', 13, 2),
    ('Alexis Sánchez', 'Delantero', 7, 3),
    ('Arturo Vidal', 'Mediocampista', 8, 3),
    ('Gary Medel', 'Defensa', 17, 3),
    ('Alphonso Davies', 'Lateral', 19, 4),
    ('Jonathan David', 'Delantero', 9, 4),
    ('Tajon Buchanan', 'Extremo', 11, 4);
```

Ahora inserten los del Grupo B:

```sql
INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id) VALUES
    ('Lamine Yamal', 'Extremo', 19, 5),
    ('Pedri', 'Mediocampista', 8, 5),
    ('Rodri', 'Mediocampista', 16, 5),
    ('Memphis Depay', 'Delantero', 9, 6),
    ('Frenkie de Jong', 'Mediocampista', 21, 6),
    ('Virgil van Dijk', 'Defensa', 4, 6),
    ('Takefusa Kubo', 'Extremo', 14, 7),
    ('Wataru Endo', 'Mediocampista', 6, 7),
    ('Daichi Kamada', 'Mediocampista', 8, 7),
    ('Achraf Hakimi', 'Lateral', 2, 8),
    ('Youssef En-Nesyri', 'Delantero', 19, 8),
    ('Sofyan Amrabat', 'Mediocampista', 4, 8);
```

Grupo C:

```sql
INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id) VALUES
    ('Vinícius Jr.', 'Extremo', 7, 9),
    ('Neymar', 'Delantero', 10, 9),
    ('Marquinhos', 'Defensa', 5, 9),
    ('Federico Valverde', 'Mediocampista', 15, 10),
    ('Darwin Núñez', 'Delantero', 9, 10),
    ('Ronald Araújo', 'Defensa', 4, 10),
    ('Luka Modrić', 'Mediocampista', 10, 11),
    ('Mateo Kovačić', 'Mediocampista', 11, 11),
    ('Josip Gvardiol', 'Defensa', 24, 11),
    ('André-Frank Zambo Anguissa', 'Mediocampista', 8, 12),
    ('Vincent Aboubakar', 'Delantero', 10, 12),
    ('Karl Toko Ekambi', 'Delantero', 12, 12);
```

Grupo D:

```sql
INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id) VALUES
    ('Kylian Mbappé', 'Delantero', 10, 13),
    ('Antoine Griezmann', 'Delantero', 7, 13),
    ('Aurélien Tchouaméni', 'Mediocampista', 14, 13),
    ('Harry Kane', 'Delantero', 9, 14),
    ('Jude Bellingham', 'Mediocampista', 10, 14),
    ('Declan Rice', 'Mediocampista', 4, 14),
    ('Christian Pulisic', 'Extremo', 10, 15),
    ('Weston McKennie', 'Mediocampista', 8, 15),
    ('Tyler Adams', 'Mediocampista', 4, 15),
    ('Mathew Ryan', 'Portero', 1, 16),
    ('Ajdin Hrustic', 'Mediocampista', 23, 16),
    ('Harry Souttar', 'Defensa', 4, 16);
```

Ahora, consultas para verificar:

```sql
-- Todos los jugadores
SELECT * FROM jugadores;

-- Todos los jugadores de Argentina (equipo_id = 1)
SELECT * FROM jugadores WHERE equipo_id = 1;

-- Todos los delanteros
SELECT * FROM jugadores WHERE posicion = 'Delantero';

-- Ordenados por dorsal descendente
SELECT * FROM jugadores ORDER BY dorsal DESC;

-- Contar cuántos jugadores hay por equipo
SELECT equipo_id, COUNT(*) FROM jugadores GROUP BY equipo_id;
```

**¿Qué pasó con `GROUP BY`?** Agrupó los jugadores por `equipo_id` y contó cuántos hay en cada grupo. Cada equipo debería tener 3 jugadores.

<details>
<summary><b>Verificación rápida</b></summary>

```sql
-- Verificar que tenemos 48 jugadores
SELECT COUNT(*) FROM jugadores;  -- debe dar 48

-- Verificar distribución por equipo
SELECT e.nombre, COUNT(j.id) AS cantidad
FROM jugadores j
INNER JOIN equipos e ON j.equipo_id = e.id
GROUP BY e.nombre
ORDER BY e.nombre;
```

Cada equipo debe tener exactamente 3 jugadores.

</details>

---

### 6C — Demo: INSERT con FK en partidos y goles

#### Insertar partidos

Ahora vamos a insertar los 8 partidos de la primera fecha. Cada partido tiene un equipo local, un equipo visitante, un marcador y una fase.

```sql
INSERT INTO partidos (goles_local, goles_visitante, fase, local_id, visitante_id) VALUES
    (2, 0, 'Grupo A', 1, 2),   -- Argentina 2-0 Perú
    (1, 1, 'Grupo A', 3, 4),   -- Chile 1-1 Canadá
    (3, 0, 'Grupo B', 5, 7),   -- España 3-0 Japón
    (2, 1, 'Grupo B', 6, 8),   -- Países Bajos 2-1 Marruecos
    (4, 1, 'Grupo C', 9, 10),  -- Brasil 4-1 Uruguay
    (1, 0, 'Grupo C', 11, 12), -- Croacia 1-0 Camerún
    (1, 1, 'Grupo D', 13, 14), -- Francia 1-1 Inglaterra
    (2, 0, 'Grupo D', 15, 16); -- EE.UU. 2-0 Australia
```

**Nota:** no estamos especificando `fecha` para simplificar, pero podrían ponerla.

Verifiquen:

```sql
SELECT * FROM partidos;
```

#### Insertar goles

Son 20 goles distribuidos en los 8 partidos. Cada gol tiene un minuto, un jugador que lo marcó, y el partido donde ocurrió.

Primero averigüen los IDs de los partidos y jugadores:

```sql
SELECT id, goles_local, local_id, goles_visitante, visitante_id FROM partidos;
SELECT id, nombre, equipo_id FROM jugadores ORDER BY equipo_id;
```

Luego inserten los goles. Asumiendo que los partidos tienen IDs 1-8 en el orden de arriba, y los jugadores tienen los IDs que asignó el SERIAL:

```sql
-- Partido 1: Argentina 2-0 Perú
INSERT INTO goles (minuto, partido_id, jugador_id) VALUES
    (35, 1, 1),   -- Messi 35' (ARG)
    (68, 1, 2);   -- Álvarez 68' (ARG)

-- Partido 2: Chile 1-1 Canadá
INSERT INTO goles (minuto, partido_id, jugador_id) VALUES
    (42, 2, 7),   -- Sánchez 42' (CHI)
    (75, 2, 11);  -- David 75' (CAN)

-- Partido 3: España 3-0 Japón
INSERT INTO goles (minuto, partido_id, jugador_id) VALUES
    (28, 3, 13),  -- Yamal 28' (ESP)
    (54, 3, 15),  -- Rodri 54' (ESP)
    (77, 3, 14);  -- Pedri 77' (ESP)

-- Partido 4: Países Bajos 2-1 Marruecos
INSERT INTO goles (minuto, partido_id, jugador_id) VALUES
    (23, 4, 16),  -- Depay 23' (NED)
    (45, 4, 23),  -- En-Nesyri 45' (MAR)
    (81, 4, 18);  -- van Dijk 81' (NED)

-- Partido 5: Brasil 4-1 Uruguay
INSERT INTO goles (minuto, es_penal, partido_id, jugador_id) VALUES
    (12, FALSE, 5, 25),  -- Vinícius Jr. 12' (BRA)
    (30, FALSE, 5, 26),  -- Neymar 30' (BRA)
    (44, FALSE, 5, 29),  -- Núñez 44' (URU)
    (67, FALSE, 5, 25),  -- Vinícius Jr. 67' (BRA)
    (85, TRUE, 5, 26);   -- Neymar 85' penal (BRA)

-- Partido 6: Croacia 1-0 Camerún
INSERT INTO goles (minuto, partido_id, jugador_id) VALUES
    (73, 6, 31);  -- Modrić 73' (CRO)

-- Partido 7: Francia 1-1 Inglaterra
INSERT INTO goles (minuto, es_penal, partido_id, jugador_id) VALUES
    (18, FALSE, 7, 37),  -- Mbappé 18' (FRA)
    (55, TRUE, 7, 40);   -- Kane 55' penal (ENG)

-- Partido 8: EE.UU. 2-0 Australia
INSERT INTO goles (minuto, partido_id, jugador_id) VALUES
    (14, 8, 43),  -- Pulisic 14' (USA)
    (63, 8, 44);  -- McKennie 63' (USA)
```

Verifiquen:

```sql
SELECT * FROM goles;
SELECT COUNT(*) FROM goles;  -- debe dar 20
```

#### Insertar posiciones_por_grupo

Después de la primera fecha, las posiciones quedan así:

```sql
INSERT INTO posiciones_por_grupo (equipo_id, grupo, pj, pg, pe, pp, gf, gc, puntos) VALUES
    (1, 'A', 1, 1, 0, 0, 2, 0, 3),   -- Argentina
    (3, 'A', 1, 0, 1, 0, 1, 1, 1),   -- Chile
    (4, 'A', 1, 0, 1, 0, 1, 1, 1),   -- Canadá
    (2, 'A', 1, 0, 0, 1, 0, 2, 0),   -- Perú
    (5, 'B', 1, 1, 0, 0, 3, 0, 3),   -- España
    (6, 'B', 1, 1, 0, 0, 2, 1, 3),   -- Países Bajos
    (8, 'B', 1, 0, 0, 1, 1, 2, 0),   -- Marruecos
    (7, 'B', 1, 0, 0, 1, 0, 3, 0),   -- Japón
    (9, 'C', 1, 1, 0, 0, 4, 1, 3),   -- Brasil
    (11, 'C', 1, 1, 0, 0, 1, 0, 3),  -- Croacia
    (10, 'C', 1, 0, 0, 1, 1, 4, 0),  -- Uruguay
    (12, 'C', 1, 0, 0, 1, 0, 1, 0),  -- Camerún
    (15, 'D', 1, 1, 0, 0, 2, 0, 3),  -- EE.UU.
    (13, 'D', 1, 0, 1, 0, 1, 1, 1),  -- Francia
    (14, 'D', 1, 0, 1, 0, 1, 1, 1),  -- Inglaterra
    (16, 'D', 1, 0, 0, 1, 0, 2, 0);  -- Australia
```

---

### 6D — GROUP BY: cuando quieren saber cantidades, promedios y totales

A veces no les importa cada registro individual, sino el **resumen**. ¿Cuántos equipos hay por confederación? ¿Cuál es el ranking promedio de cada grupo? ¿Cuál es el equipo con mejor ranking?

Para eso existen las **funciones de agregación** combinadas con `GROUP BY`.

#### Funciones de agregación (las 5 que más van a usar)

| Función | ¿Qué hace? | Ejemplo en Mundial |
|---------|-----------|-------------------|
| `COUNT(columna)` | Cuenta cuántos registros | `COUNT(*)` → total de equipos |
| `SUM(columna)` | Suma los valores | `SUM(goles_local)` → goles totales como local |
| `AVG(columna)` | Promedio | `AVG(ranking_fifa)` → ranking promedio del grupo |
| `MAX(columna)` | Máximo | `MAX(ranking_fifa)` → el peor ranking del grupo |
| `MIN(columna)` | Mínimo | `MIN(ranking_fifa)` → el mejor ranking del grupo |

#### Demo: Estadísticas de equipos por grupo

```sql
-- ¿Cuántos equipos hay por cada confederación?
SELECT confederacion, COUNT(*) AS cantidad
FROM equipos
GROUP BY confederacion;

-- Ranking FIFA promedio por grupo
SELECT grupo, AVG(ranking_fifa) AS ranking_promedio
FROM equipos
GROUP BY grupo
ORDER BY ranking_promedio;

-- El mejor y peor ranking de cada grupo
SELECT grupo,
       MIN(ranking_fifa) AS mejor_ranking,
       MAX(ranking_fifa) AS peor_ranking
FROM equipos
GROUP BY grupo;

-- Resumen completo por grupo
SELECT grupo,
       COUNT(*) AS equipos,
       MIN(ranking_fifa) AS mejor,
       MAX(ranking_fifa) AS peor,
       AVG(ranking_fifa)::NUMERIC(5,1) AS promedio
FROM equipos
GROUP BY grupo
ORDER BY promedio;
```

**Concepto clave:** cuando usan `GROUP BY`, todas las columnas del `SELECT` DEBEN estar o en el `GROUP BY` o dentro de una función de agregación. Si ponen `SELECT nombre, COUNT(*)` sin agrupar por `nombre`, PostgreSQL les va a lanzar un error.

#### HAVING — el WHERE para datos agrupados

`WHERE` filtra fila por fila antes de agrupar. `HAVING` filtra DESPUÉS de agrupar. Diferencia clave:

```sql
-- ¿Qué confederaciones tienen más de 3 equipos?
SELECT confederacion, COUNT(*) AS cantidad
FROM equipos
GROUP BY confederacion
HAVING COUNT(*) > 3;
```

`WHERE` no puede usar funciones de agregación. `HAVING` sí. Esa es la regla de oro.

```sql
-- ¿Qué grupos tienen ranking promedio menor a 20?
SELECT grupo, AVG(ranking_fifa) AS prom_ranking
FROM equipos
GROUP BY grupo
HAVING AVG(ranking_fifa) < 20;
```

---

### 6E — Demo: JOINs — cuando los IDs se convierten en nombres

Hasta ahora tenemos un problema enorme. Miren esto:

```sql
SELECT equipo_id, COUNT(*) FROM jugadores GROUP BY equipo_id;
```

Devuelve `1`, `2`, `3`... pero **¿quién es el 1? ¿El 2?** En la vida real nadie quiere ver IDs. Quieren ver "Argentina", "Perú", "Brasil".

Para eso existen los **JOINs**. Combinan dos (o más) tablas a través de sus relaciones y les permiten usar columnas de todas ellas en una sola consulta.

**Analogía:** JOIN es como agarrar dos hojas de Excel y pegarlas una al lado de la otra. La hoja A tiene los jugadores, la hoja B tiene los equipos. El JOIN las une usando el `equipo_id` de A y el `id` de B.

#### INNER JOIN — el más usado

Devuelve SOLO los registros que tienen coincidencia en AMBAS tablas.

```sql
SELECT j.nombre, j.dorsal, j.posicion, e.nombre AS equipo
FROM jugadores j
INNER JOIN equipos e ON j.equipo_id = e.id;
```

**Desglose:**

| Parte | Significado |
|-------|-------------|
| `FROM jugadores j` | La tabla principal, con alias `j` |
| `INNER JOIN equipos e` | La tabla que quieren combinar, con alias `e` |
| `ON j.equipo_id = e.id` | La condición de unión: FK de jugadores = PK de equipos |
| `e.nombre AS equipo` | Están trayendo el nombre del equipo, no el ID |

**Resultado:**

```
nombre              | dorsal | posicion       | equipo
--------------------|--------|----------------|----------
Lionel Messi        | 10     | Delantero      | Argentina
Julián Álvarez      | 9      | Delantero      | Argentina
Enzo Fernández      | 8      | Mediocampista   | Argentina
Paolo Guerrero      | 9      | Delantero      | Perú
...
```

Ahora dice "Argentina", "Perú", "Brasil". Los IDs desaparecieron. **Ese es el poder del JOIN.**

Y se puede combinar con GROUP BY:

```sql
-- ¿Cuántos jugadores tiene cada equipo? ¡CON NOMBRE!
SELECT e.nombre AS equipo, COUNT(*) AS cantidad
FROM jugadores j
INNER JOIN equipos e ON j.equipo_id = e.id
GROUP BY e.nombre
ORDER BY cantidad DESC;
```

```sql
-- ¿Qué posiciones hay en cada equipo?
SELECT e.nombre AS equipo, j.posicion, COUNT(*) AS cantidad
FROM jugadores j
INNER JOIN equipos e ON j.equipo_id = e.id
GROUP BY e.nombre, j.posicion
ORDER BY e.nombre, cantidad DESC;
```

#### JOIN con partidos (dos FK a la misma tabla)

```sql
-- Partidos con nombre del local y del visitante
SELECT p.id AS partido,
       local.nombre AS equipo_local,
       p.goles_local,
       visitante.nombre AS equipo_visitante,
       p.goles_visitante,
       p.fase
FROM partidos p
INNER JOIN equipos local ON p.local_id = local.id
INNER JOIN equipos visitante ON p.visitante_id = visitante.id;
```

**Dato importante:** aquí hicimos dos JOINs a la MISMA tabla `equipos`. ¿Por qué funciona? Porque le dimos alias distintos: `local` y `visitante`. PostgreSQL los trata como dos "copias" independientes de la misma tabla. Esto se llama **self-join** y se usa muchísimo.

#### LEFT JOIN — cuando quieren TODO, incluso lo que no coincide

¿Y si un equipo no tuviera jugadores? Con `INNER JOIN` no aparecería. Con `LEFT JOIN` aparece igual, con valores NULL donde no hay match.

```sql
-- Todos los equipos, tengan o no jugadores
SELECT e.nombre AS equipo, COUNT(j.id) AS jugadores
FROM equipos e
LEFT JOIN jugadores j ON e.id = j.equipo_id
GROUP BY e.nombre
ORDER BY jugadores DESC;
```

Con `LEFT JOIN`, el equipo "fantasma" (si existiera) aparecería con 0 jugadores. Con `INNER JOIN` no aparecería.

**Regla práctica:**

| JOIN | ¿Qué devuelve? |
|------|----------------|
| `INNER JOIN` | Solo los que tienen match en ambas tablas |
| `LEFT JOIN` | TODOS los de la izquierda, tengan o no match a la derecha |

#### Múltiples JOINs — la consulta reina

Aquí juntamos 4 tablas: goles, jugadores, partidos y equipos:

```sql
-- Todos los goles del Mundial con: jugador, su equipo, y el partido
SELECT g.minuto,
       j.nombre AS jugador,
       eq.nombre AS equipo_del_jugador,
       g.es_penal,
       local.nombre AS equipo_local,
       goles_local,
       visitante.nombre AS equipo_visitante,
       goles_visitante
FROM goles g
INNER JOIN jugadores j ON g.jugador_id = j.id
INNER JOIN equipos eq ON j.equipo_id = eq.id
INNER JOIN partidos p ON g.partido_id = p.id
INNER JOIN equipos local ON p.local_id = local.id
INNER JOIN equipos visitante ON p.visitante_id = visitante.id
ORDER BY p.id, g.minuto;
```

Esta consulta usa **5 JOINs** (dos de ellos a la misma tabla) y combina 4 tablas distintas. Si entienden esto, ya pueden consultar casi cualquier cosa en una base de datos relacional.

---

### 6F — Reto: Consultas con JOINs y GROUP BY

**Profe dice:** "La FIFA quiere reportes. No quiere IDs, quiere nombres. Resuelvan estas consultas:"

1. Mostrar todos los jugadores con el nombre de su equipo (INNER JOIN)
2. Mostrar la cantidad de jugadores por equipo, **con el nombre del equipo** (GROUP BY + JOIN)
3. Mostrar todos los partidos con el nombre del local y del visitante, ordenados por fase
4. Mostrar la tabla de posiciones del Grupo A con los nombres de los equipos
5. **Desafío:** Mostrar los goleadores del torneo: nombre del jugador, su equipo, y cuántos goles marcó, ordenado de mayor a menor

<details>
<summary><b>Solución (reto)</b></summary>

```sql
-- 1. Jugadores con nombre de equipo
SELECT j.nombre, j.dorsal, j.posicion, e.nombre AS equipo
FROM jugadores j
INNER JOIN equipos e ON j.equipo_id = e.id;

-- 2. Cantidad de jugadores por equipo (con nombre)
SELECT e.nombre AS equipo, COUNT(*) AS cantidad
FROM jugadores j
INNER JOIN equipos e ON j.equipo_id = e.id
GROUP BY e.nombre
ORDER BY cantidad DESC;

-- 3. Partidos con nombres de local y visitante
SELECT p.id,
       local.nombre AS local,
       p.goles_local,
       visitante.nombre AS visitante,
       p.goles_visitante,
       p.fase
FROM partidos p
INNER JOIN equipos local ON p.local_id = local.id
INNER JOIN equipos visitante ON p.visitante_id = visitante.id
ORDER BY p.fase, p.id;

-- 4. Tabla de posiciones del Grupo A con nombres
SELECT e.nombre AS equipo,
       pp.pj, pp.pg, pp.pe, pp.pp,
       pp.gf, pp.gc, pp.puntos
FROM posiciones_por_grupo pp
INNER JOIN equipos e ON pp.equipo_id = e.id
WHERE pp.grupo = 'A'
ORDER BY pp.puntos DESC, pp.gf DESC;

-- 5. Goleadores del torneo
SELECT j.nombre AS jugador,
       e.nombre AS equipo,
       COUNT(*) AS goles
FROM goles g
INNER JOIN jugadores j ON g.jugador_id = j.id
INNER JOIN equipos e ON j.equipo_id = e.id
GROUP BY j.nombre, e.nombre
ORDER BY goles DESC;
```

**Resultado esperado de los goleadores:** Neymar (2), Vinícius Jr. (2). El resto de jugadores con 1 gol cada uno.

</details>

---

## 7. DML Parte II — UPDATE y DELETE (20 min)

Ya saben crear y leer. Ahora: **actualizar y eliminar**. Con muchísimo cuidado, porque un `UPDATE` sin `WHERE` o un `DELETE` sin `WHERE` les puede cargar toda la base de datos.

### 7A — Demo: Actualizar y eliminar registros

```sql
-- Actualizar los puntos de un equipo en la tabla de posiciones
UPDATE posiciones_por_grupo SET puntos = 3 WHERE equipo_id = 1;

-- Actualizar varios campos a la vez
UPDATE posiciones_por_grupo
SET pg = 1, pe = 0, pp = 0, gf = 2, gc = 0, puntos = 3
WHERE equipo_id = 1;

-- Desactivar a un jugador (no se borra, solo se marca como inactivo)
UPDATE jugadores SET activo = FALSE WHERE nombre = 'Arturo Vidal';

-- Eliminar un gol específico
DELETE FROM goles WHERE id = 3;
```

**¿Qué pasa si ejecutan UPDATE sin WHERE?**

```sql
UPDATE jugadores SET activo = FALSE;
```

Eso desactiva TODOS los jugadores. No hay "¿estás seguro?". PostgreSQL ejecuta y ya. Por eso:

> **REGLAS DE ORO:**
> 1. Siempre pongan `WHERE` en UPDATE y DELETE
> 2. Primero hagan un `SELECT` con el mismo WHERE para ver qué registros van a tocar
> 3. Después conviertan el SELECT en UPDATE o DELETE

**Ejemplo de cómo deberían trabajar SIEMPRE:**

```sql
-- PASO 1: Ver qué van a modificar
SELECT id, nombre, activo FROM jugadores WHERE nombre = 'Arturo Vidal';

-- PASO 2: Hacer el UPDATE (ahora están seguros)
UPDATE jugadores SET activo = FALSE WHERE id = 8;
```

Después de un UPDATE o DELETE, verifiquen:

```sql
SELECT * FROM jugadores WHERE activo = FALSE;
```

### Transacciones — el seguro de vida

PostgreSQL tiene **transacciones**. Pueden agrupar operaciones y, si algo sale mal, deshacer todo:

```sql
BEGIN;

UPDATE posiciones_por_grupo SET puntos = 99 WHERE equipo_id = 999;
-- Ups, ese equipo no existe. No afectó ninguna fila.

ROLLBACK;  -- Deshace todo desde el BEGIN
```

O:

```sql
BEGIN;

UPDATE posiciones_por_grupo
SET pg = 1, puntos = 3
WHERE equipo_id = 1;

COMMIT;  -- Confirma los cambios, ahora son permanentes
```

**Analogía:** `BEGIN` abre una burbuja en el tiempo. Todo lo que hagan adentro es invisible para los demás hasta que hagan `COMMIT`. Si algo sale mal, `ROLLBACK` vuelve todo al estado anterior como si nunca hubiera pasado.

---

### 7B — Reto: UPDATE y DELETE en acción

**Profe dice:** "Cosas que pasan en el Mundial: jugadores que se lesionan, goles que se anulan, puntos que cambian."

1. Desactivar al jugador `Gary Medel` (se lesionó). Usen `SELECT` primero para encontrar su ID.
2. Actualizar los puntos de Perú en `posiciones_por_grupo`: después del partido contra Argentina (que perdieron 2-0), Perú tiene 0 puntos, pp=1. Verifiquen que ya está así.
3. Eliminar un gol de la tabla `goles`. Por ejemplo, si se anuló un gol por VAR, bórrenlo. Primero averigüen su ID con un SELECT.
4. Usen una transacción para: desactivar a un jugador, actualizar su equipo, y hacer COMMIT. Si algo falla, ROLLBACK.

<details>
<summary><b>Solución (reto)</b></summary>

```sql
-- 1. Desactivar a Gary Medel
SELECT id, nombre, activo FROM jugadores WHERE nombre = 'Gary Medel';
UPDATE jugadores SET activo = FALSE WHERE id = 9;  -- asumiendo que su ID es 9
-- Verificar
SELECT * FROM jugadores WHERE id = 9;

-- 2. Verificar datos de Perú en posiciones
SELECT e.nombre, pp.* FROM posiciones_por_grupo pp
INNER JOIN equipos e ON pp.equipo_id = e.id
WHERE e.nombre = 'Perú';
-- Ya debería tener pp=1, puntos=0

-- 3. Eliminar un gol (ej: el gol anulado a En-Nesyri por offside)
-- Primero buscar el gol
SELECT g.id, g.minuto, j.nombre, e.nombre AS equipo
FROM goles g
INNER JOIN jugadores j ON g.jugador_id = j.id
INNER JOIN equipos e ON j.equipo_id = e.id
WHERE j.nombre = 'Youssef En-Nesyri';
DELETE FROM goles WHERE id = 7;  -- reemplazar con el ID real

-- 4. Transacción: lesión y actualización
BEGIN;
UPDATE jugadores SET activo = FALSE WHERE nombre = 'André Carrillo';
UPDATE posiciones_por_grupo SET pp = 1 WHERE equipo_id = 2;
SELECT * FROM jugadores WHERE nombre = 'André Carrillo';
SELECT * FROM posiciones_por_grupo WHERE equipo_id = 2;
COMMIT;  -- O ROLLBACK si algo salió mal
```

> **Recuerden:** siempre verifiquen primero con SELECT antes de UPDATE o DELETE. Esa práctica les va a salvar la base de datos más de una vez.

</details>

---

## 8. Ejercicios adicionales (15 min)

Han construido una base de datos completa del Mundial 2026 desde cero. Crearon tablas, las llenaron con datos, hicieron consultas avanzadas con JOINs y GROUP BY, actualizaron y eliminaron registros. Eso es muchísimo.

Para seguir practicando, revisen el archivo `ejercicios.md` que está en esta misma carpeta. Ahí encuentran más consultas progresivas para seguir afianzando lo aprendido hoy.

Algunas ideas de lo que pueden practicar:

- Consultas con `BETWEEN`, `IN`, `LIKE`
- Subconsultas (SELECT dentro de SELECT)
- `ORDER BY` con múltiples criterios
- `DISTINCT` para valores únicos
- `COALESCE` para valores nulos
- Más variantes de JOINs

---

## Resumen de conceptos

| Tema | Demo | Reto | Conceptos clave |
|------|:----:|:----:|-----------------|
| 0. ¿Qué es una BD? | — | — | persistencia, tablas, SQL, concurrencia, relaciones |
| 1. Conexión PostgreSQL | ✅ | ✅ | pgAdmin, servidor, Query Tool, puerto 5432 |
| 2. CREATE DATABASE | ✅ | ✅ | `CREATE DATABASE`, `DROP DATABASE`, persistencia |
| 3. DDL I: CREATE TABLE | ✅ | ✅ | `SERIAL`, `PRIMARY KEY`, `VARCHAR`, `CHAR`, `NOT NULL`, `REFERENCES`, `DEFAULT` |
| 4. Relaciones + Cardinalidad | ✅ | ✅ | 1:N, `REFERENCES`, FK, crow's foot, mínima/máxima, integridad referencial |
| 5. DDL II: ALTER, TRUNCATE, DROP | ✅ | ✅ | `ALTER TABLE ADD/DROP/RENAME COLUMN`, `TRUNCATE`, `DROP`, CHECK |
| 6. DML I: SELECT, INSERT, GROUP BY, JOINs | ✅ | ✅ | `INSERT`, `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `COUNT`, `GROUP BY`, `HAVING`, `AVG`, `SUM`, `MIN`, `MAX`, `INNER JOIN`, `LEFT JOIN`, self-join, alias |
| 7. DML II: UPDATE y DELETE | ✅ | ✅ | `UPDATE`, `DELETE`, `WHERE`, `BEGIN/COMMIT/ROLLBACK`, transacciones |
| 8. Ejercicios extra | — | ✅ | Consultas progresivas en `ejercicios.md` |

---

## Diagrama final de la base de datos

```
                    ┌──────────────────────────────────┐
                    │            equipos                │
                    │  id SERIAL PK                     │
                    │  nombre VARCHAR NOT NULL           │
                    │  confederacion VARCHAR NOT NULL    │
                    │  grupo CHAR(1) NOT NULL            │
                    │  ranking_fifa INTEGER NOT NULL     │
                    │  clasificado BOOLEAN DEFAULT TRUE  │
                    │  fecha_creacion TIMESTAMP          │
                    └───────┬──────────────┬────────────┘
                            │              │
              ┌─────────────┼──────────────┼──────────────────────┐
              │             │              │                      │
              ▼             ▼              ▼                      ▼
  ┌───────────────────┐ ┌────────────┐ ┌────────────┐  ┌──────────────────────┐
  │     jugadores      │ │  partidos  │ │  partidos  │  │ posiciones_por_grupo  │
  │  id SERIAL PK      │ │ (local)   │ │ (visitante)│  │  id SERIAL PK         │
  │  nombre VARCHAR    │ │            │ │            │  │  equipo_id INTEGER FK │
  │  posicion VARCHAR  │ │ local_id   │ │ visitante_ │  │  grupo CHAR(1)        │
  │  dorsal INTEGER    │ │ INTEGER FK │ │ id INTEGER │  │  pj, pg, pe, pp       │
  │  activo BOOLEAN    │ │            │ │ FK         │  │  gf, gc, puntos       │
  │  equipo_id INTEGER │ └──────┬─────┘ └────────────┘  └──────────────────────┘
  └───────────────────┘        │
                               │
                               ▼
                    ┌─────────────────────┐
                    │       goles          │
                    │  id SERIAL PK        │
                    │  minuto INTEGER      │
                    │  es_penal BOOLEAN    │
                    │  partido_id INT FK ──┼── (1:N desde partidos)
                    │  jugador_id INT FK ──┼── (1:N desde jugadores)
                    └─────────────────────┘
```

### Leyenda de relaciones (todas 1:N):

| Desde | Hacia | A través de |
|-------|-------|-------------|
| equipos (1) | jugadores (N) | jugadores.equipo_id |
| equipos (1) | partidos como local (N) | partidos.local_id |
| equipos (1) | partidos como visitante (N) | partidos.visitante_id |
| equipos (1) | posiciones_por_grupo (N) | posiciones_por_grupo.equipo_id |
| partidos (1) | goles (N) | goles.partido_id |
| jugadores (1) | goles (N) | goles.jugador_id |

**Total: 6 tablas, 6 relaciones 1:N. Ni una 1:1, ni una N:M. Simple, limpio, poderoso.**

---

<sub>Créditos de imágenes: logos de PostgreSQL, Python y pgAdmin servidos desde Wikimedia Commons. Los logos son marcas de sus respectivos dueños y se usan solo con fines educativos de identificación. Datos del Mundial 2026 simulados con fines pedagógicos.</sub>
