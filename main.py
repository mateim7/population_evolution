from data_set_generation import data_set_generation
from missing_data import amissing_data
from missing_data import solve_missing_data
from data_split import data_split
from graph import histogram, countplot, scatterplot, boxplot, heatmap, violinplot, lineplot
from train_test import train_test
import pandas as pd

df = pd.read_csv('tema/filled_data_set.csv')

data_set_generation()
amissing_data()
solve_missing_data()
data_split()
histogram(df)
countplot(df)
scatterplot(df)
boxplot(df)
heatmap(df)
violinplot(df)
lineplot(df)
train_test()
