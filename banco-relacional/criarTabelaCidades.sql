CREATE TABLE IF NOT EXISTS cidades (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    estado_id INT UNSIGNED NOT NULL,
    area DECIMAL(10,2),
    PRIMARY KEY (id),
    FOREIGN KEY (estado_id) REFERENCES estados (id)
);

--Criando uma tabela qualquer
--CREATE TABLE IF NOT EXISTS teste(
--   id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
--);

-- Deletando a tabela
--DROP TABLE IF EXIST teste;
