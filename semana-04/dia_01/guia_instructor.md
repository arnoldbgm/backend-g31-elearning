# 🎓 Guía del Instructor — Día 1 (Semana 4): Bases de datos con PostgreSQL

> **Archivo base:** `guia_mejorada.md` — esta guía contiene **tu speech completo**, timing, y notas pedagógicas para dar la clase.
>
> **Tema:** Mundial 2026 — 16 selecciones, 48 jugadores, 8 partidos, 20 goles.

---

## 📋 Resumen de la sesión

| Bloque | Tema | Duración estimada | Formato |
|--------|------|------------------:|---------|
| 0 | ¿Qué es una base de datos? | 15 min | Exposición + analogía |
| 1 | Conexión a PostgreSQL | 10 min | Demo guiada |
| 2 | CREATE DATABASE | 15 min | Demo + Reto |
| 3 | DDL I: CREATE TABLE | 30 min | Demo + Reto |
| 4 | Relaciones + Cardinalidad | 30 min | Exposición + Demo + Reto |
| 5 | DDL II: ALTER, TRUNCATE, DROP | 20 min | Demo + Reto |
| 6 | DML I: SELECT, INSERT, GROUP BY, JOINs | 55 min | Demo + Reto |
| 7 | DML II: UPDATE y DELETE | 20 min | Demo + Reto |
| 8 | Ejercicios prácticos | 15 min | Trabajo individual |
| | **Total** | **~3h 10min** | |

**Receso sugerido:** después del bloque 3 (CREATE TABLE).

---

## 🎯 Antes de empezar

### Preparación del profe (día anterior)

- [ ] Verificar que PostgreSQL 16+ esté instalado y el servicio esté corriendo
- [ ] Verificar que pgAdmin esté instalado y accesible
- [ ] Tener una Query Tool abierta con `mundial_2026` seleccionada para proyectar
- [ ] Tener las sentencias SQL de cada Demo listas en un archivo separado (o copiadas para pegar rápido)
- [ ] Probar la conexión: `localhost:5432` con usuario `postgres`
- [ ] Preparar el esquema final impreso o en PDF para mostrarlo al final — 5 tablas, solo relaciones 1:N

### Qué esperar de los alumnos

- **Ya saben:** Flask, CRUD, listas, diccionarios, API REST
- **No saben:** qué es SQL, qué es una base de datos relacional, qué es PostgreSQL
- **Van a confundir:** DELETE (DML) con DROP (DDL), TRUNCATE con DELETE, VARCHAR(n) con INTEGER, `=` con `LIKE`, WHERE con HAVING, INNER JOIN con LEFT JOIN, alias de tablas
- **Confusiones nuevas de este esquema:**
  - `partidos` tiene `local_id` y `visitante_id` apuntando ambas a `equipos(id)` — los alumnos van a pensar que es N:M, pero son dos relaciones 1:N separadas
  - `goles` tiene dos FKs (`partido_id` y `jugador_id`) — van a preguntar "¿esto es N:M?"; hay que explicar que son dos relaciones 1:N independientes
  - Self-join con alias: van a mezclar `local.nombre` con `visitante.nombre` y olvidar los alias
- **Se van a trabar:** en la activación de pgAdmin (contraseña olvidada), en FKs múltiples (error al insertar sin la selección existente), en UPDATE sin WHERE, en self-joins
- **Errores comunes:**
  - `ERROR: relation "jugadores" does not exist` → no seleccionaron la BD correcta
  - `ERROR: insert or update on table "jugadores" violates foreign key constraint` → el `equipo_id` no existe en `equipos`
  - `ERROR: insert or update on table "partidos" violates foreign key constraint` → `local_id` o `visitante_id` no existen en `equipos`
  - `ERROR: insert or update on table "goles" violates foreign key constraint` → `partido_id` o `jugador_id` no existen
  - Olvidar el `;` al final de cada sentencia (PostgreSQL no ejecuta hasta el `;`)
  - En JOIN: poner `ON` con `=` en vez de verificar que FK = PK
  - En self-join: escribir `ON partidos.local_id = equipos.id` sin alias, y PostgreSQL no sabe a qué `equipos` referirse
  - En alias de self-join: `FROM partidos INNER JOIN equipos AS local ON partidos.local_id = local.id` mezclando alias con nombres completos

---

## 🗣️ SPEECH COMPLETO — BLOQUE POR BLOQUE

---

### BLOQUE 0 — ¿Qué es una base de datos? (15 min)

**Propósito:** Que entiendan POR QUÉ existe una BD antes de escribir SQL. Esto evita que memoricen comandos sin sentido.

**Profe dice:**

"Miren, hasta la semana pasada ustedes guardaban datos en listas de diccionarios. Y funcionaba para aprender. Pero en el mundo real, cuando trabajan con 100,000 usuarios, con datos que no pueden perderse, con 20 personas accediendo al mismo tiempo a la misma información... una lista de Python no alcanza.

Una base de datos es básicamente un programa que se encarga de guardar datos por vos. Pero no es un archivo de texto ni un Excel. Es un programa que te garantiza:

