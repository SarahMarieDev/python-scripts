degrees = int(input("Enter degrees: "))
degree_type = input("Enter 'C' for Celsius or 'F' for Fahrenheit: ")

def convertToFahrenheit(degrees):
    result = (degrees * 9/5) + 32
    print(f"{degrees} degrees Celsius is equal to {result} degrees Fahrenheit.")

def convertToCelsius(degrees):
    result = (degrees - 32) * 5/9
    print(f"{degrees} degrees Fahrenheit is equal to {result} degrees Celsius.")
    
if degree_type == "C":
    convertToFahrenheit(degrees)
elif degree_type == "F":
    convertToCelsius(degrees)
else:
    print("That entry is not valid.")