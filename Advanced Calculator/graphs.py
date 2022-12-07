import numpy as np
import matplotlib.pyplot as plt 

def trigo_graph():
    x = np.arange(-4*np.pi, 4*np.pi, 0.1)
    y = np.sin(x)
    
    plt.plot(x, y)
    plt.show()
    
    
trigo_graph()