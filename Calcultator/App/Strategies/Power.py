from App.Strategies.IOperation import IOperation

class Power(IOperation) :
    def operate(a: float, b: float) -> float:
        return a ** b

power = Power()
