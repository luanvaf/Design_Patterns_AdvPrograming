# Design Pattern: Decorator


class OrcamentoExame:

    def __init__(self, orcamento):
        self._orcamento = orcamento

    def calcular(self):
        return self._orcamento


class Particular(OrcamentoExame):

    def __init__(self, valor):
        self._valor = valor

    def calcular(self):
        return self._valor.calcular() * 0.90


class aVista(OrcamentoExame):

    def __init__(self, valor):
        self._valor = valor

    def calcular(self):
        return self._valor.calcular() * 0.90

class Cartao(OrcamentoExame):

    def __init__(self, valor):
        self._valor = valor

    def calcular(self):
        return self._valor.calcular() * 1.10


if __name__ == '__main__':

    orcamento = OrcamentoExame(1000)
    orcamento_particular = Particular(orcamento)
    orcamento_particular_a_vista = Particular(aVista(orcamento))
    orcamento_cartao = Cartao(orcamento)

    print(f'O valor original é: {orcamento.calcular()}')
    print(f'Desconto de 10% e o valor novo é: {orcamento_particular.calcular()}')
    print(f'Desconto de 10% no valor particular: {orcamento_particular_a_vista.calcular()}')
    print(f'O valor no cartão é: {orcamento_cartao.calcular()}')
