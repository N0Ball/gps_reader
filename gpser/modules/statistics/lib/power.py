from abc import abstractmethod

from ..decorator import StatDecorator

class Power(StatDecorator):

    def __init__(self, component: StatDecorator, power: int) -> None:
        super().__init__(component)
        self._NAME = 'POWER'
        self._POWER = power

    @abstractmethod
    def _operation(self, datas: list) -> list:
        return list(map(lambda x: x**self._POWER, datas))