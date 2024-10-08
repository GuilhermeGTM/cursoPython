-- todos estados
SELECT * FROM estados


-- filtrando por nome e sigla, where regiao somente do sul
SELECT nome as 'Nome do Estado', sigla FROM estados
WHERE regiao = 'Sul'

-- filtrando nome e regiao com a população >= 10 e ordenado de ordem crescente e com desc decrescente
SELECT nome, regiao, populacao FROM estados
WHERE populacao >= 10
ORDER BY populacao DESC