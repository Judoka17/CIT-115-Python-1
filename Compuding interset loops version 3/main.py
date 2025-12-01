#compound interest until goal is reached

#get starting amount
while True:
    try:
        principal = float(input("Enter starting amount: "))
        if principal <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a number.")

#get yearly interest rate
while True:
    try:
        annual_rate = float(input("Enter yearly interest rate (%): "))
        if annual_rate <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a number.")

#get target amount
while True:
    try:
        target = float(input("Enter the amount you want to reach: "))
        if target <= principal:
            print("Target must be higher than starting amount.")
            continue
        break
    except ValueError:
        print("Please enter a number.")

#change yearly rate to monthly rate
monthly_rate = annual_rate / 100 / 12

month = 1

print("Month by Month Balance")
print("----------------------")

#ading interest until goal is reached
while principal < target:
    interest = principal * monthly_rate
    principal = principal + interest
    print(f"Month {month}: ${principal:,.2f}")
    month = month + 1

print()
print(f"It took {month - 1} months to reach at least ${target:,.2f}.")
print(f"Final balance: ${principal:,.2f}")

