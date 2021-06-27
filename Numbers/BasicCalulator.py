#
#       Daniel Warren
#       Python version: 3.9
#
#       Task:
#       A simple calculator to do basic operators. Add, Subtract, Multiply, and Divide.
#

def main():
    #prompt & input
    print("Welcome to the best calculator.")
    num1 = int(input("Enter your first number: "))
    operator = str(input("Would you like to Add, Subtract, Multiply, or Divide? \n Enter [ +, -, *, / ]: "))
    num2 = int(input("Enter your first number: "))

    #check operator and call function accordingly
    if (operator == "+"):
        result = Add(num1, num2)
    elif (operator == "-"):
        result = Subtract(num1, num2)
    elif (operator == "*"):
        result = Multiply(num1, num2)
    elif (operator == "/"):
        result = Divide(num1, num2)
    else:
        print("Not a valid operator.")

    #display result
    print(result)

# Math Functions 
def Add(num1, num2):
    result = num1 + num2
    return result;

def Subtract(num1, num2):
    result = num1 - num2
    return result;

def Multiply(num1, num2):
    result = num1 * num2
    return result;

def Divide(num1, num2):
    result = num1 / num2
    return result;

if __name__  ==  '__main__':
    main()
