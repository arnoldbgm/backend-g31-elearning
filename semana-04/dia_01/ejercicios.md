# ⚽ Ejercicios SQL — Mundial 2026

> Todos los ejercicios usan PostgreSQL con el esquema `mundial2026`. Cada ejercicio está diseñado para practicar un concepto específico de SQL, desde lo más básico hasta consultas combinadas con múltiples tablas.
>
> Todos los resultados esperados están basados en los datos de prueba incluidos. Si los datos cambian, los resultados pueden variar, pero las consultas deben seguir siendo correctas.

---

## Esquema de base de datos

Ejecutá este script completo en tu herramienta SQL favorita (pgAdmin, DBeaver, psql) antes de empezar.

```sql
-- =============================================
-- ESQUEMA — Mundial 2026
-- =============================================

CREATE TABLE equipos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    confederacion VARCHAR NOT NULL,
    grupo CHAR(1) NOT NULL,
    ranking_fifa INTEGER NOT NULL,
    clasificado BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT NOW()
);

CREATE TABLE jugadores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    posicion VARCHAR NOT NULL,
    dorsal INTEGER NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    fecha_nacimiento DATE,
    equipo_id INTEGER NOT NULL REFERENCES equipos(id)
);

CREATE TABLE partidos (
    id SERIAL PRIMARY KEY,
    goles_local INTEGER DEFAULT 0,
    goles_visitante INTEGER DEFAULT 0,
    fase VARCHAR NOT NULL,
    fecha TIMESTAMP,
    local_id INTEGER NOT NULL REFERENCES equipos(id),
    visitante_id INTEGER NOT NULL REFERENCES equipos(id)
);

CREATE TABLE goles (
    id SERIAL PRIMARY KEY,
    minuto INTEGER DEFAULT 0,
    es_penal BOOLEAN DEFAULT FALSE,
    partido_id INTEGER NOT NULL REFERENCES partidos(id),
    jugador_id INTEGER NOT NULL REFERENCES jugadores(id)
);

CREATE TABLE posiciones_por_grupo (
    id SERIAL PRIMARY KEY,
    equipo_id INTEGER NOT NULL REFERENCES equipos(id),
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

---

## Datos de prueba

```sql
-- =============================================
-- INSERTS — Mundial 2026
-- =============================================

INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa, clasificado) VALUES
    ('Argentina', 'CONMEBOL', 'A', 1, TRUE),
    ('Perú', 'CONMEBOL', 'A', 31, TRUE),
    ('Chile', 'CONMEBOL', 'A', 42, TRUE),
    ('Canadá', 'CONCACAF', 'A', 48, TRUE),
    ('España', 'UEFA', 'B', 8, TRUE),
    ('Países Bajos', 'UEFA', 'B', 6, TRUE),
    ('Japón', 'AFC', 'B', 17, TRUE),
    ('Marruecos', 'CAF', 'B', 13, TRUE),
    ('Brasil', 'CONMEBOL', 'C', 5, TRUE),
    ('Uruguay', 'CONMEBOL', 'C', 14, TRUE),
    ('Croacia', 'UEFA', 'C', 9, TRUE),
    ('Camerún', 'CAF', 'C', 38, TRUE),
    ('Francia', 'UEFA', 'D', 2, TRUE),
    ('Inglaterra', 'UEFA', 'D', 4, TRUE),
    ('EE.UU.', 'CONCACAF', 'D', 11, TRUE),
    ('Australia', 'AFC', 'D', 39, TRUE);

INSERT INTO jugadores (nombre, posicion, dorsal, activo, equipo_id) VALUES
    ('Lionel Messi', 'Delantero', 10, TRUE, 1),
    ('Emiliano Martínez', 'Arquero', 23, TRUE, 1),
    ('Enzo Fernández', 'Mediocampista', 8, TRUE, 1),
    ('Paolo Guerrero', 'Delantero', 9, TRUE, 2),
    ('Renato Tapia', 'Mediocampista', 13, TRUE, 2),
    ('Pedro Gallese', 'Arquero', 1, TRUE, 2),
    ('Alexis Sánchez', 'Delantero', 7, TRUE, 3),
    ('Arturo Vidal', 'Mediocampista', 8, TRUE, 3),
    ('Gary Medel', 'Defensa', 17, TRUE, 3),
    ('Alphonso Davies', 'Mediocampista', 10, TRUE, 4),
    ('Jonathan David', 'Delantero', 20, TRUE, 4),
    ('Milan Borjan', 'Arquero', 1, TRUE, 4),
    ('Lamine Yamal', 'Delantero', 19, TRUE, 5),
    ('Pedri', 'Mediocampista', 8, TRUE, 5),
    ('Unai Simón', 'Arquero', 23, TRUE, 5),
    ('Virgil van Dijk', 'Defensa', 4, TRUE, 6),
    ('Frenkie de Jong', 'Mediocampista', 21, TRUE, 6),
    ('Memphis Depay', 'Delantero', 10, TRUE, 6),
    ('Takefusa Kubo', 'Mediocampista', 7, TRUE, 7),
    ('Wataru Endō', 'Mediocampista', 6, TRUE, 7),
    ('Ayase Ueda', 'Delantero', 11, TRUE, 7),
    ('Achraf Hakimi', 'Defensa', 2, TRUE, 8),
    ('Hakim Ziyech', 'Mediocampista', 7, TRUE, 8),
    ('Yassine Bono', 'Arquero', 1, TRUE, 8),
    ('Vinícius Jr.', 'Delantero', 7, TRUE, 9),
    ('Rodrygo', 'Delantero', 10, TRUE, 9),
    ('Alisson', 'Arquero', 1, TRUE, 9),
    ('Federico Valverde', 'Mediocampista', 15, TRUE, 10),
    ('Darwin Núñez', 'Delantero', 9, TRUE, 10),
    ('José María Giménez', 'Defensa', 3, TRUE, 10),
    ('Luka Modrić', 'Mediocampista', 10, TRUE, 11),
    ('Ivan Perišić', 'Delantero', 14, TRUE, 11),
    ('Dominik Livaković', 'Arquero', 1, TRUE, 11),
    ('Vincent Aboubakar', 'Delantero', 10, TRUE, 12),
    ('André Onana', 'Arquero', 1, TRUE, 12),
    ('Bryan Mbeumo', 'Mediocampista', 3, TRUE, 12),
    ('Kylian Mbappé', 'Delantero', 10, TRUE, 13),
    ('Antoine Griezmann', 'Mediocampista', 7, TRUE, 13),
    ('Mike Maignan', 'Arquero', 16, TRUE, 13),
    ('Harry Kane', 'Delantero', 9, TRUE, 14),
    ('Jude Bellingham', 'Mediocampista', 10, TRUE, 14),
    ('Jordan Pickford', 'Arquero', 1, TRUE, 14),
    ('Christian Pulisic', 'Mediocampista', 10, TRUE, 15),
    ('Weston McKennie', 'Mediocampista', 8, TRUE, 15),
    ('Matt Turner', 'Arquero', 1, TRUE, 15),
    ('Mathew Ryan', 'Arquero', 1, TRUE, 16),
    ('Craig Goodwin', 'Mediocampista', 23, TRUE, 16),
    ('Mitchell Duke', 'Delantero', 15, TRUE, 16);

