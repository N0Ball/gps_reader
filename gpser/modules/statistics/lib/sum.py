import statistics
from abc import abstractmethod

from ..decorator import StatDecorator

class Sum(StatDecorator):
    
    def __init__(self, component: StatDecorator) -> None:
        super().__init__(component)
        self._NAME = 'SUM'

    @abstractmethod
    def _operation(self, datas: list) -> list:
        return sum(datas)