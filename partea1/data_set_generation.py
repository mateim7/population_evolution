import pandas as pd
import numpy as np
import random

def data_set_generation():
    np.random.seed(0)
    random.seed(0)
    n = 1000
    base_population = np.random.randint(5000, 2000000, n)
    city_type = np.random.choice(['rural', 'oras-industrial', 'oras-modern'], n, p=[0.2, 0.3, 0.5])
    birth_rate = np.random.normal(12, 3, n)
    death_rate = np.random.normal(8, 2, n)
    migration_rate = np.random.normal(2, 4, n)
    health_index = np.random.uniform(0.5, 1.0, n)
    gdp_per_capita = np.random.lognormal(10, 0.5, n)
    education_index = np.random.uniform(0.7, 1.0, n)

    resulting_population = np.zeros(n)

    for i in range(n):
        growth_rate = (birth_rate[i] - death_rate[i] + migration_rate[i]) / 1000

        if city_type[i] == 'rural':
            growth_rate *= np.random.uniform(1.1, 1.2)
        elif city_type[i] == 'oras-industrial':
            growth_rate *= np.random.uniform(1.0, 1.1)
        elif city_type[i] == 'oras-modern':
            growth_rate *= np.random.uniform(1.5, 2.0)
        
        growth_rate += 0.001 * health_index[i]
        growth_rate += 0.002 * education_index[i]
        growth_rate += 0.001 * (gdp_per_capita[i] / 1000)

        resulting_population[i] = base_population[i] * (1 + growth_rate + np.random.normal(0, 0.1))
    
    df = pd.DataFrame({
        'base_population': base_population,
        'city_type': city_type,
        'birth_rate': birth_rate,
        'death_rate': death_rate,
        'migration_rate': migration_rate,
        'health_index': health_index,
        'gdp_per_capita': gdp_per_capita,
        'education_index': education_index,
        'resulting_population': resulting_population
    })
    print(df.dtypes)
    for col in df.columns:
        if col == 'resulting_population':
            continue
        x = random.randint(0, 100)
        for i in range (1, x + 1):
            j = random.randint(0, n - 1)
            df.loc[j, col] = np.nan
    print(df.describe())
    float_cols =  ['birth_rate', 'death_rate', 'migration_rate', 'health_index', 'gdp_per_capita', 'education_index', 'resulting_population']
    df[float_cols] = df[float_cols].round(2)
    int_cols = ['resulting_population']
    df[int_cols] = df[int_cols].fillna(0).astype(int)
    df.to_csv('tema/data_set.csv', index=False)
    return df

data_set_generation()
