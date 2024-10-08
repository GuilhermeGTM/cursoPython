-- Criando a tabela estado!
-- NOT NULLS não nulo n pode ser vazio
-- UNSIGNED sem sinal
-- ENUM para cadastrar algum valor tem que ser algum dos pré definidos
-- DECIMAL(5,2) 5 digitos e 2 pontos flutuantes pós virgula
-- UNIQUE KEY é para não tem duplicidade
create table estados(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    sigla VARCHAR(2) NOT NULL,
    regiao ENUM('Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul') NOT NULL,
    populacao DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY(nome),
    UNIQUE KEY(sigla)
);