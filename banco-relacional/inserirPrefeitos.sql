SELECT * FROM cidades;

-- o prefeito zenaldo coutinho é null pq não é obrigatório  not null o id da cidade
INSERT INTO prefeitos
    (nome, cidade_id)
VALUE 
    ('Rodrigo Neves', 2),
    ('Raquel Lyra', 3),
    ('Zenaldo Coutinho', NULL);

 
 SELECT * FROM prefeitos;

 INSERT INTO prefeitos
    (nome, cidade_id)
VALUES
    ('Rafael Greca', NULL);

-- nesse caso vai dar erro por causa que o id 3 já foi cadastrado e ele está na tabela prefeitos como unique
--INSERT INTO prefeitos
--    (nome, cidade_id)
--VALUES
--   ('Rafael Greca', 3)