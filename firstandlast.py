import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read dataset
lefile = pd.read_csv("./DATA HANDLING.csv",header=0)

#first five columns and last five columns(head vs iloc)
firstfive = lefile.head(5)
lastfive =  lefile.tail(5)

print(firstfive,lastfive)

