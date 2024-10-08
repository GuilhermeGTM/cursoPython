class Data:
    # por parametro todos metodos associado a uma classe recebe self
    # no momento que eu chamar o metodo __str__ o self passa a ser d1 e d2
    # metodo __str__ ele é do python ele converte de forma implicita \
    # no exemplo o int em string
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1)

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2)
