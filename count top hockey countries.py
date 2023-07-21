import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

counts = {}


data = pd.read_csv("main.csv") #import the dataset 
data = data.dropna(subset= ["PLACE_OF_BIRTH"])

country = data["PLACE_OF_BIRTH"] 



for i in country:
    if i[-3:] in counts:
        counts[i[-3:]] += 1
    else:
        counts[i[-3:]] = 0


freq = sorted(counts.items(), key = lambda x:x[1], reverse = True)
print(freq)
