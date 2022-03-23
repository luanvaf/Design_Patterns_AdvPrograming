# Design Pattern: Prototype

# import the required modules

from abc import ABCMeta, abstractmethod
import copy

class Medico(metaclass=ABCMeta):

    # constructor
    def __init__(self):
        self.nome = None
        self.especialidade = None

    @abstractmethod
    def medico(self):
        pass

    def get_especialidade(self):
        return self.especialidade

    def get_nome(self):
        return self.nome

    def set_nome(self, snome):
        self.nome = snome

    def clone(self):
        return copy.copy(self)


class Pediatra(Medico):
    def __init__(self):
        super().__init__()
        self.especialidade = "Pediatra"

    def medico(self):
        print("Inside Pediatra::medico() method")


class Cardiologista(Medico):
    def __init__(self):
        super().__init__()
        self.especialidade = "Cardiologista"

    def medico(self):
        print("Inside Cardiologista::medico() method")


# class - Courses At GeeksforGeeks Cache
class Medicos_Cache:
    # cache to store useful information
    cache = {}

    @staticmethod
    def get_medico(snome):
        Med = Medicos_Cache.cache.get(snome, None)
        return Med.clone()

    @staticmethod
    def load():
        pediatra = Pediatra()
        pediatra.set_nome("João")
        Medicos_Cache.cache[pediatra.get_nome()] = pediatra

        cardio = Cardiologista()
        cardio.set_nome("Fernando")
        Medicos_Cache.cache[cardio.get_nome()] = cardio


# main function
if __name__ == '__main__':
    Medicos_Cache.load()

    pediatra = Medicos_Cache.get_medico("João")
    print(pediatra.get_especialidade())

    cardiologista = Medicos_Cache.get_medico("Fernando")
    print(cardiologista.get_especialidade())
