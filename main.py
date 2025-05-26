x: int = int(input("Enter a number: "))
y: int = int(input("Enter another number: "))

def add(x: int, y: int) -> int:
    print("Adding two numbers...")
    return x + y

def subtract(x: int, y: int) -> int:
    print("Subtracting two numbers...")
    return x - y

def multiply(x: int, y: int) -> int:
    print("Multiplying two numbers...")
    return x * y

def divide(x: int, y: int) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    print("Dividing two numbers...")
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")    
print("3. Multiply")
print("4. Divide")

choice: str = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print(f"{x} + {y} = {add(x, y)}")
elif choice == '2':
    print(f"{x} - {y} = {subtract(x, y)}")
elif choice == '3':
    print(f"{x} * {y} = {multiply(x, y)}")
elif choice == '4':
    try:
        print(f"{x} / {y} = {divide(x, y)}")
    except ValueError as e:
        print(e)
else:
    print("Invalid input. Please enter a valid choice (1/2/3/4).")