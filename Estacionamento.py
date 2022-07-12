class Estacionamento():
    def __init__(self, nome, capacidade, ocupadas, valorFracao,
                 valorHoraCheia, valorDiariaDiurna, valorDiariaNoturna,
                 valorAcessoMensalista, valorAcessoEvento, horarioDiurnoInicial, 
                 horarioDiurnoFinal, horarioNoturnoInicial, horarioNoturnoFinal, retornoContratante):
        self.nome = nome
        self.capacidade = capacidade
        self.ocupadas = ocupadas
        self.valorFracao = valorFracao
        self.valorHoraCheia = valorHoraCheia
        self.valorDiariaDiurna = valorDiariaDiurna
        self.valorDiariaNoturna = valorDiariaNoturna
        self.valorAcessoMensalista = valorAcessoMensalista
        self.valorAcessoEvento = valorAcessoEvento
        self.horarioDiurnoInicial = horarioDiurnoInicial
        self.horarioDiurnoFinal = horarioDiurnoFinal
        self.horarioNoturnoInicial = horarioNoturnoInicial
        self.horarioNoturnoFinal = horarioNoturnoFinal
        self.retornoContratante = retornoContratante

    def calcula_acesso_horas_cheias(self, acesso):
        return 102
