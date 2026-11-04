-- =============================================================
-- MUNDIAL 2026 — Seed data
-- =============================================================
-- Orden: equipos → jugadores → partidos → goles → posiciones
-- =============================================================

BEGIN;

-- =============================================================
-- EQUIPOS (16, 4 grupos de 4)
-- =============================================================
INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa, clasificado) VALUES
-- Grupo A
('Argentina',     'CONMEBOL', 'A', 1,  TRUE),
('Perú',          'CONMEBOL', 'A', 31, TRUE),
('Chile',         'CONMEBOL', 'A', 42, TRUE),
('Canadá',        'CONCACAF', 'A', 48, TRUE),
-- Grupo B
('España',        'UEFA',     'B', 8,  TRUE),
('Países Bajos',  'UEFA',     'B', 6,  TRUE),
('Japón',         'AFC',      'B', 17, TRUE),
('Marruecos',     'CAF',      'B', 13, TRUE),
-- Grupo C
('Brasil',        'CONMEBOL', 'C', 5,  TRUE),
('Uruguay',       'CONMEBOL', 'C', 14, TRUE),
('Croacia',       'UEFA',     'C', 9,  TRUE),
('Camerún',       'CAF',      'C', 38, TRUE),
-- Grupo D
('Francia',       'UEFA',     'D', 2,  TRUE),
('Inglaterra',    'UEFA',     'D', 4,  TRUE),
('EE.UU.',        'CONCACAF', 'D', 11, TRUE),
('Australia',     'AFC',      'D', 39, TRUE);

-- =============================================================
-- JUGADORES (3 por equipo = 48)
-- =============================================================
INSERT INTO jugadores (nombre, posicion, dorsal, activo, equipo_id) VALUES
-- Argentina (1)
('Lionel Messi',        'Delantero',     10, TRUE, 1),
('Emiliano Martínez',   'Arquero',       23, TRUE, 1),
('Enzo Fernández',      'Mediocampista', 24, TRUE, 1),
-- Perú (2)
('Paolo Guerrero',      'Delantero',      9, TRUE, 2),
('Renato Tapia',        'Mediocampista', 13, TRUE, 2),
('Pedro Gallese',       'Arquero',        1, TRUE, 2),
-- Chile (3)
('Alexis Sánchez',      'Delantero',      7, TRUE, 3),
('Arturo Vidal',        'Mediocampista',  8, TRUE, 3),
('Gary Medel',          'Defensa',       17, TRUE, 3),
-- Canadá (4)
('Alphonso Davies',     'Mediocampista', 19, TRUE, 4),
('Jonathan David',      'Delantero',     20, TRUE, 4),
('Milan Borjan',        'Arquero',       18, TRUE, 4),
-- España (5)
('Lamine Yamal',        'Delantero',     19, TRUE, 5),
('Pedri',               'Mediocampista',  8, TRUE, 5),
('Unai Simón',          'Arquero',       23, TRUE, 5),
-- Países Bajos (6)
('Virgil van Dijk',     'Defensa',        4, TRUE, 6),
('Frenkie de Jong',     'Mediocampista', 21, TRUE, 6),
('Memphis Depay',       'Delantero',     10, TRUE, 6),
-- Japón (7)
('Takefusa Kubo',       'Mediocampista', 14, TRUE, 7),
('Wataru Endō',         'Mediocampista',  6, TRUE, 7),
('Ayase Ueda',          'Delantero',      9, TRUE, 7),
-- Marruecos (8)
('Achraf Hakimi',       'Defensa',        2, TRUE, 8),
('Hakim Ziyech',        'Mediocampista',  7, TRUE, 8),
('Yassine Bono',        'Arquero',        1, TRUE, 8),
-- Brasil (9)
('Vinícius Jr.',        'Delantero',      7, TRUE, 9),
('Rodrygo',             'Delantero',     10, TRUE, 9),
('Alisson',             'Arquero',        1, TRUE, 9),
-- Uruguay (10)
('Federico Valverde',   'Mediocampista', 15, TRUE, 10),
('Darwin Núñez',        'Delantero',      9, TRUE, 10),
('José María Giménez',  'Defensa',        2, TRUE, 10),
-- Croacia (11)
('Luka Modrić',         'Mediocampista', 10, TRUE, 11),
('Ivan Perišić',        'Delantero',      4, TRUE, 11),
('Dominik Livaković',   'Arquero',        1, TRUE, 11),
-- Camerún (12)
('Vincent Aboubakar',   'Delantero',     10, TRUE, 12),
('André Onana',         'Arquero',        1, TRUE, 12),
('Bryan Mbeumo',        'Mediocampista', 17, TRUE, 12),
-- Francia (13)
('Kylian Mbappé',       'Delantero',     10, TRUE, 13),
('Antoine Griezmann',   'Mediocampista',  7, TRUE, 13),
('Mike Maignan',        'Arquero',       16, TRUE, 13),
-- Inglaterra (14)
('Harry Kane',          'Delantero',      9, TRUE, 14),
('Jude Bellingham',     'Mediocampista', 10, TRUE, 14),
('Jordan Pickford',     'Arquero',        1, TRUE, 14),
-- EE.UU. (15)
('Christian Pulisic',   'Mediocampista', 10, TRUE, 15),
('Weston McKennie',     'Mediocampista',  8, TRUE, 15),
('Matt Turner',         'Arquero',        1, TRUE, 15),
-- Australia (16)
('Mathew Ryan',         'Arquero',        1, TRUE, 16),
('Craig Goodwin',       'Mediocampista', 23, TRUE, 16),
('Mitchell Duke',       'Delantero',     15, TRUE, 16);

