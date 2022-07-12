import pytest

from Estacionamento import Estacionamento
from Acesso import Acesso

estacionamento = Estacionamento('Estacionamento 1', 100, 0, 30, 102.0, 1.0, 1.0, 1.0, 1.0, '08:00', '18:00', '00:00', '23:59', 'R$ 0,00')

@pytest.mark.TesteFuncional
def teste_1_horas_cheias():
    acesso = Acesso('AA00M', '08:00', '09:00', 'horas cheias', '30.0', '0.5')
    assert estacionamento.calcula_acesso_horas_cheias(acesso, estacionamento) == 102.0

@pytest.mark.TesteFuncional
def teste_2_horas_cheias():
    acesso = Acesso('AA01M', '12:00', '14:00', 'horas cheias', '30.0', '0.5')
    assert estacionamento.calcula_acesso_horas_cheias(acesso, estacionamento) == 204.0