INSERT INTO partidos (goles_local, goles_visitante, fase, local_id, visitante_id) VALUES
    (2, 0, 'Fase de Grupos', 1, 2),
    (1, 1, 'Fase de Grupos', 3, 4),
    (3, 0, 'Fase de Grupos', 5, 7),
    (2, 1, 'Fase de Grupos', 6, 8),
    (4, 1, 'Fase de Grupos', 9, 10),
    (1, 0, 'Fase de Grupos', 11, 12),
    (1, 1, 'Fase de Grupos', 13, 14),
    (2, 0, 'Fase de Grupos', 15, 16);

INSERT INTO goles (minuto, es_penal, partido_id, jugador_id) VALUES
    (12, FALSE, 1, 1),
    (67, FALSE, 1, 1),
    (34, FALSE, 2, 7),
    (78, FALSE, 2, 11),
    (8, FALSE, 3, 13),
    (45, FALSE, 3, 14),
    (72, FALSE, 3, 13),
    (23, FALSE, 4, 18),
    (55, FALSE, 4, 23),
    (81, TRUE, 4, 18),
    (15, FALSE, 5, 25),
    (33, FALSE, 5, 26),
    (41, FALSE, 5, 25),
    (62, FALSE, 5, 29),
    (75, FALSE, 5, 26),
    (55, FALSE, 6, 31),
    (23, FALSE, 7, 37),
    (67, FALSE, 7, 40),
    (41, FALSE, 8, 43),
    (73, FALSE, 8, 44);

INSERT INTO posiciones_por_grupo (equipo_id, grupo, pj, pg, pe, pp, gf, gc, puntos) VALUES
    (1, 'A', 1, 1, 0, 0, 2, 0, 3),
    (2, 'A', 1, 0, 0, 1, 0, 2, 0),
    (3, 'A', 1, 0, 1, 0, 1, 1, 1),
    (4, 'A', 1, 0, 1, 0, 1, 1, 1),
    (5, 'B', 1, 1, 0, 0, 3, 0, 3),
    (6, 'B', 1, 1, 0, 0, 2, 1, 3),
    (7, 'B', 1, 0, 0, 1, 0, 3, 0),
    (8, 'B', 1, 0, 0, 1, 1, 2, 0),
    (9, 'C', 1, 1, 0, 0, 4, 1, 3),
    (10, 'C', 1, 0, 0, 1, 1, 4, 0),
    (11, 'C', 1, 1, 0, 0, 1, 0, 3),
    (12, 'C', 1, 0, 0, 1, 0, 1, 0),
    (13, 'D', 1, 0, 1, 0, 1, 1, 1),
    (14, 'D', 1, 0, 1, 0, 1, 1, 1),
    (15, 'D', 1, 1, 0, 0, 2, 0, 3),
    (16, 'D', 1, 0, 0, 1, 0, 2, 0);
