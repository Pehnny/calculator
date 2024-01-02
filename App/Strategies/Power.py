from App.Strategies.IOperation import IOperation

class Power(IOperation) :
    def operate(self, a: float, b: float) -> float:
        return a ** b

power = Power()
