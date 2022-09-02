from datetime import datetime, timedelta
from math import ceil

horaEmSegundo = 3600
quartoDeHoraEmSegundo = 900
qtdFracaoHora = 4

class Estacionamento():

    def __init__(self, nome, capacidade, ocupadas, valorFracao,
                 valorHoraCheia, valorDiariaDiurna, valorDiariaNoturna,
                 valorAcessoMensalista, valorAcessoEvento, horarioFuncionamentoInicial, 
                 horarioFuncionamentoFinal, horarioNoturnoInicial, horarioNoturnoFinal, retornoContratante):
        self.nome = nome
        self.capacidade = capacidade
        self.ocupadas = ocupadas
        self.valorFracao = valorFracao
        self.valorHoraCheia = valorHoraCheia
        self.valorDiariaDiurna = valorDiariaDiurna
        self.valorDiariaNoturna = valorDiariaNoturna
        self.valorAcessoMensalista = valorAcessoMensalista
        self.valorAcessoEvento = valorAcessoEvento
        self.horarioFuncionamentoInicial = horarioFuncionamentoInicial
        self.horarioFuncionamentoFinal = horarioFuncionamentoFinal
        self.horarioNoturnoInicial = horarioNoturnoInicial
        self.horarioNoturnoFinal = horarioNoturnoFinal
        self.retornoContratante = retornoContratante


    def calcula_acesso_horas_cheias(self, acesso):
        global horaEmSegundo
        diferenca = acesso.diferenca_tempo()
        restoTempo = diferenca.seconds % horaEmSegundo
        valorAcesso = self.valorHoraCheia * ((diferenca.seconds - restoTempo) / horaEmSegundo)
       
        return valorAcesso

    def calcula_acesso_fracao(self, acesso):
        global horaEmSegundo
        global quartoDeHoraEmSegundo
        global qtdFracaoHora
        diferenca = acesso.diferenca_tempo()
        minutes = int(ceil((diferenca.seconds % horaEmSegundo) / quartoDeHoraEmSegundo))
        if minutes == qtdFracaoHora:
            valorAcesso = self.valorHoraCheia
        else:
            valorAcesso = self.valorFracao * minutes
        return valorAcesso


    def calcula_acesso_noturno(self, acesso):
        valorAcesso = self.valorDiariaNoturna

        return valorAcesso
    

    def calcula_acesso_diurno(self, acesso):
        valorAcesso = self.valorDiariaDiurna

        return valorAcesso
            

    def calcula_acesso_evento(self, acesso):
        valorAcesso = self.valorAcessoEvento

        return valorAcesso
    

    def calcula_acesso_mensalista(self, acesso):
        valorAcesso = self.valorAcessoMensalista

        return valorAcesso
    

    def calcula_valor_contratante(self, acesso, valorTotal):
        valorAcesso = valorTotal * self.retornoContratante

        return valorAcesso