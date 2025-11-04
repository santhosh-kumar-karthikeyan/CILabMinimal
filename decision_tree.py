import pandas as pd
import numpy as np

def entropy(target):
    # calculate entropy: -sum(p * log2(p)) for each class
    probs = target.value_counts(normalize=True)  # get probability of each class
    return -sum(probs * np.log2(probs + 1e-9))  # add tiny value to avoid log(0)

def info_gain(feat, target):
    # parent entropy - weighted average of child entropies using crosstab
    parent_entropy = entropy(target)  # entropy before split
    ct = pd.crosstab(feat, target, normalize='index')  # crosstab with row-wise probabilities
    entropies = -(ct * np.log2(ct + 1e-9)).sum(axis=1)  # entropy for each feature value
    weights = feat.value_counts(normalize=True)  # weight by proportion of each value
    weighted_entropy = (entropies * weights).sum()  # weighted average
    return parent_entropy - weighted_entropy  # info gain = reduction in entropy

def gini_index(feat, target):
    # 1 - sum(p^2) using crosstab for vectorized computation
    ct = pd.crosstab(feat, target, normalize='index')  # row-wise probabilities
    gini_per_split = 1 - (ct ** 2).sum(axis=1)  # gini for each feature value
    weights = feat.value_counts(normalize=True)  # weight by proportion
    weighted_gini = (gini_per_split * weights).sum()  # weighted average
    # parent gini
    parent_probs = target.value_counts(normalize=True)
    parent_gini = 1 - sum(parent_probs ** 2)
    return parent_gini - weighted_gini  # gini gain

class DecisionTree:
    def __init__(self, df, target, metric="info_gain"):
        self.y = df[target]  # target column
        self.X = df[[col for col in df.columns if col != target]]  # feature columns
        self.metric = info_gain if metric == "info_gain" else gini_index  # choose metric
        self.tree = None  # will store the built tree
    
    def get_root_node(self, X, y):
        # find feature with best metric score
        best_feat, best_score = None, -1  # track best feature and its score
        for feat in X.columns:
            score = self.metric(X[feat], y)  # calculate metric for this feature
            if score > best_score:  # if better than current best
                best_score = score
                best_feat = feat
        return best_feat  # return feature name with highest info gain/gini gain
    
    def build_tree(self, X, y, depth=0, max_depth=5):
        # base case: if all same class or max depth reached, return leaf node
        if len(y.unique()) == 1 or depth >= max_depth or len(X.columns) == 0:
            return y.mode()[0]  # return most common class
        
        # recursive case: find best split and build subtrees
        root_feat = self.get_root_node(X, y)  # get best feature to split on
        tree = {root_feat: {}}  # create node with this feature
        
        for val in X[root_feat].unique():  # for each value of this feature
            # filter data where feature = val
            mask = X[root_feat] == val
            X_sub = X[mask].drop(columns=[root_feat])  # subset without this feature
            y_sub = y[mask]  # corresponding target values
            # recursively build subtree for this branch
            tree[root_feat][val] = self.build_tree(X_sub, y_sub, depth + 1, max_depth)
        
        return tree
    
    def fit(self, max_depth=5):
        # build the tree and store it
        self.tree = self.build_tree(self.X, self.y, max_depth=max_depth)
    
    def print_tree(self, tree=None, indent=""):
        # recursively print tree structure
        if tree is None:
            tree = self.tree  # start with root
        
        if isinstance(tree, dict):  # if it's a node (not leaf)
            for feat, branches in tree.items():
                print(f"{indent}{feat}:")  # print feature name
                for val, subtree in branches.items():
                    print(f"{indent}  {feat}={val}")  # print feature value
                    self.print_tree(subtree, indent + "    ")  # recurse on subtree
        else:  # leaf node
            print(f"{indent}-> {tree}")  # print predicted class

if __name__ == "__main__":
    df = pd.read_csv("assets/sample.csv")
    
    # build tree using info gain
    dt = DecisionTree(df, target="human", metric="info_gain")
    # to get root node
    print(dt.get_root_node(df[[col for col in df.columns if col != "human"]], df["human"]))
    # to build the tree
    dt.fit(max_depth=3)
    print("Decision Tree:")
    dt.print_tree()