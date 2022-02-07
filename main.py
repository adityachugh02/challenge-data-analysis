import pandas as pd

dataset = pd.read_csv("dataset-not-cleaned.csv")
print(dataset['surface_plot'].value_counts().sum())
print(dataset['surface_plot'].value_counts())

dataset['bedrooms'] = dataset['bedrooms'].fillna(2)
dataset['area'] = dataset['area'].fillna(dataset['area'].sum()/dataset['area'].value_counts().sum())
dataset['equipped_kitchen'] = dataset['equipped_kitchen'].fillna("Installed")
dataset['furnished'] = dataset['furnished'].fillna(0)
dataset['open_fire'] = dataset['open_fire'].fillna(0)
dataset['terrace'] = dataset['terrace'].fillna(0)
dataset['garden'] = dataset['garden'].fillna(0)
dataset['surface'] = dataset['surface'].fillna(dataset['surface'].sum()/dataset['surface'].value_counts().sum())
dataset['surface_plot'] = dataset['surface_plot'].fillna(dataset['surface'])
dataset['facades'] = dataset['facades'].fillna(2)
dataset['state'] = dataset['state'].fillna("Good")
dataset['swimming_pool'] = dataset['swimming_pool'].fillna(0)
print(dataset)

dataset.to_csv("dataset-cleaned.csv")