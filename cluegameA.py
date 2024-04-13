import random

suspects = ["Colonel Mustard", "Miss Scarlet", "Professor Plum", 
            "Mrs. Peacock", "Mr. Green", "Mrs. White"]
weapons = ["Knife", "Candlestick", "Revolver", "Rope", "Lead Pipe", "Wrench"]
locations = ["Kitchen", "Ballroom", "Conservatory", "Billiard Room", 
             "Library", "Study"]
all_suspects = suspects.copy()
all_weapons = weapons.copy()
all_locations = locations.copy()

# Choose the solution 
solution_suspect = random.choice(suspects)
solution_weapon = random.choice(weapons)
solution_location = random.choice(locations)

suspects.remove(solution_suspect)
weapons.remove(solution_weapon)
locations.remove(solution_location)

# Data structures for tracking clues
players = {
    "Nathan": {"seen":{"Suspects": [], "Weapons": [], "Locations": []}, "hand": []},
    "Esther": {"seen":{"Suspects": [], "Weapons": [], "Locations": []}, "hand": []},
    "Samantha": {"seen":{"Suspects": [], "Weapons": [], "Locations": []}, "hand": []},
    "Westley": {"seen":{"Suspects": [], "Weapons": [], "Locations": []}, "hand": []}
}

# Distribute remaining cards
def deal_cards():
    remaining_cards = suspects + weapons + locations
    random.shuffle(remaining_cards)

    num_players = len(players)
    cards_per_player = len(remaining_cards) // num_players

    current_player = 0
    for card in remaining_cards:
        player_name = list(players.keys())[current_player]
        players[player_name]["hand"].append(card)  # Add card to player's hand
        #Automatically add to the seen clues as well
        for category in players[player_name]["seen"]: 
            if card in all_suspects and category == "Suspects":
                players[player_name]["seen"][category].append(card)
            elif card in all_weapons and category == "Weapons":
                players[player_name]["seen"][category].append(card)
            elif card in all_locations and category == "Locations":
                players[player_name]["seen"][category].append(card)
        current_player = (current_player + 1) % num_players

# Functions for Gameplay
def print_clue_board(player):
    print("*** ", player, "'s Clue Board ***")
    print("Suspects:")
    for suspect in all_suspects:
        if suspect in players[player]["seen"]["Suspects"]:
            print("\tX", suspect)  # Mark if ruled out
        else:
            print("\t ", suspect)
    print("Weapons:")
    for weapon in all_weapons:
        if weapon in players[player]["seen"]["Weapons"]:
            print("\tX", weapon)  # Mark if ruled out
        else:
            print("\t ", weapon)
    print("Locations:")
    for location in all_locations:
        if location in players[player]["seen"]["Locations"]:
            print("\tX", location)  # Mark if ruled out
        else:
            print("\t ", location)


def make_accusation(accuser, accused, suspect, location, weapon):
    print(f"{accuser} makes an accusation: It was {suspect} in the {location} with the {weapon}! {accused}, can you prove me wrong?")
    for item in [suspect, location, weapon]:
        if item in players[accused]["hand"]:
            print(f"{accused}: I can prove you wrong! It wasn't {item}!")
            if item in all_suspects:
                category = "Suspects"
            elif item in all_weapons:
                category = "Weapons"
            else:
                category = "Locations" 
            
            #Reveal only one item
            players[accuser]["seen"][category].append(item)
            print(f"{accuser} received a clue from {accused}: {item} ({category})")
            return
    print(f"{accused}: I cannot prove you wrong...")

# ------ Additional Rounds with Gameplay  -------
def get_random_clue(giver, receiver):
    # Ensure the clue given is in the giver's hand, and not in the receiver's seen clues 
    while True: 
        potential_clues = [clue for clue in players[giver]["hand"]]
        if potential_clues: 
            clue = random.choice(potential_clues)
            if clue in all_suspects:
                category = "Suspects"
            elif clue in all_weapons:
                category = "Weapons"
            else:
                category = "Locations" 
            break 
    return category, clue

# ------ Example Game ------
deal_cards()

print("----- Round 0: Initial Boards -----")
for player in players:
    print_clue_board(player)

turn_counter = 0
for round in range(1, 9): #Simulating 9 additional rounds 
    print(f"\n----- Round {round}: -----")
    for player_name in players:
        print(f"-- {player_name}'s Turn --")
        other_players = list(players.keys())
        other_players.remove(player_name)
        clue_giver = random.choice(other_players)
        make_accusation(player_name, clue_giver, random.choice(all_suspects), random.choice(all_locations), random.choice(all_weapons))
        # clue_category, clue = get_random_clue(clue_giver, player_name)
        
        print_clue_board(player_name)
    turn_counter +=1 