# Function to let the player choose a path
def choose_path():
    print("\nStep 1: The adventure begins!")
    print("You are standing in front of two mysterious caves.")
    print("One cave leads to treasure , the other to danger! ")
    
    print("\nStep 2: Asking the player to choose a path")
    choice = input("Choose a cave (1 or 2): ")
    
    print("\nStep 3: Validating the choice")
    while choice not in ["1", "2"]:
        print("Invalid choice! Please enter 1 or 2.")
        choice = input("Choose a cave (1 or 2): ")
    
    return int(choice)


# Function to determine if the player finds treasure or danger
def find_treasure(chosen_cave):
    print("\nStep 4: Entering the cave...")
    
    print("\nStep 5: Deciding the outcome")
    correct_cave = random.randint(1, 2)  # Randomly select the winning cave
    
    print("\nStep 6: Comparing player's choice with the correct cave")
    if chosen_cave == correct_cave:
        print("🎉 Congratulations! You found the hidden treasure! ")
    else:
        print("Oh no! A dragon appeared and scared you away!")

# Main execution starts here
print("\nStep 0: Welcome to the Treasure Hunt Game! ")
chosen_cave = choose_path()

print("\nStep 7: Calling `find_treasure` function")
find_treasure(chosen_cave)

print("\nStep 8: Game Over. Thanks for playing! ")


import random

# Function to let the player choose a path
def choose_path():
    print("\nStep 1: The adventure begins!")
    print("You are standing in front of two mysterious caves.")
    print("One cave leads to treasure, the other to danger! ")
    
    print("\nStep 2: Asking the player to choose a path")
    choice = input("Choose a cave (1 or 2): ")
    
    print("\nStep 3: Validating the choice")
    while choice not in ["1", "2"]:
        print("Invalid choice! Please enter 1 or 2.")
        choice = input("Choose a cave (1 or 2): ")
    
    return int(choice)

# Function to check if the player finds a magical artifact
def find_artifact():
    print("\nStep 4: Searching for a magical artifact...")
    has_artifact = random.choice([True, False])  # 50% chance of finding an artifact
    
    if has_artifact:
        print("✨ You found a magical artifact! It may help you in danger! 🏺")
    else:
        print("No artifact found... Hope you won’t need it! 😬")
    
    return has_artifact

# Function to determine if the player finds treasure or danger
def find_treasure(chosen_cave, has_artifact):
    print("\nStep 5: Entering the cave...")
    
    print("\nStep 6: Deciding the outcome")
    correct_cave = random.randint(1, 2)  # Randomly select the winning cave
    
    print("\nStep 7: Comparing player's choice with the correct cave")
    if chosen_cave == correct_cave:
        print("🎉 Congratulations! You found the hidden treasure! ")
    else:
        print("Oh no! A dragon appeared and scared you away!")
        
        # If the player has the artifact, they escape automatically
        if has_artifact:
            print("\nStep 8: The artifact glows and teleports you to safety! ✨ You escaped! 🏃‍♂💨")
            return
        
        # New feature: The player gets one last chance to escape
        print("\nStep 9: The dragon is chasing you! You have one last chance to escape! 🏃💨")
        escape_choice = input("Quick! Choose a number (1 or 2) to dodge the dragon: ")
        
        print("\nStep 10: Checking if you escaped")
        if escape_choice == str(random.randint(1, 2)):
            print("🔥 You barely escaped the dragon and survived! 😮‍💨")
        else:
            print("💀 The dragon caught you! Game Over...")

# Main execution starts here
print("\nStep 0: Welcome to the Treasure Hunt Game! ")
chosen_cave = choose_path()

print("\nStep 11: Checking for a magical artifact...")
has_artifact = find_artifact()  # New function call to check for artifact

print("\nStep 12: Calling find_treasure function")
find_treasure(chosen_cave, has_artifact)

print("\nStep 13: Game Over. Thanks for playing! ")

