import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

lefile = pd.read_csv("./DATA HANDLING.csv",header=0)

#multivariable scatterplot
sns.scatterplot(data=lefile, x="Fare", y="Survived")
plt.show()
