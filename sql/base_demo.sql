CREATE DATABASE base_demo;

USE base_demo;

CREATE TABLE datos(
     Id varchar(50) NOT NULL PRIMARY KEY,
    Nombre varchar(32) NOT NULL,
    A_Paterno varchar(20) not null,
    A_Materno varchar(20) not null,
    Direccion varchar(50) not null,
    Telefono varchar(20) not null
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO datos (Id, Nombre, A_Paterno, A_Materno, Direccion, Telefono)
VALUES ('1002','Jose Luis','Feregrino','Trejo','San Antonio','7723456892');

SHOW TABLES;

SELECT * FROM datos;

DESCRIBE datos;

SELECT "Creando un usuario y asignandolo a la base de datos" as "Mensaje";
CREATE USER 'unid'@'localhost' IDENTIFIED BY 'unid.2018';
GRANT ALL PRIVILEGES ON base_demo.* TO 'unid'@'localhost';
-- GRANT ALL PRIVILEGES ON base_demo.* TO kuorra@'%' IDENTIFIED BY 'kuorra.remote';

FLUSH PRIVILEGES;