```

---

## NIVEL 1 — SELECT básico (Ej 1-8)

> Ejercicios para familiarizarse con SELECT, FROM, alias y DISTINCT. Son la base de todo.

---

**Ejercicio 1:** Mostrar todos los equipos con todas sus columnas.

> **Resultado esperado:** 16 filas devueltas. Columnas: id, nombre, confederacion, grupo, ranking_fifa, clasificado, fecha_creacion.

<details>
<summary>Ver solución</summary>

```sql
SELECT * FROM equipos;
```

</details>

---

**Ejercicio 2:** Mostrar solo el nombre y el ranking FIFA de cada equipo.

> **Resultado esperado:** 16 filas. Ejemplo:
> ```
> nombre       | ranking_fifa
> Argentina    | 1
> Perú         | 31
> Chile        | 42
> Canadá       | 48
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, ranking_fifa FROM equipos;
```

</details>

---

**Ejercicio 3:** Mostrar el nombre como "pais" y el ranking FIFA como "fifa_rank". Usar alias con AS.

> **Resultado esperado:** 16 filas con encabezados `pais` y `fifa_rank`.
> ```
> pais         | fifa_rank
> Argentina    | 1
> Perú         | 31
> Chile        | 42
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre AS pais, ranking_fifa AS fifa_rank FROM equipos;
```

</details>

---

**Ejercicio 4:** Mostrar todos los jugadores con todas sus columnas.

> **Resultado esperado:** 48 filas devueltas. Columnas: id, nombre, posicion, dorsal, activo, fecha_nacimiento, equipo_id.

<details>
<summary>Ver solución</summary>

```sql
SELECT * FROM jugadores;
```

</details>

---

**Ejercicio 5:** Mostrar las distintas posiciones de jugadores que existen (sin repetir).

> **Resultado esperado:** 4 filas.
> ```
> posicion
> Arquero
> Defensa
> Mediocampista
> Delantero
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT DISTINCT posicion FROM jugadores;
```

</details>

---

**Ejercicio 6:** Mostrar el nombre y dorsal de todos los jugadores.

> **Resultado esperado:** 48 filas. Ejemplo:
> ```
> nombre              | dorsal
> Lionel Messi        | 10
> Emiliano Martínez   | 23
> Enzo Fernández      | 8
> Paolo Guerrero      | 9
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, dorsal FROM jugadores;
```

</details>

---

**Ejercicio 7:** Mostrar todas las filas de la tabla posiciones_por_grupo.

> **Resultado esperado:** 16 filas devueltas. Columnas: id, equipo_id, grupo, pj, pg, pe, pp, gf, gc, puntos.

<details>
<summary>Ver solución</summary>

```sql
SELECT * FROM posiciones_por_grupo;
```

</details>

---

**Ejercicio 8:** Mostrar el nombre y grupo de cada equipo, ordenado por grupo alfabéticamente.

> **Resultado esperado:** 16 filas ordenadas por grupo.
> ```
> nombre         | grupo
> Argentina      | A
> Canadá         | A
> Chile          | A
> Perú           | A
> España         | B
> Japón          | B
> Marruecos      | B
> Países Bajos   | B
> Brasil         | C
> Camerún        | C
> Croacia        | C
> Uruguay        | C
> Australia      | D
> EE.UU.         | D
> Francia        | D
> Inglaterra     | D
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, grupo FROM equipos ORDER BY grupo;
```

</details>

---

## NIVEL 2 — WHERE (Ej 9-16)

> WHERE es el filtro de SQL. Acá empezamos a preguntarle cosas específicas a la base.

---

**Ejercicio 9:** Mostrar los equipos que pertenecen al grupo A.

> **Resultado esperado:** 4 filas.
> ```
> nombre     | grupo
> Argentina  | A
> Perú       | A
> Chile      | A
> Canadá     | A
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, grupo FROM equipos WHERE grupo = 'A';
```

</details>

---

**Ejercicio 10:** Mostrar los equipos de la CONMEBOL.

> **Resultado esperado:** 5 filas.
> ```
> nombre     | confederacion
> Argentina  | CONMEBOL
> Perú       | CONMEBOL
> Chile      | CONMEBOL
> Brasil     | CONMEBOL
> Uruguay    | CONMEBOL
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, confederacion FROM equipos WHERE confederacion = 'CONMEBOL';
```

</details>

---

**Ejercicio 11:** Mostrar todos los jugadores que son arqueros.

> **Resultado esperado:** 12 filas.
> ```
> nombre              | posicion | dorsal | equipo_id
> Emiliano Martínez   | Arquero  | 23     | 1
> Pedro Gallese       | Arquero  | 1      | 2
> Milan Borjan        | Arquero  | 1      | 4
> Unai Simón          | Arquero  | 23     | 5
> Yassine Bono        | Arquero  | 1      | 8
> Alisson             | Arquero  | 1      | 9
> Dominik Livaković   | Arquero  | 1      | 11
> André Onana         | Arquero  | 1      | 12
> Mike Maignan        | Arquero  | 16     | 13
> Jordan Pickford     | Arquero  | 1      | 14
> Matt Turner         | Arquero  | 1      | 15
> Mathew Ryan         | Arquero  | 1      | 16
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, posicion, dorsal, equipo_id FROM jugadores WHERE posicion = 'Arquero';
```

</details>

---

**Ejercicio 12:** Mostrar todos los jugadores que son delanteros.

> **Resultado esperado:** 15 filas.
> ```
> nombre              | posicion   | dorsal | equipo_id
> Lionel Messi        | Delantero  | 10     | 1
> Paolo Guerrero      | Delantero  | 9      | 2
> Alexis Sánchez      | Delantero  | 7      | 3
> Jonathan David      | Delantero  | 20     | 4
> Lamine Yamal        | Delantero  | 19     | 5
> Memphis Depay       | Delantero  | 10     | 6
> Ayase Ueda          | Delantero  | 11     | 7
> Vinícius Jr.        | Delantero  | 7      | 9
> Rodrygo             | Delantero  | 10     | 9
> Darwin Núñez        | Delantero  | 9      | 10
> Ivan Perišić        | Delantero  | 14     | 11
> Vincent Aboubakar   | Delantero  | 10     | 12
> Kylian Mbappé       | Delantero  | 10     | 13
> Harry Kane          | Delantero  | 9      | 14
> Mitchell Duke       | Delantero  | 15     | 16
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, posicion, dorsal, equipo_id FROM jugadores WHERE posicion = 'Delantero';
```

</details>

---

**Ejercicio 13:** Mostrar los equipos con ranking FIFA menor a 10 (mejor ranking).

> **Resultado esperado:** 7 filas.
> ```
> nombre         | ranking_fifa
> Argentina      | 1
> Francia        | 2
> Inglaterra     | 4
> Brasil         | 5
> Países Bajos   | 6
> España         | 8
> Croacia        | 9
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, ranking_fifa FROM equipos WHERE ranking_fifa < 10 ORDER BY ranking_fifa;
```

</details>

---

**Ejercicio 14:** Mostrar los equipos que NO son de la UEFA.

> **Resultado esperado:** 11 filas.
> ```
> nombre         | confederacion
> Argentina      | CONMEBOL
> Perú           | CONMEBOL
> Chile          | CONMEBOL
> Canadá         | CONCACAF
> Japón          | AFC
> Marruecos      | CAF
> Brasil         | CONMEBOL
> Uruguay        | CONMEBOL
> Camerún        | CAF
> EE.UU.         | CONCACAF
> Australia      | AFC
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, confederacion FROM equipos WHERE confederacion != 'UEFA';
```

</details>

---

**Ejercicio 15:** Mostrar los jugadores que usan el dorsal 10 (el clásico número de estrella).

> **Resultado esperado:** 9 filas.
> ```
> nombre              | dorsal | equipo_id
> Lionel Messi        | 10     | 1
> Alphonso Davies     | 10     | 4
> Memphis Depay       | 10     | 6
> Rodrygo             | 10     | 9
> Luka Modrić         | 10     | 11
> Vincent Aboubakar   | 10     | 12
> Kylian Mbappé       | 10     | 13
> Jude Bellingham     | 10     | 14
> Christian Pulisic   | 10     | 15
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, dorsal, equipo_id FROM jugadores WHERE dorsal = 10;
```

</details>

---

**Ejercicio 16:** Mostrar los equipos cuyo ranking FIFA está entre 10 y 20 (inclusive).

> **Resultado esperado:** 4 filas.
> ```
> nombre         | ranking_fifa
> EE.UU.         | 11
> Marruecos      | 13
> Uruguay        | 14
> Japón          | 17
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, ranking_fifa FROM equipos WHERE ranking_fifa BETWEEN 10 AND 20 ORDER BY ranking_fifa;
```

</details>

---

## NIVEL 3 — ORDER BY + LIMIT (Ej 17-24)

> Ordenar y paginar resultados. Fundamental para cualquier reporte.

---

**Ejercicio 17:** Mostrar todos los equipos ordenados por ranking FIFA de mejor a peor.

> **Resultado esperado:** 16 filas. Argentina (1) primero, Canadá (48) al final.
> ```
> nombre         | ranking_fifa
> Argentina      | 1
> Francia        | 2
> Inglaterra     | 4
> Brasil         | 5
> Países Bajos   | 6
> España         | 8
> Croacia        | 9
> EE.UU.         | 11
> Marruecos      | 13
> Uruguay        | 14
> Japón          | 17
> Perú           | 31
> Camerún        | 38
> Australia      | 39
> Chile          | 42
> Canadá         | 48
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, ranking_fifa FROM equipos ORDER BY ranking_fifa ASC;
```

</details>

---

**Ejercicio 18:** Mostrar todos los equipos ordenados por ranking FIFA de peor a mejor.

> **Resultado esperado:** Misma tabla que el anterior pero Canadá (48) aparece primero y Argentina (1) al final.
> ```
> nombre         | ranking_fifa
> Canadá         | 48
> Chile          | 42
> Australia      | 39
> Camerún        | 38
> Perú           | 31
> Japón          | 17
> Uruguay        | 14
> Marruecos      | 13
> EE.UU.         | 11
> Croacia        | 9
> España         | 8
> Países Bajos   | 6
> Brasil         | 5
> Inglaterra     | 4
> Francia        | 2
> Argentina      | 1
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, ranking_fifa FROM equipos ORDER BY ranking_fifa DESC;
```

</details>

---

**Ejercicio 19:** Mostrar los 3 equipos con mejor ranking FIFA (top 3).

> **Resultado esperado:**
> ```
> nombre         | ranking_fifa
> Argentina      | 1
> Francia        | 2
> Inglaterra     | 4
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, ranking_fifa FROM equipos ORDER BY ranking_fifa ASC LIMIT 3;
```

</details>

---

**Ejercicio 20:** Mostrar todos los equipos ordenados alfabéticamente por nombre.

> **Resultado esperado:** 16 filas en orden alfabético.
> ```
> nombre
> Argentina
> Australia
> Brasil
> Camerún
> Canadá
> Chile
> Croacia
> EE.UU.
> España
> Francia
> Inglaterra
> Japón
> Marruecos
> Países Bajos
> Perú
> Uruguay
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre FROM equipos ORDER BY nombre;
```

</details>

---

**Ejercicio 21:** Mostrar los 5 equipos con mejor ranking FIFA.

> **Resultado esperado:**
> ```
> nombre         | ranking_fifa
> Argentina      | 1
> Francia        | 2
> Inglaterra     | 4
> Brasil         | 5
> Países Bajos   | 6
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, ranking_fifa FROM equipos ORDER BY ranking_fifa ASC LIMIT 5;
```

</details>

---

**Ejercicio 22:** Mostrar las posiciones por grupo ordenadas por puntos de mayor a menor.

> **Resultado esperado:** 16 filas, primeros los que tienen 3 puntos.
> ```
> equipo_id | grupo | puntos
> 1         | A     | 3
> 5         | B     | 3
> 6         | B     | 3
> 9         | C     | 3
> 11        | C     | 3
> 15        | D     | 3
> 3         | A     | 1
> 4         | A     | 1
> 13        | D     | 1
> 14        | D     | 1
> 2         | A     | 0
> 7         | B     | 0
> 8         | B     | 0
> 10        | C     | 0
> 12        | C     | 0
> 16        | D     | 0
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT equipo_id, grupo, puntos FROM posiciones_por_grupo ORDER BY puntos DESC;
```

</details>

---

**Ejercicio 23:** Mostrar los equipos ordenados por ranking FIFA, pero saltando los 3 primeros (paginación, página 2).

> **Resultado esperado:** Filas 4 a 6 del ranking.
> ```
> nombre         | ranking_fifa
> Brasil         | 5
> Países Bajos   | 6
> España         | 8
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, ranking_fifa FROM equipos ORDER BY ranking_fifa ASC LIMIT 3 OFFSET 3;
```

</details>

---

**Ejercicio 24:** Mostrar las posiciones por grupo ordenadas por goles a favor (gf) de mayor a menor.

> **Resultado esperado:** Brasil (4 goles) primero.
> ```
> equipo_id | grupo | gf
> 9         | C     | 4
> 5         | B     | 3
> 1         | A     | 2
> 6         | B     | 2
> 15        | D     | 2
> 3         | A     | 1
> 4         | A     | 1
> 8         | B     | 1
> 10        | C     | 1
> 11        | C     | 1
> 13        | D     | 1
> 14        | D     | 1
> 2         | A     | 0
> 7         | B     | 0
> 12        | C     | 0
> 16        | D     | 0
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT equipo_id, grupo, gf FROM posiciones_por_grupo ORDER BY gf DESC;
```

</details>

---

## NIVEL 4 — GROUP BY + Agregadas (Ej 25-32)

> Funciones de agregación: COUNT, AVG, SUM, MAX, MIN. Combinadas con GROUP BY para hacer estadísticas.

---

**Ejercicio 25:** Contar cuántos equipos hay por cada confederación.

> **Resultado esperado:**
> ```
> confederacion | cantidad
> CONMEBOL      | 5
> UEFA          | 5
> CAF           | 2
> CONCACAF      | 2
> AFC           | 2
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT confederacion, COUNT(*) AS cantidad
FROM equipos
GROUP BY confederacion
ORDER BY cantidad DESC;
```

</details>

---

**Ejercicio 26:** Contar cuántos equipos hay por cada grupo.

> **Resultado esperado:** 4 grupos, 4 equipos cada uno.
> ```
> grupo | cantidad
> A     | 4
> B     | 4
> C     | 4
> D     | 4
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT grupo, COUNT(*) AS cantidad
FROM equipos
GROUP BY grupo
ORDER BY grupo;
```

</details>

---

**Ejercicio 27:** Calcular el promedio del ranking FIFA por confederación.

> **Resultado esperado:**
> ```
> confederacion | ranking_promedio
> UEFA          | 5.8
> CONMEBOL      | 18.6
> CAF           | 25.5
> AFC           | 28.0
> CONCACAF      | 29.5
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT confederacion, ROUND(AVG(ranking_fifa), 1) AS ranking_promedio
FROM equipos
GROUP BY confederacion
ORDER BY ranking_promedio;
```

</details>

---

**Ejercicio 28:** Calcular el total de goles a favor (gf) por grupo desde la tabla posiciones_por_grupo.

> **Resultado esperado:**
> ```
> grupo | goles_totales
> B     | 6
> C     | 6
> A     | 4
> D     | 4
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT grupo, SUM(gf) AS goles_totales
FROM posiciones_por_grupo
GROUP BY grupo
ORDER BY goles_totales DESC;
```

</details>

---

**Ejercicio 29:** Mostrar el minuto más tardío en el que se anotó un gol en cada partido.

> **Resultado esperado:**
> ```
> partido_id | minuto_maximo
> 1          | 67
> 2          | 78
> 3          | 72
> 4          | 81
> 5          | 75
> 6          | 55
> 7          | 67
> 8          | 73
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT partido_id, MAX(minuto) AS minuto_maximo
FROM goles
GROUP BY partido_id
ORDER BY partido_id;
```

</details>

---

**Ejercicio 30:** Mostrar cuántos goles anotó cada jugador, ordenado de mayor a menor.

> **Resultado esperado:** jugador_id 1 (Messi) = 2, 13 (Yamal) = 2, 18 (Depay) = 2, 25 (Vinícius Jr.) = 2, 26 (Rodrygo) = 2. El resto con 1 gol cada uno.
> ```
> jugador_id | goles
> 1          | 2
> 13         | 2
> 18         | 2
> 25         | 2
> 26         | 2
> 7          | 1
> 11         | 1
> 14         | 1
> 23         | 1
> 29         | 1
> 31         | 1
> 37         | 1
> 40         | 1
> 43         | 1
> 44         | 1
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT jugador_id, COUNT(*) AS goles
FROM goles
GROUP BY jugador_id
ORDER BY goles DESC;
```

</details>

---

**Ejercicio 31:** Mostrar los grupos que tienen más de 5 goles a favor en total. Usar HAVING.

> **Resultado esperado:** Solo los grupos con 6 o más goles.
> ```
> grupo | goles_totales
> B     | 6
> C     | 6
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT grupo, SUM(gf) AS goles_totales
FROM posiciones_por_grupo
GROUP BY grupo
HAVING SUM(gf) > 5
ORDER BY goles_totales DESC;
```

</details>

---

**Ejercicio 32:** Contar cuántas posiciones de jugador distintas existen.

> **Resultado esperado:**
> ```
> posiciones_distintas
> 4
> ```
> Las 4 posiciones son: Arquero, Defensa, Mediocampista, Delantero.

<details>
<summary>Ver solución</summary>

```sql
SELECT COUNT(DISTINCT posicion) AS posiciones_distintas FROM jugadores;
```

</details>

---

## NIVEL 5 — JOINs (Ej 33-40)

> Combinar tablas con JOIN. Acá los IDs se convierten en nombres y la base de datos relacional muestra su poder.

---

**Ejercicio 33:** Mostrar todos los jugadores con el nombre de su equipo. INNER JOIN equipos y jugadores.

> **Resultado esperado:** 48 filas. Ejemplo:
> ```
> jugador             | posicion        | equipo
> Emiliano Martínez   | Arquero         | Argentina
> Enzo Fernández      | Mediocampista   | Argentina
> Lionel Messi        | Delantero       | Argentina
> Craig Goodwin       | Mediocampista   | Australia
> Mitchell Duke       | Delantero       | Australia
> Mathew Ryan         | Arquero         | Australia
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT j.nombre AS jugador, j.posicion, e.nombre AS equipo
FROM jugadores j
INNER JOIN equipos e ON j.equipo_id = e.id
ORDER BY e.nombre, j.nombre;
```

</details>

---

**Ejercicio 34:** Mostrar todos los partidos con el nombre del equipo local.

> **Resultado esperado:** 8 filas.
> ```
> id | equipo_local   | goles_local | goles_visitante | fase
> 1  | Argentina      | 2           | 0               | Fase de Grupos
> 2  | Chile          | 1           | 1               | Fase de Grupos
> 3  | España         | 3           | 0               | Fase de Grupos
> 4  | Países Bajos   | 2           | 1               | Fase de Grupos
> 5  | Brasil         | 4           | 1               | Fase de Grupos
> 6  | Croacia        | 1           | 0               | Fase de Grupos
> 7  | Francia        | 1           | 1               | Fase de Grupos
> 8  | EE.UU.         | 2           | 0               | Fase de Grupos
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT p.id, e.nombre AS equipo_local, p.goles_local, p.goles_visitante, p.fase
FROM partidos p
INNER JOIN equipos e ON p.local_id = e.id;
```

</details>

---

**Ejercicio 35:** Mostrar todos los partidos con el nombre del equipo local Y del equipo visitante. Self-JOIN con alias.

> **Resultado esperado:** 8 filas con nombres completos.
> ```
> id | equipo_local   | goles_local | equipo_visitante | goles_visitante | fase
> 1  | Argentina      | 2           | Perú             | 0               | Fase de Grupos
> 2  | Chile          | 1           | Canadá           | 1               | Fase de Grupos
> 3  | España         | 3           | Japón            | 0               | Fase de Grupos
> 4  | Países Bajos   | 2           | Marruecos        | 1               | Fase de Grupos
> 5  | Brasil         | 4           | Uruguay          | 1               | Fase de Grupos
> 6  | Croacia        | 1           | Camerún          | 0               | Fase de Grupos
> 7  | Francia        | 1           | Inglaterra       | 1               | Fase de Grupos
> 8  | EE.UU.         | 2           | Australia        | 0               | Fase de Grupos
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT p.id,
       local.nombre AS equipo_local,
       p.goles_local,
       visitante.nombre AS equipo_visitante,
       p.goles_visitante,
       p.fase
