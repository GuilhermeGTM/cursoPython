-- esse SELECT vai consultar a soma total de populaçao por regiao dos estados
-- se usa o as 'exemplo' ai na saida de dados sai oq está dentro do ''
-- GROUP BY agrupar por região
-- sum função agregadora vai somar a populacao
-- ORDER BY colocar em ordem o DESC coloca decrescente
SELECT 
    regiao as 'Região',
    SUM(populacao) as Total
FROM estados
GROUP BY regiao
ORDER BY Total DESC


-- esse SELECT me da soma total de todas populações
SELECT 
    SUM(populacao) as Total
FROM estados


-- esse SELECT me da média populacional dos estados
SELECT 
    AVG(populacao) as Total
FROM estados