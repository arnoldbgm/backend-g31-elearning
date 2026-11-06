-- =============================================================
-- MÚSICA PERUANA — Schema completo
-- 2 tablas: artistas y canciones (relación 1:N)
-- Para usar en PostgreSQL
-- =============================================================

-- =============================================================
-- 1. ARTISTAS (la tabla principal)
-- =============================================================
CREATE TABLE artistas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    pais_origen VARCHAR(50) DEFAULT 'Perú',
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT NOW()
);

-- =============================================================
-- 2. CANCIONES (con FK a artistas)
-- =============================================================
CREATE TABLE canciones (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    album VARCHAR(150),
    duracion_segundos INTEGER,
    anio_lanzamiento INTEGER,
    artista_id INTEGER NOT NULL REFERENCES artistas(id)
);

-- =============================================================
-- DATOS DE PRUEBA — Artistas Peruanos e Internacionales
-- =============================================================

INSERT INTO artistas (nombre, genero, pais_origen) VALUES
    ('Grupo 5', 'Cumbia', 'Perú'),
    ('Agua Marina', 'Cumbia', 'Perú'),
    ('Armonía 10', 'Cumbia', 'Perú'),
    ('Libido', 'Rock', 'Perú'),
    ('Arena Hash', 'Rock', 'Perú'),
    ('Pedro Suárez Vértiz', 'Rock', 'Perú'),
    ('Chabuca Granda', 'Criolla', 'Perú'),
    ('Zambo Cabero', 'Criolla', 'Perú'),
    ('Bon Jovi', 'Rock', 'Estados Unidos'),
    ('Kiss', 'Rock', 'Estados Unidos');

-- =============================================================
-- CANCIONES DE EJEMPLO
-- =============================================================

INSERT INTO canciones (titulo, album, duracion_segundos, anio_lanzamiento, artista_id) VALUES
    -- Grupo 5 (id=1)
    ('La Cumbia de las Aventuras', 'Grupo 5', 210, 2005, 1),
    ('Nadie como Tú', 'Cumbia Total', 195, 2008, 1),
    ('Loca', 'Loca', 200, 2010, 1),

    -- Agua Marina (id=2)
    ('Cariñito', 'Cariñito', 195, 1995, 2),
    ('La Ladrona', 'La Ladrona', 210, 1997, 2),
    ('Me Engañaste', 'Grandes Éxitos', 185, 1998, 2),

    -- Armonía 10 (id=3)
    ('Me Persigue una Sombra', 'Armonía 10', 220, 2000, 3),
    ('Corazón de Piedra', 'Corazón de Piedra', 200, 2002, 3),

    -- Libido (id=4)
    ('Frío', 'Libido', 230, 1998, 4),
    ('Lamento', 'Libido', 245, 1998, 4),
    ('Noches de Sal', 'Libido', 210, 2000, 4),

    -- Arena Hash (id=5)
    ('De Música Ligera', 'Arena Hash', 225, 1988, 5),
    ('Cara de Niño', 'Arena Hash', 200, 1988, 5),

    -- Pedro Suárez Vértiz (id=6)
    ('El Mismo Cielo', 'Pedro Suárez Vértiz', 240, 1991, 6),
    ('Entra en Mi Vida', 'Best of', 235, 1993, 6),
    ('Aire', 'Aire', 220, 1996, 6),

    -- Chabuca Granda (id=7)
    ('La Flor de la Canela', 'La Flor de la Canela', 210, 1957, 7),
    ('El Puente de los Suspiros', 'Lo Mejor de Chabuca', 230, 1960, 7),

    -- Zambo Cabero (id=8)
    ('El Carretero', 'Zambo Cabero', 200, 1975, 8),
    ('La Gallarda', 'Clausuras del Perú', 215, 1978, 8),

    -- Bon Jovi (id=9)
    ('Livin on a Prayer', 'Slippery When Wet', 245, 1986, 9),
    ('It s My Life', 'Crush', 225, 2000, 9),
    ('Wanted Dead or Alive', '7800° Fahrenheit', 270, 1987, 9),

    -- Kiss (id=10)
    ('Rock and Roll All Nite', 'Dressed to Kill', 195, 1975, 10),
    ('I Was Made for Lovin You', 'Dynasty', 240, 1979, 10);

-- =============================================================
-- VERIFICACIÓN
-- =============================================================

-- Ver todos los artistas
SELECT * FROM artistas;

-- Ver todas las canciones con el nombre del artista
SELECT c.titulo, a.nombre AS artista, a.genero, c.anio_lanzamiento
FROM canciones c
INNER JOIN artistas a ON c.artista_id = a.id
ORDER BY a.nombre, c.anio_lanzamiento;

-- Contar canciones por artista
SELECT a.nombre, COUNT(c.id) AS canciones
FROM artistas a
LEFT JOIN canciones c ON a.id = c.artista_id
GROUP BY a.nombre
ORDER BY canciones DESC;

-- Contar artistas por género
SELECT genero, COUNT(*) AS cantidad
FROM artistas
GROUP BY genero;
