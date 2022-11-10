import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

lefile = pd.read_csv("./DATA HANDLING.csv",header=0)
#replace categorical values with numerical values("male"= 1,"female"=0)
numeric_var = {"Sex":{"male":1,"female":2}} 
rig= lefile.replace(numeric_var)

corr = rig.corr()
corr2 = lefile.corr()

#heatmap with NaN and categorical-numerical conversion
ax1 = sns.heatmap(corr, cbar=0, linewidths=2,vmax=1, vmin=0, square=True, cmap='Blues')
plt.show()

#heatmap without
ax2 = sns.heatmap(corr2, cbar=0, linewidths=2,vmax=1, vmin=0, square=True, cmap='Blues')
plt.show()
