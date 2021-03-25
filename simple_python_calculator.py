# define functions
def add(a,b):
    result = a + b
    print(f'{a} + {b} = {result}')

def sub(a,b):
    result = a - b
    print(f'{a} - {b} = {result}')

def mul(a,b):
    result = a * b
    print(f'{a} * {b} = {result}')

def div(a,b):
    result = a / b
    print(f'{a} / {b} = {result}')

#getting inputs
a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))
op = input('Enter the operator number : ')

# selecting which function to run via operator
if op == '+':
    add(a,b)
elif op == '-':
    sub(a,b)
elif op == '*':
    mul(a,b)
elif op == '/':
    div(a,b)
else:
    print('Invalid Operator')
