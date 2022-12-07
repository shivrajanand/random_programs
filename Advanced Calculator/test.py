# import matplotlib.pyplot as plt

# def sum(num):
#     xlist = [i for i in range(1, num+1)]
#     ylist =[]
#     # print(xlist)
#     for i in xlist:
#         val = (i*(i+1))/2
#         print(f"{i} <-------> {val}")
#         ylist.append(val)
    
#     plt.plot(xlist,ylist)
#     plt.show()
    
    
# sum(10000000000000000000)

from sympy import *
import math

x = Symbol('x') 
y = (x*(x+1))/2
lim = limit(y, x, oo)

print(lim)