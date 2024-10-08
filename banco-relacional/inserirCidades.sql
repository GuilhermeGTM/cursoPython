SELECT * FROM cidades

INSERT INTO cidades (nome, area, estado_id)
VALUE ('Campinas', 795, 32)

INSERT INTO cidades (nome, area, estado_id)
VALUE ('Niterói', 133.9, 26)


-- Inserindo nome, area, estado_id selecionando o id da sigla 'PE'
INSERT INTO cidades
    (nome, area, estado_id)
VALUE(
    'Caruaru',
    920.6,
    (SELECT id FROM estados WHERE sigla = 'PE'))


INSERT INTO cidades
    (nome, area, estado_id)
VALUE(
    'Juazeiro do Norte',
    248.2,
    (SELECT id FROM estados WHERE sigla = 'CE'))