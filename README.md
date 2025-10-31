 Project Description

This project develops a Strategic Rule-Based AI opponent for the 6x7 Connect Four game board. The AI is designed to make more challenging and strategic moves by using a Heuristic Scoring System (center control, 3-in-a-row potential) in addition to basic win/block rules.

🛠️ Development Environment and Dependencies

The project was developed using only Python's standard libraries, requiring no external dependencies.

Development Language: Python 3.x

Graphical Interface: Turtle Library (Python Standard Library)

AI Method: Rule-Based Agent (Enhanced Heuristics)

Main File: connect4_final_pro.py

⚙️ Setup and Running Instructions

Running the project only requires Python 3.x to be installed.

1. Setup

Clone this GitHub repository to your local machine:

git clone [https://github.com/berzanunsal1621-max/AI_GAME.git](https://github.com/berzanunsal1621-max/AI_GAME.git)






Navigate to the cloned directory.

2. Running the Game

Open your command line (Terminal/CMD) and run the main project file:

python connect4_3.py





The game will start in a graphical Turtle window.

🎮 How to Play

Making a Move: After the window opens, click on the column where you want to drop your disk. (Red disks are yours.)

Turn Tracking: You can follow the current turn in the message area at the top of the board.

Restarting (Reset): To reset the board and start a new game at any time, press the R key on your keyboard.

🧠 Artificial Intelligence (AI) Logic Overview

The AI determines its moves based on the following priority sequence for every turn:

Priority 1: Winning Move: Immediately takes any move that results in an instant win.

Priority 2: Critical Block: Blocks the human player's immediate winning move (Defensive Strategy).

Priority 3: Heuristic Scoring: If no critical threat is present, it evaluates all possible moves and selects the one that provides the highest strategic score. Scoring encourages center control and building potential 3-in-a-row threats.
