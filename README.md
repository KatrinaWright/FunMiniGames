# FunMiniGames

A collection of simple mini-games implemented in Python.

## Games Included

- Clue Game: A simplified implementation of the classic board game Clue
- Simple MineSweeper: A text-based minesweeper game
- Nonograms: Logic puzzles with a graphical grid

## Running the Clue Game

To play the Clue game, run:

```bash
python cluegameA.py
```

## Testing the Clue Game

The Clue game has a suite of unit tests to ensure proper functionality. The tests verify:

1. That the game has properly started with cards dealt
2. That all cards are accounted for (including solution cards)
3. That cards given to a player are correctly held in that player's hand

To run the tests, use the following command from the repository root:

```bash
# Run all tests
pytest -v test_clue_game.py

# Run a specific test
pytest -v test_clue_game.py::TestClueGame::test_game_has_started

# Run with output shown
pytest -v test_clue_game.py -s
```

Make sure pytest is installed by running:

```bash
pip install pytest
```
