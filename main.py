from Estacionamento import Estacionamento
from Acesso import Acesso
from datetime import datetime

dados = {}

def main():
    estacionamento_1 = Estacionamento('Estacionamento 1', 100, 0, 30, 102.0, 120.0, 54.0, 600.0, 50.0, '06:00', '22:00', '19:00', '08:00', 0.5)
    acesso1 = Acesso('AA00M', '12/07/2022 12:31', '12/07/2022 15:48', 'horas cheias', 30.0, 0.5) # horas cheias e fracao
    acesso2 = Acesso('JA60F', '12/07/2022 19:17', '13/07/2022 02:19', 'acesso noturno', 30.0, 0.5) # noturno
    acesso3 = Acesso('RE52G', '12/07/2022 08:30', '12/07/2022 17:48', 'acesso diurno', 30.0, 0.5) # diurno
    acesso4 = Acesso('RE52G', '12/07/2022 23:30', '13/07/2022 05:00', 'acesso noturno', 30.0, 0.5) # diurno

    print('Acesso1: R$', definir_tipo_acesso(acesso1, estacionamento_1))
    print('Acesso2: R$', definir_tipo_acesso(acesso2, estacionamento_1))
    print('Acesso3: R$', definir_tipo_acesso(acesso3, estacionamento_1))
    print('Acesso4: R$', definir_tipo_acesso(acesso4, estacionamento_1))

    

def definir_tipo_acesso(acesso, estacionamento):
    tempoIntervalo = acesso.diferenca_tempo()
    horaEntrada = datetime.strptime(acesso.dadoEntrada , "%d/%m/%Y %H:%M")
    horaSaida = datetime.strptime(acesso.dadoSaida , "%d/%m/%Y %H:%M")
    horaNoturnoFixoEntrada = datetime.strptime(estacionamento.horarioNoturnoInicial , "%H:%M")
    horaNoturnoFixoSaida = datetime.strptime(estacionamento.horarioNoturnoFinal , "%H:%M")
    # horarioFuncionamentoInicial = datetime.strptime(estacionamento.horarioFuncionamentoInicial , "%H:%M")
    # horarioFuncionamentoInicial = datetime.strptime(estacionamento.horarioFuncionamentoFinal , "%H:%M")
    # print(horaNoturnoFixoSaida.hour)
    # print(tempoIntervalo)
    # print(horaEntrada.hour)
    # print(horaNoturnoFixoEntrada.hour)
    
    if (horaEntrada.hour >= horaNoturnoFixoEntrada.hour) and (horaEntrada.hour <= 23) and (horaSaida.hour < horaNoturnoFixoSaida.hour):
        valorTotal = estacionamento.calcula_acesso_noturno(acesso)
        return valorTotal, estacionamento.calcula_valor_contratante(acesso, valorTotal)
    else:
        if tempoIntervalo.seconds >= 9*3600:
            valorTotal = estacionamento.calcula_acesso_diurno(acesso)
            return valorTotal, estacionamento.calcula_valor_contratante(acesso, valorTotal)
        else:
            if tempoIntervalo.seconds >= 1*3600:
                horasCheias = estacionamento.calcula_acesso_horas_cheias(acesso)
                horasFracao = estacionamento.calcula_acesso_fracao(acesso)
            elif tempoIntervalo.seconds < 3600:
                horasCheias = 0
                horasFracao = estacionamento.calcula_acesso_fracao(acesso)
            # print(horasCheias, horasFracao)
            valorTotal = horasCheias + horasFracao
            return valorTotal, estacionamento.calcula_valor_contratante(acesso, valorTotal)

if __name__ == "__main__":
    main()