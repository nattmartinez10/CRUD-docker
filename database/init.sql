CREATE DATABASE IF NOT EXISTS crud_db;

USE crud_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    numdoc VARCHAR(50) UNIQUE,
    nombre VARCHAR(50),
    segundo_nombre VARCHAR(50),
    apellidos VARCHAR(50),
    f_nacimiento VARCHAR(50),
    genero VARCHAR(50),
    correo VARCHAR(50),
    celular VARCHAR(50),
    foto LONGBLOB
);

CREATE TABLE IF NOT EXISTS logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    document VARCHAR(50),
    fecha_transaccion DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (tipo, numdoc, nombre, segundo_nombre, apellidos, f_nacimiento, genero, correo, celular, foto)
VALUES 
('CC', '1234567890', 'Juan', 'Carlos', 'Perez', '1985-01-01', 'M', 'juan.perez@example.com', '3001234567', NULL),
('CC', '0987654321', 'Maria', 'Luisa', 'Gomez', '1990-02-02', 'F', 'maria.gomez@example.com', '3109876543', NULL);

INSERT INTO logs (tipo, document)
VALUES 
('CREATE', '1234567890'),
('CREATE', '0987654321');


