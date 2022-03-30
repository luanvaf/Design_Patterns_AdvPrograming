# Design Pattern: Composite

class Colaborador:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.salario = salario

    @property
    def nome(self):
        return self.__nome


class Recepcionista(Colaborador):
    def __init__(self, nome, salario, setor=None):
        super(Recepcionista, self).__init__(nome, salario)
        self.__setor = setor

    @property
    def setor(self):
        return self.__setor


class Medico(Colaborador):
    def __init__(self, nome, salario, especialidade=None):
        super(Medico, self).__init__(nome, salario)
        self.__especialidade = especialidade

    @property
    def especialidade(self):
        return self.__especialidade


class Clinica:
    def __init__(self):
        self.__colaboradores = list()

    def add_colaborador(self, colaborador):
        self.__colaboradores.append(colaborador)

    def total_salarios(self):
        salarios = 0
        for colaborador in self.__colaboradores:
            salarios += colaborador.salario
        return salarios


if __name__ == '__main__':
    joao = Recepcionista('Joao da Silva', 1800)
    carla = Medico('Carla Camila', 1900)

    clinica = Clinica()
    clinica.add_colaborador(joao)
    clinica.add_colaborador(carla)

    print(f'Total salários: {clinica.total_salarios()}')