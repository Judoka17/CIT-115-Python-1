#Temperture converter
#Ask user if they are using celsius or fahrenheit
scale = input("Type C for Celsius or F for Fahrenheit: ")

#Ask for the temperature
temp = float(input("Enter the temperature: "))

#temperature conversions
if not (scale == "F") and temp <= 100:
    # Convert from Celsius to Fahrenheit
    result = (temp * 9 / 5) + 32
    print(f"That is {result:,.2f} degrees in fahrenheit.")
    
elif not (scale == "C") and temp <= 212:
    #convert from fahrenheit to celsius
    result = (temp - 32) * 5 / 9
    print(f"That is {result:,.2f} degrees in celsius.")
