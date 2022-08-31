import pandas as pd
import matplotlib.pyplot as plt
import random
data = pd.read_csv("QueryResults.csv", names=["Date", "Tag", "Posts"], header=0).dropna()
data.Date = pd.to_datetime(data.Date)
new_data = data.pivot(index="Date", columns="Tag", values="Posts")
new_data.fillna(0, inplace=True)
new_data = new_data.rolling(window=12).mean()
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("Date", fontsize=14)
plt.ylabel("number of posts", fontsize=14)
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
for column in new_data.columns:
    red = "".join(random.choices(values, k=2))
    green = "".join(random.choices(values, k=2))
    blue = "".join(random.choices(values, k=2))
    color = "#" + red + green + blue
    plt.plot(new_data.index, new_data[column], label=column, color=color)


plt.legend(fontsize=11)
plt.show()