1. **Persistencia:** los datos sobreviven a un reinicio. Apagá la compu, prendela al otro día, los datos siguen ahí.
2. **Velocidad:** podés buscar entre millones de registros en milisegundos.
3. **Concurrencia:** miles de personas pueden leer y escribir al mismo tiempo sin pisarse.
4. **Integridad:** el motor evita que guardes datos inconsistentes.

Todo esto sin que vos tengas que escribir ni una línea de lógica de persistencia. Solo decís 'guardá esto' y el motor se encarga.

Hoy arrancamos con PostgreSQL, que es el motor de base de datos open source más potente del mundo. Es el mismo que usa Instagram, Spotify, Reddit. No estamos aprendiendo un juguete.

Y para que no sea aburrido, todo lo vamos a hacer con datos del **Mundial 2026**. 16 selecciones, 48 jugadores, 8 partidos, goles, posiciones... todo lo que ves en un mundial de verdad."

**Nota pedagógica:** hacé la analogía del archivero vs la hoja suelta. La hoja suelta es la lista de Python. El archivero es la BD. Preguntales: "¿Qué pasa si se cae un café en la hoja suelta? ¿Y si varios quieren guardar al mismo tiempo?"

**Pregunta para la clase:** "¿Alguien usó Excel para guardar datos de verdad? ¿Qué problemas tuvieron?" (esto conecta con su experiencia real)

---

### BLOQUE 1 — Conexión a PostgreSQL (10 min)

**Propósito:** Que todos estén en el mismo punto de partida. Nada de "en mi compu no funciona".

**Profe dice:**

"Abran pgAdmin. Lo encuentran en el menú de inicio. La primera vez les va a pedir una contraseña maestra — es solo para pgAdmin, no para la BD. Pongan la que quieran, pero acuérdense.

Después, en el panel izquierdo, busquen **Servers**. Si ven algo como **PostgreSQL 16**, ya está conectado. Si no, tienen que registrar el servidor: click derecho en **Servers** → **Register** → **Server...**. Ahí ponen:
- Name: `Local`
- Connection: host `localhost`, port `5432`, user `postgres`, password la de instalación.

Si alguien no puede conectar, el problema más común es que el servicio de PostgreSQL no está corriendo. En Windows: busquen **Services**, encuentren `postgresql-x64-16`, y asegúrense que esté en 'Running'. Si no, click derecho → Start."

**Nota pedagógica:** caminá por los puestos y ayudá a los que estén trabados. Este bloque es corto pero crítico — si alguien no puede conectar, no va a poder hacer nada del resto de la clase.

**Error común:** "Profe, no recuerdo mi contraseña de postgres". Solución: si es Windows, pueden cambiar la contraseña desde `psql` con `ALTER USER postgres PASSWORD 'nueva';`. Pero mejor tenerla anotada.

---

### BLOQUE 2 — CREATE DATABASE (15 min)

**Propósito:** Que creen su primer objeto en la BD y entiendan la diferencia entre BD, esquema y tabla.

**Profe dice:**

"Vamos a crear nuestra base de datos del Mundial 2026. En pgAdmin: click derecho en **Databases** → **Create** → **Database...**. La llamamos `mundial_2026`. Owner: postgres. Y listo.

Pero también quiero que aprendan a hacerlo por SQL. Porque en el trabajo no siempre vas a tener una interfaz gráfica — a veces solo tenés una terminal. Abran una **Query Tool**: seleccionen el servidor → Tools → Query Tool. Escriban:

```sql
CREATE DATABASE mundial_2026;
```

Ejecuten con F5 o el botón de play. Y ya está. Ahora `mundial_2026` aparece en la lista de databases.

**Pregunta:** ¿dónde está guardada físicamente esta BD? En la carpeta de datos de PostgreSQL. No necesitan saber la ruta exacta, pero sepan que está en disco. Si apagan la compu y la vuelven a prender, la BD sigue ahí."

**Demo importante:** mostrá que al expandir `mundial_2026` aparece **Schemas** → **public** → **Tables** (vacío). Explicá que `public` es el esquema por defecto. Una BD puede tener muchos esquemas (como pisos de un edificio), pero nosotros usamos `public`.

**Nota pedagógica:** no profundices en esquemas. Solo mencioná que existen y que trabajamos en `public`. Si alguien pregunta, decí "es como una carpeta para organizar tablas. Más adelante lo vemos."

---

### BLOQUE 3 — DDL I: CREATE TABLE (30 min)

**Propósito:** Que entiendan los tipos de datos, restricciones y cómo se define una tabla. Vamos a crear las 5 tablas del esquema en orden de dependencia.

**Profe dice:**

"Ya tenemos la BD vacía. Ahora necesitamos crear las tablas. Esto se hace con `CREATE TABLE`. Es DDL — **Data Definition Language**. No estamos metiendo datos todavía; estamos definiendo el molde.

Vamos a crear 5 tablas. El orden importa: no puedo crear una tabla que referencia a otra que todavía no existe. Así que el orden es:

