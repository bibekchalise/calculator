import sys
import tkinter as tk
from tkinter import simpledialog, messagebox

def sum():
    a = int(simpledialog.askstring("Input", "Enter a first number:"))
    b = int(simpledialog.askstring("Input", "Enter a second number:"))
    return a + b

def subtract():
    a = int(simpledialog.askstring("Input", "Enter a first number:"))
    b = int(simpledialog.askstring("Input", "Enter a second number:"))
    return a - b

def multiply():
    a = int(simpledialog.askstring("Input", "Enter a first number:"))
    b = int(simpledialog.askstring("Input", "Enter a second number:"))
    return a * b

def divide():
    a = int(simpledialog.askstring("Input", "Enter a first number:"))
    b = int(simpledialog.askstring("Input", "Enter a second number:"))
    return a / b

def handle_option(option):
    if option == 1:
        result = sum()
        messagebox.showinfo("Result", f"Result: {result}")
    elif option == 2:
        result = subtract()
        messagebox.showinfo("Result", f"Result: {result}")
    elif option == 3:
        result = multiply()
        messagebox.showinfo("Result", f"Result: {result}")
    elif option == 4:
        result = divide()
        messagebox.showinfo("Result", f"Result: {result}")
    elif option == 6:
        sys.exit()

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.config(bg="lightblue")
    while True:
        option = simpledialog.askinteger("Menu", "X-----------------X\n1. Add.\n2. Subtract.\n3. Multiply.\n4. Divide.\n6. Exit\n\nSelect an option:")
        handle_option(option)

if __name__ == "__main__":
    main()
