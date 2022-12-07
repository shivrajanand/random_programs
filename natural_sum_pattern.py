import matplotlib.pyplot as plt 
import numpy as np 

def graph(n):
    axis = []
    list = np.array([i for i in range(1, n)], dtype=np.float64)
    ylist = []
    x=0
    xlist = []

    for i in list:
        val = (i*(i+1)*(2*i+1))/6
        ylist.append(val)
        x+=1
        xlist.append(x)
        
    axis.append(xlist)
    axis.append(ylist)
    
    return axis
    



if __name__ == '__main__':
    figure, axis = plt.subplots(2, 2)
  
    #for n = 10
    l1 = graph(10)
    axis[0, 0].plot(l1[0], l1[1])
    axis[0, 0].set_title("n = 10")
  
    #for n = 10
    l2 = graph(100)
    axis[0, 1].plot(l2[0], l2[1])
    axis[0, 1].set_title("n = 100")
  
    #for n = 10
    l3 = graph(1000)
    axis[1, 0].plot(l3[0], l3[1])
    axis[1, 0].set_title("n = 1000")
  
    #for n = 10
    l4 = graph(1000000)
    axis[1, 1].plot(l4[0], l4[1])
    axis[1, 1].set_title("n = 1000000")
    
    
plt.show()