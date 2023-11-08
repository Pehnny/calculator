from abc import ABCMeta, abstractmethod

class IOperation(metaclass = ABCMeta):
    @abstractmethod
    def operate(self, a: float, b: float) -> float:
        pass
