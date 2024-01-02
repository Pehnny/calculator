from App.Strategies.IOperation import IOperation

class Product(IOperation) :
    def operate(self, a: float, b: float) -> float:
        return a * b

product = Product()