FROM partidos p
INNER JOIN equipos local ON p.local_id = local.id
INNER JOIN equipos visitante ON p.visitante_id = visitante.id;
```

</details>

---

**Ejercicio 36:** Mostrar todos los equipos, incluso aquellos que no hayan jugado como locales todavía. LEFT JOIN.

> **Resultado esperado:** 16 filas. Los equipos que nunca fueron locales aparecen con NULL.
> ```
> equipo         | partido_id | goles_local
> Argentina      | 1          | 2
> Australia      | NULL       | NULL
> Brasil         | 5          | 4
> Camerún        | NULL       | NULL
> Canadá         | NULL       | NULL
> Chile          | 2          | 1
> Croacia        | 6          | 1
> EE.UU.         | 8          | 2
> España         | 3          | 3
> Francia        | 7          | 1
> Inglaterra     | NULL       | NULL
> Japón          | NULL       | NULL
> Marruecos      | NULL       | NULL
> Países Bajos   | 4          | 2
> Perú           | NULL       | NULL
> Uruguay        | NULL       | NULL
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT e.nombre AS equipo, p.id AS partido_id, p.goles_local
FROM equipos e
LEFT JOIN partidos p ON e.id = p.local_id
ORDER BY e.nombre;
```

</details>

---

**Ejercicio 37:** Mostrar todos los goles con el nombre del jugador y el ID del partido. JOIN entre goles y jugadores.

> **Resultado esperado:** 20 filas. Ejemplo:
> ```
> gol_id | jugador          | minuto | es_penal | partido_id
> 1      | Lionel Messi     | 12     | false    | 1
> 2      | Lionel Messi     | 67     | false    | 1
> 3      | Alexis Sánchez   | 34     | false    | 2
> 4      | Jonathan David   | 78     | false    | 2
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT g.id AS gol_id, j.nombre AS jugador, g.minuto, g.es_penal, g.partido_id
FROM goles g
INNER JOIN jugadores j ON g.jugador_id = j.id
ORDER BY g.partido_id, g.minuto;
```

</details>

---

**Ejercicio 38:** Mostrar todos los goles con el nombre del jugador y el nombre de su equipo. JOIN goles → jugadores → equipos.

> **Resultado esperado:** 20 filas. Ejemplo:
> ```
> jugador          | equipo     | minuto | es_penal
> Lionel Messi     | Argentina  | 12     | false
> Lionel Messi     | Argentina  | 67     | false
> Alexis Sánchez   | Chile      | 34     | false
> Jonathan David   | Canadá     | 78     | false
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT j.nombre AS jugador, e.nombre AS equipo, g.minuto, g.es_penal
FROM goles g
INNER JOIN jugadores j ON g.jugador_id = j.id
INNER JOIN equipos e ON j.equipo_id = e.id
ORDER BY g.partido_id, g.minuto;
```

</details>

---

**Ejercicio 39:** Mostrar todos los goles con nombre del jugador, su equipo, y los equipos del partido. JOIN de 4 tablas.

> **Resultado esperado:** 20 filas. Muestra el contexto completo de cada gol.
> ```
> jugador          | equipo_del_jugador | equipo_local  | equipo_visitante | minuto
> Lionel Messi     | Argentina          | Argentina     | Perú             | 12
> Lionel Messi     | Argentina          | Argentina     | Perú             | 67
> Alexis Sánchez   | Chile              | Chile         | Canadá           | 34
> Jonathan David   | Canadá             | Chile         | Canadá           | 78
> Lamine Yamal     | España             | España        | Japón            | 8
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT j.nombre AS jugador, e.nombre AS equipo_del_jugador,
       local.nombre AS equipo_local, visitante.nombre AS equipo_visitante,
       g.minuto, g.es_penal