-- =============================================================
-- PARTIDOS (8 — 2 por grupo, con resultados)
-- =============================================================
INSERT INTO partidos (local_id, visitante_id, goles_local, goles_visitante, fase, fecha) VALUES
-- Grupo A
(1,  2,  2,  0,  'Fase de Grupos', '2026-06-14 18:00:00'),
(3,  4,  1,  1,  'Fase de Grupos', '2026-06-15 15:00:00'),
-- Grupo B
(5,  7,  3,  0,  'Fase de Grupos', '2026-06-16 18:00:00'),
(6,  8,  2,  1,  'Fase de Grupos', '2026-06-16 21:00:00'),
-- Grupo C
(9,  10, 4,  1,  'Fase de Grupos', '2026-06-17 18:00:00'),
(11, 12, 1,  0,  'Fase de Grupos', '2026-06-17 21:00:00'),
-- Grupo D
(13, 14, 1,  1,  'Fase de Grupos', '2026-06-18 18:00:00'),
(15, 16, 2,  0,  'Fase de Grupos', '2026-06-18 21:00:00');

-- =============================================================
-- GOLES (20 — desglose de los 8 partidos)
-- =============================================================
INSERT INTO goles (minuto, es_penal, partido_id, jugador_id) VALUES
-- Partido 1: Argentina 2-0 Perú
(12, FALSE, 1, 1),   -- Messi ⚽
(67, FALSE, 1, 1),   -- Messi ⚽
-- Partido 2: Chile 1-1 Canadá
(34, FALSE, 2, 7),   -- Alexis Sánchez ⚽
(78, FALSE, 2, 11),  -- Jonathan David ⚽
-- Partido 3: España 3-0 Japón
(8,  FALSE, 3, 13),  -- Lamine Yamal ⚽
(45, FALSE, 3, 14),  -- Pedri ⚽
(72, FALSE, 3, 13),  -- Lamine Yamal ⚽
-- Partido 4: Países Bajos 2-1 Marruecos
(23, FALSE, 4, 18),  -- Memphis Depay ⚽
(55, FALSE, 4, 23),  -- Hakim Ziyech ⚽
(81, TRUE,  4, 18),  -- Memphis Depay ⚽ (penal)
-- Partido 5: Brasil 4-1 Uruguay
(15, FALSE, 5, 25),  -- Vinícius Jr. ⚽
(33, FALSE, 5, 26),  -- Rodrygo ⚽
(41, FALSE, 5, 25),  -- Vinícius Jr. ⚽
(62, FALSE, 5, 29),  -- Darwin Núñez ⚽
(75, FALSE, 5, 26),  -- Rodrygo ⚽
-- Partido 6: Croacia 1-0 Camerún
(55, FALSE, 6, 31),  -- Luka Modrić ⚽
-- Partido 7: Francia 1-1 Inglaterra
(23, FALSE, 7, 37),  -- Kylian Mbappé ⚽
(67, FALSE, 7, 40),  -- Harry Kane ⚽
-- Partido 8: EE.UU. 2-0 Australia
(41, FALSE, 8, 43),  -- Christian Pulisic ⚽
(73, FALSE, 8, 44);  -- Weston McKennie ⚽

-- =============================================================
-- POSICIONES POR GRUPO (16 equipos, 1 fila cada uno)
-- =============================================================
INSERT INTO posiciones_por_grupo (equipo_id, grupo, pj, pg, pe, pp, gf, gc, puntos) VALUES
-- Grupo A
(1,  'A', 1, 1, 0, 0, 2, 0, 3),   -- Argentina
(2,  'A', 1, 0, 0, 1, 0, 2, 0),   -- Perú
(3,  'A', 1, 0, 1, 0, 1, 1, 1),   -- Chile
(4,  'A', 1, 0, 1, 0, 1, 1, 1),   -- Canadá
-- Grupo B
(5,  'B', 1, 1, 0, 0, 3, 0, 3),   -- España
(6,  'B', 1, 1, 0, 0, 2, 1, 3),   -- Países Bajos
(7,  'B', 1, 0, 0, 1, 0, 3, 0),   -- Japón
(8,  'B', 1, 0, 0, 1, 1, 2, 0),   -- Marruecos
-- Grupo C
(9,  'C', 1, 1, 0, 0, 4, 1, 3),   -- Brasil
(10, 'C', 1, 0, 0, 1, 1, 4, 0),   -- Uruguay
(11, 'C', 1, 1, 0, 0, 1, 0, 3),   -- Croacia
(12, 'C', 1, 0, 0, 1, 0, 1, 0),   -- Camerún
-- Grupo D
(13, 'D', 1, 0, 1, 0, 1, 1, 1),   -- Francia
(14, 'D', 1, 0, 1, 0, 1, 1, 1),   -- Inglaterra
(15, 'D', 1, 1, 0, 0, 2, 0, 3),   -- EE.UU.
(16, 'D', 1, 0, 0, 1, 0, 2, 0);   -- Australia

COMMIT;
