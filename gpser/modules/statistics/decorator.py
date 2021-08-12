from abc import abstractclassmethod

from .base import StatComponent

class StatDecorator(StatComponent):

    _COMPONENT: StatComponent = None

    def __init__(self, component: StatComponent) -> None:
        self._COMPONENT = component

    def __repr__(self) -> str:
        return repr(self._COMPONENT) + ' -> ' + self._NAME 

    def __call__(self) -> list:
        return self._operation(self._COMPONENT())

    @abstractclassmethod
    def _operation(self) -> list:
        pass