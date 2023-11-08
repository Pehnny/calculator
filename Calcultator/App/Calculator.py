import tkinter as tk
from time import sleep
from App.Strategies.IOperation import IOperation
from App.Context.Operator import Operator
from App.Digits import Digits
from App.Operations import operations
from App.Order_of_operations import Order_of_operations

class Calculator:
    def __init__(self) -> None:
        self.__operations: dict[str, IOperation] = operations
        self.__order_of_operations: Order_of_operations = Order_of_operations()
        self.__queue: list[str] = []
        self.digits: Digits = Digits()
        self.operator: Operator = Operator()

    def append_operator(self, screen: tk.Label, button: tk.Button) -> None:
        if screen["text"] != "":
            if len(self.__queue) == 1:
                self.__queue.append(button["text"])
            else:
                self.__queue.extend([screen["text"], button["text"]])
            screen["text"] = ""
        elif self.__queue[-1] in self.__operations.keys():
            self.__queue[-1] = button["text"]
        print(self.__queue)

    def clear(self, screen: tk.Label) -> None:
        if screen["text"] != "":
            screen["text"] = ""
        else:
            self.__queue.clear()

    def solve(self, screen: tk.Label) -> None:
        if len(self.__queue) == 0:
            return
        if screen["text"] != "":
            self.__queue.append(screen["text"])
            print(self.__queue)
        while len(self.__queue) > 1:
            index: int = self.__order_of_operations.index(self.__queue)
            if index == 0:
                break
            if index == len(self.__queue):
                self.__queue.pop()
            operator: str = self.__queue.pop(index)
            self.operator.operation = self.__operations[operator]
            a: float = float(self.__queue[index-1])
            b: float = float(self.__queue.pop(index))
            try:
                self.__queue[index-1] = str(self.operator.operation.operate(a, b))
            except ZeroDivisionError:
                screen["text"] = "Error !"
                sleep(5)
                self.clear(screen)
                self.clear(screen)
                return
        screen["text"] = self.__queue[0]
        print(self.__queue)
    
calculator = Calculator()
