from utilities.datetime_utils import datetime_menu
from utilities.math_utils import math_menu
from utilities.random_utils import random_menu
from utilities.uuid_utils import uuid_menu
from utilities.file_utils import file_menu

def explore_modules():
    import datetime
    import math
    import random
    import uuid
    import time

    modules = {"datetime": datetime,
        "math": math,
        "random": random,
        "uuid": uuid,
        "time": time}

    print("\n===== MODULE EXPLORER =====")

    for name, module in modules.items():
        print(f"\n{name.upper()} MODULE")
        print(dir(module))

def main_menu():
    while True:
        print("\n===================================")
        print("       MULTI-UTILITY TOOLKIT")
        print("===================================")
        print("1. Date and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. UUID Generation")
        print("5. File Operations")
        print("6. Explore Built-in Modules")
        print("7. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            uuid_menu()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_modules()

        elif choice == "7":
            print("Thank you for using Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice! Please enter 1-7.")

if __name__ == "__main__":
    main_menu()