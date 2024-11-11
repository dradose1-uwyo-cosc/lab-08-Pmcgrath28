# Patrick McGrath
# UWYO COSC 1010
# Submission Date: 11/7/2024
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


def check_string(s):

    s = input("Enter a value to convert: ")

    try:
        value = int(s)
        return value
    except ValueError:
        pass

    try:
        value = float(s)
        if '.' in s and len(s.split('.')[1]) == 1:
            return value
        else:
            return False
    except ValueError:
        pass
    return False

s = input("Enter a value to convert: ")
result = check_string(s)

if result is False:
    print("The input could not be converted")
else:
    print(f"The converted value is: {result}")
        
print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def point_slope(m, b, lower_bound, upper_bound):
    if not isinstance(lower_bound, int) or not isinstance(upper_bound, int):
        return False
    
    if lower_bound > upper_bound:
        return False
    
    y_value = []

    for x in range(lower_bound, upper_bound +1):
        y = m * x + b
        y_value.append(y)

    return y_value

def calculate():
    try:
        m = float(input("Enter a value of slope for (m): "))
        b = float(input("Enter y-intercept (b): "))
        lower_bound = int(input("Enter the lower bound for x: "))
        upper_bound = int(input("Enter the upper bound for x: "))

        if lower_bound > upper_bound:
            print("The lower bound cannot be greater than the upper bound.")
            return
        
        result = point_slope(m, b, lower_bound, upper_bound)
        if result is False:
            print("Try again")
        else:
            print(f"Calculated y_values for x in range [{lower_bound}, {upper_bound}]: {result}")
    except ValueError:
        print("Invalid input")

calculate()
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def squareroot(value):
    if value < 0:
        return None 
    

    guess = value / 2.0  
    precision = 1e-10 
    
    while True:
        new_guess = 0.5 * (guess + value / guess)
        if abs(guess - new_guess) < precision:
            break
        guess = new_guess
    
    return guess

def quadratic_formula():
    
    while True:
        try:
            a = float(input("Enter coefficient a (not zero): "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            
        
            if a == 0:
                print("Coefficient 'a' cannot be zero. Please try again.")
                continue 
                
            break 
        except ValueError:
            print("Invalid input. Please enter numeric values for a, b, and c.")


    numerator = b**2 - 4 * a * c

    sqrt_numerator = squareroot(numerator)

    if sqrt_numerator is None:
        print("The value under the squareroot is negative, so there are no real solutions.")
        return 
    
    
    root1 = (-b + sqrt_numerator) / (2 * a)
    root2 = (-b - sqrt_numerator) / (2 * a)

    
    print(f"The roots of the quadratic equation are: {root1} and {root2}")

quadratic_formula()
