from matplotlib import pyplot as plt 
import numpy as np
plt.style.use("fivethirtyeight")
print(plt.style.available)
ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35
          ]

x_indexes=np.arange(len(ages_x))
width=0.2
print(x_indexes)
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes-width,py_dev_y,width=width,label="Python",color="yellow")
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes,js_dev_y,width=width,label="Javascript",color="black")
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(x_indexes,dev_y,label="All",color="blue")
plt.legend()
plt.tight_layout()
plt.grid(color="red")
plt.xticks(labels=ages_x,ticks=x_indexes)
plt.show()