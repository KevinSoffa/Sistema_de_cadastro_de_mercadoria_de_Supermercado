CREATE SCHEMA IF NOT EXISTS `mercado`;
USE `mercado`;

CREATE TABLE IF NOT exists `admin`(
	idAdmin INT(11) NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    status int(11) NOT NULL,
    primary key(`idAdmin`)
);

CREATE TABLE IF NOT exists `produtos`(
	idProdutos INT(11) NOT NULL AUTO_INCREMENT,
    nomeProduto VARCHAR(80) NOT NULL,
    quantidade INT(4) NOT NULL,
    tipo int(2),
    primary key(`idProdutos`)
);

INSERT INTO admin (nome,email,senha,status) VALUE ('kevin','kevin@gmail.com', '123456',1);
SELECT * FROM admin;