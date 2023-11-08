from App.Strategies.IOperation import IOperation

class Product(IOperation) :
    def operate(a: float, b: float) -> float:
        return a * b

product = Product()
