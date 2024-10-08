-- estados = e, cidades = c colocamos apelidos para facilitar a busca de cada tabela
-- importante fazer um filtro com WHERE para ele não fazer uma pesquisa cartesiano
SELECT 
    e.nome as Estado,
    c.nome as Cidade,
    regiao as Região
FROM estados e, cidades c
WHERE e.id = c.estado_id;

-- INNER JOIN  faz uma junção
SELECT
    c.nome as Cidade,
    e.nome as Estado,
    regiao as Região
FROM estados e
INNER JOIN cidades c on e.id = c.estado_id