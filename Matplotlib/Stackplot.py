from matplotlib import pyplot as plt

days = [1,2,3,4,5,6,7]

surya = [4,2,3,1,5,4,8]
alphine = [4,4,4,4,4,4,4]

labels = ["Surya","Alphine"]
plt.style.use("fivethirtyeight")
plt.stackplot(days,surya,alphine,labels=labels)
plt.tight_layout()
plt.legend()
plt.show()