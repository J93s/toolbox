from toolbox.data.ml import correlation_diagram
import pandas as pd


def test_correlation_diagram():
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    assert correlation_diagram(iris) != None
