#Design Pattern: Abstract Factory


# Importação de metaclasse para criação de classe abstrata
from Design_Pattern.criacao.AbstractFactory.consulta import ConsultaCardiologia, ConsultaOrtopedia

class Consultorio:

    def __init__(self):
        pass

    def marcarConsultas(self):
        for fabrica in [ConsultaCardiologia(), ConsultaOrtopedia()]:
            self.fabrica = fabrica
            self.marcarConsultaAdulto = self.fabrica.marcarConsultaAdulto()
            self.marcarConsultaCrianca = self.fabrica.marcarConsultaCrianca()
            self.marcarConsultaAdulto.prepare()
            self.marcarConsultaCrianca.serve(self.marcarConsultaAdulto)


consulta = Consultorio()
consulta.marcarConsultas()