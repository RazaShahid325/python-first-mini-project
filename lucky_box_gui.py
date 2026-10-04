# Lucky Box GUI - A 10-level game using tkinter
# Each level needs 30 points to pass
# If you don't get 30 points or hit a bomb, you fail the level
# Complete all 10 levels to win the game!
import random
import tkinter as tk
from tkinter import messagebox

# --- Game variables ---
score = 0            # Player's current score for this level
round_number = 1     # Which round we are on
game_over = False    # Becomes True if the bomb is found
items = []           # The hidden items for the current round
buttons = []         # List to hold the box buttons (dynamic)

# --- Level variables ---
current_level = 1    # Which level the player is on (1 to 10)
target_score = 30    # Points needed to pass each level

# --- Level settings (we change these based on the level) ---
num_boxes = 3        # How many boxes to show
num_rounds = 5       # How many rounds to play
coin_points = 10     # Points for finding a coin
num_bombs = 1        # How many bombs are hidden

# --- Create the main window ---
window = tk.Tk()
window.title("Lucky Box Game - 10 Levels")
window.geometry("620x720")

# Give the whole window a nice dark background color
window.configure(bg="#1e1e2e")

# --- Beautiful color palette (Catppuccin Mocha theme) ---
bg_color = "#1e1e2e"       # Dark background
header_bg = "#313244"      # Slightly lighter for header frame
info_bg = "#181825"        # Darker for info frame
box_frame_bg = "#11111b"   # Darkest for box area

title_color = "#f5c2e7"    # Pink for title
subtitle_color = "#89dceb" # Light blue for subtitle
round_color = "#89dceb"    # Light blue for round text
score_color = "#f9e2af"    # Gold for score text
result_color = "#fab387"   # Orange for result text
footer_color = "#6c7086"   # Gray for footer text
level_color = "#a6e3a1"    # Green for level text
target_color = "#f38ba8"   # Pink for target text

# Colors for when we reveal what is inside
coin_color = "#f9e2af"     # Gold yellow for the coin
bomb_color = "#f38ba8"     # Red pink for the bomb
empty_color = "#6c7086"    # Gray for the empty box

# --- A list of bright colors for the boxes ---
box_colors = [
    "#f38ba8",  # Pink
    "#a6e3a1",  # Green
    "#89b4fa",  # Blue
    "#fab387",  # Orange
    "#cba6f7",  # Purple
    "#f9e2af",  # Yellow
    "#94e2d5",  # Teal
    "#f5c2e7",  # Light pink
]

# Lighter shades for hover effect
box_hover_colors = [
    "#eba0ac",  # Lighter pink
    "#b5e3a1",  # Lighter green
    "#a6c4fa",  # Lighter blue
    "#fbc9a0",  # Lighter orange
    "#d4b8f7",  # Lighter purple
    "#faecb5",  # Lighter yellow
    "#a8e8df",  # Lighter teal
    "#f8d1ec",  # Lighter light pink
]

# --- Header frame at the top ---
header_frame = tk.Frame(window, bg=header_bg, bd=0)
header_frame.pack(fill="x", pady=(0, 5))

# --- Title label (big and beautiful) ---
title_label = tk.Label(header_frame, text="✨  Lucky Box  ✨",
                       font=("Helvetica", 30, "bold"),
                       fg=title_color, bg=header_bg)
title_label.pack(pady=(15, 3))

# --- Subtitle label ---
subtitle_label = tk.Label(header_frame, text="Complete all 10 levels!",
                          font=("Helvetica", 13, "italic"),
                          fg=subtitle_color, bg=header_bg)
subtitle_label.pack(pady=(0, 14))

# --- Info frame (holds level, round and score) ---
info_frame = tk.Frame(window, bg=info_bg, bd=0)
info_frame.pack(fill="x", padx=15, pady=5)

# --- Level label (shows the current level) ---
level_label = tk.Label(info_frame, text="🎯 Level 1 of 10",
                       font=("Helvetica", 14, "bold"),
                       fg=level_color, bg=info_bg)
level_label.pack(side="left", padx=10, pady=8)

# --- Round label (shows the current round) ---
round_label = tk.Label(info_frame, text="🎮 Round 1 of 5",
                       font=("Helvetica", 13, "bold"),
                       fg=round_color, bg=info_bg)
round_label.pack(side="left", padx=10, pady=8)

# --- Score label (shows the current score) ---
score_label = tk.Label(info_frame, text="🏆 Score: 0",
                       font=("Helvetica", 13, "bold"),
                       fg=score_color, bg=info_bg)
score_label.pack(side="right", padx=10, pady=8)

# --- Target label (shows points needed to pass) ---
target_label = tk.Label(window, text="🎯 Need 30 points to pass this level!",
                        font=("Helvetica", 13, "bold"),
                        fg=target_color, bg=bg_color)
target_label.pack(pady=5)

