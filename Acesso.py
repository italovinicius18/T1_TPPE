from datetime import datetime, timedelta

from Excecoes import DescricaoEmBrancoException, ValorAcessoInvalidoException

class Acesso():
    def __init__(self, *args):

        placa, dadoEntrada, dadoSaida, valorAcesso, valorContratante = args

        parametros = ['placa', 'dadoEntrada', 'dadoSaida', 'valorAcesso', 'valorContratante']

        for arg, parametro in zip(args, parametros):
            if arg == "" or arg == None:
                raise DescricaoEmBrancoException(f"{parametro} não pode ser vazio ou nulo")

        if valorAcesso == None or valorAcesso < 0 or valorContratante == None or valorContratante <= 0:
            raise ValorAcessoInvalidoException("Valor do acesso e valor do contratante não podem ser nulos ou negativos")

        self.placa = placa
        self.dadoEntrada = dadoEntrada
        self.dadoSaida = dadoSaida
        self.valorAcesso = valorAcesso
        self.valorContratante = valorContratante

    def diferenca_tempo(self):
        dadoEntrada = datetime.strptime(self.dadoEntrada , "%d/%m/%Y %H:%M")
        dadoSaida = datetime.strptime(self.dadoSaida , "%d/%m/%Y %H:%M")
        diferenca = dadoSaida - dadoEntrada
        return diferenca