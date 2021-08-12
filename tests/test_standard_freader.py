import pytest

from conftest import get_test_data

from gpser.modules.file_reader import Standard

cases, parameters = get_test_data("./tests/data/test_standard_freader.yaml")

class TestStandardFReader(object):

    @pytest.mark.parametrize(("case, test_input, expected"), parameters)
    def test_standard_freader(self, case, test_input, expected):
        test_standard_reader = Standard(test_input['file_path'])
        assert test_standard_reader() == expected['result']