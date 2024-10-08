-- alterando a tabela empresas o campo cnpj que era INT para VARCHAR
ALTER TABLE empresas MODIFY cnpj VARCHAR(14);

-- Inserindo empresas
INSERT INTO empresas
    (nome, cnpj)
VALUES
    ('Bradesco', 95694186000123),
    ('Vale', 27887148000146),
    ('Cielo', 01598317000134);

-- DESC descreve a tabela
DESC empresas;
SELECT * FROM empresas;
SELECT * FROM cidades;

INSERT INTO empresas_unidades
    (empresa_id, cidade_id, sede)
VALUE
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 2);