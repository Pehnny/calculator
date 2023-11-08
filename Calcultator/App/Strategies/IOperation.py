from abc import ABCMeta, abstractmethod

class IOperation(metaclass = ABCMeta):
    @abstractmethod
    def operate(a: float, b: float) -> float:
        pass
