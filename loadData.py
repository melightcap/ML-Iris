# Load libraries
from pandas import read_csv

def loadData():
    # Load dataset
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    # in case of network connection issues
    # url = "./iris.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = read_csv(url, names = names)

    return (names, dataset)

names, dataset = loadData()