1. `equipos` — no depende de nadie
2. `jugadores` — depende de equipos
3. `partidos` — depende de equipos (dos veces)
4. `goles` — depende de partidos y jugadores
5. `posiciones_por_grupo` — depende de equipos

Arranquemos con `equipos`:

```sql
CREATE TABLE equipos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    confederacion VARCHAR(50),
    grupo CHAR(1),
    ranking_fifa INTEGER,
    clasificado BOOLEAN DEFAULT TRUE,
    fecha_creacion DATE DEFAULT CURRENT_DATE
);
```

Expliquemos cada línea:
- `id SERIAL PRIMARY KEY` → id se genera solo (1, 2, 3...) y es único para cada fila
- `nombre VARCHAR(100) NOT NULL UNIQUE` → texto de hasta 100 caracteres, obligatorio, no se repite
- `confederacion VARCHAR(50)` → CONMEBOL, UEFA, etc. Texto opcional
- `grupo CHAR(1)` → 'A', 'B', 'C', 'D'. Exactamente 1 carácter
- `ranking_fifa INTEGER` → número entero, el ranking de FIFA
- `clasificado BOOLEAN DEFAULT TRUE` → verdadero/falso, si no ponés nada es TRUE
- `fecha_creacion DATE DEFAULT CURRENT_DATE` → fecha, si no ponés nada es la fecha actual

Ejecuten y después expandan **Tables** en pgAdmin. Ahí está `equipos`. Hagan click derecho → **Properties** y vean las columnas. Eso que ven es la estructura que definieron con SQL."

**Analogía:** "Pensá en un formulario de papel. CREATE TABLE es el diseño del formulario (cuántos campos, qué tipo de datos va en cada uno, cuáles son obligatorios). INSERT es llenar el formulario con datos. Tenés que tener el formulario diseñado ANTES de llenarlo."

**Reto (5 min):** "Ahora creen ustedes la tabla `jugadores`. Necesita: id, nombre VARCHAR(100), posicion VARCHAR(50), dorsal INTEGER, activo BOOLEAN con DEFAULT TRUE, fecha_nacimiento DATE, y equipo_id INTEGER. Sin FK todavía — solo las columnas. La solución en 2 minutos."

```sql
CREATE TABLE jugadores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    posicion VARCHAR(50),
    dorsal INTEGER,
    activo BOOLEAN DEFAULT TRUE,
    fecha_nacimiento DATE,
    equipo_id INTEGER
);
```

"Bien. Ahora sigo yo con `partidos`. Acá prestá atención porque es la tabla más tricky del esquema:

```sql
CREATE TABLE partidos (
    id SERIAL PRIMARY KEY,
    goles_local INTEGER DEFAULT 0,
    goles_visitante INTEGER DEFAULT 0,
    fase VARCHAR(50),
    fecha DATE,
    local_id INTEGER,
    visitante_id INTEGER
);
```

Fíjense: `local_id` y `visitante_id` son dos columnas que apuntan a `equipos`. Pero eso NO es una relación N:M. Son **dos relaciones 1:N separadas**: un equipo puede ser local en muchos partidos (1:N) Y un equipo puede ser visitante en muchos partidos (otro 1:N)."

**Reto (5 min):** "Creen la tabla `goles`. Necesita: id, minuto INTEGER, es_penal BOOLEAN con DEFAULT FALSE, partido_id INTEGER, jugador_id INTEGER. No se olviden de las columnas."

```sql
CREATE TABLE goles (
    id SERIAL PRIMARY KEY,
    minuto INTEGER,
    es_penal BOOLEAN DEFAULT FALSE,
    partido_id INTEGER,
    jugador_id INTEGER
);
```

**Demo final:** creamos la quinta tabla:

```sql
CREATE TABLE posiciones_por_grupo (
    id SERIAL PRIMARY KEY,
    equipo_id INTEGER,
    grupo CHAR(1),
    pj INTEGER DEFAULT 0,
    pg INTEGER DEFAULT 0,
    pe INTEGER DEFAULT 0,
    pp INTEGER DEFAULT 0,
    gf INTEGER DEFAULT 0,
    gc INTEGER DEFAULT 0,
    puntos INTEGER DEFAULT 0
);
```

"Esta tabla es clásica de un mundial: guarda los puntos, partidos jugados, goles a favor y en contra de cada equipo. La vamos a usar después para UPDATE."

**Nota pedagógica:** no te apures en este bloque. CREATE TABLE es la base de todo. Si se apuran, después no entienden las FKs. Son 5 tablas, tómate tu tiempo.

---

### BLOQUE 4 — Relaciones entre tablas + Cardinalidad (30 min)

**Propósito:** Que entiendan el concepto de foreign key, los tipos de relaciones, y la notación de cardinalidad. En este esquema solo hay 1:N, ni una sola 1:1 ni N:M.

**Profe dice:**

"Ahora viene lo que realmente hace poderosa a una base de datos relacional: las relaciones entre tablas.

