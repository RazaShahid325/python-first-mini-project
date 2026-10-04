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

1. There are **boxes** 📦 shown to the player (number depends on level).
2. Behind the boxes are randomly hidden:
   - One **Coin** 🪙
   - One or more **Bombs** 💣
   - The rest are **Empty** boxes 🫥
3. The player **chooses a box**.
4. Results:
   - 🪙 **Coin** → +points (depends on level)
   - 💣 **Bomb** → Game over!
   - 🫥 **Empty** → 0 points
5. The game lasts for a set number of **rounds** (unless you hit a bomb).
6. After the game, you can **play again** or choose a new level!

---

## 🎯 Difficulty Levels

The GUI version has **4 difficulty levels**:

| Level | Boxes | Rounds | Points per Coin | Bombs |
|-------|-------|--------|-----------------|-------|
| 🟢 Easy | 3 | 5 | +10 | 1 |
| 🟡 Medium | 4 | 6 | +15 | 1 |
| 🟠 Hard | 5 | 7 | +20 | 2 |
| 🔴 Expert | 6 | 8 | +30 | 2 |

Pick a level at the start screen and test your luck!

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
- 🎨 **Dark background** with colorful boxes (Catppuccin Mocha theme)
- 📦 **Dynamic boxes** — 3 to 6 boxes depending on the level
- 🎯 **4 difficulty levels** — Easy, Medium, Hard, Expert
- 🪙 **Coin** = Gold, 💣 **Bomb** = Red, 🫥 **Empty** = Gray
- ✨ **Bold Helvetica fonts** for a beautiful look
- 🏆 Live score, round counter, and level indicator
- 🖱️ **Hover effects** — buttons lighten when you hover
- 📦 **3D raised buttons** with colorful borders
- 📊 **Score-based messages** — "Amazing!" for high scores

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