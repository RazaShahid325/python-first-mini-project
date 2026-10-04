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
   - 💣 **Bomb** → Level failed!
   - 🫥 **Empty** → 0 points
5. Each level lasts for a set number of **rounds**.
6. You need **30 points** to pass each level!
7. If you don't reach 30 points or hit a bomb, you can **retry** the level.
8. Complete all **10 levels** to win the game!

---

## 🎯 10 Levels

The GUI version has **10 levels** that get harder as you progress.
Each level requires **30 points** to pass!

| Level | Boxes | Rounds | Points per Coin | Bombs | Difficulty |
|-------|-------|--------|-----------------|-------|------------|
| 1-2 | 3 | 5 | +10 | 1 | 🟢 Easy |
| 3-4 | 4 | 5 | +10 | 1 | 🟢 Easy |
| 5 | 4 | 4 | +10 | 1 | 🟡 Medium |
| 6 | 5 | 4 | +10 | 2 | 🟡 Medium |
| 7 | 5 | 4 | +15 | 2 | 🟠 Hard |
| 8 | 6 | 3 | +15 | 2 | 🟠 Hard |
| 9 | 7 | 3 | +15 | 2 | 🔴 Expert |
| 10 | 8 | 3 | +15 | 3 | 🔴 Boss! |

Pass all 10 levels to become a **Lucky Box Master!** 🏆

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
- 📦 **Dynamic boxes** — 3 to 8 boxes depending on the level
- 🎯 **10 levels** — each needs 30 points to pass, gets harder as you go
- 🪙 **Coin** = Gold, 💣 **Bomb** = Red, 🫥 **Empty** = Gray
- ✨ **Bold Helvetica fonts** for a beautiful look
- 🏆 Live score, round counter, and level indicator
- 🖱️ **Hover effects** — buttons lighten when you hover
- 📦 **3D raised buttons** with colorful borders
- 🔄 **Retry option** — if you fail, try the level again
- 🏆 **Win screen** — complete all 10 levels to win!

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