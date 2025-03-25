import tkinter as tk
from tkinter import messagebox
import math


def calculate():
    operator = operator_entry.get()
    try:
        num1 = float(num1_entry.get())
        if operator != "sqrt":
            num2 = float(num2_entry.get())
        else:
            num2 = None
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")
        return

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            messagebox.showerror("Math Error", "Division by zero")
            return
    elif operator == "**":
        result = num1 ** num2
    elif operator == "%":
        result = num1 % num2
    elif operator == "sqrt":
        result = math.sqrt(num1)
    else:
        messagebox.showerror("Input Error", f"{operator} is not a valid operator")
        return

    result_label.config(text=f"Result: {round(result, 2)}")


app = tk.Tk()
app.title("Simple Calculator")

tk.Label(app, text="Operator (+, -, *, /, **, %, sqrt):").pack()
operator_entry = tk.Entry(app)
operator_entry.pack()

tk.Label(app, text="First Number:").pack()
num1_entry = tk.Entry(app)
num1_entry.pack()

tk.Label(app, text="Second Number (leave blank for sqrt):").pack()
num2_entry = tk.Entry(app)
num2_entry.pack()

tk.Button(app, text="Calculate", command=calculate).pack()
result_label = tk.Label(app, text="Result: ")
result_label.pack()

app.mainloop()
