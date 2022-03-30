# Design Pattern: Abstract Factory

# Importação de metaclasse para criação de classe abstrata
from abc import ABCMeta, abstractmethod


class MarcaConsulta(metaclass=ABCMeta):

    @abstractmethod
    def marcarConsultaAdulto(self):
        pass

    @abstractmethod
    def marcarConsultaCrianca(self):
        pass


class ConsultaCardiologia(MarcaConsulta):
    def marcarConsultaAdulto(self):
        return ConsultaCardiologiaAdulto()

    def marcarConsultaCrianca(self):
        return ConsultaCardiologiaCrianca()


class ConsultaOrtopedia(MarcaConsulta):
    def marcarConsultaAdulto(self):
        return ConsultaOrtopediaAdulto()

    def marcarConsultaCrianca(self):
        return ConsultaOrtopediaCrianca()


class ConsAdulto(metaclass=ABCMeta):
    @abstractmethod
    def marcar(self, ConsAdulto):
        pass


class ConsCrianca(metaclass=ABCMeta):
    @abstractmethod
    def atender(self, ConsCrianca):
        pass


class ConsultaOrtopediaAdulto(ConsAdulto):
    def marcar(self):
        print("Marcando", type(self).__name__)


class ConsultaOrtopediaCrianca(ConsCrianca):
    def atender(self, ConsAdulto):
        print("Marcando", type(self).__name__, "Foi Marcacado", type(ConsAdulto).__name__)


class ConsultaCardiologiaAdulto(ConsAdulto):
    def marcar(self):
        print("Marcando", type(self).__name__)


class ConsultaCardiologiaCrianca(ConsCrianca):
    def atender(self, ConsAdulto):
        print("Marcando", type(self).__name__, "Foi Marcacado", type(ConsAdulto).__name__)
