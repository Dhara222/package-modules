import uuid


def generate_uuid():
    unique_id = uuid.uuid4()
    print(f"Generated UUID: {unique_id}")


def generate_multiple_uuids():
    try:
        count = int(input("How many UUIDs do you want to generate? "))

        if count <= 0:
            print("Please enter a positive number.")
            return

        for i in range(count):
            unique_id = uuid.uuid4()
            print(f"UUID {i + 1}: {unique_id}")

    except ValueError:
        print("Please enter a valid integer.")


def generate_hex_uuid():
    unique_id = uuid.uuid4().hex
    print(f"UUID without hyphens: {unique_id}")


def uuid_menu():
    while True:
        print("\n===== UNIQUE IDENTIFIER GENERATION =====")
        print("1. Generate a UUID")
        print("2. Generate Multiple UUIDs")
        print("3. Generate UUID without Hyphens")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_uuid()
        elif choice == "2":
            generate_multiple_uuids()
        elif choice == "3":
            generate_hex_uuid()
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    uuid_menu()