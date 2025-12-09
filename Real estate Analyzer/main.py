#Real estate anylizer
def getFloatInput(prompt):
    #keeps asking until user enters a number
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def getMedian(numbers):
    length = len(numbers)
    mid = length // 2

    if length % 2 == 1:            
        return numbers[mid]
    else:                          
        return (numbers[mid - 1] + numbers[mid]) / 2


def main():
    sales = []

    while True:
        price = getFloatInput("Enter a sales price: ")
        sales.append(price)

        again = input("Enter another value? (Y/N): ").lower()
        if again != "y":
            break

    #sorts the lists
    sales.sort()

    #prints the values
    print("\nSales Entered (sorted):")
    for value in sales:
        print(value)

    #math
    minimum = sales[0]
    maximum = sales[-1]
    total = sum(sales)
    count = len(sales)
    average = total / count
    median = getMedian(sales)
    commission = total * 0.03

    #summary of stuff
    print("\nSummary:")
    print("Number of entries:", count)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Total:", total)
    print("Average:", average)
    print("Median:", median)
    print("Commission (3%):", commission)


main()