import pytest

from conftest import get_test_data

from gpser.modules.statistics import Variance

class VariaceTestStub(Variance):

    def result():
        try:
            super().result()
        except ValueError as e:
            return e

ERROR = 0.005

case, parameter = get_test_data('./tests/data/test_statistics_variance.yaml')
case, invalid_parameter = get_test_data('./tests/data/test_statistics_invalid_variance.yaml')

class TestStatisticsVariance(object):

    @pytest.mark.parametrize('case, test_input, expected', parameter)
    def test_statistics_variance(self, case, test_input, expected):
        target = Variance(test_input['input'])
        assert abs(expected['result'] - target.result()) < ERROR

    @pytest.mark.parametrize('case, test_input, expected', invalid_parameter)
    def test_statistics_invalid_variance(self, case, test_input, expected):
        
        with pytest.raises(ValueError) as e:
            target = Variance(test_input['input'])
        
        assert expected['result'] == str(e.value)
