### Simple Calculator ###

import math

# Convert to int
def const(N):
    if N == "pi" or N == "PI" or N == "Pi":   
        NUM = math.pi
    elif N == "e":
        NUM = math.e
    else:
        NUM = float(N)
    return NUM
    
def sum(N1, N2):
    Result = N1 + N2
    return Result
def difference(N1, N2):
    Result = N1 - N2
    return Result
def multiplication(N1, N2):
    Result = N1 * N2
    return Result
def division(N1, N2):
    Result = N1 / N2
    return Result
def modulus(N1, N2):
    Result = N1 % N2
    return Result
def exp(N, EXP):
    Result = N ** EXP
    return Result
def root(N, ROOT):
    Result = N ** (1/ROOT)
    return Result
def fact(N):
    result = 1
    for i in range(1, N+1):
        result = result * i
    return result

if __name__ == "__main__":

    run = 1

    while(run == 1):        
        OP = "***********************\n  1 - Addition\n  2 - Subtraction\n  3 - Multiplication\n  4 - Division\n  5 - Modulus\n  6 - Square\n  7 - X-Power\n  8 - Square Root\n  9 - X-Root\n  10 - Factorial\nChoose an operation: "
        result = ""
        operation = input(OP)

        # End Condition
        if operation == "0":
            run = 0
            print("Program Terminated.")
            break

        # Addition
        elif operation == "1":
            n1 = input("First Number: ")
            n2 = input("Second Number: ")
            num1 = const(n1)
            num2 = const(n2)
            print(num1, "+", num2)
            result = sum(num1, num2)

        # Subtraction
        elif operation == "2":
            n1 = input("First Number: ")
            n2 = input("Second Number: ")
            num1 = const(n1)
            num2 = const(n2)
            print(num1, "-", num2)
            result = difference(num1, num2)

        # Multiplication
        elif operation == "3":
            n1 = input("Multiplicand: ")
            n2 = input("Multiplier: ")
            num1 = const(n1)
            num2 = const(n2)
            print(num1, "*", num2)
            result = multiplication(num1, num2)

        # Division
        elif operation == "4":
            n1 = input("Dividend: ")
            n2 = input("Divisor: ")
            num1 = const(n1)
            num2 = const(n2)
            print(num1, "/", num2)
            result = division(num1, num2)

        # Modulus
        elif operation == "5":
            n1 = input("Main Number: ")
            n2 = input("Divisor Number: ")
            num1 = const(n1)
            num2 = const(n2)
            print(num1, "%", num2)
            result = modulus(num1, num2)
        
        # Square
        elif operation == "6":
            n1 = input("Number: ")
            num1 = const(n1)
            num2 = 2
            print(num1, "^", num2)
            result = exp(num1, num2)

        # To the X power
        elif operation == "7":
            n1 = input("Number: ")
            n2 = input("Power: ")
            num1 = const(n1)
            num2 = const(n2)
            print(num1, "^", num2)
            result = exp(num1, num2)

        # Square Root
        elif operation == "8":
            n1 = input("Number: ")
            num1 = const(n1)
            num2 = 2
            print("The square root of", num1)
            result = root(num1, num2)

        # Finds the X root
        elif operation == "9":
            n1 = input("Number: ")
            n2 = input("Root: ")
            num1 = const(n1)
            num2 = const(n2)
            result = root(num1, num2)

        # Factorial
        elif operation == "10":
            n1 = input("Number: ")
            num1 = const(n1)
            print(num1, "!")
            result = fact(num1)

        # Input Error Catch
        else:
            print("The number you chose is not a valid operation")
            result = "Please Try Again"

        print("=", result)