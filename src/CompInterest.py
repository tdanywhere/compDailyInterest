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
