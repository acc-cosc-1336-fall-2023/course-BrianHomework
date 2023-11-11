#

from class_a import Die

die = Die()

def main():
    while True:
        print("1. Roll the die")
        print("2. Exit")
    
        choice = input("Enter your choice: ")

        if choice == "1":
            die.roll()
            print(die)
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
main()            