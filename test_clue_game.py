import pytest
import random
import sys
import os
from importlib import reload
import importlib.util

# Function to dynamically import the cluegameA module
def import_clue_game():
    # Save the current state of random.seed and random.choice
    original_random_seed = random.seed
    original_random_choice = random.choice
    
    # Define a predictable random choice function for testing
    def fixed_choice(seq):
        return seq[0]
    
    try:
        # Make random.choice deterministic for testing
        random.seed(42)
        random.choice = fixed_choice
        
        # Dynamically import the module
        spec = importlib.util.spec_from_file_location("cluegameA", os.path.join(os.path.dirname(__file__), "cluegameA.py"))
        clue_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(clue_module)
        
        return clue_module
    finally:
        # Restore the original random functions
        random.seed = original_random_seed
        random.choice = original_random_choice

class TestClueGame:
    
    def test_game_has_started(self):
        """
        Test 1: Verify that the game has started by checking if cards have been dealt.
        The game has started when:
        - Solution cards have been selected
        - Remaining cards have been distributed to players' hands
        """
        # Import the module
        clue_module = import_clue_game()
        
        # Check if solution cards have been selected
        assert hasattr(clue_module, 'solution_suspect')
        assert hasattr(clue_module, 'solution_weapon')
        assert hasattr(clue_module, 'solution_location')
        
        # Check that these solution cards exist in the predefined lists
        assert clue_module.solution_suspect in clue_module.all_suspects
        assert clue_module.solution_weapon in clue_module.all_weapons
        assert clue_module.solution_location in clue_module.all_locations
        
        # Check if cards have been dealt to players
        for player_name, player_data in clue_module.players.items():
            assert len(player_data["hand"]) > 0, f"Player {player_name} has no cards"
    
    def test_all_cards_accounted_for(self):
        """
        Test 2: Verify that all cards are accounted for, including solution cards.
        This means:
        - All cards should be either in the solution or in a player's hand
        - No card should appear twice
        """
        clue_module = import_clue_game()
        
        # Get all cards in play (those in players' hands plus solution cards)
        cards_in_play = [clue_module.solution_suspect, clue_module.solution_weapon, clue_module.solution_location]
        
        for player_data in clue_module.players.values():
            cards_in_play.extend(player_data["hand"])
        
        # Get all possible cards
        all_possible_cards = clue_module.all_suspects + clue_module.all_weapons + clue_module.all_locations
        
        # Check if all cards are accounted for
        assert len(cards_in_play) == len(all_possible_cards), "Not all cards are accounted for"
        
        # Check if every card is in play
        for card in all_possible_cards:
            assert card in cards_in_play, f"Card '{card}' is missing from play"
        
        # Check for duplicates
        assert len(cards_in_play) == len(set(cards_in_play)), "There are duplicate cards in play"
    
    def test_player_cards_in_hand(self):
        """
        Test 3: Verify that cards given to a player are correctly held in that player's hand.
        This means:
        - Cards in a player's hand should also be marked as "seen" by that player
        - Cards in a player's hand should actually be valid cards from the game
        """
        clue_module = import_clue_game()
        
        # For each player
        for player_name, player_data in clue_module.players.items():
            # Check if all cards in the player's hand are valid game cards
            for card in player_data["hand"]:
                assert (card in clue_module.all_suspects or 
                        card in clue_module.all_weapons or 
                        card in clue_module.all_locations), f"Invalid card '{card}' in {player_name}'s hand"
            
            # Check if all cards in the player's hand are also in their "seen" lists
            for card in player_data["hand"]:
                if card in clue_module.all_suspects:
                    assert card in player_data["seen"]["Suspects"], f"Card '{card}' in {player_name}'s hand but not in their seen Suspects"
                elif card in clue_module.all_weapons:
                    assert card in player_data["seen"]["Weapons"], f"Card '{card}' in {player_name}'s hand but not in their seen Weapons"
                elif card in clue_module.all_locations:
                    assert card in player_data["seen"]["Locations"], f"Card '{card}' in {player_name}'s hand but not in their seen Locations"
