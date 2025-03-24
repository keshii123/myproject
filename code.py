# Function to let the player choose a path
def choose_path():
    print("\nStep 1: The adventure begins!")
    print("You are standing in front of two mysterious caves.")
    print("One cave leads to treasure 💰, the other to danger! 🐉")
    
    print("\nStep 2: Asking the player to choose a path")
    choice = input("Choose a cave (1 or 2): ")
    
    print("\nStep 3: Validating the choice")
    while choice not in ["1", "2"]:
        print("Invalid choice! Please enter 1 or 2.")
        choice = input("Choose a cave (1 or 2): ")
    
    return int(choice)
