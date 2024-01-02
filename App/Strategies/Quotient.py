from App.Strategies.IOperation import IOperation

class Quotient(IOperation) :
    def operate(self, a: float, b: float) -> float:
        return a / b

quotient = Quotient()
