# Clue Game Tests

This directory contains pytest files for testing the Clue game implementation.

## Running Tests

To run the tests, use the following command from the root directory of the project:

```bash
pytest test_clue_game.py -v
```

### Git Bash Command Example

```bash
./pytest test_clue_game.py -v
```

or

```bash
python -m pytest test_clue_game.py -v
```

## Test Descriptions

1. `test_game_has_started`: Verifies that the game has started correctly with solutions selected.
2. `test_all_cards_accounted_for`: Verifies that all cards are accounted for (including the solutions).
3. `test_player_cards_distribution`: Verifies that cards are correctly dealt to players and each player has the appropriate cards in their hand.

## Prerequisites

- Python 3.6+
- pytest package installed: `pip install pytest`
