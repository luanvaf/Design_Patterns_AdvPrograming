# Factory Method

from abc import ABCMeta, abstractmethod


class Secao(metaclass=ABCMeta):

    @abstractmethod
    def descricao(self):
        pass


class SecaoPaciente(Secao):
    def descricao(self):
        print("Seção Paciente")


class SecaoMedico(Secao):
    def descricao(self):
        print("Seção Médico")


class SecaoAdmin(Secao):
    def descricao(self):
        print("Seção ADMIN")


class CriadorPerfil(metaclass=ABCMeta):
    def __init__(self):
        self.secoes = []
        self.criarPerfil()

    @abstractmethod
    def criarPerfil(self):
        pass

    def getSecao(self):
        return self.secoes

    def addSecao(self, secao):
        self.secoes.append(secao)


class Exames(CriadorPerfil):
    def criarPerfil(self):
        self.addSecao(SecaoMedico())
        self.addSecao(SecaoAdmin())


class Resultados(CriadorPerfil):
    def criarPerfil(self):
        self.addSecao(SecaoMedico())
        self.addSecao(SecaoPaciente())
        self.addSecao(SecaoAdmin())


class Marcacao(CriadorPerfil):
    def criarPerfil(self):
        self.addSecao(SecaoMedico())
        self.addSecao(SecaoPaciente())
        self.addSecao(SecaoAdmin())


tipo_perfil = "Exames"
perfil = eval(tipo_perfil)()
print("Criando perfil", type(perfil).__name__)

tipo_perfil2 = "Resultados"
perfil2 = eval(tipo_perfil2)()
print("Criando perfil", type(perfil2).__name__)

tipo_perfil3 = "Marcacao"
perfil3 = eval(tipo_perfil3)()
print("Criando perfil", type(perfil3).__name__)