FROM goles g
INNER JOIN jugadores j ON g.jugador_id = j.id
INNER JOIN equipos e ON j.equipo_id = e.id
INNER JOIN partidos p ON g.partido_id = p.id
INNER JOIN equipos local ON p.local_id = local.id
INNER JOIN equipos visitante ON p.visitante_id = visitante.id
ORDER BY g.partido_id, g.minuto;
```

</details>

---

**Ejercicio 40:** Mostrar la tabla de posiciones con nombres de equipos en lugar de IDs.

> **Resultado esperado:** 16 filas con los nombres de los equipos.
> ```
> equipo         | grupo | pj | pg | pe | pp | gf | gc | puntos
> Argentina      | A     | 1  | 1  | 0  | 0  | 2  | 0  | 3
> Chile          | A     | 1  | 0  | 1  | 0  | 1  | 1  | 1
> Canadá         | A     | 1  | 0  | 1  | 0  | 1  | 1  | 1
> Perú           | A     | 1  | 0  | 0  | 1  | 0  | 2  | 0
> España         | B     | 1  | 1  | 0  | 0  | 3  | 0  | 3
> Países Bajos   | B     | 1  | 1  | 0  | 0  | 2  | 1  | 3
> Marruecos      | B     | 1  | 0  | 0  | 1  | 1  | 2  | 0
> Japón          | B     | 1  | 0  | 0  | 1  | 0  | 3  | 0
> Brasil         | C     | 1  | 1  | 0  | 0  | 4  | 1  | 3
> Croacia        | C     | 1  | 1  | 0  | 0  | 1  | 0  | 3
> Uruguay        | C     | 1  | 0  | 0  | 1  | 1  | 4  | 0
> Camerún        | C     | 1  | 0  | 0  | 1  | 0  | 1  | 0
> EE.UU.         | D     | 1  | 1  | 0  | 0  | 2  | 0  | 3
> Francia        | D     | 1  | 0  | 1  | 0  | 1  | 1  | 1
> Inglaterra     | D     | 1  | 0  | 1  | 0  | 1  | 1  | 1
> Australia      | D     | 1  | 0  | 0  | 1  | 0  | 2  | 0
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT e.nombre AS equipo, p.grupo, p.pj, p.pg, p.pe, p.pp, p.gf, p.gc, p.puntos
FROM posiciones_por_grupo p
INNER JOIN equipos e ON p.equipo_id = e.id
ORDER BY p.grupo, p.puntos DESC;
```

</details>

---

## NIVEL 6 — Combinados (Ej 41-48)

> Acá se junta todo: JOINs, GROUP BY, subconsultas, UPDATE, DELETE. Son ejercicios desafiantes que reflejan problemas reales.

---

**Ejercicio 41:** Mostrar todos los goles que anotó Lionel Messi, incluyendo el equipo rival contra el que jugaba y el minuto.

> **Resultado esperado:** Messi anotó 2 goles, ambos contra Perú.
> ```
> jugador       | minuto | equipo_rival | es_penal
> Lionel Messi  | 12     | Perú         | false
> Lionel Messi  | 67     | Perú         | false
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT j.nombre AS jugador, g.minuto,
       visitante.nombre AS equipo_rival, g.es_penal
