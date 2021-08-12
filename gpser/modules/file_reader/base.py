from abc import abstractclassmethod

class FReader:

    _FILE_PATH: str = ''
    _RAW_DATA: str = ''
    _PARSED_DATA: dict = {}

    def __init__(self, file_path: str) -> None:
        self._FILE_PATH = file_path

        with open(file_path, 'r') as f:
            self._RAW_DATA = f.read()

        self._PARSED_DATA = self._parser()

    def __call__(self) -> dict:
        return self._PARSED_DATA

    def __repr__(self) -> str:
        return repr(self._PARSED_DATA)

    @abstractclassmethod
    def _parser(self):
        pass