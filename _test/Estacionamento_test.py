import pytest

from Estacionamento import Estacionamento
from Acesso import Acesso

@pytest.mark.TesteFuncional
def teste_1():
    estacionamento = Estacionamento('Estacionamento 1', 10, 0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, '08:00', '18:00', '00:00', '23:59', 'R$ 0,00')
    acesso = Acesso('Contratante 1', '08:00', '18:00', '00:00', '23:59', 'R$ 0,00')

    assert estacionamento.calcula_valor_acesso(acesso) == 1.0