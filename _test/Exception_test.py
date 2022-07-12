import pytest

@pytest.mark.TesteExcecao
def test_exception():
    with pytest.raises(Exception):
        raise Exception('test')