# --- Result label (shows what the player found) ---
result_label = tk.Label(window, text="👇 Pick a box below! 👇",
                        font=("Helvetica", 15, "bold"),
                        fg=result_color, bg=bg_color)
result_label.pack(pady=10)

# --- Box frame (holds the box buttons) ---
box_frame = tk.Frame(window, bg=box_frame_bg, bd=0)
box_frame.pack(pady=10)

# --- Footer label at the bottom ---
footer_label = tk.Label(window, text="",
                        font=("Helvetica", 11, "bold"),
                        fg=footer_color, bg=bg_color)
footer_label.pack(side="bottom", pady=10)


# ============================================================
#   LEVEL SETTINGS
# ============================================================

# --- This function sets up the difficulty for each level ---
# As levels go up, the game gets harder:
#   - More boxes (harder to find the coin)
#   - More bombs (more chance of game over)
#   - Fewer rounds (less chances to find coins)
def setup_level(level):
    global num_boxes, num_rounds, coin_points, num_bombs

    # Level 1-2: Easy - 3 boxes, 1 bomb, 5 rounds
    if level <= 2:
        num_boxes = 3
        num_bombs = 1
        num_rounds = 5
        coin_points = 10

    # Level 3-4: 4 boxes, 1 bomb, 5 rounds
    elif level <= 4:
        num_boxes = 4
        num_bombs = 1
        num_rounds = 5
        coin_points = 10

    # Level 5: 4 boxes, 1 bomb, 4 rounds
    elif level == 5:
        num_boxes = 4
        num_bombs = 1
        num_rounds = 4
        coin_points = 10

    # Level 6: 5 boxes, 2 bombs, 4 rounds
    elif level == 6:
        num_boxes = 5
        num_bombs = 2
        num_rounds = 4
        coin_points = 10

    # Level 7: 5 boxes, 2 bombs, 4 rounds, 15 points per coin
    elif level == 7:
        num_boxes = 5
        num_bombs = 2
        num_rounds = 4
        coin_points = 15

    # Level 8: 6 boxes, 2 bombs, 3 rounds (must find coin often!)
    elif level == 8:
        num_boxes = 6
        num_bombs = 2
        num_rounds = 3
        coin_points = 15

    # Level 9: 7 boxes, 2 bombs, 3 rounds
    elif level == 9:
        num_boxes = 7
        num_bombs = 2
        num_rounds = 3
        coin_points = 15

    # Level 10: BOSS LEVEL - 8 boxes, 3 bombs, 3 rounds
    else:
        num_boxes = 8
        num_bombs = 3
        num_rounds = 3
        coin_points = 15


# --- This function starts a level ---
def start_level(level):
    global current_level, score, round_number

    # Set the current level
    current_level = level

    # Set up the difficulty for this level
    setup_level(level)

    # Reset score and round for the new level
    score = 0
    round_number = 1

    # Update all the labels
    level_label.config(text="🎯 Level " + str(level) + " of 10")
    round_label.config(text="🎮 Round 1 of " + str(num_rounds))
    score_label.config(text="🏆 Score: 0")
    target_label.config(text="🎯 Need " + str(target_score) + " points to pass this level!")

    # Update the footer with this level's rules
    footer_label.config(text="🪙 Coin = +" + str(coin_points) + "  |  💣 Bomb = Game Over  |  "
                        + str(num_bombs) + " bomb(s) hidden")

    # Create the box buttons for this level
    create_boxes()

    # Start the first round
    start_round()


# --- This function creates the box buttons based on the level ---
def create_boxes():
    global buttons

    # Clear any old buttons
    for b in buttons:
        b.destroy()
    buttons = []

    # Create a button for each box
    for i in range(num_boxes):
        # Get the color for this box (cycle through the color list)
        color = box_colors[i % len(box_colors)]
        hover_color = box_hover_colors[i % len(box_hover_colors)]

        # Create the button
        # We use lambda with default value i to pass the box number
        btn = tk.Button(box_frame, text="📦\n\nBox " + str(i + 1),
                        font=("Helvetica", 15, "bold"),
                        width=7, height=4, bg=color, fg="white",
                        activebackground=hover_color, relief="raised", bd=3,
                        command=lambda box_num=i + 1: open_box(box_num))

        # Arrange buttons in rows of 4
        row = i // 4
        col = i % 4
        btn.grid(row=row, column=col, padx=5, pady=5)

        # Add hover effects using lambda with default values
        btn.bind("<Enter>", lambda e, b=btn, hc=hover_color: on_enter(b, hc))
        btn.bind("<Leave>", lambda e, b=btn, bc=color: on_leave(b, bc))

        # Add this button to our list
        buttons.append(btn)


# --- Hover effects: make buttons lighter when mouse is over them ---
def on_enter(button, hover_color):
    if button["state"] == "normal":
        button.config(bg=hover_color)

def on_leave(button, normal_color):
    if button["state"] == "normal":
        button.config(bg=normal_color)


