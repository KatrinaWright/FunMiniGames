import numpy as np

# Define the size of the galaxy map
galaxy_size = 100

# Create a 3D array to represent the galaxy
galaxy = np.zeros((galaxy_size, galaxy_size, galaxy_size), dtype=int)

# Define the number of stars to generate
num_stars = 100

# Generate random coordinates for each star
star_coords = np.random.randint(0, galaxy_size, (num_stars, 3))

# Assign a value of 1 to each star's coordinates in the galaxy array
galaxy[star_coords[:, 0], star_coords[:, 1], star_coords[:, 2]] = 1

# Visualize the galaxy using matplotlib
import matplotlib.pyplot as plt

def dostuff(event):
    # Get the clicked point
    point = event['points'][0]

    # Get the index of the clicked star
    index = np.where((star_coords[:, 0] == point['x']) & (star_coords[:, 1] == point['y']) & (star_coords[:, 2] == point['z']))[0]

    # Update the color of the clicked star to green
    fig.data[0].marker.color[index] = 'green'

    # Update the plot
    fig.update()

plt.on_click(dostuff)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.voxels(galaxy, edgecolor='k', facecolor='b')
plt.show()