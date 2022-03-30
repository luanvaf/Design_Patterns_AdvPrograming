# Design Pattern: Builder

# Adaptar código abaixo

# Abstract Exame
class Exame:

    def __init__(self):
        self.Preco()
        self.vagas_disponiveis()

    def Preco(self):
        raise NotImplementedError

    def vagas_disponiveis(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Preco : {0.preco} | Vagas disponiveis : {0.vagas}'.format(self)


# concrete exames
class EDS(Exame):
    """Classe para Exame de Sangue """

    def Preco(self):
        self.preco = 8000

    def vagas_disponiveis(self):
        self.vagas = 5

    def __str__(self):
        return "Exame de Sangue"


# concrete exame
class EDV(Exame):
    """Class para Exame de Vista"""

    def Preco(self):
        self.preco = 10000

    def vagas_disponiveis(self):
        self.vagas = 4

    def __str__(self):
        return "Exame de Vista"


# concrete exame
class EDC(Exame):
    """Class for Exame de Coração"""

    def Preco(self):
        self.preco = 5000

    def vagas_disponiveis(self):
        self.vagas = 7

    def __str__(self):
        return "Exame de Coração"


# Complex Exame
# Caso para quando é necessário criar o método builder a parte (apenas para estudo)
class ComplexExame:

    def __repr__(self):
        return 'Preco : {0.preco} | vagas_disponiveis: {0.vagas}'.format(self)


# Complex Exame
class Complexexame(ComplexExame):

    def Preco(self):
        self.preco = 7000

    def vagas_disponiveis(self):
        self.vagas = 6


# construct exame
def construct_exame(cls):
    exame = cls()
    exame.Preco()
    exame.vagas_disponiveis()

    return exame  # retorna o obj exame


# main method
if __name__ == "__main__":
    eds = EDS()  # objeto para EDS Exame
    edv = EDV()  # objeto para EDV Exame
    edc = EDC()  # objeto para EDC Exame

    print(eds)
    print(eds.__repr__())
    print(f'Preço do Exame de sangue: {eds.preco}')
    print(f'Preço do Exame de Coração: {edc.preco}')

    #complex_exame = construct_exame(Complexexame)
    #print(f'Dados do exame complexo: {complex_exame}')