FROM goles g
INNER JOIN jugadores j ON g.jugador_id = j.id
INNER JOIN partidos p ON g.partido_id = p.id
INNER JOIN equipos visitante ON p.visitante_id = visitante.id
WHERE j.nombre = 'Lionel Messi'
ORDER BY g.minuto;
```

</details>

---

**Ejercicio 42:** Mostrar los equipos que tienen más de 1 gol anotado en el torneo. Usar JOIN + GROUP BY + HAVING.

> **Resultado esperado:** 5 equipos.
> ```
> equipo         | goles
> Brasil         | 4
> España         | 3
> Argentina      | 2
> Países Bajos   | 2
> EE.UU.         | 2
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT e.nombre AS equipo, COUNT(*) AS goles
FROM goles g
INNER JOIN jugadores j ON g.jugador_id = j.id
INNER JOIN equipos e ON j.equipo_id = e.id
GROUP BY e.nombre
HAVING COUNT(*) > 1
ORDER BY goles DESC;
```

</details>

---

**Ejercicio 43:** Mostrar el equipo con el ranking FIFA más bajo (el peor ranking = número más grande). Usar subconsulta.

> **Resultado esperado:**
> ```
> nombre  | ranking_fifa
> Canadá  | 48
> ```
> Nota: ranking_fifa más alto = peor ranking. Canadá está en el puesto 48, el más bajo del torneo.

<details>
<summary>Ver solución</summary>

```sql
SELECT nombre, ranking_fifa
FROM equipos
WHERE ranking_fifa = (SELECT MAX(ranking_fifa) FROM equipos);
```

</details>

---

**Ejercicio 44:** Mostrar los jugadores del equipo con mejor ranking FIFA. Usar subconsulta.

> **Resultado esperado:** Argentina (ranking 1) tiene 3 jugadores.
> ```
> nombre              | posicion        | dorsal
> Lionel Messi        | Delantero       | 10
> Emiliano Martínez   | Arquero         | 23
> Enzo Fernández      | Mediocampista   | 8
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT j.nombre, j.posicion, j.dorsal
FROM jugadores j
WHERE j.equipo_id = (
    SELECT id FROM equipos ORDER BY ranking_fifa ASC LIMIT 1
);
```

</details>

---

**Ejercicio 45:** Actualizar los puntos en la tabla posiciones_por_grupo usando una subconsulta. Sumar 3 puntos por victoria y 1 por empate.

> **Resultado esperado:** Después del UPDATE:
> ```
> equipo_id | pg | pe | pp | puntos
> 1         | 1  | 0  | 0  | 3
> 2         | 0  | 0  | 1  | 0
> 3         | 0  | 1  | 0  | 1
> 4         | 0  | 1  | 0  | 1
> ```
> Verificar con: `SELECT * FROM posiciones_por_grupo ORDER BY grupo, puntos DESC;`
>
> Nota: los puntos ya están correctos en los datos iniciales, esta consulta serviría para recalcularlos si cambiaran los valores de pg/pe.

<details>
<summary>Ver solución</summary>

```sql
UPDATE posiciones_por_grupo
SET puntos = pg * 3 + pe * 1;
```

</details>

---

**Ejercicio 46:** Borrar todos los goles del partido entre Argentina y Perú.

> **Resultado esperado:** 2 filas eliminadas (los goles de Messi en los minutos 12 y 67).
>
> Verificar con: `SELECT * FROM goles;` → ya no aparecen los goles con partido_id = 1.
>
> Después de ejecutar, para restaurar los datos, volvé a insertar:
> ```sql
> INSERT INTO goles (minuto, es_penal, partido_id, jugador_id) VALUES
> (12, FALSE, 1, 1),
> (67, FALSE, 1, 1);
> ```

<details>
<summary>Ver solución</summary>

```sql
DELETE FROM goles
WHERE partido_id = (SELECT id FROM partidos WHERE local_id = 1 AND visitante_id = 2);
```

O directamente sabiendo el ID del partido:

```sql
DELETE FROM goles WHERE partido_id = 1;
```

</details>

---

**Ejercicio 47 (Desafío):** Mostrar un ranking de goleadores con: nombre del jugador, nombre de su equipo, cantidad de goles, y los minutos en los que anotó. Ordenar por goles descendente.

> **Resultado esperado:** 15 filas (15 jugadores anotaron). Los máximos goleadores tienen 2 goles.
> ```
> jugador          | equipo         | goles | minutos
> Lionel Messi     | Argentina      | 2     | 12, 67
> Lamine Yamal     | España         | 2     | 8, 72
> Memphis Depay    | Países Bajos   | 2     | 23, 81
> Vinícius Jr.     | Brasil         | 2     | 15, 41
> Rodrygo          | Brasil         | 2     | 33, 75
> Alexis Sánchez   | Chile          | 1     | 34
> Jonathan David   | Canadá         | 1     | 78
> Pedri            | España         | 1     | 45
> Hakim Ziyech     | Marruecos      | 1     | 55
> Darwin Núñez     | Uruguay        | 1     | 62
> Luka Modrić      | Croacia        | 1     | 55
> Kylian Mbappé    | Francia        | 1     | 23
> Harry Kane       | Inglaterra     | 1     | 67
> Christian Pulisic| EE.UU.         | 1     | 41
> Weston McKennie  | EE.UU.         | 1     | 73
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT j.nombre AS jugador, e.nombre AS equipo,
       COUNT(*) AS goles,
       STRING_AGG(g.minuto::TEXT, ', ' ORDER BY g.minuto) AS minutos
