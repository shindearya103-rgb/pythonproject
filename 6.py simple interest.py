principal = float(input("Enter the principal amount (P): "))
rate = float(input("Enter the annual interest rate (R in %): "))
time = float(input("Enter the time period in years (T):"))
                   
simple_interest = (principal * rate * time) / 100

print(f"\nThe Simple Interest is: {simple_interest:.2f}")
print(f"The Total Amount (Principal + Interest) is: {principal + simple_interest:.2f}")
