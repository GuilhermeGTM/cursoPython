SELECT * FROM prefeitos;
SELECT * FROM cidades;

-- INNER JOIN busca tudo relacionado com as tabelas prefeitos e cidades
SELECT * FROM cidades c INNER JOIN prefeitos p ON c.id = p.cidade_id;

-- LEFT OUTER JOIN ou LEFT JOIN que é a mesma coisa
-- busca tudo que está relacionado a prefeitos e cidades + tudo da tabela esquerda cidades
-- trazendo até as cidades sem prefeitos cadastrados
SELECT * FROM cidades c LEFT OUTER JOIN prefeitos p ON c.id = p.cidade_id;

-- RIGHT JOIN busca a relação de prefetios e cidades + tudo da tabela direita prefeitos
-- trazendo até os prefeitos sem cidades cadastradas
SELECT * FROM cidades c RIGHT JOIN prefeitos p ON c.id = p.cidade_id;

-- nesse caso o mysql não suporta o FUll join que seria o exemplo abaixo
-- SELECT * FROM cidades c FULL JOIN prefeitos p ON c.id = p.cidade_id;
-- assim usamos UNION que faz a junção das consultas
-- buscando tudo que tem nas tabelas
-- Detalhe se usar UNION ALL ele traz as duplicações tbm
SELECT * FROM cidades c LEFT OUTER JOIN prefeitos p ON c.id = p.cidade_id
UNION
SELECT * FROM cidades c RIGHT JOIN prefeitos p ON c.id = p.cidade_id;
