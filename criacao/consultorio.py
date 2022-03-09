# Importação de metaclasse para criação de classe abstrata
from criacao.consulta import ConsultaCardiologia, ConsultaOrtopedia

class Consultorio:

    def __init__(self):
        pass

    def marcarConsultas(self):
        for fabrica in [ConsultaCardiologia(), ConsultaOrtopedia()]:
            self.fabrica = fabrica
            self.marcarConsultaNormal = self.fabrica.marcarConsultaNormal()
            self.marcarConsultaPediatria = self.fabrica.marcarConsultaPediatria()
            self.marcarConsultaNormal.prepare()
            self.marcarConsultaPediatria.serve(self.marcarConsultaNormal)


consulta = Consultorio()
consulta.marcarConsultas()