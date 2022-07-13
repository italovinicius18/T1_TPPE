from datetime import datetime, timedelta

class Acesso():
    def __init__(self, placa, dadoEntrada, dadoSaida, tipoAcesso, valorAcesso, valorContratante):
        self.placa = placa
        self.dadoEntrada = dadoEntrada
        self.dadoSaida = dadoSaida
        self.tipoAcesso = tipoAcesso
        self.valorAcesso = valorAcesso
        self.valorContratante = valorContratante

    def diferenca_tempo(self):
        dadoEntrada = datetime.strptime(self.dadoEntrada , "%d/%m/%Y %H:%M")
        dadoSaida = datetime.strptime(self.dadoSaida , "%d/%m/%Y %H:%M")
        diferenca = dadoSaida - dadoEntrada
        return diferenca