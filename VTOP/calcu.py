import tkinter as tk

def perform_operation(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Invalid Input")
    except ZeroDivisionError:
        result_label.config(text="Error: Division by Zero")

# Main window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root, width=15)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root, width=15)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Buttons for operations
tk.Button(root, text="Add", command=lambda: perform_operation("add")).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Subtract", command=lambda: perform_operation("subtract")).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Multiply", command=lambda: perform_operation("multiply")).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Divide", command=lambda: perform_operation("divide")).grid(row=3, column=1, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
