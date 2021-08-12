from .base import StatComponent
from .lib import Power, Sum, Normal

class Variance:

    _datas: list = []
    
    def __init__(self, datas: list) -> None:

        if not isinstance(datas, list):
            raise ValueError('Value or Variance must only list')

        if not isinstance(datas[0], int) and not isinstance(datas[0], float):
            raise ValueError('Values of list must be only int or float')
        
        self._datas = datas

    def result(self) -> dict:
        return self._cal()

    def _cal(self) -> list:
        return self._operation(StatComponent(self._datas))

    def _operation(self, target: StatComponent):
        return Sum(Power(Normal(target), 2))() / (target.length - 1)
