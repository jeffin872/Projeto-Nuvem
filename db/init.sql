--Criando uma tabela e inserindo alguns dados

CREATE TABLE IF NOT EXISTS usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(20) NOT NULL
);

INSERT INTO usuario (nome, cpf, email, senha) VALUES 
('Jefferson Rocha', '12345678901', 'jefferson@ufca.edu.br', 'senha123'),
('Admin Sistema', '98765432100', 'admin@projeto.com', 'admin789'),
('Usuario Teste', '11122233344', 'teste@gmail.com', 'teste456');