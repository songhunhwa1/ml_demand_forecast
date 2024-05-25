import pandas as pd

#!kaggle datasets download -d varsharam/walmart-sales-dataset-of-45stores
#!unzip walmart-sales-dataset-of-45stores.zip

walmart = pd.read_csv("walmart-sales-dataset-of-45stores.csv")