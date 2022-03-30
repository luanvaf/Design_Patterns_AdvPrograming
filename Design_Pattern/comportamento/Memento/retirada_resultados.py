# Design Pattern: Memento

from datetime import date


class RetiradaResultados:
    def __init__(self, data, paciente, tipo):
        self.data = data
        self.paciente = paciente
        self.tipo = tipo

    def avanca(self):
        if self.tipo == 'AGUARDANDO RESULTADO':
            self.tipo = 'DISPONÍVEL PARA RETIRADA'
        elif self.tipo == 'DISPONÍVEL PARA RETIRADA':
            self.tipo = 'RETIRADO'
        elif self.tipo == 'RETIRADO':
            self.tipo = 'CONCLUIDO'

    def salva_estado(self):
        # Não podemos passar o self para o RetiradaResultados pois se o resultado fosse
        # alterado o estado anterior dele também seria alterado
        return Estado(
            RetiradaResultados(data=self.data, paciente=self.paciente, tipo=self.tipo)
        )

    def restaura_estado(self, estado):
        self.paciente = estado.resultado.paciente
        self.data = estado.resultado.data
        self.tipo = estado.resultado.tipo


class Estado:
    def __init__(self, resultado):
        self.__resultado = resultado

    @property
    def resultado(self):
        return self.__resultado


class Historico:
    def __init__(self):
        self.__estados_salvos = list()

    def obtem_estado(self, indice):
        return self.__estados_salvos[indice]

    def adiciona_estado(self, estado):
        self.__estados_salvos.append(estado)


if __name__ == '__main__':

    historico = Historico()

    resultado = RetiradaResultados(data=date.today(), paciente='Joao da Silva Santos', tipo='AGUARDANDO RESULTADO')
    print(resultado.paciente)
    print(resultado.tipo)

    resultado.avanca()

    print(resultado.paciente)
    print(resultado.tipo)
    historico.adiciona_estado(resultado.salva_estado())

    resultado.avanca()

    print(resultado.paciente)
    print(resultado.tipo)

    # Caso onde o nome teria sido errado
    resultado.paciente = 'Joao Ferreira Santos'

    historico.adiciona_estado(resultado.salva_estado())

    print(resultado.paciente)
    print(resultado.tipo)

    resultado.avanca()

    historico.adiciona_estado(resultado.salva_estado())

    print(resultado.paciente)
    print(resultado.tipo)

    resultado.restaura_estado(historico.obtem_estado(0))

    print(resultado.paciente)
    print(resultado.tipo)
