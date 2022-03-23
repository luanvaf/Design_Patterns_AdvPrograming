# Design Pattern: Iterator

class FilaPacientes:
    def __init__(self, posicao):
        self.__posicao = posicao

    @property
    def posicao(self):
        return self.__posicao


class ListaFila:
    def __init__(self):
        self.__posicoes = list()
        self.__counter = 0

    def add_na_fila(self, fila):
        self.__posicoes.append(fila)

    def remove_da_fila(self, posicao):
        for index in range(0, len(self.__posicoes)):
            if self.__posicoes[index].posicao == posicao:
                self.__posicoes.pop(index)
                break
        else:
            print('Paciente não encontrado na fila')

    def count(self):
        return len(self.__posicoes)

    def atual(self):
        return self.__posicoes[self.__counter].posicao

    def key(self):
        return self.__counter

    def __next__(self):
        self.__counter += 1

    def rewind(self):
        self.__counter = 0


if __name__ == '__main__':
    fila = ListaFila()

    fila.add_na_fila(FilaPacientes("João"))
    fila.add_na_fila(FilaPacientes("Fernando"))
    fila.add_na_fila(FilaPacientes("Márcia"))
    fila.add_na_fila(FilaPacientes("Júlia"))

    print(f'Quantidade de Pacientes na fila: {fila.count()}')
    fila.remove_da_fila("Márcia")
    print(f'Quantidade de Pacientes na fila: {fila.count()}')

    print(f'Ultimo paciente chamado: {fila.atual()}')
    next(fila)
    print(f'Ultimo paciente chamado: {fila.atual()}')