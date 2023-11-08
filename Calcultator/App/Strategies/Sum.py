from App.Strategies.IOperation import IOperation

class Sum(IOperation) :
    def operate(a: float, b: float) -> float:
        return a + b

addition = Sum()
