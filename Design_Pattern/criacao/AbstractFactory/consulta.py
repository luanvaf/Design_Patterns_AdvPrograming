# Design Pattern: Abstract Factory

from abc import ABCMeta, abstractmethod


class ConsultorioFactory(metaclass=ABCMeta):
    @abstractmethod
    def marcarConsultaAdulto(self):
        pass

    @abstractmethod
    def marcarConsultaCrianca(self):
        pass


class ConsultorioCardiologiaFactory(ConsultorioFactory):
    def marcarConsultaAdulto(self):
        return ConsultaCardiologia()

    def marcarConsultaCrianca(self):
        return ConsultaPediatria()


class ConsultorioOrtopediaFactory(ConsultorioFactory):
    def marcarConsultaAdulto(self):
        return ConsultaOrtopedia()

    def marcarConsultaCrianca(self):
        return ConsultaPediatriaOrtopedica()


class ConsultaAdulto(metaclass=ABCMeta):
    @abstractmethod
    def marcar(self, consulta):
        pass


class ConsultaCrianca(metaclass=ABCMeta):
    @abstractmethod
    def marcar(self, consulta):
        pass


class ConsultaCardiologia(ConsultaAdulto):
    def marcar(self):
        print('Marcando', type(self).__name__)


class ConsultaPediatria(ConsultaCrianca):
    def marcar(self):
        print('Marcando', type(self).__name__)


class ConsultaOrtopedia(ConsultaAdulto):
    def marcar(self):
        print('Marcando', type(self).__name__)


class ConsultaPediatriaOrtopedica(ConsultaCrianca):
    def marcar(self):
        print('Marcando', type(self).__name__)


class Consultorio:
    def consultorio(self):
        for factory in [ConsultorioCardiologiaFactory(), ConsultorioOrtopediaFactory()]:
            cons_crianca = factory.marcarConsultaCrianca()
            cons_adulto = factory.marcarConsultaAdulto()
            cons_adulto.marcar()
            cons_crianca.marcar()


if __name__ == '__main__':
    consultorio = Consultorio()
    consultorio.consultorio()