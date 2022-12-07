import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []
for i in range(0, len(x)):
    y.append(x[i]**2)

plt.plot(x, y)

plt.show()
