from datetime import datetime
import math
import os
import random
import time
import uuid

# --- File Utility Functions ---

def create_file(name):
    with open(name, "w") as f:
        pass
    print("File created successfully.")

def write_file(name, data):
    with open(name, "w") as f:
        f.write(data)
    print("Data written successfully.")

def append_file(name, data):
    with open(name, "a") as f:
        f.write(data)
    print("Data appended successfully.")

def read_file(name):
    try:
        with open(name, "r") as f:
            print("\nFile Content:")
            print(f.read())
    except FileNotFoundError:
        print("File not found.")

def delete_file(name):
    if os.path.exists(name):
        os.remove(name)
        print("File deleted successfully.")
    else:
        print("File not found.")


# --- Main Menu Loop ---

while True:
    print("\n========== PYTHON MODULE PROJECT ==========")
    print("1. Date & Time")
    print("2. Math Operations")
    print("3. Random Module")
    print("4. UUID Module")
    print("5. File Operations")
    print("6. Explore Module (dir)")
    print("7. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        while True:
            print("\n Date & Time Operations:")
            print("1. Current Date & Time")
            print("2. Calculate difference between two dates")
            print("3. Format date into custom format")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            print("6. Back to Main Menu\n")

            try:
                choice = int(input("Enter Your choice: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice == 1:
                print("\nCurrent Date & Time :", datetime.now())
            elif choice == 2:
                create_date = input("Enter the first date (YYYY-MM-DD): ")
                end_date = input("Enter the second date (YYYY-MM-DD): ")
                try:
                    d1 = datetime.strptime(create_date, "%Y-%m-%d")
                    d2 = datetime.strptime(end_date, "%Y-%m-%d")
                    print("Difference between two dates :", d2 - d1)
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            elif choice == 3:
                date_input = input("Enter a date (YYYY-MM-DD): ")
                try:
                    date_obj = datetime.strptime(date_input, "%Y-%m-%d")
                    print("Formatted Date :", date_obj.strftime("%A, %B %d, %Y"))
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            elif choice == 4:
                input("Press Enter to start the stopwatch...")
                start_time = datetime.now()
                input("Press Enter to stop the stopwatch...")
                end_time = datetime.now()
                print("Elapsed Time:", end_time - start_time)
            elif choice == 5:
                try:
                    seconds = int(input("Enter countdown time in seconds: "))
                    while seconds > 0:
                        print(f"Time remaining: {seconds}s", end="\r")
                        time.sleep(1)
                        seconds -= 1
                    print("\nTime's up!")
                except ValueError:
                    print("Please enter a valid number of seconds.")
            elif choice == 6:
                break
            else:
                print("Invalid choice. Try again.")

    elif ch == "2":
        try:
            n = float(input("Enter a number: "))
            if n >= 0:
                print("Square Root :", math.sqrt(n))
                print("Factorial :", math.factorial(int(n)))
            else:
                print("Square root and factorial require a non-negative number.")
            print("Power (n^2):", math.pow(n, 2))
            print("Ceil :", math.ceil(n / 2))
            print("Floor :", math.floor(n / 2))
        except ValueError:
            print("Please enter a valid numeric value.")

    elif ch == "3":
        print("Random Number :", random.randint(1, 100))
        print("Random List :", random.sample(range(1, 100), 5))

        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        password = "".join(random.choices(chars, k=8))
        print("Random Password :", password)

        print("OTP :", random.randint(100000, 999999))
        data = ['A', 'B', 'C', 'D', 'E']
        print("Random Sample :", random.sample(data, 3))
        print("Dice Roll :", random.randint(1, 6))

    elif ch == "4":
        print("Generated UUID :", uuid.uuid4())

    elif ch == "5":
        while True:
            print("\n========== FILE OPERATIONS ==========")
            print("1. Create a new File")
            print("2. Write to a File")
            print("3. Append to a File")
            print("4. Read from a File")
            print("5. Delete a File")
            print("6. Back to Main Menu")

            file_choice = input("Enter your choice: ")

            if file_choice == "1":
                filename = input("Enter file name to create: ")
                create_file(filename)
            elif file_choice == "2":
                filename = input("Enter file name to write: ")
                data = input("Enter data to write: ")
                write_file(filename, data)
            elif file_choice == "3":
                filename = input("Enter file name to append: ")
                data = input("Enter data to append: ")
                append_file(filename, data)
            elif file_choice == "4":
                filename = input("Enter file name to read: ")
                read_file(filename)
            elif file_choice == "5":
                filename = input("Enter file name to delete: ")
                delete_file(filename)
            elif file_choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    elif ch == "6":
        print("\ndir(math):", dir(math))
        print("\ndir(random):", dir(random))
        print("\ndir(uuid):", dir(uuid))

    elif ch == "7":
        print("Thank you for using the Multi-Utility Toolkit!")
        break

    else:
        print("Invalid choice. Please try again.")