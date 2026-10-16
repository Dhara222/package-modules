import random
import string

def generate_random_number():
    try:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        if start > end:
            print("Starting number cannot be greater than ending number.")
            return

        number = random.randint(start, end)
        print(f"Random Number: {number}")

    except ValueError:
        print("Please enter valid integers.")

def generate_random_list():
    try:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))
        count = int(input("How many numbers do you want? "))

        if start > end:
            print("Starting number cannot be greater than ending number.")
            return

        if count <= 0:
            print("Count must be greater than zero.")
            return

        numbers = [random.randint(start, end)
            for _ in range(count)]

        print(f"Random List: {numbers}")

    except ValueError:
        print("Please enter valid integers.")

def generate_password():
    try:
        length = int(input("Enter password length: "))

        if length < 1:
            print("Password length must be at least 1.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation

        password = "".join(random.choice(characters)
            for _ in range(length))
        print(f"Generated Password: {password}")

    except ValueError:
        print("Please enter a valid length.")

def generate_otp():
    otp = "".join(random.choices(string.digits, k=6))
    print(f"Generated OTP: {otp}")


def simulate_random_sampling():
    try:
        data = input("Enter items separated by commas: ")
        items = [item.strip() for item in data.split(",") if item.strip()]

        if not items:
            print("Please enter at least one item.")
            return

        count = int(input("How many items should be selected? "))

        if count < 1 or count > len(items):
            print(f"Enter a number between 1 and {len(items)}.")
            return

        sample = random.sample(items, count)
        print(f"Random Sample: {sample}")

    except ValueError:
        print("Please enter a valid number.")

def simulate_random_game():
    secret_number = random.randint(1, 10)

    print("\nGuess the number between 1 and 10.")

    try:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Correct! You guessed the number.")
        else:
            print(f"Incorrect! The number was {secret_number}.")

    except ValueError:
        print("Please enter a valid integer.")

def random_menu():
    while True:
        print("\n===== RANDOM DATA GENERATION =====")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Generate Random Password")
        print("4. Generate Random OTP")
        print("5. Simulate Random Sampling")
        print("6. Play Number Guessing Game")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_random_number()
        elif choice == "2":
            generate_random_list()
        elif choice == "3":
            generate_password()
        elif choice == "4":
            generate_otp()
        elif choice == "5":
            simulate_random_sampling()
        elif choice == "6":
            simulate_random_game()
        elif choice == "7":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    random_menu()