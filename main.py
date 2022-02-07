import pandas as pd

data = pd.read_csv("./data/raw_data.csv")

data = data.drop_duplicates()

