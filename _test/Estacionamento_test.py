import pytest

from Estacionamento import Estacionamento
from Acesso import Acesso

estacionamento_1 = Estacionamento('Estacionamento 1', 100, 0, 30, 102.0, 120.0, 54.0, 600.0, 50.0, '06:00', '22:00', '19:00', '08:00', 0.5)

estacionamento_2 = Estacionamento('Estacionamento 2', 200, 0, 20, 72.0, 70.0, 21.0, 455.0, 60.0, '00:00', '23:59', '21:00', '07:00', 0.6)

estacionamento_3 = Estacionamento('Estacionamento 3', 400, 0, 10, 40.0, 50.0, 20.0, 350.0, 40.0, '06:00', '22:00', '20:00', '08:00', 0.7)

#------------------------------------ Horas Cheias ------------------------------------

@pytest.mark.TesteFuncional
def teste_1_horas_cheias():
    acesso = Acesso('AA00M', '12/07/2022 08:00', '12/07/2022 09:00', 30.0, 0.5)
    assert estacionamento_1.calcula_acesso_horas_cheias(acesso) == 102.0

@pytest.mark.TesteFuncional
def teste_2_horas_cheias():
    acesso = Acesso('AA01M', '12/07/2022 12:00', '12/07/2022 14:00', 30.0, 0.5)
    assert estacionamento_1.calcula_acesso_horas_cheias(acesso) == 204.0

@pytest.mark.TesteFuncional
def teste_3_horas_cheias():
    acesso = Acesso('HI139', '12/07/2022 08:30', '12/07/2022 09:30', 20.0, 0.6)
    assert estacionamento_2.calcula_acesso_horas_cheias(acesso) == 72.0

#------------------------------------ Acesso Noturno ------------------------------------

@pytest.mark.TesteFuncional
def teste_1_acesso_noturno():
    acesso = Acesso('RM3A9', '12/07/2022 21:01', '13/07/2022 06:59', 30.0, 0.5)
    assert estacionamento_1.calcula_acesso_noturno(acesso) == 54.0

@pytest.mark.TesteFuncional
def teste_2_acesso_noturno():
    acesso = Acesso('JF42A', '12/07/2022 11:00', '13/07/2022 03:30', 20.0, 0.6)
    assert estacionamento_2.calcula_acesso_noturno(acesso) == 21.0

@pytest.mark.TesteFuncional
def teste_3_acesso_noturno():
    acesso = Acesso('AB64A', '12/07/2022 22:00', '13/07/2022 07:59', 10.0, 0.7)
    assert estacionamento_3.calcula_acesso_noturno(acesso) == 20.0

#------------------------------------ Acesso Diurno ------------------------------------

@pytest.mark.TesteFuncional
def teste_1_acesso_diurno():
    acesso = Acesso('RM3A9', '12/07/2022 07:01', '12/07/2022 16:59', 30.0, 0.5)
    assert estacionamento_1.calcula_acesso_diurno(acesso) == 120.0

@pytest.mark.TesteFuncional
def teste_2_acesso_diurno():
    acesso = Acesso('JF42A', '12/07/2022 11:00', '12/07/2022 22:30', 20.0, 0.6)
    assert estacionamento_2.calcula_acesso_diurno(acesso) == 70.0

@pytest.mark.TesteFuncional
def teste_3_acesso_diurno():
    acesso = Acesso('AB64A', '12/07/2022 17:00', '13/07/2022 03:59', 10.0, 0.7)
    assert estacionamento_3.calcula_acesso_diurno(acesso) == 50.0
    
#------------------------------------ Acesso por Frações ------------------------------------

@pytest.mark.TesteFuncional
def teste_1_fracao():
    acesso = Acesso('RM3A9', '15/07/2022 07:01', '15/07/2022 07:46', 30.0, 0.5)
    assert estacionamento_1.calcula_acesso_fracao(acesso) == 90.0