FROM goles g
INNER JOIN jugadores j ON g.jugador_id = j.id
INNER JOIN equipos e ON j.equipo_id = e.id
GROUP BY j.nombre, e.nombre
ORDER BY goles DESC, j.nombre;
```

</details>

---

**Ejercicio 48 (Super Desafío):** Armar un reporte completo por partido que muestre: ID del partido, equipos (local vs visitante), resultado, cantidad de goles del partido, y lista de goleadores separada por comas. Ordenar por cantidad de goles descendente.

> **Resultado esperado:**
> ```
> id | resultado                     | total_goles | goleadores
> 5  | Brasil 4 - 1 Uruguay          | 5           | Darwin Núñez, Rodrygo, Vinícius Jr.
> 3  | España 3 - 0 Japón            | 3           | Lamine Yamal, Pedri
> 4  | Países Bajos 2 - 1 Marruecos  | 3           | Hakim Ziyech, Memphis Depay
> 1  | Argentina 2 - 0 Perú          | 2           | Lionel Messi
> 2  | Chile 1 - 1 Canadá            | 2           | Alexis Sánchez, Jonathan David
> 7  | Francia 1 - 1 Inglaterra      | 2           | Harry Kane, Kylian Mbappé
> 8  | EE.UU. 2 - 0 Australia        | 2           | Christian Pulisic, Weston McKennie
> 6  | Croacia 1 - 0 Camerún         | 1           | Luka Modrić
> ```

<details>
<summary>Ver solución</summary>

```sql
SELECT p.id,
       local.nombre || ' ' || p.goles_local || ' - ' || p.goles_visitante || ' ' || visitante.nombre AS resultado,
       COUNT(g.id) AS total_goles,
       COALESCE(STRING_AGG(DISTINCT j.nombre, ', ' ORDER BY j.nombre), 'Sin goles') AS goleadores
