-- =============================================================
-- MUNDIAL 2026 — Schema completo
-- 6 tablas, puras relaciones 1:N, sin N:M, sin 1:1
-- =============================================================
-- Orden: primero las tablas sin FK, después las que dependen
-- =============================================================

-- =============================================================
-- 1. EQUIPOS (0 FKs)
-- =============================================================
CREATE TABLE equipos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    confederacion VARCHAR NOT NULL,
    grupo CHAR(1) NOT NULL,
    ranking_fifa INTEGER NOT NULL,
    clasificado BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT NOW()
);

-- =============================================================
-- 2. JUGADORES (FK → equipos)
-- =============================================================
CREATE TABLE jugadores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    posicion VARCHAR NOT NULL,
    dorsal INTEGER NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    fecha_nacimiento DATE,
    equipo_id INTEGER NOT NULL REFERENCES equipos(id)
);

-- =============================================================
-- 3. PARTIDOS (FKs → equipos: local y visitante)
-- =============================================================
CREATE TABLE partidos (
    id SERIAL PRIMARY KEY,
    goles_local INTEGER DEFAULT 0,
    goles_visitante INTEGER DEFAULT 0,
    fase VARCHAR NOT NULL,
    fecha TIMESTAMP,
    local_id INTEGER NOT NULL REFERENCES equipos(id),
    visitante_id INTEGER NOT NULL REFERENCES equipos(id)
);

-- =============================================================
-- 4. GOLES (FKs → partidos y jugadores)
-- =============================================================
CREATE TABLE goles (
    id SERIAL PRIMARY KEY,
    minuto INTEGER DEFAULT 0,
    es_penal BOOLEAN DEFAULT FALSE,
    partido_id INTEGER NOT NULL REFERENCES partidos(id),
    jugador_id INTEGER NOT NULL REFERENCES jugadores(id)
);

-- =============================================================
-- 5. POSICIONES POR GRUPO (FK → equipos)
-- =============================================================
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
