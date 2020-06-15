# import modules
import matplotlib.pyplot as plt

# data setting
x = list(range(1, 9))
data1 = [i ** 2 for i in x]
data2 = [1, 2, 3, 6, 9, 15, 24, 39]

# graph setting
plt.figure(facecolor='lightgreen')
plt.plot(x, data1, 'b.--', x, data2, 'r.--', linewidth=1)
plt.title('Figure', fontsize=24)
plt.xlabel('x-Value', fontsize=16)
plt.ylabel('y-Value', fontsize=16)
plt.axis([0, 8, 0, 70])

# show the graph
plt.show()

