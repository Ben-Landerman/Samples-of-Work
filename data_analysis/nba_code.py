import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("2019_nba.csv")

#calculate and round attributes: 3 point attempt percentage, 2 point attempt percentage, and win/lose percentage
df['3PA%'] = df['3PA']/df['FGA']
df['3PA%'] = df['3PA%'].apply(lambda x: round(x, 3))
df['2PA%'] = df['2PA']/df['FGA']
df['2PA%'] = df['2PA%'].apply(lambda x: round(x, 3))
df['W/L%'] = df['W']/df['G']
df['W/L%'] = df['W/L%'].apply(lambda x: round(x, 3))

#drop unwanted attributes
df.drop(['Rk', 'Team', 'G', 'MP', 'W', 'L'], axis=1, inplace=True)

X = df.iloc[:,0:23]  #independent columns
y = df.iloc[:,-1]    #target column: W/L%

#print correlations of each attribute
corrmat = df.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(23,23))
#plot heat map
g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")