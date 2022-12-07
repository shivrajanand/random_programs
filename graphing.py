import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([x for x in range(1, 10001)])

y = [(1)/t for t in x]

plt.plot(x, y)

plt.show()
