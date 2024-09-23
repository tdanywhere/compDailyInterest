# Import tkinter library   
from tkinter import *


"""
Compute the daily interest for a given principal and annual interest rate.

:param principal: The initial amount of money
:param annual_rate: The annual interest rate (as a percentage)
:return: The daily interest amount
"""
principal_amount = 1000  # Example principal amount
annual_interest_rate = 2.75  # Example annual interest rate in percentage


def compute_daily_interest(principal, annual_rate):
    # Convert annual interest rate to a daily interest rate
    daily_rate = annual_rate / 365 / 100
    
    # Calculate daily interest
    daily_interest = principal * daily_rate
# Example usage
    
    return daily_interest


daily_interest = compute_daily_interest(principal_amount, annual_interest_rate)
print(f"Daily interest for principal amount €{principal_amount} at an annual rate of {annual_interest_rate}% is: €{daily_interest:.2f}")


def btn_show_daily_interest():
    principal_amount = float(inp_principal.get())
    annual_interest_rate = float(inp_annual_rate.get())

    daily_interest = compute_daily_interest(principal_amount, annual_interest_rate)
    
    lbl_result.config(text=f"Daily interest: €{daily_interest:.2f}")

# Create the main window
window = Tk()
window.title("Daily Interest Calculator")
window.geometry('500x300')

# Create the input labels and entry fields
lbl_principal = Label(window, text="Principal amount:")
lbl_principal.pack()
inp_principal = Entry(window)
inp_principal.pack()

lbl_annual_rate = Label(window, text="Annual interest rate (%):")
lbl_annual_rate.pack()
inp_annual_rate = Entry(window)
inp_annual_rate.pack()

# Create the calculate button
btn_calculate = Button(window, text="Calculate", command=btn_show_daily_interest)
btn_calculate.pack()

# Create the result label
lbl_result = Label(window, text="Daily interest: ")
lbl_result.pack()

# Start the main loop
window.mainloop()