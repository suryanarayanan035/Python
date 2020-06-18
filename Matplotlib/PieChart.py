import pandas as pd 
from matplotlib import pyplot as plt 
from collections import Counter 

plt.xkcd()

data = pd.read_csv("~/Python/Python/Matplotlib/languagepopularity.csv")
data = data["LanguagesWorkedWith"]
counter = Counter()

for row in data:
    counter.update(row.split(";"))
most_common = counter.most_common(5)
languages = []
no_of_developers = []
for i in most_common:
    languages.append(i[0])
    no_of_developers.append(i[1])
plt.pie(no_of_developers,labels=languages,autopct="%1.1f%%")
plt.title("Dominanace of Programming Languages")
plt.show()