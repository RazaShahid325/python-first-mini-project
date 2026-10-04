# Lucky Box GUI - A beautiful game using tkinter
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
window.geometry("500x680")

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

# Box colors - each box gets a different bright color
box1_color = "#f38ba8"     # Pink for Box 1
box2_color = "#a6e3a1"     # Green for Box 2
box3_color = "#89b4fa"     # Blue for Box 3

# Lighter shades for hover effect
box1_hover = "#eba0ac"     # Lighter pink
box2_hover = "#b5e3a1"     # Lighter green
box3_hover = "#a6c4fa"     # Lighter blue

# Colors for when we reveal what is inside
coin_color = "#f9e2af"     # Gold yellow for the coin
bomb_color = "#f38ba8"     # Red pink for the bomb
empty_color = "#6c7086"    # Gray for the empty box

# --- Header frame at the top ---
# A frame is like a container that holds other widgets
header_frame = tk.Frame(window, bg=header_bg, bd=0)
header_frame.pack(fill="x", pady=(0, 5))

# --- Title label (big and beautiful) ---
title_label = tk.Label(header_frame, text="✨  Lucky Box  ✨",
                       font=("Helvetica", 32, "bold"),
                       fg=title_color, bg=header_bg)
title_label.pack(pady=(20, 5))

# --- Subtitle label ---
subtitle_label = tk.Label(header_frame, text="Pick the right box and win coins!",
                          font=("Helvetica", 13, "italic"),
                          fg=subtitle_color, bg=header_bg)
subtitle_label.pack(pady=(0, 18))

# --- Info frame (holds round and score) ---
info_frame = tk.Frame(window, bg=info_bg, bd=0)
info_frame.pack(fill="x", padx=20, pady=5)

# --- Round label (shows the current round) ---
round_label = tk.Label(info_frame, text="🎮 Round 1 of 5",
                       font=("Helvetica", 16, "bold"),
                       fg=round_color, bg=info_bg)
round_label.pack(side="left", padx=30, pady=12)

# --- Score label (shows the current score) ---
score_label = tk.Label(info_frame, text="🏆 Score: 0",
                       font=("Helvetica", 16, "bold"),
                       fg=score_color, bg=info_bg)
score_label.pack(side="right", padx=30, pady=12)

# --- Result label (shows what the player found) ---
result_label = tk.Label(window, text="👇 Pick a box below! 👇",
                        font=("Helvetica", 15, "bold"),
                        fg=result_color, bg=bg_color)
result_label.pack(pady=15)

# --- Box frame (holds the three box buttons side by side) ---
box_frame = tk.Frame(window, bg=box_frame_bg, bd=0)
box_frame.pack(pady=10)

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
    round_label.config(text="🎮 Round " + str(round_number) + " of 5")

    # Reset the result text
    result_label.config(text="👇 Pick a box below! 👇", fg=result_color)

    # Show all three box buttons again with their pretty colors
    button1.config(state="normal", text="📦\n\nBox 1", bg=box1_color, fg="white")
    button2.config(state="normal", text="📦\n\nBox 2", bg=box2_color, fg="white")
    button3.config(state="normal", text="📦\n\nBox 3", bg=box3_color, fg="white")


# --- Hover effects: make buttons lighter when mouse is over them ---
def on_enter1(event):
    if button1["state"] == "normal":
        button1.config(bg=box1_hover)

def on_leave1(event):
    if button1["state"] == "normal":
        button1.config(bg=box1_color)

def on_enter2(event):
    if button2["state"] == "normal":
        button2.config(bg=box2_hover)

def on_leave2(event):
    if button2["state"] == "normal":
        button2.config(bg=box2_color)

def on_enter3(event):
    if button3["state"] == "normal":
        button3.config(bg=box3_hover)

def on_leave3(event):
    if button3["state"] == "normal":
        button3.config(bg=box3_color)


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
        show_text = "🪙\n\nCoin!"
        show_color = coin_color
    elif result == "Bomb":
        show_text = "💣\n\nBomb!"
        show_color = bomb_color
    else:
        show_text = "🫥\n\nEmpty"
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
        result_label.config(text="🎉 You found a Coin! +10 points! 🎉", fg=coin_color)
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
    elif round_number > 5:
        # All 5 rounds are done - end the game after a short delay
        window.after(1800, end_game)
    else:
        # Wait a moment, then start the next round
        window.after(1800, start_round)


# --- This function ends the game and asks to play again ---
def end_game():
    global score, round_number

    # Show the final score in a popup message
    # Give a different message based on the score
    if score >= 40:
        msg = "🏆 Amazing! Final score: " + str(score)
    elif score >= 20:
        msg = "🎉 Good job! Final score: " + str(score)
    else:
        msg = "Game Over! Final score: " + str(score)

    messagebox.showinfo("Game Over", msg)

    # Ask the player if they want to play again
    play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")

    if play_again == True:
        # Reset everything for a new game
        score = 0
        round_number = 1
        score_label.config(text="🏆 Score: 0")
        start_round()
    else:
        # Player does not want to continue - close the window
        window.destroy()


# --- Create the three box buttons side by side with pretty colors ---
# All buttons use big bold text so they look beautiful
# relief="raised" gives a slight 3D effect to the buttons
button1 = tk.Button(box_frame, text="📦\n\nBox 1", font=("Helvetica", 18, "bold"),
                    width=8, height=4, bg=box1_color, fg="white",
                    activebackground=box1_hover, relief="raised", bd=3,
                    command=lambda: open_box(1))
button1.grid(row=0, column=0, padx=8, pady=10)

button2 = tk.Button(box_frame, text="📦\n\nBox 2", font=("Helvetica", 18, "bold"),
                    width=8, height=4, bg=box2_color, fg="white",
                    activebackground=box2_hover, relief="raised", bd=3,
                    command=lambda: open_box(2))
button2.grid(row=0, column=1, padx=8, pady=10)

button3 = tk.Button(box_frame, text="📦\n\nBox 3", font=("Helvetica", 18, "bold"),
                    width=8, height=4, bg=box3_color, fg="white",
                    activebackground=box3_hover, relief="raised", bd=3,
                    command=lambda: open_box(3))
button3.grid(row=0, column=2, padx=8, pady=10)

# --- Add hover events to the buttons ---
# When the mouse enters a button, it gets lighter
# When the mouse leaves, it goes back to normal
button1.bind("<Enter>", on_enter1)
button1.bind("<Leave>", on_leave1)
button2.bind("<Enter>", on_enter2)
button2.bind("<Leave>", on_leave2)
button3.bind("<Enter>", on_enter3)
button3.bind("<Leave>", on_leave3)

# --- Footer label at the bottom ---
footer_label = tk.Label(window, text="🪙 Coin = +10  |  💣 Bomb = Game Over  |  🫥 Empty = 0",
                        font=("Helvetica", 11, "bold"),
                        fg=footer_color, bg=bg_color)
footer_label.pack(side="bottom", pady=15)

# --- Start the first round ---
start_round()

# --- Run the window (this keeps the game open) ---
window.mainloop()
