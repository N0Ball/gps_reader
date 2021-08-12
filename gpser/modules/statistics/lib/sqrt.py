from abc import abstractmethod
import math

from ..decorator import StatDecorator

class Sqrt(StatDecorator):

    def __init__(self, component: StatDecorator) -> None:
        super().__init__(component)
        self._NAME = 'SQRT'

    @abstractmethod
    def _operation(self, datas: list) -> list:
        return list(map(lambda x: math.sqrt(x), datas))