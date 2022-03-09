# Importação de metaclasse para criação de classe abstrata
from abc import ABCMeta, abstractmethod


class MarcaConsulta(metaclass=ABCMeta):

    @abstractmethod
    def marcarConsultaNormal(self):
        pass

    @abstractmethod
    def marcarConsultaPediatria(self):
        pass


class ConsultaCardiologia(MarcaConsulta):
    def marcarConsultaNormal(self):
        return ConsultaCardiologiaNormal()

    def marcarConsultaPediatria(self):
        return ConsultaCardiologiaPediatria()


class ConsultaOrtopedia(MarcaConsulta):
    def marcarConsultaNormal(self):
        return ConsultaOrtopediaNormal()

    def marcarConsultaPediatria(self):
        return ConsultaOrtopediaPediatra()


class ConsNormal(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, ConsNormal):
        pass


class ConsPediatria(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, ConsPediatria):
        pass


class ConsultaOrtopediaNormal(ConsNormal):
    def prepare(self):
        print("Marcando", type(self).__name__)


class ConsultaOrtopediaPediatra(ConsPediatria):
    def serve(self, ConsNormal):
        print("Marcando", type(self).__name__, "Foi Marcacado", type(ConsNormal).__name__)


class ConsultaCardiologiaNormal(ConsNormal):
    def prepare(self):
        print("Marcando", type(self).__name__)


class ConsultaCardiologiaPediatria(ConsPediatria):
    def serve(self, ConsNormal):
        print("Marcando", type(self).__name__, "Foi Marcacado", type(ConsNormal).__name__)
