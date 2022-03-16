# Design Pattern: Builder

# Adaptar código abaixo

# Abstract course
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
    """Class for Exame de Sangue """

    def Preco(self):
        self.preco = 8000

    def vagas_disponiveis(self):
        self.vagas = 5

    def __str__(self):
        return "EDS"


# concrete exame
class EDV(Exame):
    """Class for Exame de Vista"""

    def Preco(self):
        self.preco = 10000

    def vagas_disponiveis(self):
        self.vagas = 4

    def __str__(self):
        return "EDV"


# concrete exame
class EDC(Exame):
    """Class for Exame de Coração"""

    def Preco(self):
        self.preco = 5000

    def vagas_disponiveis(self):
        self.vagas = 7

    def __str__(self):
        return "EDC"


# Complex Exame
class ComplexExame:

    def __repr__(self):
        return 'Preco : {0.preco} | vagas_disponiveis: {0.vagas}'.format(self)


# Complex course
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

    return exame  # return the exame object


# main method
if __name__ == "__main__":
    eds = EDS()  # object for EDS Exame
    edv = EDV()  # object for EDV Exame
    edc = EDC()  # object for EDC Exame

    complex_exame = construct_exame(Complexexame)
    print(complex_exame)