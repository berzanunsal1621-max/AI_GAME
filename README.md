# AI Connect4: Rule-Based Heuristic Agent

A Connect Four game with a custom AI opponent built from scratch in Python. The AI uses a priority-based heuristic system instead of tree search (no Minimax) — it evaluates board state in real-time and picks moves based on a scoring matrix.

## How the AI Decides

The agent runs through a simple priority chain on every turn:

1. **Win check** — If dropping in any column gives 4-in-a-row, take it
2. **Block check** — If the opponent has a winning move next turn, block it
3. **Positional scoring** — When there's no immediate threat, score each column:
   - Center columns get extra weight (more connection paths)
   - Columns that extend existing 3-in-a-row structures score higher
   - Columns that disrupt opponent sequences also score well

No neural networks, no game trees — just a deterministic priority sequence that ends up being surprisingly hard to beat.

## Tech

- **Language:** Pure Python 3 (no external dependencies)
- **UI:** Python's built-in `turtle` module for the board rendering
- **Architecture:** Procedural game loop with state evaluation

## Running it

```bash
git clone https://github.com/berzanunsal1621-max/AI_GAME.git
cd AI_GAME
python connect4_3.py
```

- **You** play as Red, **AI** plays as Yellow
- Click on a column to drop your token
- Press `R` to reset the board

## Author

Berzan Unsal — Computer Engineering, Mugla Sitki Kocman University
