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
    
    
def cadastrar_acesso():
    estacionamento = int(input('Escolha o estacionamento (1, 2 ou 3): '))
    placa = input('Digite a placa do veículo: ')
    dadoEntrada = input('Digite a data e hora de entrada(dd/MM/yyyy hh:mm): ')
    dadoSaida = input('Digite a data e hora de saída(dd/MM/yyyy hh:mm): ')
    acessoEvento = input('Você está acessando o estacionamento para evento? (s/n): ')
    acessoMensalista = input('Você paga mensalidade no estacionamento? (s/n): ')

    if estacionamento == 1:
        acesso = Acesso(placa, dadoEntrada, dadoSaida, 30.0, 0.5)
        if acessoEvento.lower() == 'n' and acessoMensalista.lower() == 'n':
            dados['Estacionamento 1'].append(definir_tipo_acesso(acesso, estacionamento_1)[1])
        elif acessoEvento.lower() == 's' and acessoMensalista.lower() == 'n':
            dados['Estacionamento 1'].append(estacionamento_1.calcula_valor_contratante(acesso, estacionamento_1.calcula_acesso_evento(acesso)))
        elif acessoEvento.lower() == 'n' and acessoMensalista.lower() == 's':
            dados['Estacionamento 1'].append(estacionamento_1.calcula_valor_contratante(acesso, estacionamento_1.calcula_acesso_mensalista(acesso)))
            
    elif estacionamento == 2:
        acesso = Acesso(placa, dadoEntrada, dadoSaida, 20.0, 0.6)
        if acessoEvento.lower() == 'n' and acessoMensalista.lower() == 'n':
            dados['Estacionamento 2'].append(definir_tipo_acesso(acesso, estacionamento_2)[1])
        elif acessoEvento.lower() == 's' and acessoMensalista.lower() == 'n':
            dados['Estacionamento 2'].append(estacionamento_2.calcula_valor_contratante(acesso, estacionamento_2.calcula_acesso_evento(acesso)))
        elif acessoEvento.lower() == 'n' and acessoMensalista.lower() == 's':
            dados['Estacionamento 2'].append(estacionamento_2.calcula_valor_contratante(acesso, estacionamento_2.calcula_acesso_mensalista(acesso)))

    elif estacionamento == 3:
        acesso = Acesso(placa, dadoEntrada, dadoSaida, 10.0, 0.7)
        if acessoEvento.lower() == 'n' and acessoMensalista.lower() == 'n':
            dados['Estacionamento 3'].append(definir_tipo_acesso(acesso, estacionamento_3)[1])
        elif acessoEvento.lower() == 's' and acessoMensalista.lower() == 'n':
            dados['Estacionamento 3'].append(estacionamento_3.calcula_valor_contratante(acesso, estacionamento_3.calcula_acesso_evento(acesso)))
        elif acessoEvento.lower() == 'n' and acessoMensalista.lower() == 's':
            dados['Estacionamento 3'].append(estacionamento_3.calcula_valor_contratante(acesso, estacionamento_3.calcula_acesso_mensalista(acesso)))


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

    if opcao == 1:
        cadastrar_acesso()
        
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