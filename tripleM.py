import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read dataset
lefile = pd.read_csv("./DATA HANDLING.csv",header=0)
num_cols = lefile.select_dtypes(exclude='object')
#num_cols1 = lefile.select_dtypes(exclude='object').columns

mean = num_cols.mean()
mode = num_cols.mode()
median = num_cols.median()
print(mean,mode,median)
