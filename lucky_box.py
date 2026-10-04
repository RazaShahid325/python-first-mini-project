# Lucky Box - A simple terminal game
# We use the random module to shuffle the boxes
import random

# Main game loop - keeps running until the player quits
while True:

    # Start score at 0 for a new game
    score = 0

    # We play up to 5 rounds
    round_number = 1

    # This flag tells us if the game is over (bomb found)
    game_over = False

    print("\n==============================")
    print("   Welcome to Lucky Box! 🎉")
    print("==============================")

    # Loop through 5 rounds
    while round_number <= 5:

        # Show the three boxes to the player
        print("\n--- Round", round_number, "of 5 ---")
        print("Box 1 📦   Box 2 📦   Box 3 📦")

        # Make a list of the three hidden items
        items = ["Coin 🪙", "Bomb 💣", "Empty"]

        # Shuffle the items so they are placed randomly
        random.shuffle(items)

        # Ask the player to choose a box
        choice = input("Choose a box (1, 2, or 3): ")

        # Make sure the player types a valid number
        if choice == "1" or choice == "2" or choice == "3":
            # Convert the choice from text to a number
            box_number = int(choice)
        else:
            print("That is not a valid choice. Try again.")
            # Skip the rest of this loop and ask again
            continue

        # The player chose a box, so we reveal what was inside
        # We subtract 1 because lists start at 0
        result = items[box_number - 1]

        print("You opened Box", box_number, "->", result)

        # Check what the player found
        if result == "Coin 🪙":
            # Coin gives 10 points
            score = score + 10
            print("You found a Coin! +10 points 🎉")
        elif result == "Bomb 💣":
            # Bomb ends the game
            print("BOOM! You found a Bomb! Game over. 💥")
            game_over = True
        else:
            # Empty box gives 0 points
            print("The box is empty. 0 points. 🫥")

        # Show the current score after the round
        print("Current score:", score)

        # If the bomb was found, stop playing
        if game_over == True:
            break

        # Move to the next round
        round_number = round_number + 1

    # Game finished - show the final score
    print("\n==============================")
    print("   Game Over!")
    print("   Final score:", score)
    print("==============================")

    # Ask the player if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ")

    # Check the answer (we use lower() so YES or Yes also work)
    if play_again.lower() == "yes":
        # Go back to the start of the main loop
        continue
    else:
        # Player does not want to continue
        print("Thanks for playing Lucky Box! Goodbye! 👋")
        break