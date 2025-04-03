#!/bin/bash

# Set up the test environment
echo "Setting up test environment..."

# Create necessary directory structure if needed
mkdir -p $(dirname "/tmp/outputs/test_clue_game.py")

# Copy files if not already in place
if [ ! -f "/tmp/outputs/FunMiniGames/cluegameA.py" ]; then
  mkdir -p "/tmp/outputs/FunMiniGames"
  cp /tmp/inputs/FunMiniGames/cluegameA.py /tmp/outputs/FunMiniGames/
fi

# Run the tests
echo "Running tests..."
cd /tmp/outputs
python -m pytest -v test_clue_game.py

echo "Test execution complete."
