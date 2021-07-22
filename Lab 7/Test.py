import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size = 1000)
plt.hist(x, density=True, bins=10)

plt.show()