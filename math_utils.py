import math

def calculate_factorial():
    try:
        number = int(input("Enter a non-negative integer: "))

        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = math.factorial(number)
            print(f"Factorial of {number} is {result}")

    except ValueError:
        print("Please enter a valid integer.")

def calculate_compound_interest():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time_period = float(input("Enter time in years: "))

        if principal < 0 or rate < 0 or time_period < 0:
            print("Values cannot be negative.")
            return

        amount = principal * (1 + rate / 100) ** time_period
        interest = amount - principal

        print(f"Final Amount: {amount:.2f}")
        print(f"Compound Interest: {interest:.2f}")

    except ValueError:
        print("Please enter valid numeric values.")

def calculate_trigonometry():
    try:
        angle = float(input("Enter angle in degrees: "))
        radians = math.radians(angle)

        print(f"Sine: {math.sin(radians):.4f}")
        print(f"Cosine: {math.cos(radians):.4f}")
        print(f"Tangent: {math.tan(radians):.4f}")

    except ValueError:
        print("Please enter a valid angle.")

def calculate_area():
    try:
        print("\nChoose a shape:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")

        choice = input("Enter your choice: ")

        if choice == "1":
            radius = float(input("Enter radius: "))

            if radius < 0:
                print("Radius cannot be negative.")
                return

            area = math.pi * radius ** 2
            print(f"Area of Circle: {area:.2f}")

        elif choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))

            if length < 0 or width < 0:
                print("Dimensions cannot be negative.")
                return

            area = length * width
            print(f"Area of Rectangle: {area:.2f}")

        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            if base < 0 or height < 0:
                print("Dimensions cannot be negative.")
                return

            area = 0.5 * base * height
            print(f"Area of Triangle: {area:.2f}")

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter valid numeric values.")

def math_menu():
    while True:
        print("\n===== MATHEMATICAL OPERATIONS =====")
        print("1. Calculate Factorial")
        print("2. Calculate Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculate_factorial()
        elif choice == "2":
            calculate_compound_interest()
        elif choice == "3":
            calculate_trigonometry()
        elif choice == "4":
            calculate_area()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    math_menu()