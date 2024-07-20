""" 
Objective: Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.
"""

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shoppping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            shoppping_list.append(item)
            print(f"'{item}' has been added to the list.")
        elif choice == "2":
            item = input("Enter the item to remove: ")
            if item in shoppping_list:
                shoppping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == "3":
            if shoppping_list:
                print("Current Shopping List: ")
                for i, item in enumerate(shoppping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is currently empty.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()