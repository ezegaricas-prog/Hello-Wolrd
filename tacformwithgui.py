import tkinter as tk
from tkinter import messagebox

TAX_RATE = 0.15  # 15%

def compute_tax():
    try:
        gross_income = float(gross_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a numeric value for Gross Income.")
        return

    tax_due = gross_income * TAX_RATE
    tax_var.set(f"${tax_due:,.2f}")

def clear_output():
    tax_var.set("")

# Create main window
window = tk.Tk()
window.title("Tax Calculator")

# Labels
tk.Label(window, text="Gross income:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
tk.Label(window, text="Federal tax withheld:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
tk.Label(window, text="Tax due:").grid(row=2, column=0, sticky="w", padx=5, pady=5)

# Input fields
gross_entry = tk.Entry(window)
gross_entry.grid(row=0, column=1, padx=5, pady=5)
gross_entry.insert(0, "50000.00")  # default value

withheld_entry = tk.Entry(window)
withheld_entry.grid(row=1, column=1, padx=5, pady=5)
withheld_entry.insert(0, "7500.00")  # default value (not used in calculation for simplicity)

# Output field
tax_var = tk.StringVar()
tax_entry = tk.Entry(window, textvariable=tax_var, state="readonly")
tax_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
compute_button = tk.Button(window, text="Compute", command=compute_tax)
compute_button.grid(row=3, column=0, padx=5, pady=10)

quit_button = tk.Button(window, text="Quit", command=window.destroy)
quit_button.grid(row=3, column=1, padx=5, pady=10)

# Run the window
window.mainloop()
