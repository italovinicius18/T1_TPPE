import pytest

from Acesso import Acesso

@pytest.mark.TesteExcecao
def teste_acesso_vazio():
    with pytest.raises(Exception):
        acesso = Acesso("", "", "", "", "")

@pytest.mark.TesteExcecao
def teste_acesso_vazio_placa():
    with pytest.raises(Exception):
        acesso = Acesso('', '12/07/2022 12:31', '12/07/2022 15:48', 30.0, 0.5)

@pytest.mark.TesteExcecao
def teste_acesso_vazio_dadoEntrada():
    with pytest.raises(Exception):
        acesso = Acesso('AA00M', '', '12/07/2022 15:48', 30.0, 0.5)

@pytest.mark.TesteExcecao
def teste_acesso_vazio_dadoSaida():
    with pytest.raises(Exception):
        acesso = Acesso('AA00M', '12/07/2022 12:31', '', 30.0, 0.5)

@pytest.mark.TesteExcecao
def teste_acesso_vazio_valorAcesso():
    with pytest.raises(Exception):
        acesso = Acesso('AA00M', '12/07/2022 12:31', '12/07/2022 15:48', '', 0.5)

@pytest.mark.TesteExcecao
def teste_acesso_vazio_valorContratante():
    with pytest.raises(Exception):
        acesso = Acesso('AA00M', '12/07/2022 12:31', '12/07/2022 15:48', 30.0, '')

@pytest.mark.TesteExcecao
def teste_acesso_valorAcesso_negativo():
    with pytest.raises(Exception):
        acesso = Acesso('AA00M', '12/07/2022 12:31', '12/07/2022 15:48', -30, 0.5)

@pytest.mark.TesteExcecao
def teste_acesso_valorContratante_negativo():
    with pytest.raises(Exception):
        acesso = Acesso('AA00M', '12/07/2022 12:31', '12/07/2022 15:48', 30, -0.5)

@pytest.mark.TesteExcecao
def teste_acesso_valorAcesso_valorContratante_negativos():
    with pytest.raises(Exception):
        acesso = Acesso('AA00M', '12/07/2022 12:31', '12/07/2022 15:48', -30, -0.5)