from App.Strategies.IOperation import IOperation

class Quotient(IOperation) :
    def operate(a: float, b: float) -> float:
        return a / b

quotient = Quotient()
