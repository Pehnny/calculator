class Order_of_operations:
    def __init__(self) -> None:
        pass
        
    def index(self, list: list[str]) -> int:
        if list.count("^"):
            return list.index("^")
        elif list.count("*"):
            return list.index("*")
        elif list.count("/"):
            return list.index("/")
        elif list.count("+"):
            return list.index("+")
        elif list.count("-"):
            return list.index("-")
        return 0