@pytest.mark.TesteFuncional
def teste_2_fracao():
    acesso = Acesso('JF42A', '15/07/2022 11:23', '15/07/2022 11:34', 20.0, 0.6)
    assert estacionamento_2.calcula_acesso_fracao(acesso) == 20.0

@pytest.mark.TesteFuncional
def teste_3_fracao():
    acesso = Acesso('AB64A', '15/07/2022 17:37', '15/07/2022 18:12', 10.0, 0.7)
    assert estacionamento_3.calcula_acesso_fracao(acesso) == 30.0
    
#------------------------------------ Acesso por Evento ------------------------------------

@pytest.mark.TesteFuncional
def teste_1_evento():
    acesso = Acesso('RM3A9', '15/07/2022 08:31', '15/07/2022 16:29', 50.0, 0.5)
    assert estacionamento_1.calcula_acesso_evento(acesso) == 50.0

@pytest.mark.TesteFuncional
def teste_2_evento():
    acesso = Acesso('JF42A', '15/07/2022 14:58', '15/07/2022 23:07', 60.0, 0.6)
    assert estacionamento_2.calcula_acesso_evento(acesso) == 60.0

@pytest.mark.TesteFuncional
def teste_3_evento():
    acesso = Acesso('AB64A', '15/07/2022 06:05', '15/07/2022 21:17', 40.0, 0.7)
    assert estacionamento_3.calcula_acesso_evento(acesso) == 40.0
    
#------------------------------------ Acesso Mensalista ------------------------------------

@pytest.mark.TesteFuncional
def teste_1_mensalista():
    acesso = Acesso('RM3A9', '16/07/2022 08:31', '16/07/2022 16:29', 50.0, 0.5)
    assert estacionamento_1.calcula_acesso_mensalista(acesso) == 600.0

@pytest.mark.TesteFuncional
def teste_2_mensalista():
    acesso = Acesso('JF42A', '16/07/2022 14:58', '16/07/2022 23:07', 60.0, 0.6)
    assert estacionamento_2.calcula_acesso_mensalista(acesso) == 455.0

@pytest.mark.TesteFuncional
def teste_3_mensalista():
    acesso = Acesso('AB64A', '16/07/2022 06:05', '16/07/2022 21:17', 40.0, 0.7)
    assert estacionamento_3.calcula_acesso_mensalista(acesso) == 350.0

#------------------------------------ Valor Contratante ------------------------------------

@pytest.mark.TesteFuncional
def teste_1_contratante():
    acesso = Acesso('RM3A9', '15/07/2022 08:31', '15/07/2022 16:29', 50.0, 0.5)
    assert estacionamento_1.calcula_valor_contratante(acesso, 50.0) == 25.0

@pytest.mark.TesteFuncional 
def teste_2_contratante():
    acesso = Acesso('JF42A', '12/07/2022 11:00', '12/07/2022 22:30', 20.0, 0.6)
    assert estacionamento_2.calcula_valor_contratante(acesso, 70.0) == 42.0

@pytest.mark.TesteFuncional
def teste_3_contratante():
    valorTotalContratante = 0
    acesso1 = Acesso('RM3A9', '15/07/2022 07:01', '15/07/2022 07:46', 30.0, 0.5)
    acesso2 = Acesso('AB64A', '15/07/2022 08:31', '15/07/2022 16:29', 50.0, 0.5)
    acesso3 = Acesso('JF42A', '12/07/2022 07:01', '12/07/2022 16:59', 30.0, 0.5)
    valorTotalContratante += estacionamento_1.calcula_valor_contratante(acesso1, estacionamento_1.calcula_acesso_fracao(acesso1))
    valorTotalContratante += estacionamento_1.calcula_valor_contratante(acesso2, estacionamento_1.calcula_acesso_evento(acesso2))
    valorTotalContratante += estacionamento_1.calcula_valor_contratante(acesso3, estacionamento_1.calcula_acesso_diurno(acesso3))
    assert valorTotalContratante == 130.0

