class Order_of_operations:
    def __init__(self) -> None:
        pass
        
    def index(self, queue: list[str]) -> int:
        if queue.count("^"):
            return queue.index("^")
        elif queue.count("*"):
            if queue.count("/"):
                return min(queue.index("*"), queue.index("/"))
            return queue.index("*")
        elif queue.count("/"):
            if queue.count("*"):
                return min(queue.index("/"), queue.index("*"))
            return queue.index("/")
        elif queue.count("+"):
            if queue.count("-"):
                return min(queue.index("+"), queue.index("-"))
            return queue.index("+")
        elif queue.count("-"):
            if queue.count("+"):
                return min(queue.index("-"), queue.index("+"))
            return queue.index("-")
        return 0