Acá va la verdad más importante del día: en nuestro esquema del Mundial 2026 **solo hay relaciones 1:N (uno a muchos)**. No hay 1:1, no hay N:M. Solo UNO A MUCHOS en todas direcciones.

Veamos cada una:

1. **Equipos → Jugadores:** un equipo tiene MUCHOS jugadores. Un jugador pertenece a UN equipo.
2. **Equipos → Partidos (por local):** un equipo juega MUCHOS partidos como local. Cada partido tiene UN local.
3. **Equipos → Partidos (por visitante):** un equipo juega MUCHOS partidos como visitante. Cada partido tiene UN visitante.
4. **Equipos → Posiciones_por_grupo:** un equipo tiene UNA fila de posiciones. Cada fila pertenece a UN equipo.
5. **Partidos → Goles:** un partido tiene MUCHOS goles. Cada gol pertenece a UN partido.
6. **Jugadores → Goles:** un jugador puede meter MUCHOS goles. Cada gol es metido por UN jugador.

¿Cómo se representa esto en SQL? Con una **foreign key**. Es una columna en la tabla 'muchos' que apunta a la primary key de la tabla 'uno'.

Las tablas que crearon ya tienen las columnas, pero sin la FK. Vamos a agregarlas con ALTER TABLE. Primero, la más fácil:

```sql
ALTER TABLE jugadores ADD FOREIGN KEY (equipo_id) REFERENCES equipos(id);
```

Ahora `partidos` tiene dos FKs:

```sql
ALTER TABLE partidos ADD FOREIGN KEY (local_id) REFERENCES equipos(id);
ALTER TABLE partidos ADD FOREIGN KEY (visitante_id) REFERENCES equipos(id);
```

'Atención: son dos restricciones separadas. Cada una se verifica por separado. PostgreSQL no va a dejar que inserten un partido con un `local_id` que no exista en `equipos`, ni con un `visitante_id` que no exista.'

```sql
ALTER TABLE goles ADD FOREIGN KEY (partido_id) REFERENCES partidos(id);
ALTER TABLE goles ADD FOREIGN KEY (jugador_id) REFERENCES jugadores(id);
```

Y por último:

```sql
ALTER TABLE posiciones_por_grupo ADD FOREIGN KEY (equipo_id) REFERENCES equipos(id);
```

**Probemos la protección:**

```sql
INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id)
VALUES ('Lionel Messi', 'Delantero', 10, 1);
```

Esto funciona si existe un equipo con ID 1.

Ahora probemos esto:

```sql
INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id)
VALUES ('Jugador Fantasma', 'Inexistente', 99, 999);
```

**Va a fallar.** PostgreSQL dice: 'ERROR: insert or update on table "jugadores" violates foreign key constraint'. No existe equipo con ID 999. El motor nos protege de datos huérfanos."

**Explicación de la cardinalidad:**

"Además de las relaciones, existe el concepto de **cardinalidad**. Cardinalidad son DOS números:
1. **Máxima:** cuántos registros de una tabla se relacionan con la otra (1 o N)
2. **Mínima:** si la relación es obligatoria (1) u opcional (0)

Ejemplo: equipo → jugador.
- Máxima: un equipo tiene MUCHOS jugadores. Un jugador pertenece a UN equipo.
- Mínima: un equipo PUEDE no tener jugadores recién creado (opcional). Un jugador DEBE tener equipo (obligatorio... aunque en nuestro esquema la columna permite NULL por ahora).

