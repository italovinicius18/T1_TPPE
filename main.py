import locale
locale.setlocale( locale.LC_ALL, 'pt_BR.UTF-8' )

from Estacionamento import Estacionamento
from Acesso import Acesso
from datetime import datetime

dados = {'Estacionamento 1': [],
'Estacionamento 2': [],
'Estacionamento 3': []}
estacionamento_1 = Estacionamento('Estacionamento 1', 100, 0, 30, 102.0, 120.0, 54.0, 600.0, 50.0, '06:00', '22:00', '19:00', '08:00', 0.5)
estacionamento_2 = Estacionamento('Estacionamento 2', 200, 0, 20, 72.0, 70.0, 21.0, 455.0, 60.0, '00:00', '23:59', '21:00', '07:00', 0.6)
estacionamento_3 = Estacionamento('Estacionamento 3', 400, 0, 10, 40.0, 50.0, 20.0, 350.0, 40.0, '06:00', '22:00', '20:00', '08:00', 0.7)
    
def calcula_estacionamento(acesso, num_estacionamento, acessoEvento, acessoMensalista):
    if(num_estacionamento==1):
        estacionamento = estacionamento_1
    elif(num_estacionamento==2):
        estacionamento = estacionamento_2
    else:
        estacionamento = estacionamento_3

    if acessoEvento.lower() == 'n' and acessoMensalista.lower() == 'n':
        dados[f'Estacionamento {num_estacionamento}'].append(definir_tipo_acesso(acesso, estacionamento)[1])
    elif acessoEvento.lower() == 's' and acessoMensalista.lower() == 'n':
        dados[f'Estacionamento {num_estacionamento}'].append(estacionamento.calcula_valor_contratante(acesso, estacionamento.calcula_acesso_evento(acesso)))
    elif acessoEvento.lower() == 'n' and acessoMensalista.lower() == 's':
        dados[f'Estacionamento {num_estacionamento}'].append(estacionamento.calcula_valor_contratante(acesso, estacionamento.calcula_acesso_mensalista(acesso)))

class Cadastrar_acesso():
    def __init__(self):
        self.__estacionamento = int(input('Escolha o estacionamento (1, 2 ou 3): '))
        self.__placa = input('Digite a placa do veículo: ')
        self.__dadoEntrada = input('Digite a data e hora de entrada(dd/MM/yyyy hh:mm): ')
        self.__dadoSaida = input('Digite a data e hora de saída(dd/MM/yyyy hh:mm): ')
        self.__acessoEvento = input('Você está acessando o estacionamento para evento? (s/n): ')
        self.__acessoMensalista = input('Você paga mensalidade no estacionamento? (s/n): ')


    def define_acesso(self):
        if self.__estacionamento == 1:
            acesso = Acesso(self.__placa, self.__dadoEntrada, self.__dadoSaida, 30.0, 0.5)
            calcula_estacionamento(acesso, self.__estacionamento, self.__acessoEvento, self.__acessoMensalista)
                     
        elif self.__estacionamento == 2:
            acesso = Acesso(self.__placa, self.__dadoEntrada, self.__dadoSaida, 20.0, 0.6)
            calcula_estacionamento(acesso, self.__estacionamento, self.__acessoEvento, self.__acessoMensalista)

        elif self.__estacionamento == 3:
            acesso = Acesso(self.__placa, self.__dadoEntrada, self.__dadoSaida, 10.0, 0.7)
            calcula_estacionamento(acesso, self.__estacionamento, self.__acessoEvento, self.__acessoMensalista)


def apurar_acesso():
    print('\n===========================================\n')
    print(f'Valor apurado do Estacionamento 1 = {locale.currency(sum(dados["Estacionamento 1"]), grouping=True)}')
    print(f'Valor apurado do Estacionamento 2 = {locale.currency(sum(dados["Estacionamento 2"]), grouping=True)}')
    print(f'Valor apurado do Estacionamento 3 = {locale.currency(sum(dados["Estacionamento 3"]), grouping=True)}')
    print('\n===========================================\n')


def menu():
    print('1 - Cadastrar acesso')
    print('2 - Apurar valores de acesso')
    print('3 - Sair')
    opcao = int(input('Digite a opção desejada: '))

# 01/02/2022 08:30
    if opcao == 1:
        classe = Cadastrar_acesso()
        classe.define_acesso()
        
    elif opcao == 2:
        apurar_acesso()

    elif opcao == 3:
        print('Saindo do programa...')
        exit()
    else:
        print('Opcao invalida, escolha outra opcao')

def main():
    while True:
        menu()

def formataHora(dado):
    formato = "%d/%m/%Y %H:%M"
    return datetime.strptime(dado, formato)

def formataHoraNoturno(horario):
    formato = "%H:%M"
    return datetime.strptime(horario, formato)

def calculaValorTotal(acesso, estacionamento, tempoIntervalo, horaEntrada, horaNoturnoFixoEntrada, horaSaida, horaNoturnoFixoSaida):
    if (horaEntrada.hour >= horaNoturnoFixoEntrada.hour) and (horaEntrada.hour <= 23) and (horaSaida.hour < horaNoturnoFixoSaida.hour):
        return estacionamento.calcula_acesso_noturno(acesso)
    else:
        if tempoIntervalo.seconds >= 9*3600:
            return estacionamento.calcula_acesso_diurno(acesso)
        else:
            if tempoIntervalo.seconds >= 1*3600:
                horasCheias = estacionamento.calcula_acesso_horas_cheias(acesso)
                horasFracao = estacionamento.calcula_acesso_fracao(acesso)
            elif tempoIntervalo.seconds < 3600:
                horasCheias = 0
                horasFracao = estacionamento.calcula_acesso_fracao(acesso)
            return horasCheias + horasFracao
    

def definir_tipo_acesso(acesso, estacionamento):
    tempoIntervalo = acesso.diferenca_tempo()
    horaEntrada = formataHora(acesso.dadoEntrada)
    horaSaida = formataHora(acesso.dadoSaida)
    horaNoturnoFixoEntrada = formataHoraNoturno(estacionamento.horarioNoturnoInicial)
    horaNoturnoFixoSaida = formataHoraNoturno(estacionamento.horarioNoturnoFinal)

    valorTotal = calculaValorTotal(acesso, estacionamento, tempoIntervalo, horaEntrada, horaNoturnoFixoEntrada, horaSaida, horaNoturnoFixoSaida)
    return valorTotal, estacionamento.calcula_valor_contratante(acesso, valorTotal)

if __name__ == "__main__":
    main()