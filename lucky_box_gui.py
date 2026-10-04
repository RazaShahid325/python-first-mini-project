# Lucky Box GUI - A beautiful game with levels using tkinter
# We use tkinter for the window and buttons
# We use random to shuffle the boxes
import random
import tkinter as tk
from tkinter import messagebox

# --- Game variables ---
score = 0            # Player's current score
round_number = 1     # Which round we are on
game_over = False    # Becomes True if the bomb is found
items = []           # The hidden items for the current round
buttons = []         # List to hold the box buttons (dynamic)

# --- Level settings (we change these when player picks a level) ---
num_boxes = 3        # How many boxes to show
num_rounds = 5       # How many rounds to play
coin_points = 10     # Points for finding a coin
num_bombs = 1        # How many bombs are hidden
current_level = 1    # Which level the player is on
level_name = "Easy"  # Name of the current level

# --- Create the main window ---
window = tk.Tk()
window.title("Lucky Box Game")
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

# Colors for when we reveal what is inside
coin_color = "#f9e2af"     # Gold yellow for the coin
bomb_color = "#f38ba8"     # Red pink for the bomb
empty_color = "#6c7086"    # Gray for the empty box

# --- A list of bright colors for the boxes ---
# We cycle through these colors for each box
box_colors = [
    "#f38ba8",  # Pink
    "#a6e3a1",  # Green
    "#89b4fa",  # Blue
    "#fab387",  # Orange
    "#cba6f7",  # Purple
    "#f9e2af",  # Yellow
]

# Lighter shades for hover effect
box_hover_colors = [
    "#eba0ac",  # Lighter pink
    "#b5e3a1",  # Lighter green
    "#a6c4fa",  # Lighter blue
    "#fbc9a0",  # Lighter orange
    "#d4b8f7",  # Lighter purple
    "#faecb5",  # Lighter yellow
]

# --- Header frame at the top ---
header_frame = tk.Frame(window, bg=header_bg, bd=0)
header_frame.pack(fill="x", pady=(0, 5))

# --- Title label (big and beautiful) ---
title_label = tk.Label(header_frame, text="✨  Lucky Box  ✨",
                       font=("Helvetica", 32, "bold"),
                       fg=title_color, bg=header_bg)
title_label.pack(pady=(18, 5))

# --- Subtitle label ---
subtitle_label = tk.Label(header_frame, text="Pick the right box and win coins!",
                          font=("Helvetica", 13, "italic"),
                          fg=subtitle_color, bg=header_bg)
subtitle_label.pack(pady=(0, 16))

# --- Info frame (holds level, round and score) ---
info_frame = tk.Frame(window, bg=info_bg, bd=0)
info_frame.pack(fill="x", padx=20, pady=5)

# --- Level label (shows the current level) ---
level_label = tk.Label(info_frame, text="🟢 Easy Level",
                       font=("Helvetica", 13, "bold"),
                       fg=level_color, bg=info_bg)
level_label.pack(side="left", padx=15, pady=10)

# --- Round label (shows the current round) ---
round_label = tk.Label(info_frame, text="🎮 Round 1 of 5",
                       font=("Helvetica", 14, "bold"),
                       fg=round_color, bg=info_bg)
round_label.pack(side="left", padx=15, pady=10)

# --- Score label (shows the current score) ---
score_label = tk.Label(info_frame, text="🏆 Score: 0",
                       font=("Helvetica", 14, "bold"),
                       fg=score_color, bg=info_bg)
score_label.pack(side="right", padx=15, pady=10)

# --- Result label (shows what the player found) ---
result_label = tk.Label(window, text="👇 Pick a box below! 👇",
                        font=("Helvetica", 15, "bold"),
                        fg=result_color, bg=bg_color)
result_label.pack(pady=12)

# --- Box frame (holds the box buttons) ---
box_frame = tk.Frame(window, bg=box_frame_bg, bd=0)
box_frame.pack(pady=10)

# --- Footer label at the bottom ---
footer_label = tk.Label(window, text="",
                        font=("Helvetica", 11, "bold"),
                        fg=footer_color, bg=bg_color)
footer_label.pack(side="bottom", pady=12)


# ============================================================
#   LEVEL SELECTION SCREEN
# ============================================================

