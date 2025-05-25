import numpy as np
import pandas as pd
import random
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv('tema/data_set.csv')

def amissing_data(df):
    for col in df.columns:
        if col == 'resulting_population':
            continue
        a = df[col].isna().sum()
        b = a
        a = a / len(df[col]) * 100
        print(f"Coloana {col} are {b} valori lipsa ({a:.2f}%) date lipsa")

def solve_missing_data():
    df = pd.read_csv('tema/data_set.csv')
    new_df = df.copy()
    mask = new_df['base_population'].isna()
    new_df.loc[mask, 'base_population'] = new_df.loc[mask, 'resulting_population'] * 0.9
    new_df['birth_rate'] = new_df['birth_rate'].fillna(new_df['birth_rate'].mean())
    new_df['death_rate'] = new_df['death_rate'].fillna(new_df['death_rate'].mean())
    new_df['migration_rate'] = new_df['migration_rate'].fillna(new_df['migration_rate'].mean())
    new_df['health_index'] = new_df['health_index'].fillna(new_df['health_index'].mean())
    new_df['gdp_per_capita'] = new_df['gdp_per_capita'].fillna(new_df['gdp_per_capita'].mean())
    new_df['education_index'] = new_df['education_index'].fillna(new_df['education_index'].mean())
    new_df['city_type'] = new_df['city_type'].fillna(new_df['city_type'].mode()[0])
    city_type_mapping = {'rural': 0, 'oras-industrial': 1, 'oras-modern': 2}
    new_df['city_type'] = new_df['city_type'].map(city_type_mapping)
    

    return new_df

amissing_data(df)
new_df = solve_missing_data()
new_df.to_csv('tema/filled_data_set.csv', index=False)

print(new_df.describe().round(2))