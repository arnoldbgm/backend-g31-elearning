-- 01. Copia, pegado el schema
-- 02. Ejecutado el schema
-- 03. Limpiamos todo
-- 04. Copiamos y pegamos el seed
-- 05. Ejecutamos todo el seed
-- 06. Limpiamos todo

SELECT * FROM jugadores;

SELECT * FROM equipos;

-- JOINS
-- UNIR TABLAS
-- jugadores tendra como alias j
SELECT j.nombre, j.dorsal, j.posicion, e.nombre, e.confederacion
FROM jugadores j
INNER JOIN equipos e ON e.id = j.equipo_id;

SELECT * FROM posiciones_por_grupo;

-- RETO 04:
-- Devolver el nombre del equipo, pj, pg, pe y puntos
-- Usando un INNER JOIN, solo de los que juegan en el grupo C;

-- SELECT
-- FROM
-- JOIN
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY
-- LIMIT

SELECT e.nombre, pg.grupo , pg.pj, pg.pg, pg.pe, pg.puntos
FROM posiciones_por_grupo pg
INNER JOIN equipos e ON pg.equipo_id = e.id
WHERE pg.grupo ILIKE 'C'
ORDER BY pg.puntos DESC;


-- Se muestre los partidos
-- local, goles local, visitante, goles visitante
SELECT * FROM partidos;

SELECT 
	elocal.nombre AS "Equipo Local", 
	p.goles_local AS "Goles Local", 
	evisitante.nombre AS "Equipo Visitante", 
	p.goles_visitante AS "Goles Visitante"
FROM partidos p
INNER JOIN equipos elocal 
		ON p.local_id = elocal.id
INNER JOIN equipos evisitante 
		ON p.visitante_id = evisitante.id;

-- Cantidades, promedios y totales
-- ¿Cuantos goles hay?
-- COUNT(*)
SELECT COUNT(*) AS "Total de goles"
FROM goles;

SELECT COUNT(*) AS "Total de Jugadores"
FROM jugadores
WHERE posicion ILIKE 'delantero';

-- DELANTERO 15
-- DEFENSA   12
-- PORTERO    1
-- GROUP BY
SELECT posicion, COUNT(*)
FROM jugadores
GROUP BY posicion;

-- Ranking FIFA promedio por grupo
SELECT grupo, AVG(ranking_fifa)
FROM equipos
GROUP BY grupo
ORDER BY grupo;

-- El mejor y el peor rankign de cada grupo
SELECT grupo,
	MIN(ranking_fifa) AS "Mejor Ranking",
	MAX(ranking_fifa) AS "Peor Ranking"
FROM equipos
GROUP BY grupo
ORDER BY grupo;
