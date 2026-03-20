CREATE DATABASE inventario;

\c inventario

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    categoria TEXT,
    stock INT DEFAULT 0,
    precio DECIMAL(10,2),
    estado TEXT DEFAULT 'disponible'
);

INSERT INTO productos (nombre, categoria, stock, precio, estado) VALUES
('Laptop Gamer', 'Computación', 5, 1200.00, 'disponible'),
('Mouse Inalámbrico', 'Accesorios', 50, 25.50, 'disponible'),
('Monitor 24 pulgadas', 'Computación', 12, 180.00, 'disponible'),
('Teclado Mecánico', 'Accesorios', 0, 85.00, 'agotado'),
('Memoria RAM 16GB', 'Componentes', 20, 75.00, 'disponible'),
('Disco Duro 1TB', 'Componentes', 8, 50.00, 'disponible'),
('Cable HDMI 2m', 'Accesorios', 100, 10.00, 'disponible'),
('Silla Ergonómica', 'Muebles', 3, 250.00, 'disponible');

-- UPDATE

UPDATE productos SET precio = 30.00 WHERE nombre = 'Mouse Inalámbrico';

-- Cambiar a no disponible cuando el stock sea 0

UPDATE productos SET estado = 'no disponible' WHERE stock = 0;

-- TRANSACCIONES 
-- INDICAMOS QUE VAMOS A INICIAR UNA TRANSACCION
BEGIN;
UPDATE productos SET precio = 3;


-- Si queremos dejar sin efecto las modificaciones, inserciones o eliminaciones 
ROLLBACK;

-- Indicamos que todas las acciones en la transaccion esta ok y queremos guardarlas de manera permanente
COMMIT;

-- DELETE 

DELETE FROM productos WHERE id = 7;

-- SELECT
-- pARA PONER EL ALIAS SE USA EL AS
-- TAMBIEN ES OPCIONAL DEJAR SOLO UN ESPACIO
SELECT nombre, precio AS costo_unitario FROM productos;

SELECT nombre,precio AS costo_unitario
FROM productos
WHERE precio > 40.00;

-- en where se puede poner 
-- >, >=, <, <=, =, != o <> (diferente)

-- Se puede utilizar AND y OR
SELECT nombre,precio AS costo_unitario
FROM productos
WHERE precio > 40.00 AND precio < 80.00;

-- ordenamientos 
SELECT *
FROM productos
ORDER BY id ASC; --- DESC

-- Se pueden agregar varios ordenamientos si se repite

SELECT *
FROM productos
ORDER BY categoria ASC, nombre DESC;


--Paginacion
SELECT *
FROM productos;
LIMIT 2
OFFSET 0;