import random

grid_size = 20
building_types = {
    "residential": {"size": (1, 1), "max_blocks": 4},  # Can occupy 1-4 blocks
    "commercial": {"size": (1, 1), "max_blocks": 2},
    "industrial": {"size": (2, 2), "max_blocks": 1},
    "park": {"size": (2, 3), "max_blocks": 1},
    "fast food restaurant": {"size": (1, 1), "max_blocks": 1},
    "gas station": {"size": (1, 1), "max_blocks": 1},
    "office": {"size": (2, 1), "max_blocks": 2},
    "shopping mall": {"size": (3, 3), "max_blocks": 1}
}

def generate_city_grid():

    grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]  # 2D array

    for row_i in range(grid_size):
        row = []
        for col_i in range(grid_size):
            block_type, block_size = choose_building_type(row_i, col_i)

            # Mark occupied blocks in the grid
            for i in range(block_size[0]):
                for j in range(block_size[1]):
                    if row_i + i < grid_size and col_i + j < grid_size:
                        row.append({
                            "type": block_type,
                            "occupied_by": (row_i, col_i)  # Reference to origin block
                        })
                    else:  # Block extends beyond grid boundaries
                        row.append(None)
        grid.append(row)
    return grid

def choose_building_type(row_i, col_i):
   # Zoning rules (simplified example)
   if row_i < grid_size // 3:
       zone = "residential"
   elif row_i < 2 * grid_size // 3:
       zone = "mixed"
   else:
       zone = "industrial"

   # Distribution rules based on zone and some randomness
   available_types = [
       t for t in building_types if t.startswith(zone) or random.random() < 0.2
   ]
    # Placeholder logic - replace with your zoning/distribution rules
    #available_types = list(building_types.keys())
    #while available_types:
    #    block_type = random.choice(available_types)
    #    block_size = building_types[block_type]["size"]
    #    if check_space_available(row_i, col_i, block_size):
    #        return block_type, block_size
    #    else:
    #        available_types.remove(block_type)
    #return None, (0, 0)  # No suitable building found

def check_space_available(row_i, col_i, block_size):
   for i in range(block_size[0]):
       for j in range(block_size[1]):
           if not (0 <= row_i + i < grid_size and 0 <= col_i + j < grid_size):
               return False
           if grid[row_i + i][col_i + j] is not None:
               return False
   return True

city_grid = generate_city_grid()
print(city_grid)

