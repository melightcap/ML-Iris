# summarize the data
from pandas import read_csv
from loadData import loadData

# Load dataset
names, dataset = loadData()

# shape
print(dataset.shape)

# head
print(dataset.head(20))

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('class').size())