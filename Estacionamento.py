from datetime import datetime, timedelta
from math import ceil

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
        diferenca = acesso.diferenca_tempo()
        valorAcesso = self.valorHoraCheia * diferenca.seconds / 3600
        return valorAcesso


    def calcula_acesso_noturno(self, acesso):
        valorAcesso = self.valorDiariaNoturna

        return valorAcesso
    

    def calcula_acesso_diurno(self, acesso):
        valorAcesso = self.valorDiariaDiurna

        return valorAcesso


    def calcula_acesso_fracao(self, acesso):
        diferenca = acesso.diferenca_tempo()
        minutes = int(ceil(diferenca.seconds / 900))
        print("min ", minutes)
        valorAcesso = self.valorFracao * minutes
        print(valorAcesso)

        return valorAcesso
    

    def calcula_acesso_evento(self, acesso):
        valorAcesso = self.valorAcessoEvento
        print(valorAcesso)

        return valorAcesso
    

    def calcula_acesso_mensalista(self, acesso):
        valorAcesso = self.valorAcessoMensalista
        print(valorAcesso)

        return valorAcesso
