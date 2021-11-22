import pandas as pd
import seaborn as sns


def correlation_diagram(data):
    """converts a pandas dataframe into a correlation diagram"""
    corr = data.corr()
    sns.heatmap(corr,
                xticklabels=corr.columns,
                yticklabels=corr.columns,
                cmap="YlGnBu")


if __name__ == "__main__":
    # Le Wagon location
    data = sns.load_dataset("penguins")
    correlation_diagram(data)
