import tkinter as tk
from App.Calculator import calculator



#   Window
window = tk.Tk()
window.resizable(width = False, height = False)
window.title("calculator")
frame = tk.Frame(window, relief = "raised", padx = 5, pady = 5, bg = "gray")
width = 10
height = 3



#   Screen
row = 0
screen = tk.Label(frame, width = 4*(width + 1), height = height, bg = "lightgray", relief = "sunken", text = "")
screen.grid(row = row, column = 0, columnspan = 4, sticky = "we")



#   Buttons
digits = {
    "0": tk.Button(frame, text = "0", width = 2*(width + 1), height = height),
    ".": tk.Button(frame, text = ".", width = width, height = height),
    "1": tk.Button(frame, text = "1", width = width, height = height),
    "2": tk.Button(frame, text = "2", width = width, height = height),
    "3": tk.Button(frame, text = "3", width = width, height = height),
    "4": tk.Button(frame, text = "4", width = width, height = height),
    "5": tk.Button(frame, text = "5", width = width, height = height),
    "6": tk.Button(frame, text = "6", width = width, height = height),
    "7": tk.Button(frame, text = "7", width = width, height = height),
    "8": tk.Button(frame, text = "8", width = width, height = height),
    "9": tk.Button(frame, text = "9", width = width, height = height),
}
operators = {
    "+": tk.Button(frame, text = "+", width = width, height = height),
    "-": tk.Button(frame, text = "-", width = width, height = height),
    "*": tk.Button(frame, text = "*", width = width, height = height),
    "/": tk.Button(frame, text = "/", width = width, height = height),
    "^": tk.Button(frame, text = "^", width = width, height = height),
}
specials = {
    "c": tk.Button(frame, text = "c", width = width, height = height),
    "=": tk.Button(frame, text = "=", width = 2*(width + 1), height = height),
}

#   Firts row
row += 1
specials["="].grid(row = row, column = 0, columnspan = 2, sticky = "w")
specials["c"].grid(row = row, column = 2, sticky = "we")
operators["^"].grid(row = row, column = 3, sticky = "e")

#   Second row
row += 1
digits["7"].grid(row = row, column = 0, sticky = "w")
digits["8"].grid(row = row, column = 1, sticky = "e")
digits["9"].grid(row = row, column = 2, sticky = "we")
operators["+"].grid(row = row, column = 3, sticky = "e")

#   Third row
row += 1
digits["4"].grid(row = row, column = 0, sticky = "w")
digits["5"].grid(row = row, column = 1, sticky = "e")
digits["6"].grid(row = row, column = 2, sticky = "we")
operators["-"].grid(row = row, column = 3, sticky = "e")

#   Fourth row
row += 1
digits["1"].grid(row = row, column = 0, sticky = "w")
digits["2"].grid(row = row, column = 1, sticky = "e")
digits["3"].grid(row = row, column = 2, sticky = "we")
operators["*"].grid(row = row, column = 3, sticky = "e")

#   Fifth row
row += 1
digits["0"].grid(row = row, column = 0, columnspan = 2, sticky = "w")
digits["."].grid(row = row, column = 2, sticky = "e")
operators["/"].grid(row = row, column = 3, sticky = "e")



#   Bind Buttons
for key, button in digits.items():
    button.bind("<Button-1>", lambda event: calculator.digits.append_digit(screen, button))
for key, button in operators.items():
    button.bind("<Button-1>", lambda event: calculator.append_operator(screen, button))
specials["c"].bind("<Button-1>", lambda event: calculator.clear(screen))
specials["="].bind("<Button-1>", lambda event: calculator.solve(screen))



#   Pack
frame.pack()
