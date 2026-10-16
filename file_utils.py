import os

def create_file():
    filename = input("Enter file name (e.g., notes.txt): ")

    try:
        with open(filename, "x", encoding="utf-8") as file:
            pass

        print(f"File '{filename}' created successfully!")

    except FileExistsError:
        print("File already exists!")

def write_file():
    filename = input("Enter file name: ")
    content = input("Enter content to write: ")

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content + "\n")

        print("Data written successfully!")

    except OSError as error:
        print(f"File error: {error}")

def read_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        print("\nFile Content:")
        print(content)

    except FileNotFoundError:
        print("File does not exist!")

    except OSError as error:
        print(f"File error: {error}")

def append_file():
    filename = input("Enter file name: ")
    content = input("Enter content to append: ")

    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(content + "\n")

        print("Data appended successfully!")

    except OSError as error:
        print(f"File error: {error}")

def file_menu():
    while True:
        print("\n===== FILE OPERATIONS =====")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            append_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    file_menu()