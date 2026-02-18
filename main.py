def display_menu():
    print("Welcome to the Trading Bot Application!")
    print("1. Start Trading")
    print("2. View Trading History")
    print("3. Settings")
    print("4. Exit")

    choice = input("Please select an option (1-4): ")
    return choice


def main():
    while True:
        user_choice = display_menu()
        
        if user_choice == '1':
            print("Starting Trading...")  # Placeholder for actual trading logic
        elif user_choice == '2':
            print("Displaying Trading History...")  # Placeholder for history logic
        elif user_choice == '3':
            print("Opening Settings...")  # Placeholder for settings logic
        elif user_choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()