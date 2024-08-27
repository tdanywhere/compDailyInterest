# Import tkinter library   
from tkinter import *


"""
Compute the daily interest for a given principal and annual interest rate.

:param principal: The initial amount of money
:param annual_rate: The annual interest rate (as a percentage)
:return: The daily interest amount
"""
def compute_daily_interest(principal, annual_rate):
    # Convert annual interest rate to a daily interest rate
    daily_rate = annual_rate / 365 / 100
    
    # Calculate daily interest
    daily_interest = principal * daily_rate
    
    return daily_interest

# Example usage
principal_amount = 1000  # Example principal amount
annual_interest_rate = 2.75  # Example annual interest rate in percentage

daily_interest = compute_daily_interest(principal_amount, annual_interest_rate)
print(f"Daily interest for principal amount €{principal_amount} at an annual rate of {annual_interest_rate}% is: €{daily_interest:.2f}")


def calculate_daily_interest():
    principal_amount = float(principal_entry.get())
    annual_interest_rate = float(annual_rate_entry.get())

    daily_interest = compute_daily_interest(principal_amount, annual_interest_rate)
    
    result_label.config(text=f"Daily interest: €{daily_interest:.2f}")

# Create the main window
window = Tk()
window.title("Daily Interest Calculator")
window.geometry('500x300')

# Create the input labels and entry fields
principal_label = Label(window, text="Principal amount:")
principal_label.pack()
principal_entry = Entry(window)
principal_entry.pack()

annual_rate_label = Label(window, text="Annual interest rate (%):")
annual_rate_label.pack()
annual_rate_entry = Entry(window)
annual_rate_entry.pack()

# Create the calculate button
calculate_button = Button(window, text="Calculate", command=calculate_daily_interest)
calculate_button.pack()

# Create the result label
result_label = Label(window, text="Daily interest: ")
result_label.pack()

# Start the main loop
window.mainloop()