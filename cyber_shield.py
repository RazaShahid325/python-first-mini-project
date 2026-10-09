# Cyber Shield: Defender
# A retro terminal-style hacking mini-game with 3 levels
# Uses only standard libraries: os, sys, time, random

import os
import sys
import time
import random


# ============================================================
#   UTILITY FUNCTIONS
# ============================================================

# --- Clear the screen (works on Windows and Linux/Mac) ---
def clear_screen():
    # os.name is "nt" on Windows, "posix" on Linux/Mac
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# --- Animated typing effect for text ---
# This prints text one character at a time with a small delay
def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


# --- Print a separator line ---
def separator():
    print("=" * 55)


# --- Pause and wait for the player to press Enter ---
def pause():
    type_text("\n[ Press ENTER to continue ]", 0.02)
    input()


# ============================================================
#   ASCII ART BANNER
# ============================================================

# --- Show the game banner with ASCII art ---
def show_banner():
    clear_screen()
    banner = r"""
   ____      _               _____ _    _ _   _  _____
  / ___\    | |        /\    / ____| |  | | \ | |/ ____|
 | |       | |       /  \  | (___ | |__| |  \| | |
 | |       | |      / /\ \  \___ \|  __  | . ` | |
 | |____   | |____ / ____ \ ____) | |  | | |\  | |____
  \____/   |______/_/    \_\_____/|_|  |_|_| \_|\_____|

   _____ _    _ _   _  _____  ____  _____   ____
  / ____| |  | | \ | |/ ____|/ __ \|  __ \ / __ \
 | (___ | |__| |  \| | |  __| |  | | |__) | |  | |
  \___ \|  __  | . ` | | |_ | |  | |  _  /| |  | |
  ____) | |  | | |\  | |__| | |__| | | \ \| |__| |
 |_____/|_|  |_|_| \_|\_____|\____/|_|  \_\\____/

    [ SECURE TERMINAL v3.7.1 // ACCESS GRANTED ]
"""
    print(banner)
    separator()
    type_text("  >> INITIALIZING CYBER DEFENSE PROTOCOL...", 0.02)
    time.sleep(0.5)
    type_text("  >> FIREWALL STATUS: ACTIVE", 0.02)
    time.sleep(0.3)
    type_text("  >> ENCRYPTION: AES-256", 0.02)
    time.sleep(0.3)
    type_text("  >> READY FOR DEFENSE MISSION", 0.02)
    separator()


# ============================================================
#   LEVEL 1: BINARY DECODING
# ============================================================

# --- Level 1: Convert a binary string to decimal ---
# The player has 15 seconds to answer
def level_one():
    clear_screen()
    separator()
    type_text("  [ LEVEL 1 ] BINARY DECODING", 0.02)
    separator()
    type_text("\n  >> INCOMING ENCRYPTED SIGNAL DETECTED!", 0.02)
    type_text("  >> Decode the binary string to decimal.", 0.02)
    type_text("  >> You have 15 SECONDS to respond!\n", 0.02)

    # Generate a random binary string (5 to 8 bits)
    num_bits = random.randint(5, 8)
    decimal_value = random.randint(1, 255)
    binary_string = format(decimal_value, "0" + str(num_bits) + "b")

    # Show the binary string
    separator()
    type_text("  BINARY: " + binary_string, 0.05)
    separator()

    # Record the start time
    start_time = time.time()

    # Get the player's answer
    type_text("\n  Enter the decimal value: ", 0.02)
    answer = input("  > ")

    # Calculate how much time passed
    elapsed = time.time() - start_time

    # Check if time ran out
    if elapsed > 15:
        type_text("\n  >> TIME EXPIRED! 15 seconds passed.", 0.02)
        type_text("  >> Correct answer was: " + str(decimal_value), 0.02)
        return False

    # Check if the answer is correct
    try:
        if int(answer) == decimal_value:
            type_text("\n  >> DECODE SUCCESSFUL! Signal decrypted.", 0.02)
            type_text("  >> Time: " + str(round(elapsed, 2)) + "s", 0.02)
            return True
        else:
            type_text("\n  >> DECODE FAILED! Wrong value.", 0.02)
            type_text("  >> Correct answer was: " + str(decimal_value), 0.02)
            return False
    except ValueError:
        # Player typed something that is not a number
        type_text("\n  >> INVALID INPUT! Not a number.", 0.02)
        type_text("  >> Correct answer was: " + str(decimal_value), 0.02)
        return False


# ============================================================
#   LEVEL 2: MEMORY NODE BREACH
# ============================================================

# --- Level 2: Memorize a sequence of network nodes ---
# Shows 4 nodes for 3 seconds, then asks the player to repeat them
def level_two():
    clear_screen()
    separator()
    type_text("  [ LEVEL 2 ] MEMORY NODE BREACH", 0.02)
    separator()
    type_text("\n  >> Network nodes detected in sector!", 0.02)
    type_text("  >> Memorize the EXACT sequence of 4 nodes.", 0.02)
    type_text("  >> You have 3 SECONDS to memorize!\n", 0.02)

    # The 4 possible network nodes
    all_nodes = ["ALPHA", "BETA", "GAMMA", "DELTA"]

    # Pick 4 random nodes (they can repeat)
    sequence = []
    for i in range(4):
        sequence.append(random.choice(all_nodes))

    # Show the sequence
    separator()
    type_text("  NODE SEQUENCE:", 0.02)
    print()
    for i in range(4):
        type_text("    [" + str(i + 1) + "] " + sequence[i], 0.05)
        time.sleep(0.3)
    print()
    separator()

    # Wait for 3 seconds so the player can memorize
    type_text("\n  >> Memorize... ", 0.02)
    for countdown in range(3, 0, -1):
        sys.stdout.write("\r  >> " + str(countdown) + "...  ")
        sys.stdout.flush()
        time.sleep(1)
    print()

    # Clear the screen so the sequence is hidden
    clear_screen()
    separator()
    type_text("  [ LEVEL 2 ] MEMORY NODE BREACH", 0.02)
    separator()
    type_text("\n  >> Sequence cleared from display!", 0.02)
    type_text("  >> Enter the 4 nodes in order (separated by spaces):\n", 0.02)

    # Get the player's answer
    answer = input("  > ").strip().upper()

    # Split the answer into words
    player_sequence = answer.split()

    # Check if the player got all 4 nodes correct
    if len(player_sequence) == 4 and player_sequence == sequence:
        type_text("\n  >> BREACH SUCCESSFUL! All nodes matched.", 0.02)
        return True
    else:
        type_text("\n  >> BREACH FAILED! Sequence mismatch.", 0.02)
        type_text("  >> Correct sequence: " + " ".join(sequence), 0.02)
        return False


