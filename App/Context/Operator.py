from App.Strategies.IOperation import IOperation

class Operator :
    def __init__(self) -> None:
        self.operation: IOperation

    def calculate(self, a: float, b: float) -> float:
        return self.operation.operate(a, b)
