 -- UPDATE nome da tabela
 -- SET oq tu quer mudar se tem mais algum item se usa ,
 -- WHERE geralmente se usa a PK(primarykey) mas no caso está usando a sigla caso n tenha o WHERE vai mudar todas linhas
 -- SEMPRE TEM QUE TER O WHERE, CASO CONTRARIO VAI ALTERAR TUDO 
 UPDATE estados
 SET nome = 'Maranhão'
 WHERE sigla = 'MA'

 SELECT nome FROM estados WHERE sigla = 'MA'

 UPDATE estados
 SET nome = 'Paraná', populacao = 11.32
 WHERE sigla = 'PR'

 SELECT nome, sigla, populacao FROM estados WHERE sigla = 'PR'