# ============================================================
#   LEVEL 3: LOGIC BUG PATCHING
# ============================================================

# --- Level 3: Find the missing operator in an equation ---
# e.g., 8 [ ? ] 3 = 24  ->  answer is *
def level_three():
    clear_screen()
    separator()
    type_text("  [ LEVEL 3 ] LOGIC BUG PATCHING", 0.02)
    separator()
    type_text("\n  >> Logic bug detected in system code!", 0.02)
    type_text("  >> Find the missing operator to fix the equation.", 0.02)
    type_text("  >> Operators: + (add), - (subtract), * (multiply)\n", 0.02)

    # Generate two random numbers
    a = random.randint(2, 9)
    b = random.randint(2, 9)

    # Pick a random operator and calculate the result
    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    else:
        result = a * b

    # Show the equation with the missing operator
    separator()
    type_text("  EQUATION: " + str(a) + " [ ? ] " + str(b) + " = " + str(result), 0.05)
    separator()

    # Get the player's answer
    type_text("\n  Enter the correct operator (+, -, *): ", 0.02)
    answer = input("  > ").strip()

    # Check if the answer is correct
    if answer == operator:
        type_text("\n  >> BUG PATCHED! Logic restored.", 0.02)
        return True
    else:
        type_text("\n  >> PATCH FAILED! Wrong operator.", 0.02)
        type_text("  >> Correct operator was: " + operator, 0.02)
        return False


# ============================================================
#   END SCREEN: GRADE AND SUMMARY
# ============================================================

# --- Show the final results with grade and security score ---
def show_results(levels_passed, total_time):
    clear_screen()
    separator()

    # Calculate the security score (0-100)
    # Base score is levels passed * 33, capped at 100
    security_score = min(levels_passed * 33, 100)

    # Determine the grade
    if levels_passed == 3:
        grade = "S"
        rank = "ELITE DEFENDER"
    elif levels_passed == 2:
        grade = "A"
        rank = "SKILLED DEFENDER"
    elif levels_passed == 1:
        grade = "B"
        rank = "ROOKIE DEFENDER"
    else:
        grade = "F"
        rank = "COMPROMISED"

    # Determine mission status
    if levels_passed == 3:
        status = "MISSION COMPLETE"
    else:
        status = "MISSION FAILED"

    # Print the results
    print()
    type_text("           CYBER SHIELD MISSION REPORT", 0.02)
    separator()
    print()
    type_text("  Levels Cleared : " + str(levels_passed) + " / 3", 0.02)
    type_text("  Total Time     : " + str(round(total_time, 2)) + "s", 0.02)
    type_text("  Security Score : " + str(security_score) + " / 100", 0.02)
    type_text("  Grade          : " + grade, 0.02)
    type_text("  Rank           : " + rank, 0.02)
    type_text("  Mission Status : " + status, 0.02)
    print()
    separator()

    # Show a final message based on performance
    if levels_passed == 3:
        type_text("\n  >> All threats neutralized. System secure!", 0.02)
        type_text("  >> You are a true Cyber Shield Defender! 🛡", 0.02)
    elif levels_passed == 0:
        type_text("\n  >> System compromised. All defenses breached.", 0.02)
        type_text("  >> Try again, agent. The system needs you. 🛡", 0.02)
    else:
        type_text("\n  >> Partial defense successful.", 0.02)
        type_text("  >> Some threats remain. Try again! 🛡", 0.02)

    separator()


# ============================================================
#   MAIN GAME LOOP
# ============================================================

# --- The main function that runs the whole game ---
def main():
    # Show the banner
    show_banner()
    pause()

    # Track how many levels the player passed
    levels_passed = 0

    # Record the total start time
    total_start = time.time()

    # --- Level 1 ---
    if level_one():
        levels_passed = levels_passed + 1
        pause()
    else:
        # Player failed Level 1 - go to results
        total_time = time.time() - total_start
        show_results(levels_passed, total_time)
        return

    # --- Level 2 ---
    if level_two():
        levels_passed = levels_passed + 1
        pause()
    else:
        # Player failed Level 2 - go to results
        total_time = time.time() - total_start
        show_results(levels_passed, total_time)
        return

    # --- Level 3 ---
    if level_three():
        levels_passed = levels_passed + 1
        pause()
    else:
        # Player failed Level 3 - go to results
        total_time = time.time() - total_start
        show_results(levels_passed, total_time)
        return

    # All levels passed - show the final results
    total_time = time.time() - total_start
    show_results(levels_passed, total_time)


# --- Start the game ---
if __name__ == "__main__":
    main()