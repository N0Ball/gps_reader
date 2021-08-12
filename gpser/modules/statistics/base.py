class StatComponent:

    _DATA: list = []
    _NAME: str = ''

    def __init__(self, data: list) -> None:
        self._DATA = data
        self._NAME = 'BASE'

    def __repr__(self) -> str:
        return self._NAME

    def __call__(self) -> list:
        return self._DATA

    @property
    def DATA(self) -> list:
        return self._DATA
    
    @property
    def length(self) -> int:
        return len(self._DATA)