import tkinter as tk

class Digits:
    def __init__(self) -> None:
        pass

    def append_digit(self, screen: tk.Label, button: tk.Button) -> None:
        screen["text"] += button["text"]
