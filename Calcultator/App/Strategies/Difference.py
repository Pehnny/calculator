from App.Strategies.IOperation import IOperation

class Difference(IOperation) :
    def operate(a: float, b: float) -> float:
        return a - b

difference = Difference()
