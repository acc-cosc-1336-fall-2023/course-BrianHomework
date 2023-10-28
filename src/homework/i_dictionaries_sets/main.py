from dictionary import add_inventory, remove_inventory_widget

def display_menu():
    print("Inventory Menu\n")
    print("1- Add or Update Item")
    print("2- Delete Item")
    print("3- Exit")

def main():
        inventory = {}  # Initialize an empty inventory dictionary

        while True:
            display_menu()
            choice = input("Select an option (1, 2, or 3): ")

            if choice == '1':
                # Add or update item
                item_name = str(input("Enter the item name: "))
                try:
                    quantity = int(input("Enter the quantity: "))
                    add_inventory(inventory, item_name, quantity)
                    print(f"{item_name} with a quantity of {quantity} has been added or updated.")
                except ValueError:
                     print("That aint a number!")
                           
            elif choice == '2':
                # Delete item
                item_name = input("Enter the item name to delete: ")
                result = remove_inventory_widget(inventory, item_name)
                print(result)

            elif choice == '3':
                # Exit the program
                print("Exiting the program.")
                break

            else:
            # Invalid input
                print("Select a Valid Input, please try again.")
    