# --- This function shows the level selection screen ---
def show_level_screen():
    global buttons

    # Clear any old buttons
    for b in buttons:
        b.destroy()
    buttons = []

    # Update the labels for the level screen
    level_label.config(text="Choose a Level")
    round_label.config(text="")
    score_label.config(text="🏆 Score: " + str(score))
    result_label.config(text="Select your difficulty below 👇", fg=result_color)
    footer_label.config(text="🪙 Coin = points  |  💣 Bomb = Game Over  |  🫥 Empty = 0")

    # Level options: (level number, name, boxes, rounds, points, bombs, emoji, color)
    levels = [
        (1, "Easy",   3, 5, 10, 1, "🟢", "#a6e3a1"),
        (2, "Medium", 4, 6, 15, 1, "🟡", "#f9e2af"),
        (3, "Hard",   5, 7, 20, 2, "🟠", "#fab387"),
        (4, "Expert", 6, 8, 30, 2, "🔴", "#f38ba8"),
    ]

    # Create a button for each level
    for lvl in levels:
        lvl_num, name, boxes, rounds, pts, bombs, emoji, color = lvl

        # Build the description text for this level button
        desc = emoji + "  " + name + "\n"
        desc += str(boxes) + " boxes  |  " + str(rounds) + " rounds\n"
        desc += "+" + str(pts) + " per coin  |  " + str(bombs) + " bomb(s)"

        # Create the level button
        # We use lambda with default values to pass the level info
        btn = tk.Button(box_frame, text=desc,
                        font=("Helvetica", 13, "bold"),
                        width=18, height=4, bg=color, fg="black",
                        relief="raised", bd=3,
                        command=lambda n=lvl_num, nm=name, nb=boxes,
                               nr=rounds, cp=pts, bm=bombs: start_game(n, nm, nb, nr, cp, bm))
        btn.pack(pady=6, fill="x", padx=30)
        buttons.append(btn)


# --- This function starts the game with the chosen level ---
# n = level number, nm = level name, nb = number of boxes,
# nr = number of rounds, cp = coin points, bm = number of bombs
def start_game(n, nm, nb, nr, cp, bm):
    global current_level, level_name, num_boxes, num_rounds
    global coin_points, num_bombs, score, round_number

    # Save the level settings
    current_level = n
    level_name = nm
    num_boxes = nb
    num_rounds = nr
    coin_points = cp
    num_bombs = bm

    # Reset score and round for the new game
    score = 0
    round_number = 1

    # Update the labels
    score_label.config(text="🏆 Score: 0")

    # Set the level label with the right emoji and color
    if n == 1:
        level_label.config(text="🟢 " + nm + " Level", fg="#a6e3a1")
    elif n == 2:
        level_label.config(text="🟡 " + nm + " Level", fg="#f9e2af")
    elif n == 3:
        level_label.config(text="🟠 " + nm + " Level", fg="#fab387")
    else:
        level_label.config(text="🔴 " + nm + " Level", fg="#f38ba8")

    # Update the footer with this level's rules
    footer_label.config(text="🪙 Coin = +" + str(cp) + "  |  💣 Bomb = Game Over  |  🫥 Empty = 0")

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
                        font=("Helvetica", 16, "bold"),
                        width=8, height=4, bg=color, fg="white",
                        activebackground=hover_color, relief="raised", bd=3,
                        command=lambda box_num=i + 1: open_box(box_num))
        btn.grid(row=0, column=i, padx=6, pady=10)

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

    # Move to the next round or end the game
    round_number = round_number + 1

    # Check if the game should end
    if game_over == True:
        # Bomb was found - end the game after a short delay
        window.after(1800, end_game)
    elif round_number > num_rounds:
        # All rounds are done - end the game after a short delay
        window.after(1800, end_game)
    else:
        # Wait a moment, then start the next round
        window.after(1800, start_round)


# --- This function ends the game and asks what to do next ---
def end_game():
    global score, round_number

    # Build a message based on the score and level
    max_possible = num_rounds * coin_points
    if score >= max_possible * 0.7:
        msg = "🏆 Amazing! You scored " + str(score) + " points!\n"
        msg += "You are a Lucky Box master!"
    elif score >= max_possible * 0.4:
        msg = "🎉 Good job! You scored " + str(score) + " points!"
    else:
        msg = "Game Over! You scored " + str(score) + " points."

    messagebox.showinfo(level_name + " Level - Game Over", msg)

    # Ask the player what they want to do next
    play_again = messagebox.askyesno("Play Again?",
                                    "Do you want to choose a level and play again?")

    if play_again == True:
        # Reset everything and show the level screen
        score = 0
        round_number = 1
        score_label.config(text="🏆 Score: 0")
        show_level_screen()
    else:
        # Player does not want to continue - close the window
        window.destroy()


# --- Show the level selection screen when the game starts ---
show_level_screen()

# --- Run the window (this keeps the game open) ---
window.mainloop()
