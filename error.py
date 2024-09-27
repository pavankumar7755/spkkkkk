mobile_number= int(inpit("enter your mobilr number:"))

print(mobile_number)



"""
    SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
    TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
    NameError: This exception is raised when a variable or function name is not found in the current scope.
    IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
    KeyError: This exception is raised when a key is not found in a dictionary.
    ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
    AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
    IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
    ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
    ImportError: This exception is raised when an import statement fails to find or load a module.


a = 10
try:
    print(a/0)
except:
    print("Zero devision error")


try:
    phone_num = int(input("Enter num:"))
    print(phone_num)

except ValueError:
    print("Only use numbers for phone number")


try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("Can't devide anything with zero")"""

try:
    file = open("python_intro.txt","r")

    for text in file:
        print(text)

except FileNotFoundError:
    print("File is not found")

finally:
    print("Success")

