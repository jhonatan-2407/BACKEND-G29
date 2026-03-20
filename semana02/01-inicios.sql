-- este comando es de psql, no de sql por ende solo se puede usar en psql
-- sirve para listar las BD del servidor
\l

-- DML (Data Manipulation Language) sus acciones son
-- CREATE: Crear bases de datos o tablas o indices o algun componente para la base de datos
-- ALTER: Modificar alguna propiedad de la BD
-- DROP: Eliminar de manera permanente
-- TRUNCATE: Elimina la data de una tabla sin eliminar la configuracion
-- RENAME: Cambia el nombre de las entidades 
CREATE DATABASE pruebas;
-- PARA CAMBIAR DE BD
\C 
CREATE TABLE personas (
    --llave primaria | no acepte nulos | valor unica | valor por defecto
    -- PRIMARY KEY   | NULL | NOT NULL  | UNIQUE     | DEFAULT

    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT,
    correo TEXT UNIQUE,
    fecha_nacimiento TIMESTAMP 
);

-- usando el comando ALTER para modificar la tabla
ALTER TABLE personas ADD COLUMN nickname TEXT;  -- Configuraciones adicionales NOT NULL UNIQUE PRIMARY KEY DEFAULT

-- Eliminar columna
ALTER TABLE personas DROP COLUMN nickname;

-- Cambiar el nombre de una columna
ALTER TABLE personas RENAME COLUMN nombre TO nombres;

-- cambiar el tipo de dato
ALTER TABLE personas ALTER COLUMN nombres TYPE VARCHAR(200);

-- Muestra todas las tablas de la BD
\dt 

-- Muestra las tablas y sus secuenciales
\d 



-- DDL (Data Definition language)
-- INSERT
-- SELECT
-- UPDATE
-- DELETE


-- Las fechas en las BD siguen el formato ISO 8601 (de mas a menos)
INSERT INTO personas (id, nombres, apellido, correo, fecha_nacimiento) VALUES
                    ( DEFAULT, 'Eduardo Ramiro', 'de Rivero','ederrivero@gmail.com', '1992-08-01');

-- al no indicar las columnas si o si las tenemos q declarar todas
INSERT INTO personas VALUES (DEFAULT,'Roxana Diana', 'Huayra', 'rhuayra@gmail.com', '2001-03-18');


-- SELECT
SELECT id,nombres FROM personas;

-- para ver todo
SELECT * FROM personas;