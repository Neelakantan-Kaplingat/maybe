def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please select a valid operation.")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == 1:
            print(f"The result is: {add(num1, num2)}")
        elif choice == 2:
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == 3:
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == 4:
            print(f"The result is: {divide(num1, num2)}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

while True:
    calculator()
    cont = input("Do you want to perform another calculation? (yes/no): ").lower()
    if cont != "yes":
        print("Thank you for using the calculator!")
        break