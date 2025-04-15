import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0.1, 100, 100)
y = np.log10(x)

# Plot
plt.plot(x, y, 'b')
plt.xlabel('x')
plt.ylabel('log(x)')
plt.title('Logarithmic Function')
plt.grid(True)
plt.show()