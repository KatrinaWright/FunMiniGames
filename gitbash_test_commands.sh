#!/bin/bash

# These are the commands you would run in a GitBash terminal to test the Clue game

# Navigate to your project directory
# cd path/to/FunMiniGames

# Make sure pytest is installed
pip install pytest

# Run all tests for the clue game
pytest -v test_clue_game.py

# Run a specific test if needed
# pytest -v test_clue_game.py::TestClueGame::test_all_cards_accounted_for

# Run with output showing
# pytest -v -s test_clue_game.py

# Display test coverage (requires pytest-cov package)
# pip install pytest-cov
# pytest --cov=cluegameA test_clue_game.py --cov-report term-missing
