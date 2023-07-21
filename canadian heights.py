import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("playercan.csv") #import the dataset 
country = data["PLACE_OF_BIRTH"] 
can = country.str.contains("CAN") #select players with Canadian nationalities

# not required for analysis, drop:
to_drop = ["PLAYER_ID", 
           "FIRST_NAME", 
           "LAST_NAME", 
           "SHOOTS", "CONTRACT_THRU", 
           "DRAFT_YEAR", 
           "DRAFT_ROUND", 
           "DRAFT_OVERALL"]
data.drop(to_drop, inplace=True, axis=1)

# filter out non-Canadians, modify dataset to include only Canadians
data = data[can == True]
print(data.head())

height = np.array(data["HEIGHT_CM"])

# dropping nan values
df2 = data.dropna()
height = np.array(df2["HEIGHT_CM"])


print("Mean of heights = ", height.mean())
print("Standard deviation of heights = ", height.std())
print("Minimum height = ", height.min())
print("Maximum height = ", height.max())
6
sns.set()
plt.hist(height, bins = 15, range = (160, 200))
plt.title("Height Distribution of Canadian Born Hockey Players")
plt.xlabel("height(cm)")
plt.ylabel("Number")
plt.show()

