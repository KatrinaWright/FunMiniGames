import numpy as np

class MetalPlate:
    def __init__(self, rows, cols, rivets):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)  
        self.rivets = self._get_rivet_positions()

        # ... (Mark rivet positions)

    def _get_rivet_positions(self):
        rivets = []
        num_rivets = int(input("Enter the number of rivets: "))

        for i in range(num_rivets):
            while True:
                rivet_str = input(f"Enter coordinates for rivet {i+1} (x,y): ")
                try:
                    x, y = map(int, rivet_str.split(','))
                    if 0 <= x < self.rows and 0 <= y < self.cols:
                        rivets.append((x, y))
                        break
                    else:
                        print("Coordinates must be within plate boundaries.")
                except ValueError:
                    print("Invalid input format. Please enter x,y")

        return rivets
        

    def simulate_wear(self):
        for _ in range(100):  # Simulate wear iterations
            # Randomly break a part
            x, y = np.random.randint(0, self.rows), np.random.randint(0, self.cols)
            if (x, y) in self.rivets:  # Damage at a rivet location
                print("rivet popped", x, " ", y)
                self.rivets.remove((x, y))  # Remove the rivet 
            self.grid[x, y] = 1

            # Check for and "drop" disconnected sections
            for x, y in np.ndindex(self.grid.shape):
                if self.grid[x, y] == 0 and not self._is_connected_to_rivet(x, y):
                    self._break_section(x, y)
                    print("broken section", x, " ", y)
                    self.visualize()
                    print(" ")

    def _is_connected_to_rivet(self, x, y):
        """Checks if a part is connected to a rivet (iteratively)"""
        visited = set()
        queue = [(x, y)]

        while queue:
            x, y = queue.pop(0)
            if (x, y) in self.rivets:
                return True

            if (x, y) not in visited:
                visited.add((x, y))
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.rows and 0 <= ny < self.cols and \
                       self.grid[nx, ny] == 0:
                        queue.append((nx, ny))
        print("hole created")
        self.visualize()
        print(" ")
        return False

    def _break_section(self, x, y):
        """Marks a section as broken and propagates to connected parts"""
        self.grid[x, y] = 1
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and \
               self.grid[nx, ny] == 0:
                self._break_section(nx, ny)

    def visualize(self):
        for row in self.grid:
            print(" ".join("o" if part == 0 else "x" for part in row))

# Example usage
plate = MetalPlate(10, 15, [(0, 0), (9, 0), (0, 14), (9, 14)])
plate.simulate_wear()
plate.visualize()


#print("\033[91m" + "o" + "\033[0m", end=" ")