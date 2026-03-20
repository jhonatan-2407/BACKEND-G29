-- Crear base de datos llamada viajes 

CREATE DATABASE viajes;

\c viajes


-- Usando la base de datos viajes crear la tabla destinos con las siguientes columnas
-- id SERIAL y llave primaria
-- ciudad TEXTO y no puede ser nulo
-- pais TEXTO y no puede ser nulo
-- codigo_postal TEXTO y es unico
-- puntuacion ENTERO 
-- fecha_registro TIMESTAMP

CREATE TABLE destinos(
    id SERIAL PRIMARY KEY,
    ciudad TEXT NOT NULL,
    pais TEXT NOT NULL,
    codigo_postal TEXT UNIQUE,
    puntuacion INT,
    fecha_registro TIMESTAMP

);
-- Luego de crear la tabla agregar una columna llamada descripcion que sera TEXT
-- cambiar la columna puntuacion a ranking

ALTER TABLE destinos ADD COLUMN descripcion TEXT;
ALTER TABLE destinos RENAME COLUMN puntuacion TO ranking;
-- Insertar:
-- ciudad: Paris
-- pais: Francia
-- codigo_postal: 75001
-- rating: 5

-- ciudad: Tokio
-- pais: Japon
-- codigo_postal: 100-0001
-- rating: 5

INSERT INTO destinos VALUES (DEFAULT,'Paris','Francia','75001','5','2026-02-15','bonito');
INSERT INTO destinos VALUES (DEFAULT,'Tokio','Japon','100-0001','5','2025-03-20','hermoso');
-- mostrar solo la ciudad y el rating

SELECT ciudad,ranking FROM destinos;
-- mostrar todas las columnas de la tabla
SELECT * FROM destinos;