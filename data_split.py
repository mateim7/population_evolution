import numpy as np
import pandas as pd
import random
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def data_split():
    df = pd.read_csv('tema/filled_data_set.csv')
    X = df.drop(columns=['resulting_population'])
    y = df['resulting_population']

    X_train , X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    X_train.to_csv('tema/X_train.csv', index=False)
    X_test.to_csv('tema/X_test.csv', index=False)
    y_train.to_csv('tema/y_train.csv', index=False)
    y_test.to_csv('tema/y_test.csv', index=False)

data_split()