FROM partidos p
INNER JOIN equipos local ON p.local_id = local.id
INNER JOIN equipos visitante ON p.visitante_id = visitante.id
LEFT JOIN goles g ON p.id = g.partido_id
LEFT JOIN jugadores j ON g.jugador_id = j.id
GROUP BY p.id, local.nombre, visitante.nombre, p.goles_local, p.goles_visitante
ORDER BY total_goles DESC;
```

</details>

---

## 💥 Bonus Track — La consulta definitiva

Si llegaste hasta acá, felicitaciones. Esta consulta combina TODO lo aprendido: JOINs múltiples, funciones de agregación, GROUP BY, HAVING, ORDER BY, y subconsultas.

**Objetivo:** Mostrar, para cada grupo, el equipo líder (el que tiene más puntos), su cantidad de goles, cantidad de jugadores, y el goleador del equipo.

> **Resultado esperado:**
> ```
> grupo | equipo_lider  | puntos | goles_favor | cantidad_jugadores | maximo_goleador
> A     | Argentina     | 3      | 2           | 3                  | Lionel Messi
> B     | España        | 3      | 3           | 3                  | Lamine Yamal
> C     | Brasil        | 3      | 4           | 3                  | Vinícius Jr.
> D     | EE.UU.        | 3      | 2           | 3                  | Christian Pulisic
> ```
> Nota: En los grupos B y C hay empate en puntos (Países Bajos y Croacia también tienen 3). La subconsulta con MAX resuelve, pero podrías agregar criterios de desempate como diferencia de gol.

<details>
<summary>Ver solución</summary>

```sql
SELECT
    pp.grupo,
    e.nombre AS equipo_lider,
    pp.puntos,
    pp.gf AS goles_favor,
    (SELECT COUNT(*) FROM jugadores j WHERE j.equipo_id = e.id) AS cantidad_jugadores,
    COALESCE((
        SELECT j2.nombre
        FROM goles g2
        INNER JOIN jugadores j2 ON g2.jugador_id = j2.id
        WHERE j2.equipo_id = e.id
        GROUP BY j2.nombre
        ORDER BY COUNT(*) DESC, j2.nombre
        LIMIT 1
    ), 'Sin goles') AS maximo_goleador
FROM posiciones_por_grupo pp
INNER JOIN equipos e ON pp.equipo_id = e.id
WHERE pp.puntos = (
    SELECT MAX(pp2.puntos)
    FROM posiciones_por_grupo pp2
    WHERE pp2.grupo = pp.grupo
)
ORDER BY pp.grupo;
```

</details>

---

## 📋 Checklist de verificación

| Ejercicios | Concepto | Lo resolviste? | Coincide con el resultado? |
|---|---|---|---|
| 1-8 | SELECT, alias, DISTINCT, ORDER BY básico | ☐ | ☐ |
| 9-16 | WHERE, =, !=, BETWEEN, comparación | ☐ | ☐ |
| 17-24 | ORDER BY ASC/DESC, LIMIT, OFFSET | ☐ | ☐ |
| 25-32 | COUNT, AVG, SUM, MAX, GROUP BY, HAVING | ☐ | ☐ |
| 33-40 | INNER JOIN, LEFT JOIN, múltiples JOINs | ☐ | ☐ |
| 41-48 | JOINs + agregadas, subconsultas, UPDATE, DELETE | ☐ | ☐ |
