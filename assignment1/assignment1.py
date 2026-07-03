# task1
def hello():
    return "Hello!"

# task2
def greet(name):
    return "Hello, " + name + "!"

# task3
def calc(num1, num2, operation="multiply"):
    if operation == "multiply":
        try:
            return num1 * num2
        except TypeError:
            return "You can't multiply those values!"
    elif operation == "add":
        try:
            return num1 + num2
        except TypeError:
            return "You can't add those values!"
    elif operation == "subtract":
        try:
            return num1 - num2
        except TypeError:
            return "You can't subtract those values!"
    elif operation == "divide":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "You can't divide by 0!"
        except TypeError:
            return "You can't divide those values!"
    elif operation == "modulo":
        try:
            return num1 % num2
        except TypeError:
            return "You can't calculate the modulo of those values!"
    elif operation == "power":
        try:
            return num1 ** num2
        except TypeError:
            return "You can't power those values!"
    

#task 4

def data_type_conversion(value, target_type):
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
        else:
            return "Invalid target type."
    except ValueError:
        return f"You can't convert {value} into a {target_type}."
    