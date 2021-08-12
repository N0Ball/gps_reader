import pytest

from conftest import get_test_data

case, parameter = get_test_data('./tests/data/test_conftest.yaml')

type_table = {
    'str': str,
    'int': int,
    'float': float
}

class TestConfTest(object):

    @pytest.mark.parametrize("case, test_input, expected", parameter)
    def test_conftest(self, case, test_input, expected):
        assert test_input['input'] == expected['output']
        assert isinstance(test_input['input'], type_table[expected['type']])