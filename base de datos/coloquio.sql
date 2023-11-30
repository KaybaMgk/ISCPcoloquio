create database coloquio;
use coloquio;

CREATE TABLE leyes(
id_leyes INT PRIMARY KEY AUTO_INCREMENT,
nro_leyes INT,
fecha DATE,
descripcion VARCHAR(1000),
categoria VARCHAR(35),
jurisdiccion VARCHAR(35),
or_legislativo VARCHAR(200),
palabra_clave VARCHAR(200)
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    contraseña VARCHAR(100) NOT NULL
);


select * from leyes;
select * from usuarios;