# ============================================================
#   GAMEPLAY
# ============================================================

# --- This function starts a new round ---
def start_round():
    global items, game_over

    # Reset the game over flag
    game_over = False

    # Build the list of hidden items for this round
    # We need: 1 coin, some bombs, and the rest are empty
    items = []

    # Add 1 coin
    items.append("Coin")

    # Add bombs based on the level
    for i in range(num_bombs):
        items.append("Bomb")

    # Fill the rest with empty boxes
    while len(items) < num_boxes:
        items.append("Empty")

    # Shuffle the items so they are random
    random.shuffle(items)

    # Update the round label
    round_label.config(text="🎮 Round " + str(round_number) + " of " + str(num_rounds))

    # Reset the result text
    result_label.config(text="👇 Pick a box below! 👇", fg=result_color)

    # Reset all box buttons to their original colors
    for i in range(num_boxes):
        color = box_colors[i % len(box_colors)]
        buttons[i].config(state="normal", text="📦\n\nBox " + str(i + 1),
                          bg=color, fg="white")


# --- This function runs when a box button is clicked ---
# box_choice is 1, 2, 3, etc.
def open_box(box_choice):
    global score, round_number, game_over

    # If the game is already over, do nothing
    if game_over == True:
        return

    # Disable all buttons so the player cannot click again this round
    for b in buttons:
        b.config(state="disabled")

    # Find out what was inside the chosen box
    # We subtract 1 because lists start at 0
    result = items[box_choice - 1]

    # Show the result on the chosen button with a matching color
    if result == "Coin":
        show_text = "🪙\n\nCoin!"
        show_color = coin_color
    elif result == "Bomb":
        show_text = "💣\n\nBomb!"
        show_color = bomb_color
    else:
        show_text = "🫥\n\nEmpty"
        show_color = empty_color

    # Put the result text and color on the chosen button
    buttons[box_choice - 1].config(text=show_text, bg=show_color, fg="black")

    # Check what the player found and update the score
    if result == "Coin":
        # Coin gives points based on the level
        score = score + coin_points
        result_label.config(text="🎉 You found a Coin! +" + str(coin_points) + " points! 🎉",
                             fg=coin_color)
    elif result == "Bomb":
        # Bomb ends the game
        game_over = True
        result_label.config(text="💥 BOOM! You found a Bomb! 💥", fg=bomb_color)
    else:
        # Empty box gives 0 points
        result_label.config(text="🫥 The box is empty. 0 points.", fg=empty_color)

    # Update the score label
    score_label.config(text="🏆 Score: " + str(score))

    # Move to the next round or end the level
    round_number = round_number + 1

    # Check if the level should end
    if game_over == True:
        # Bomb was found - end the level after a short delay
        window.after(1800, fail_level)
    elif round_number > num_rounds:
        # All rounds are done - check if player passed the level
        window.after(1800, check_level)
    else:
        # Wait a moment, then start the next round
        window.after(1800, start_round)


# --- This function checks if the player passed the level ---
def check_level():
    global score, current_level

    # Did the player reach the target score?
    if score >= target_score:
        # Player passed the level!
        level_complete()
    else:
        # Player did not get enough points
        fail_level()


# --- This function runs when the player passes a level ---
def level_complete():
    global current_level

    # Check if the player has completed all 10 levels
    if current_level >= 10:
        # Player won the entire game!
        messagebox.showinfo("🏆 YOU WIN!",
                           "🎉 Congratulations! You completed all 10 levels!\n"
                           "You are a Lucky Box Master! 🏆")

        # Ask if they want to play again from level 1
        play_again = messagebox.askyesno("Play Again?",
                                        "Do you want to start over from Level 1?")

        if play_again == True:
            start_level(1)
        else:
            window.destroy()
    else:
        # Player passed this level - show a message
        messagebox.showinfo("✅ Level " + str(current_level) + " Complete!",
                           "🎉 Great job! You passed Level " + str(current_level) + "!\n"
                           "You scored " + str(score) + " points.\n"
                           "Get ready for Level " + str(current_level + 1) + "!")

        # Move to the next level
        start_level(current_level + 1)


# --- This function runs when the player fails a level ---
def fail_level():
    global score, current_level

    # Show a failure message
    if game_over == True:
        reason = "You hit a bomb! 💥"
    else:
        reason = "You only scored " + str(score) + " points.\nYou needed " + str(target_score) + " to pass."

    messagebox.showinfo("❌ Level " + str(current_level) + " Failed",
                       "Game Over!\n" + reason)

    # Ask the player what they want to do
    choice = messagebox.askyesno("Try Again?",
                               "Do you want to retry Level " + str(current_level) + "?")

    if choice == True:
        # Retry the same level
        start_level(current_level)
    else:
        # Player gives up - close the window
        window.destroy()


# --- Start the game at Level 1 ---
start_level(1)

# --- Run the window (this keeps the game open) ---
window.mainloop()
