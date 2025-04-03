#!/bin/bash
# Script to run clue game tests

echo "Running Clue Game Tests..."
python -m pytest test_clue_game.py -v

echo "Tests completed."
