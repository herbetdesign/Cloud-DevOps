CREATE DATABASE IF NOT EXISTS empresa;
USE empresa;

CREATE TABLE IF NOT EXISTS funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

INSERT INTO funcionarios (nome) VALUES
('Toshiro Shibakita'),
('Docker'),
('Microsserviços'),
('NGINX'),
('Docker Swarm');
