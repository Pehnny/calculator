from App.Strategies.IOperation import IOperation

class Difference(IOperation) :
    def operate(self, a: float, b: float) -> float:
        return a - b
