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


def find_treasure(chosen_cave):
    print("\nStep 4: Entering the cave...")
    
    print("\nStep 5: Deciding the outcome")
    correct_cave = random.randint(1, 2)  # Randomly select the winning cave
    
    print("\nStep 6: Comparing player's choice with the correct cave")
    if chosen_cave == correct_cave:
        print("🎉 Congratulations! You found the hidden treasure! 💰")
    else:
        print("😱 Oh no! A dragon appeared and scared you away! 🐉🔥")


# Main execution starts here
print("\nStep 0: Welcome to the Treasure Hunt Game! 🎭")
chosen_cave = choose_path()

print("\nStep 7: Calling `find_treasure` function")
find_treasure(chosen_cave)

print("\nStep 8: Game Over. Thanks for playing! 🎮")
