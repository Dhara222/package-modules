from datetime import datetime
import time

def show_current_datetime():
    current_datetime = datetime.now()

    print("\n===== CURRENT DATE AND TIME =====")
    print(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_date_difference():
    try:
        date1 = input("Enter first date (YYYY-MM-DD): ")
        date2 = input("Enter second date (YYYY-MM-DD): ")

        first_date = datetime.strptime(date1, "%Y-%m-%d")
        second_date = datetime.strptime(date2, "%Y-%m-%d")

        difference = abs((second_date - first_date).days)

        print(f"Difference: {difference} days")

    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")

def format_custom_date():
    current_datetime = datetime.now()

    print("\nChoose Date Format:")
    print("1. DD-MM-YYYY")
    print("2. YYYY-MM-DD")
    print("3. Day, Month DD, YYYY")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(current_datetime.strftime("%d-%m-%Y"))

    elif choice == "2":
        print(current_datetime.strftime("%Y-%m-%d"))

    elif choice == "3":
        print(current_datetime.strftime("%A, %B %d, %Y"))

    else:
        print("Invalid choice!")

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start = time.time()

    input("Press Enter to stop the stopwatch...")
    end = time.time()

    elapsed_time = end - start

    print(f"Elapsed time: {elapsed_time:.2f} seconds")

def countdown_timer():
    try:
        seconds = int(input("Enter countdown time in seconds: "))

        if seconds <= 0:
            print("Please enter a positive number!")
            return

        while seconds > 0:
            print(f"Time remaining: {seconds} seconds")
            time.sleep(1)
            seconds -= 1

        print("Countdown finished!")

    except ValueError:
        print("Please enter a valid integer!")

def datetime_menu():
    while True:
        print("\n===== DATETIME AND TIME OPERATIONS =====")
        print("1. Display Current Date and Time")
        print("2. Calculate Difference Between Dates")
        print("3. Format Date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_current_datetime()

        elif choice == "2":
            calculate_date_difference()

        elif choice == "3":
            format_custom_date()

        elif choice == "4":
            stopwatch()

        elif choice == "5":
            countdown_timer()

        elif choice == "6":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    datetime_menu()