Esto se dibuja con la **notación de pata de cuervo** (crow's foot):

```
equipos ──╼<│── jugadores
   1              N
 opcional     obligatorio
```

**Pregunta clave:** ¿y `goles`? Tiene dos FKs. ¿Eso es N:M? **No.** Es un partido que tiene muchos goles (1:N) Y un jugador que mete muchos goles (otro 1:N). Son dos relaciones independientes que convergen en la misma tabla. No confundas 'dos FKs' con 'N:M'."

**Actividad rápida:** dibujá en la pizarra el diagrama completo de las 5 tablas con sus relaciones. Pediles que digan qué tipo de relación hay entre cada par.

---

### BLOQUE 5 — DDL II: ALTER, TRUNCATE, DROP (20 min)

**Propósito:** Que aprendan a modificar la estructura sin romper todo.

**Profe dice:**

"¿Qué pasa si creamos una tabla y después nos olvidamos de una columna? No la borramos y la creamos de nuevo. Usamos `ALTER TABLE`.

**Demo:**

```sql
ALTER TABLE equipos ADD COLUMN entrenador VARCHAR(100);
```

"Acabamos de agregar la columna `entrenador` a `equipos`. La tabla se actualiza sin perder datos.

También podemos modificar tipos:

```sql
ALTER TABLE equipos ALTER COLUMN grupo TYPE VARCHAR(2);
```

Ahora grupo acepta hasta 2 caracteres (por si algún día usamos 'AA').

Y podemos renombrar:

```sql
ALTER TABLE equipos RENAME COLUMN clasificado TO clasificado_mundial;
```

Otros comandos importantes:

```sql
-- Truncate (vacía la tabla, no la borra)
TRUNCATE TABLE jugadores;

-- Drop (borra la tabla con todo y estructura)
DROP TABLE jugadores;
```

La diferencia clave:
- `DELETE` (lo vemos después): borra filas, se puede deshacer con ROLLBACK
- `TRUNCATE`: borra todo rápido, no se puede deshacer fácil (pero es más rápido que DELETE sin WHERE)
- `DROP`: borra la tabla entera, estructura incluida. Adiós para siempre."

**Analogía:** "CREATE es construir el molde. ALTER es modificarle una pieza. TRUNCATE es vaciar lo que salió del molde. DROP es romper el molde a martillazos."

**Reto (5 min):** "Agreguen la columna `tecnico` a `equipos`. Después renombren `fecha_creacion` a `fecha_registro`. Y después borren la columna `entrenador` que agregué. Todo con ALTER."

```sql
ALTER TABLE equipos ADD COLUMN tecnico VARCHAR(100);
ALTER TABLE equipos RENAME COLUMN fecha_creacion TO fecha_registro;
ALTER TABLE equipos DROP COLUMN entrenador;
```

**Nota pedagógica:** mostrá que `DROP COLUMN` es permanente. No hay confirmación. Si alguien pregunta "¿y si me arrepiento?", decí "no existe Ctrl+Z en SQL. Por eso siempre verificamos antes de ejecutar."

---

### BLOQUE 6 — DML I: SELECT, INSERT, GROUP BY, JOINs (55 min)

**Propósito:** Que hagan sus primeras consultas, aprendan a insertar datos, agrupar y combinar tablas con JOIN. Es el bloque más largo y el más importante.

#### Parte 1: INSERT (15 min)

**Profe dice:**

"Llegó el momento de meter datos de verdad. Ya tenemos las tablas con sus FKs. Primero insertemos los equipos. Acuerdense del orden: primero `equipos` (no depende de nadie), después `jugadores` y `partidos`, después `goles`.

**Demo: insertar equipos**

```sql
INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa)
VALUES ('Argentina', 'CONMEBOL', 'A', 1);

INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa)
VALUES ('Brasil', 'CONMEBOL', 'A', 5);

INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa)
VALUES ('España', 'UEFA', 'B', 8);

INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa)
VALUES ('Japón', 'AFC', 'B', 18);
```

Insertamos 4 equipos de ejemplo. Después consultamos:

```sql
SELECT * FROM equipos;
```

Ese `*` significa 'todas las columnas'. Siempre arrancamos con `SELECT *` para ver qué hay.

**Ahora insertamos jugadores (con FK a equipos):**

```sql
INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id)
VALUES ('Lionel Messi', 'Delantero', 10, 1);

INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id)
VALUES ('Julián Álvarez', 'Delantero', 9, 1);

INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id)
VALUES ('Enzo Fernández', 'Mediocampista', 8, 1);

INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id)
VALUES ('Vinícius Jr', 'Delantero', 7, 2);

INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id)
VALUES ('Rodrygo', 'Delantero', 10, 2);

INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id)
VALUES ('Pedri', 'Mediocampista', 8, 3);

INSERT INTO jugadores (nombre, posicion, dorsal, equipo_id)
VALUES ('Takefusa Kubo', 'Mediocampista', 14, 4);
```

**Reto (5 min):** "Ahora inserten ustedes 1 equipo más y 3 jugadores para ese equipo. Usen equipos de CONMEBOL o UEFA, el que quieran."

**Ahora insertamos partidos (con dos FKs):**

```sql
INSERT INTO partidos (local_id, visitante_id, goles_local, goles_visitante, fase)
VALUES (1, 2, 2, 1, 'Grupo A');

INSERT INTO partidos (local_id, visitante_id, goles_local, goles_visitante, fase)
VALUES (3, 4, 3, 0, 'Grupo B');
```

"Fíjense: `local_id = 1` (Argentina) y `visitante_id = 2` (Brasil). PostgreSQL verifica que AMBOS IDs existan en `equipos`."

**Y ahora goles (con dos FKs):**

```sql
INSERT INTO goles (minuto, es_penal, partido_id, jugador_id)
VALUES (10, FALSE, 1, 1);  -- Messi al minuto 10, partido 1

INSERT INTO goles (minuto, es_penal, partido_id, jugador_id)
VALUES (35, FALSE, 1, 3);  -- Enzo Fernández al 35, partido 1

INSERT INTO goles (minuto, es_penal, partido_id, jugador_id)
VALUES (50, TRUE, 1, 4);   -- Vinícius Jr de penal al 50, partido 1

INSERT INTO goles (minuto, es_penal, partido_id, jugador_id)
VALUES (15, FALSE, 2, 6);  -- Pedri al 15, partido 2

INSERT INTO goles (minuto, es_penal, partido_id, jugador_id)
VALUES (42, FALSE, 2, 6);  -- Pedri otra vez al 42, partido 2

INSERT INTO goles (minuto, es_penal, partido_id, jugador_id)
VALUES (78, FALSE, 2, 7);  -- Kubo al 78, partido 2
```

**Nota pedagógica:** mostrá que Pedri aparece dos veces en `goles`. Un jugador puede tener muchos goles — eso es exactamente la relación 1:N entre jugadores y goles.

#### Parte 2: SELECT con WHERE, ORDER BY (10 min)

**Profe dice:**

"Ahora que tenemos datos, empecemos a preguntarle a la base. Esto es lo que más vas a hacer como dev: SELECT.

```sql
-- Todos los equipos
SELECT * FROM equipos;

-- Solo algunos campos
SELECT nombre, ranking_fifa FROM equipos;

-- Filtrar por grupo
SELECT * FROM equipos WHERE grupo = 'A';

-- Filtrar por confederación
SELECT * FROM equipos WHERE confederacion = 'CONMEBOL';

-- Ordenar
SELECT * FROM equipos ORDER BY ranking_fifa;

-- Orden descendente
SELECT * FROM equipos ORDER BY ranking_fifa DESC;

-- Contar
SELECT COUNT(*) FROM equipos;

-- Jugadores de un equipo específico
SELECT * FROM jugadores WHERE equipo_id = 1;
```

Cada una de estas es una consulta diferente. SQL es así: describís lo que querés, no cómo obtenerlo. El motor decide la mejor forma de ejecutarlo."

**Analogía:** "SELECT es como preguntarle al archivero. 'Dame todos los equipos' es `SELECT *`. 'Dame solo los del grupo A' es `WHERE grupo = 'A'`. 'Ordenalos por ranking' es `ORDER BY`. No le decís cómo tiene que buscar — solo le decís qué querés."

**Reto (5 min):** "Consulten los jugadores que tengan dorsal = 10. Después consulten los partidos de la fase 'Grupo A'. Ordenen los equipos por ranking_fifa de menor a mayor (el mejor ranking primero)."

#### Parte 3: GROUP BY y funciones de agregación (10 min)

**Profe dice:**

"Hasta ahora usamos SELECT para ver filas individuales. Pero muchas veces no te importa cada fila — te importa el resumen. '¿Cuántos jugadores tiene cada equipo?' '¿Cuántos goles se metieron en total?'

Para eso existen las **funciones de agregación**:
- `COUNT(*)` → cuenta filas
- `SUM(columna)` → suma valores
- `AVG(columna)` → promedio
- `MAX(columna)` / `MIN(columna)` → máximo/mínimo

Y se combinan con `GROUP BY` para agrupar.

**Demo:**

```sql
-- Cuántos jugadores tiene cada equipo
SELECT equipo_id, COUNT(*)
FROM jugadores
GROUP BY equipo_id;

-- Goles totales por jugador
SELECT jugador_id, COUNT(*) AS goles
FROM goles
GROUP BY jugador_id;

-- Promedio de goles por partido
SELECT AVG(goles_local + goles_visitante) AS promedio_goles
FROM partidos;
```

**Regla de oro:** cualquier columna en el SELECT que NO esté dentro de una función de agregación, tiene que estar en el GROUP BY.

Después tenemos `HAVING`, que es como un WHERE pero para datos agrupados. WHERE filtra filas ANTES de agrupar. HAVING filtra DESPUÉS.

```sql
SELECT jugador_id, COUNT(*) AS goles
FROM goles
GROUP BY jugador_id
HAVING COUNT(*) > 1;
```

Esto solo muestra los jugadores que metieron más de 1 gol. No se puede hacer con WHERE porque `COUNT(*)` no existe hasta después de agrupar."

**Nota pedagógica:** la confusión más común es poner condiciones del WHERE en el HAVING y viceversa. Aclaralo con un ejemplo concreto. Mostrá que `WHERE partido_id = 1` filtra antes y es más eficiente que `HAVING partido_id = 1`.

#### Parte 4: JOINs (15 min)

**Profe dice:**

"Fíjense algo. Cuando hacemos:

```sql
SELECT equipo_id, COUNT(*) FROM jugadores GROUP BY equipo_id;
```

¿Qué vemos? 1, 2, 3, 4. Pero... ¿quién es el 1? ¿Argentina? ¿Brasil? No sabemos. Eso no sirve para un reporte de verdad.

Acá es donde entra el **JOIN**. JOIN combina dos tablas a través de una relación, y te deja usar columnas de ambas en el mismo SELECT.

El más común es **INNER JOIN**:

```sql
SELECT j.nombre, e.nombre AS equipo
FROM jugadores j
INNER JOIN equipos e ON j.equipo_id = e.id;
```

Fíjense: `j.equipo_id` (FK) = `e.id` (PK). Eso es el JOIN. Y ahora, en vez de ver un número, vemos 'Argentina', 'Brasil', etc.

Y lo mejor: podés combinar JOIN con GROUP BY:

```sql
SELECT e.nombre, COUNT(*) AS cantidad_jugadores
FROM jugadores j
INNER JOIN equipos e ON j.equipo_id = e.id
GROUP BY e.nombre;
```

**Ahora el reporte tiene sentido.** Le mostrás eso a un jefe y entiende.

**El self-join — el que siempre complica:**

'Nuestro caso más interesante: la tabla `partidos` se relaciona consigo misma a través de `equipos`. Para traer el nombre del local y del visitante en una misma consulta, necesitamos **dos JOINs a la misma tabla con alias distintos**.' 

```sql
SELECT 
    p.id,
    local.nombre AS equipo_local,
    visitante.nombre AS equipo_visitante,
    p.goles_local,
    p.goles_visitante,
    p.fase
FROM partidos p
INNER JOIN equipos AS local ON p.local_id = local.id
INNER JOIN equipos AS visitante ON p.visitante_id = visitante.id;
```

'Acá pasa algo clave: estamos usando la tabla `equipos` DOS VECES. La primera vez con alias `local`, la segunda con alias `visitante`. Es como si fueran dos copias de la misma tabla. Si no usáramos alias, PostgreSQL no sabría a qué `equipos` referirse.'

**LEFT JOIN — el otro que necesitás:**

"¿Qué pasa si tenés jugadores sin equipo? Con INNER JOIN desaparecen. Si querés que aparezcan igual (aunque sea con NULL), usás LEFT JOIN.

**Regla práctica:** INNER JOIN = 'solo los que existen en ambas'. LEFT JOIN = 'todos los de la izquierda, existan o no a la derecha'."

**Y ahora el JOIN de 3 tablas — el plato fuerte:**

```sql
SELECT 
    j.nombre AS jugador,
    e.nombre AS equipo,
    p.id AS partido,
    g.minuto
FROM goles g
INNER JOIN jugadores j ON g.jugador_id = j.id
INNER JOIN equipos e ON j.equipo_id = e.id
INNER JOIN partidos p ON g.partido_id = p.id;
```

"Acá estamos combinando 4 tablas para responder: '¿quién metió gol, para qué equipo, en qué partido y en qué minuto?' Eso es la potencia de un BD relacional."

**Reto (5 min):** "Hagan un JOIN entre `posiciones_por_grupo` y `equipos` para mostrar el nombre del equipo junto a sus puntos. Después hagan el self-join de `partidos` con `equipos`."

**Posible confusión:** los alias de tabla. Explicá que `j`, `e`, `p`, `g` son alias para no tener que escribir el nombre completo cada vez. Sin alias tendrías que escribir `jugadores.nombre`, `equipos.nombre`, etc.

---

### BLOQUE 7 — DML II: UPDATE y DELETE (20 min)

**Propósito:** Que aprendan a modificar y eliminar registros, siempre con cuidado.

**Profe dice:**

"Último bloque de comandos. Ya sabemos crear tablas, insertar datos, consultarlos. Ahora: actualizar y eliminar.

**UPDATE — el caso perfecto: posiciones_por_grupo**

'La tabla `posiciones_por_grupo` está hecha para UPDATE. Primero insertemos los datos iniciales:'

```sql
INSERT INTO posiciones_por_grupo (equipo_id, grupo, pj, pg, pe, pp, gf, gc, puntos)
VALUES (1, 'A', 1, 1, 0, 0, 2, 1, 3);

INSERT INTO posiciones_por_grupo (equipo_id, grupo, pj, pg, pe, pp, gf, gc, puntos)
VALUES (2, 'A', 1, 0, 0, 1, 1, 2, 0);

INSERT INTO posiciones_por_grupo (equipo_id, grupo, pj, pg, pe, pp, gf, gc, puntos)
VALUES (3, 'B', 1, 1, 0, 0, 3, 0, 3);

INSERT INTO posiciones_por_grupo (equipo_id, grupo, pj, pg, pe, pp, gf, gc, puntos)
VALUES (4, 'B', 1, 0, 0, 1, 0, 3, 0);
```

'Ahora actualicemos: después del partido Argentina 2-1 Brasil, actualizamos los puntos:'

```sql
UPDATE posiciones_por_grupo 
SET pj = 2, pg = 2, puntos = 6
WHERE equipo_id = 1;
```

'Argentina jugó 2 partidos, ganó 2, tiene 6 puntos.'

**UPDATE más simple:**

```sql
UPDATE jugadores SET activo = FALSE WHERE nombre = 'Enzo Fernández';
```

"Fíjense que el `WHERE` es IDÉNTICO al de SELECT. De hecho, la regla de oro es: primero hacé SELECT con el WHERE, verificá, después convertilo en UPDATE.

**DELETE:**

```sql
DELETE FROM goles WHERE minuto < 20;
```

Esto borra los goles que fueron antes del minuto 20.

**¿Qué pasa si olvidás el WHERE?**

```sql
UPDATE posiciones_por_grupo SET puntos = 0;  -- TODOS los equipos tienen 0 puntos ahora
DELETE FROM goles;  -- TODOS los goles se borraron
```

No hay confirmación. No hay '¿estás seguro?'. PostgreSQL hace exactamente lo que le decís. Por eso el WHERE no es opcional — es obligatorio mentalmente.

**Para protegerse de esto, existen las transacciones:**

```sql
BEGIN;
DELETE FROM goles;
-- Ups, me equivoqué
ROLLBACK;  -- Todo vuelve a como estaba antes del BEGIN
```

`BEGIN` abre una burbuja donde todo es reversible hasta que hacés `COMMIT`."

**Analogía:** "BEGIN es como decir 'modo seguro'. Trabajás dentro de una burbuja. Si algo sale mal, ROLLBACK revienta la burbuja y todo vuelve a como estaba. Si todo está bien, COMMIT hace los cambios permanentes."

**Reto (10 min):** "Actualicen los puntos de Brasil después de su próxima victoria. Después desactiven a un jugador (activo = FALSE). Después inserten un gol y elimínenlo. Todo con WHERE y verificando primero con SELECT."

---

### BLOQUE 8 — Ejercicios prácticos (15 min)

**Propósito:** Consolidar lo aprendido resolviendo consultas por su cuenta.

**Profe dice:**

"Les voy a dar 15 minutos para que resuelvan ejercicios del `ejercicios.md`. Cada uno a su ritmo. Los niveles 1-3 son los básicos que todos deberían poder hacer. Si terminan, pasen al nivel 4 y 5.

**Parejas recomendadas:** los que van más lento con los que van más rápido. Así aprenden entre ustedes.

**Recuerden:** la solución está en `<details>`. **NO miren la solución primero.** Cada ejercicio incluye un resultado esperado. Si tu consulta devuelve lo mismo que dice el resultado esperado, la resolviste bien. Si no, revisá dónde está la diferencia.

Después de resolver, comparen SU resultado con el esperado. Esa comparación les va a enseñar más que cualquier explicación."

**Nota pedagógica:** caminá por los puestos. Los errores más comunes en este punto son: olvidar el `;`, escribir mal los nombres de columnas, y confundir `=` con `LIKE`. Corregí preguntando en vez de diciendo — "¿qué creés que está mal acá?"

---

## 🧩 Posibles desvíos y cómo volver

| Situación | Qué hacer |
|-----------|-----------|
| Alguien no tiene PostgreSQL instalado | Que trabaje con un compañero. Al final de la clase, ayudalo a instalarlo. |
| Se olvidaron la contraseña de postgres | En Windows: abrir psql como admin, `ALTER USER postgres PASSWORD 'nueva';` |
| Error de FK al insertar en jugadores | Pedirles que ejecuten `SELECT * FROM equipos` para ver los IDs reales. |
| Error de FK al insertar en partidos | Verificar que TANTO `local_id` como `visitante_id` existan en `equipos`. |
| Error de FK al insertar en goles | Verificar que `partido_id` exista en `partidos` Y `jugador_id` en `jugadores`. Dos FKs = dos verificaciones. |
| Confunden self-join con N:M | Explicar con dibujo: un equipo puede ser local en muchos partidos (1:N) y visitante en muchos partidos (otro 1:N). No hay relación entre locales y visitantes. |
| La Query Tool no ejecuta | Probablemente falta el `;` al final. Preguntales primero antes de decirles. |
| Borraron datos sin querer | Si estaban en una transacción, ROLLBACK. Si no, recrear los INSERT. Recordarles que la próxima usen BEGIN. |
| Se adelantaron e hicieron todo rápido | Tener el reto final (el de self-join con 3 tablas) para que los rápidos tengan algo que hacer. |

---

## ✅ Checklist de cierre

Antes de terminar la clase, verificá que cada alumno pueda:

- [ ] Abrir pgAdmin y conectarse al servidor
- [ ] Crear una base de datos (`mundial_2026`)
- [ ] Crear una tabla con PRIMARY KEY, NOT NULL, UNIQUE, DEFAULT
- [ ] Crear las 5 tablas del esquema: equipos, jugadores, partidos, goles, posiciones_por_grupo
- [ ] Agregar FOREIGN KEY con ALTER TABLE
- [ ] Explicar por qué `goles` tiene dos FKs pero no es N:M (son dos relaciones 1:N independientes)
- [ ] Insertar registros con INSERT respetando el orden de dependencia
- [ ] Consultar con SELECT, WHERE, ORDER BY
- [ ] Usar GROUP BY con COUNT, SUM, AVG
- [ ] Usar HAVING para filtrar datos agrupados
- [ ] Hacer INNER JOIN entre dos tablas
- [ ] Hacer self-join con `partidos` y `equipos` usando alias
- [ ] Hacer JOIN de 3 tablas (goles + jugadores + partidos)
- [ ] Actualizar con UPDATE y WHERE (ej: posiciones_por_grupo)
- [ ] Eliminar con DELETE y WHERE
- [ ] Explicar la diferencia entre DELETE, TRUNCATE y DROP
- [ ] Resolver al menos 5 ejercicios de `ejercicios.md`

Si alguien no puede hacer todo esto, dale ejercicios extras o decile que se queda 10 min después de clase.
