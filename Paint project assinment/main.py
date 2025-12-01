#simple Paint Job Estimator
import math

def get_gallons(square_feet, feet_per_gallon):
    return math.ceil(square_feet / feet_per_gallon)

def get_labor_hours(gallons, hours_per_gallon):
    return gallons * hours_per_gallon

def get_sales_tax(state):
    state = state.upper()

#sales txes in differnt states
    if state == "CT":
        return 0.06
    elif state == "MA":
        return 0.0625
    elif state == "ME":
        return 0.085
    elif state == "NH":
        return 0.0
    elif state == "RI":
        return 0.07
    elif state == "VT":
        return 0.06
    else:
        return 0.0


def main():
    print("Paint Job Estimator\n")

    #user inputs
    square_feet = float(input("Enter square feet to paint: "))
    price_per_gallon = float(input("Enter price per gallon: "))
    feet_per_gallon = float(input("Enter feet covered per gallon: "))
    hours_per_gallon = float(input("Enter labor hours per gallon: "))
    hourly_rate = float(input("Enter labor charge per hour: "))
    state = input("Enter job state (2 letter code): ")
    last_name = input("Enter customer's last name: ")

    #calculations
    gallons = get_gallons(square_feet, feet_per_gallon)
    paint_cost = gallons * price_per_gallon
    labor_hours = get_labor_hours(gallons, hours_per_gallon)
    labor_cost = labor_hours * hourly_rate

    tax_rate = get_sales_tax(state)
    sales_tax = paint_cost * tax_rate

    total_cost = paint_cost + labor_cost + sales_tax

    #display results
    print("\n----- Paint Job Estimate -----")
    print("Gallons needed:", gallons)
    print("Paint cost: $", format(paint_cost, ".2f"))
    print("Labor hours:", labor_hours)
    print("Labor cost: $", format(labor_cost, ".2f"))
    print("Sales tax: $", format(sales_tax, ".2f"))
    print("Total cost: $", format(total_cost, ".2f"))

    #write to file
    filename = last_name + "_PaintJobOutput.txt"
    file = open(filename, "w")

    file.write("Paint Job Estimate\n")
    file.write("-------------------\n")
    file.write("Gallons needed: " + str(gallons) + "\n")
    file.write("Paint cost: $" + format(paint_cost, ".2f") + "\n")
    file.write("Labor hours: " + str(labor_hours) + "\n")
    file.write("Labor cost: $" + format(labor_cost, ".2f") + "\n")
    file.write("Sales tax: $" + format(sales_tax, ".2f") + "\n")
    file.write("Total cost: $" + format(total_cost, ".2f") + "\n")

    file.close()
    print("\nOutput saved to", filename)


main()