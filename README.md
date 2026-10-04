# 🎉 Lucky Box Game

A simple Python game where you pick boxes and try to find coins while avoiding bombs!

## 📋 Table of Contents

- [About](#about)
- [Game Rules](#game-rules)
- [Files](#files)
- [How to Run](#how-to-run)
- [Screenshots](#screenshots)
- [Requirements](#requirements)
- [Author](#author)

---

## About

This project contains two versions of the **Lucky Box** game:

| Version | File | Description |
|---------|------|-------------|
| Terminal | `lucky_box.py` | Runs in the command line / terminal |
| GUI | `lucky_box_gui.py` | Runs in a graphical window using tkinter |

Both versions are beginner-friendly with simple code and helpful comments.

---

## Game Rules

1. There are **3 boxes** 📦 shown to the player.
2. Behind the boxes are randomly hidden:
   - One **Coin** 🪙
   - One **Bomb** 💣
   - One **Empty** box 🫥
3. The player **chooses a box** (1, 2, or 3).
4. Results:
   - 🪙 **Coin** → +10 points
   - 💣 **Bomb** → Game over!
   - 🫥 **Empty** → 0 points
5. The game lasts **5 rounds** (unless you hit a bomb).
6. After the game, you can **play again**!

---

## Files

```
python-first-mini-project/
├── lucky_box.py        # Terminal version of the game
├── lucky_box_gui.py    # GUI version (tkinter) with colors
├── main.py             # Python course practice file
├── resources.py        # Python course practice file
└── .gitignore          # Tells Git which files to ignore
```

---

## How to Run

### Terminal Version

```bash
python lucky_box.py
```

Then type `1`, `2`, or `3` to choose a box.

### GUI Version

```bash
python lucky_box_gui.py
```

A window will open with 3 colorful buttons. Click a box to open it!

---

## Screenshots

### Terminal Version

```
==============================
   Welcome to Lucky Box! 🎉
==============================

--- Round 1 of 5 ---
Box 1 📦   Box 2 📦   Box 3 📦
Choose a box (1, 2, or 3): 2
You opened Box 2 -> Coin 🪙
You found a Coin! +10 points 🎉
Current score: 10
```

### GUI Version

The GUI version features:
- 🎨 **Dark background** with colorful boxes
- 📦 **Box 1** = Pink, **Box 2** = Green, **Box 3** = Blue
- 🪙 **Coin** = Gold, 💣 **Bomb** = Red, 🫥 **Empty** = Gray
- ✨ **Bold Helvetica fonts** for a beautiful look
- 🏆 Live score and round counter

---

## Requirements

- **Python 3** (any version 3.6 or higher)
- No external packages needed!
- The GUI version uses `tkinter` (included with Python)

---

## Author

**RazaShahid325**

GitHub: [https://github.com/RazaShahid325](https://github.com/RazaShahid325)

---

> Made with ❤️ as a beginner Python learning project