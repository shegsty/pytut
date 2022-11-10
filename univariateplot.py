import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read dataset
lefile = pd.read_csv("./DATA HANDLING.csv",header=0)
#num_cols = lefile.select_dtypes(exclude='object')
num_cols1 = lefile.select_dtypes(exclude='object').columns



#perform a univariate analysis using bar chart to show the distribution of passengers across sex ,passenger class and embarked(Pvsex,pvembarked,pvclass).
cols = 3
rows = 3

fig = plt.figure( figsize=(cols*5, rows*5))
for i, col in enumerate(num_cols1):
    
    ax=fig.add_subplot(rows,cols,i+1)
    
    sns.countplot(x = lefile[col], ax = ax)
    
fig.tight_layout()  
plt.show()



