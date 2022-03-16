# Design Pattern: Factory Method

from abc import ABCMeta, abstractmethod


class Perfil(metaclass=ABCMeta):

    @abstractmethod
    def descricao(self):
        pass


class PerfilPaciente(Perfil):
    def descricao(self):
        print("Perfil Paciente")


class PerfilMedico(Perfil):
    def descricao(self):
        print("Perfil Médico")


class PerfilAdmin(Perfil):
    def descricao(self):
        print("Perfil ADMIN")


class CriadorPerfil(metaclass=ABCMeta):
    def __init__(self):
        self.perfis = []
        self.criarPerfil()

    @abstractmethod
    def criarPerfil(self):
        pass

    def getPerfil(self):
        return self.perfis

    def addPerfil(self, perfil):
        self.perfis.append(perfil)


class Exames(CriadorPerfil):
    def criarPerfil(self):
        self.addPerfil(PerfilMedico())
        self.addPerfil(PerfilAdmin())


class Resultados(CriadorPerfil):
    def criarPerfil(self):
        self.addPerfil(PerfilMedico())
        self.addPerfil(PerfilPaciente())
        self.addPerfil(PerfilAdmin())


class Marcacao(CriadorPerfil):
    def criarPerfil(self):
        self.addPerfil(PerfilMedico())
        self.addPerfil(PerfilPaciente())
        self.addPerfil(PerfilAdmin())


tipo_perfil = "Exames"
perfil = eval(tipo_perfil)()
print("Criando perfil", type(perfil).__name__)

tipo_perfil2 = "Resultados"
perfil2 = eval(tipo_perfil2)()
print("Criando perfil", type(perfil2).__name__)

tipo_perfil3 = "Marcacao"
perfil3 = eval(tipo_perfil3)()
print("Criando perfil", type(perfil3).__name__)
