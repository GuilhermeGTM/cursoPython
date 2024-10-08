class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo!')
        self._idade = idade

    # metodo de instancia, recebe self como parametro
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    # metodo estatico, não recebe parametro
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapies')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # metodo de classe, recebe cls como parametro e retorna a classe
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapies(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapies('Jose')
    jose.set_idade(30)
    print(f'Nome: {jose.nome} Idade: {jose.get_idade()}')
