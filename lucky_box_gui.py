# Lucky Box GUI - A simple game using tkinter
# We use tkinter for the window and buttons
# We use random to shuffle the boxes
import random
import tkinter as tk
from tkinter import messagebox

# --- Game variables ---
score = 0          # Player's current score
round_number = 1   # Which round we are on (1 to 5)
game_over = False  # Becomes True if the bomb is found
items = []         # The hidden items for the current round

# --- Create the main window ---
window = tk.Tk()
window.title("Lucky Box Game")
window.geometry("460x580")

# Give the whole window a nice dark background color
window.configure(bg="#1e1e2e")

# --- Some colors we will use ---
bg_color = "#1e1e2e"       # Dark background
title_color = "#f5e0fc"    # Light purple for title
round_color = "#89dceb"    # Light blue for round text
score_color = "#f9e2af"    # Gold for score text
result_color = "#fab387"   # Orange for result text

# Box colors - each box gets a different bright color
box1_color = "#f38ba8"     # Pink for Box 1
box2_color = "#a6e3a1"     # Green for Box 2
box3_color = "#89b4fa"     # Blue for Box 3

# Colors for when we reveal what is inside
coin_color = "#f9e2af"     # Gold yellow for the coin
bomb_color = "#f38ba8"     # Red pink for the bomb
empty_color = "#6c7086"    # Gray for the empty box

# --- Title label at the top ---
# Big bold title with a decorative look
title_label = tk.Label(window, text="✨ Lucky Box! ✨",
                       font=("Helvetica", 28, "bold"),
                       fg=title_color, bg=bg_color)
title_label.pack(pady=18)

# --- Round label (shows the current round) ---
round_label = tk.Label(window, text="Round 1 of 5",
                       font=("Helvetica", 16, "bold"),
                       fg=round_color, bg=bg_color)
round_label.pack(pady=6)

# --- Score label (shows the current score) ---
score_label = tk.Label(window, text="Score: 0",
                       font=("Helvetica", 16, "bold"),
                       fg=score_color, bg=bg_color)
score_label.pack(pady=6)

# --- Result label (shows what the player found) ---
result_label = tk.Label(window, text="Pick a box!",
                        font=("Helvetica", 14, "bold"),
                        fg=result_color, bg=bg_color)
result_label.pack(pady=12)

# --- This function starts a new round ---
def start_round():
    global items, game_over

    # Reset the game over flag
    game_over = False

    # Make the list of three hidden items
    items = ["Coin", "Bomb", "Empty"]

    # Shuffle the items so they are random
    random.shuffle(items)

    # Update the round label
    round_label.config(text="Round " + str(round_number) + " of 5")

    # Reset the result text
    result_label.config(text="Pick a box!", fg=result_color)

    # Show all three box buttons again with their pretty colors
    button1.config(state="normal", text="📦\nBox 1", bg=box1_color, fg="white")
    button2.config(state="normal", text="📦\nBox 2", bg=box2_color, fg="white")
    button3.config(state="normal", text="📦\nBox 3", bg=box3_color, fg="white")


# --- This function runs when a box button is clicked ---
# box_choice is 1, 2, or 3
def open_box(box_choice):
    global score, round_number, game_over

    # If the game is already over, do nothing
    if game_over == True:
        return

    # Disable all buttons so the player cannot click again this round
    button1.config(state="disabled")
    button2.config(state="disabled")
    button3.config(state="disabled")

    # Find out what was inside the chosen box
    # We subtract 1 because lists start at 0
    result = items[box_choice - 1]

    # Show the result on the chosen button with a matching color
    if result == "Coin":
        show_text = "🪙\nCoin!"
        show_color = coin_color
    elif result == "Bomb":
        show_text = "💣\nBomb!"
        show_color = bomb_color
    else:
        show_text = "🫥\nEmpty"
        show_color = empty_color

    # Put the result text and color on the chosen button
    if box_choice == 1:
        button1.config(text=show_text, bg=show_color, fg="black")
    elif box_choice == 2:
        button2.config(text=show_text, bg=show_color, fg="black")
    elif box_choice == 3:
        button3.config(text=show_text, bg=show_color, fg="black")

    # Check what the player found and update the score
    if result == "Coin":
        # Coin gives 10 points
        score = score + 10
        result_label.config(text="You found a Coin! +10 points 🎉", fg=coin_color)
    elif result == "Bomb":
        # Bomb ends the game
        game_over = True
        result_label.config(text="BOOM! You found a Bomb! 💥", fg=bomb_color)
    else:
        # Empty box gives 0 points
        result_label.config(text="The box is empty. 0 points.", fg=empty_color)

    # Update the score label
    score_label.config(text="Score: " + str(score))

    # Move to the next round or end the game
    round_number = round_number + 1

    # Check if the game should end
    if game_over == True:
        # Bomb was found - end the game after a short delay
        window.after(1500, end_game)
    elif round_number > 5:
        # All 5 rounds are done - end the game after a short delay
        window.after(1500, end_game)
    else:
        # Wait a moment, then start the next round
        window.after(1500, start_round)


# --- This function ends the game and asks to play again ---
def end_game():
    global score, round_number

    # Show the final score in a popup message
    messagebox.showinfo("Game Over", "Final score: " + str(score))

    # Ask the player if they want to play again
    play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")

    if play_again == True:
        # Reset everything for a new game
        score = 0
        round_number = 1
        score_label.config(text="Score: 0")
        start_round()
    else:
        # Player does not want to continue - close the window
        window.destroy()


# --- Create the three box buttons with pretty colors ---
# Each button calls open_box() with its number when clicked
# All buttons use big bold text so they look beautiful
button1 = tk.Button(window, text="📦\nBox 1", font=("Helvetica", 18, "bold"),
                    width=10, height=3, bg=box1_color, fg="white",
                    activebackground="#eba0ac", command=lambda: open_box(1))
button1.pack(pady=10)

button2 = tk.Button(window, text="📦\nBox 2", font=("Helvetica", 18, "bold"),
                    width=10, height=3, bg=box2_color, fg="white",
                    activebackground="#94e2d5", command=lambda: open_box(2))
button2.pack(pady=10)

button3 = tk.Button(window, text="📦\nBox 3", font=("Helvetica", 18, "bold"),
                    width=10, height=3, bg=box3_color, fg="white",
                    activebackground="#b4befe", command=lambda: open_box(3))
button3.pack(pady=10)

# --- Start the first round ---
start_round()

# --- Run the window (this keeps the game open) ---
window.mainloop()
