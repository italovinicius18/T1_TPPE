import pytest

from Estacionamento import Estacionamento
from Acesso import Acesso

estacionamento_1 = Estacionamento('Estacionamento 1', 100, 0, 30, 102.0, 120.0, 54.0, 1.0, 1.0, '08:00', '18:00', '00:00', '23:59', 'R$ 0,00')

estacionamento_2 = Estacionamento('Estacionamento 2', 200, 0, 20, 72.0, 70.0, 21.0, 1.0, 1.0, '08:00', '18:00', '00:00', '23:59', 'R$ 0,00')

estacionamento_3 = Estacionamento('Estacionamento 3', 400, 0, 10, 40.0, 50.0, 20.0, 1.0, 1.0, '08:00', '18:00', '00:00', '23:59', 'R$ 0,00')

#------------------------------------ Horas Cheias ------------------------------------

@pytest.mark.TesteFuncional
def teste_1_horas_cheias():
    acesso = Acesso('AA00M', '12/07/2022 08:00', '12/07/2022 09:00', 'horas cheias', '30.0', '0.5')
    assert estacionamento_1.calcula_acesso_horas_cheias(acesso) == 102.0

@pytest.mark.TesteFuncional
def teste_2_horas_cheias():
    acesso = Acesso('AA01M', '12/07/2022 12:00', '12/07/2022 14:00', 'horas cheias', '30.0', '0.5')
    assert estacionamento_1.calcula_acesso_horas_cheias(acesso) == 204.0

@pytest.mark.TesteFuncional
def teste_3_horas_cheias():
    acesso = Acesso('HI139', '12/07/2022 08:30', '12/07/2022 09:30', 'horas cheias', '20.0', '0.6')
    assert estacionamento_2.calcula_acesso_horas_cheias(acesso) == 72.0

#------------------------------------ Acesso Noturno ------------------------------------

@pytest.mark.TesteFuncional
def teste_1_acesso_noturno():
    acesso = Acesso('RM3A9', '12/07/2022 21:01', '13/07/2022 06:59', 'acesso noturno', '30.0', '0.5')
    assert estacionamento_1.calcula_acesso_noturno(acesso) == 54.0

@pytest.mark.TesteFuncional
def teste_2_acesso_noturno():
    acesso = Acesso('JF42A', '12/07/2022 11:00', '13/07/2022 03:30', 'acesso noturno', '20.0', '0.6')
    assert estacionamento_2.calcula_acesso_noturno(acesso) == 21.0

@pytest.mark.TesteFuncional
def teste_3_acesso_noturno():
    acesso = Acesso('AB64A', '12/07/2022 22:00', '13/07/2022 07:59', 'acesso noturno', '10.0', '0.7')
    assert estacionamento_3.calcula_acesso_noturno(acesso) == 20.0

#------------------------------------ Acesso Diurno ------------------------------------

@pytest.mark.TesteFuncional
def teste_1_acesso_diurno():
    acesso = Acesso('RM3A9', '12/07/2022 07:01', '12/07/2022 16:59', 'acesso diurno', '30.0', '0.5')
    assert estacionamento_1.calcula_acesso_diurno(acesso) == 120.0

@pytest.mark.TesteFuncional
def teste_2_acesso_diurno():
    acesso = Acesso('JF42A', '12/07/2022 11:00', '12/07/2022 22:30', 'acesso diurno', '20.0', '0.6')
    assert estacionamento_2.calcula_acesso_diurno(acesso) == 70.0

@pytest.mark.TesteFuncional
def teste_3_acesso_diurno():
    acesso = Acesso('AB64A', '12/07/2022 17:00', '13/07/2022 03:59', 'acesso diurno', '10.0', '0.7')
    assert estacionamento_3.calcula_acesso_diurno(acesso) == 50.0