# classe abstrata

from abc import abstractmethod


class EstadoAtendimento():
    @abstractmethod
    def em_atendimento(self):
        pass

    @abstractmethod
    def esperando_na_fila(self):
        pass


class EstadoAtendimentoPreferencial(EstadoAtendimento):
    def esperando_na_fila(self):
        return "O paciente com preferencial está aguardando na fila."

    def em_atendimento(self):
        return "O paciente com preferencial está sendo atendido."


class EstadoAtendimentoNormal(EstadoAtendimento):
    def esperando_na_fila(self):
        return "O paciente está aguardando na fila."

    def em_atendimento(self):
        return "O paciente está sendo atendido."


class Paciente(EstadoAtendimento):
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def esperando_na_fila(self):
        return self.state.esperando_na_fila()

    def em_atendimento(self):
        return self.state.em_atendimento()


if __name__ == '__main__':
    person = Paciente(EstadoAtendimentoNormal())
    print("Atendimento Normal: " + person.em_atendimento())
    print("Atendimento Normal: " + person.esperando_na_fila())

    person.set_state(EstadoAtendimentoPreferencial())
    print("Atendimento Preferencial: " + person.em_atendimento())
    print("Atendimento Preferencial: " + person.esperando_na_fila())
