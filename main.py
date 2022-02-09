import pandas as pd

from utils.preparation_dataset import PreparationDataset

data = pd.read_csv("./data/raw_data.csv")


prep_dataset = PreparationDataset(data)

result = prep_dataset.start_preparation()
print(result)


