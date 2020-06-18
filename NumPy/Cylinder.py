import numpy as np


no_of_items = 10
upper_limit=25
lower_limit=5

#values = np.random.seed(0)
values = np.random.randint(lower_limit,upper_limit,no_of_items)

print("Generated Values",values)
container = np.reshape(values,(5,2))

print("container:",container)

height = container[:,0]
radius = container[:,1]

volume = np.pi * (radius**2)*height

print("The total volume is:",volume.sum())
print("Individual voulmes are:",volume)
print("Minimum volume is:",volume.min())
print("Maximum  volume is:",volume.max())