import statistics
from abc import abstractmethod

from ..decorator import StatDecorator

class Mean(StatDecorator):
    
    def __init__(self, component: StatDecorator) -> None:
        super().__init__(component)
        self._NAME = 'MEAN'

    @abstractmethod
    def _operation(self, datas: list) -> list:
        return [statistics.mean(datas)]