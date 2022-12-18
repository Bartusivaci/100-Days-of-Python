from logo import logo

print(logo)

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : divide
}

num1 = float(input("What's the first number? : "))
for operation in operations:
    print(operation)
keep_going = True
while keep_going:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? : "))
    function = operations[operation_symbol]
    result = function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}\n")
    answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")
    if answer == 'n':
        keep_going = False
    else:
        num1 = result