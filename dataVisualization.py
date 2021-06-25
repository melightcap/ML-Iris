# visualize the data
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from loadData import loadData

# Load dataset
names, dataset = loadData()

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

# histograms
dataset.hist()
pyplot.show()

# scatter plot matrix
scatter_matrix(dataset)
pyplot.show()