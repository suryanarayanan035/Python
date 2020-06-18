from matplotlib import pyplot as plt 
import csv
from collections import Counter
import pandas as pd
plt.style.use("Solarize_Light2")

data = pd.read_csv("languagepopularity.csv")
language = data['LanguagesWorkedWith']
language_counter = Counter()
for row in language:
    language_counter.update(row.split(";"))

items = language_counter.most_common(15)
    
language = []
popularity = []
for item in items:
    language.append(item[0])
    popularity.append(item[1])
    
language.reverse()
popularity.reverse()
plt.barh(language,popularity,color="red")
plt.grid(color="black")
plt.tight_layout()
plt.title("Languages Popularity")
plt.xlabel("No of Developers")
plt.show()