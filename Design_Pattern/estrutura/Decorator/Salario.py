# Design Pattern: Decorator

from Design_Pattern.estrutura.impostos import ICMS, ICPP, IKCV, ISS


class CalculadorImpostos:
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':

    from Design_Pattern.estrutura.orcamento import Orcamento, Item

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('item 0', 50.0))
    orcamento.adiciona_item(Item('item 1', 200.0))
    orcamento.adiciona_item(Item('item 2', 250.0))

    calculador = CalculadorImpostos()

    print('ISS e ICMS')
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print('ISS com ICMS')
    calculador.realiza_calculo(orcamento, ISS(ICMS()))

    print('ICPP e IKCV')
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

    print('ICPP com IKCV')
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))