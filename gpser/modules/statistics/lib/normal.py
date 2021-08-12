import statistics
from abc import abstractmethod

from ..decorator import StatDecorator

class Normal(StatDecorator):

    def __init__(self, component: StatDecorator) -> None:
        super().__init__(component)
        self._NAME = 'NORMAL'

    @abstractmethod
    def _operation(self, datas: list) -> list:
        mean = statistics.mean(datas)
        return [data - mean for data in datas]