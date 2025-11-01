import pandas as pd
import numpy as np

def info_gain(feat, target):
    cross_tab = pd.crosstab(feat, target)
    print(cross_tab)
    print(cross_tab.sum(axis = 1))

def gini_index(feat, target):
    pass

class Classifer:
    def __init__(self,df, target, metric):
        self.y = df[target]
        self.X = df[[col for col in df.columns if col != target]]
        self.metric = info_gain if metric == "info_gain" else gini_index
    def get_root_node(self):
        metrics = []
        for feat in self.X.columns:
            metrics.append((self.metric(self.X[feat], self.y)))
        return max(metrics)
    
    
if __name__ == "__main__":
    df = pd.read_csv("assets/sample.csv")
    info_gain(df["legs"], df["human"])