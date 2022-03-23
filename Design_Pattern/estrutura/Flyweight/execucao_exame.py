# Design Pattern: flyweight

class ExecucaoExames:
    def __init__(self, exame_type):
        self.__tea_type = exame_type

    @property
    def exame_type(self):
        return self.exame_type


class ExecutorExames:
    def __init__(self):
        self.__exames_disponiveis = dict()

    def executor(self, escolha):
        if escolha not in self.__exames_disponiveis:
            self.__exames_disponiveis[escolha] = ExecucaoExames(escolha)
        return self.__exames_disponiveis[escolha]


class Laboratorio:
    def __init__(self, executor_exame):
        self.__solicitacao = dict()
        self.__executor_exame = executor_exame

    def solicitar(self, exame_type, sala):
        if sala not in self.__solicitacao:
            self.__solicitacao[sala] = list()
        self.__solicitacao[sala].append(self.__executor_exame.executor(exame_type))

    def realizar(self):
        for sala, solicitacao in self.__solicitacao.items():
            print(f'Exame realizado na sala {sala}')


if __name__ == '__main__':
    executor_exame = ExecutorExames()
    lab = Laboratorio(executor_exame)

    lab.solicitar('Exame de Sangue', 1)
    lab.solicitar('Exame de Vista', 2)
    lab.solicitar('Exame Cardíaco', 3)

    lab.realizar()