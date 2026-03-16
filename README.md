# AI Connect4: Rule-Based Heuristic Agent

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Turtle](https://img.shields.io/badge/UI-Turtle_Graphics-green?style=for-the-badge)

A strategic Connect Four game featuring a custom-built, rule-based Artificial Intelligence opponent. Developed from scratch in Python without relying on external machine learning or game engine libraries.

This project was developed for the **CENG 3550: Artificial Intelligence** Midterm Project. The primary objective is to demonstrate how a deterministic, heuristic-driven evaluation model can effectively simulate intelligent gameplay and consistently challenge human players.

---

## 🧠 Intelligence Architecture

Rather than utilizing tree-search algorithms (like Minimax) or trained neural networks, this AI operates on a real-time **Heuristic Priority Sequence**. It analyzes the board state on every turn and executes the highest-priority tactical maneuver:

1.  **Immediate Victory Identification:**
    *   Scans all available columns. If a drop results in an immediate 4-in-a-row, the AI executes the winning move.
2.  **Critical Threat Mitigation (Blocking):**
    *   Simulates the opponent's next turn. If the opponent has a winning move available, the AI immediately blocks that specific column.
3.  **Strategic Positional Scoring:**
    *   When no immediate win or loss is detected, the AI relies on a heuristic scoring matrix:
        *   **Center Control:** Strong bias towards central columns, as they statistically offer the highest number of connective pathways.
        *   **Offensive Sequencing:** Prioritizes building its own potential 3-in-a-row structures.
        *   **Defensive Sequencing:** Actively disrupts the opponent's attempts to build combinations.

---

## 🛠️ Technical Implementation

*   **Language:** Pure Python 3
*   **Graphics Rendering:** Python Standard Library `turtle` module. Chosen specifically to demonstrate core algorithmic logic without the overhead of heavy external dependencies like Pygame.
*   **Architecture:** Procedural game loop with state evaluation matrix.

---

## 🚀 Quick Start

Because the project relies purely on standard Python libraries, no dependency installation (`requirements.txt` or `pip install`) is necessary.

### 1. Clone the repository
```bash
git clone https://github.com/berzanunsal1621-max/AI_GAME.git
cd AI_GAME
```

### 2. Launch the game
```bash
python connect4_3.py
```

### 🎮 How to Play
*   A Turtle graphics window will initialize the game board.
*   **Human Player:** Red Tokens
*   **AI Opponent:** Yellow Tokens
*   **Controls:** Simply use your mouse to click on the column where you want to drop your token.
*   **Reset:** Press the `R` key on your keyboard at any time to instantly reset the board for a new game.

---

## 👨‍💻 Author

**Berzan Ünsal**
Computer Engineering
Muğla Sıtkı Koçman University
