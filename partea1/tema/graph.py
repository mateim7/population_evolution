import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('tema/filled_data_set.csv')

def histogram(df):
    plt.figure(figsize=(12, 8))
    for i, col in enumerate(df.columns):
        if col == 'resulting_population':
            continue
        plt.subplot(3, 3, i + 1)
        sns.histplot(df[col], kde=True, bins=30, color='red', edgecolor='black')
        plt.title(f'Histograma {col}')
        plt.xlabel(col)
        plt.ylabel('N')
    plt.tight_layout()
    plt.show()

def countplot(df):
    plt.figure(figsize=(12, 8))
    sns.countplot(data=df, x='city_type', palette='pastel', legend=False, hue='city_type')
    plt.title('Count of City Types')
    plt.xlabel('City Type')
    plt.ylabel('N')
    plt.show()

def scatterplot(df):
    plt.figure(figsize=(12, 8))
    for i, col in enumerate(df.columns):
        if col == 'resulting_population':
            continue
        plt.subplot(3, 3, i + 1)
        sns.scatterplot(data=df, x=col, y='resulting_population', color='blue')
        plt.title(f'{col} vs resulting population')
        plt.xlabel(col)
        plt.ylabel('resulting population')
    plt.tight_layout()
    plt.show()

def boxplot(df):
    plt.figure(figsize=(12, 8))
    for i, col in enumerate(df.columns):
        if col == 'resulting_population':
            continue
        plt.subplot(3, 3, i + 1)
        sns.boxplot(x=df[col], color='lightblue')
        plt.title(f'Boxplot {col}')
        plt.xlabel(col)
        plt.ylabel('N')
    plt.tight_layout()
    plt.show()

def heatmap(df):
    plt.figure(figsize=(12, 8))
    df_numeric = df.drop(columns=['city_type'], errors='ignore')
    corr = df_numeric.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Heatmap')
    plt.show()

def violinplot(df):
    plt.figure(figsize=(12, 8))
    sns.violinplot(data=df, x='city_type', y='resulting_population', palette='muted', legend=False, hue='city_type')
    plt.title('Violin Plot')
    plt.xlabel('City Type')
    plt.ylabel('Resulting Population')
    plt.show()

def lineplot(df):
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=df, x='base_population', y='resulting_population', hue='city_type', marker='o')
    plt.title('Base vs Resulting Population')
    plt.xlabel('Base Population')
    plt.ylabel('Resulting Population')
    plt.legend(title='City Type')
    plt.show()

histogram(df)
countplot(df)
scatterplot(df)
boxplot(df)
heatmap(df)
violinplot(df)
lineplot(df)
