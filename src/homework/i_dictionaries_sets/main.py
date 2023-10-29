from dictionary import add_inventory, remove_inventory_widget

def display_menu():
    print("Inventory Menu\n")
    print("1- Add or Update Item")
    print("2- Delete Item")
    print("3- Exit")
    print("4- Check Inventory")

def main():
    inventory = {}  # Initialize an empty inventory dictionary

    while True:
        display_menu()
        choice = input("Select an option (1, 2, 3, or 4): ")

        if choice == '1':
            while True:
                # Add or update item
                item_name = input("Enter the item name: ")
                try:
                    quantity = int(input("Enter the quantity: "))
                    add_inventory(inventory, item_name, quantity)
                    print(f"{item_name} with a quantity of {quantity} has been added or updated.")
                except ValueError:
                    print("Invalid quantity. Please enter a valid number.")
                another_item = input("Would you like to add another item to inventory (Y/N)? ").strip().lower()
                if another_item not in ['y', 'yes']:
                    break

        elif choice == '2':
            # Delete item or quantity
            while True:  # Add a loop to handle multiple deletions
                item_name = input("Enter the item name to delete: ")
                result = remove_inventory_widget(inventory, item_name)
                print(result)

                another_deletion = input("Do you want to delete another item (Y/N)?: ").strip().lower()
                if another_deletion not in ['y', 'yes']:
                    break  # Break out of the deletion loop if not 'Y' or 'yes    

        elif choice == '3':
            # Exit the program
            print("Exiting the program.")
            break

        elif choice == '4':
            if not inventory:  # Check if inventory is empty
                print("No Inventory to Count. Add Items if you have any.")

            else:
                for item_name, quantity in inventory.items():
                    print(f"{item_name}: {quantity}")

                menu = input("Press Enter to go back to the main menu")
                if menu != None:
                    print("Going to the main menu")

        else:
            # Invalid input
            print("Select a Valid Input, please try again.")
main()
