import matplotlib.pyplot as plt
import numpy as np
from numpy import random
random_normal = np.random.normal(loc=0, scale=1, size=1000)


plt.scatter(range(1000), random_normal, alpha=0.6)
plt.xlabel("Numbers(1-1000)")
plt.ylabel("Random values")
plt.title("Scatter Graph from Normal Distribution")
plt.show()