import pandas as pd
from statistics import mode

def euclidean(x1, x2):
    return sum((x1[i] - x2[i]) ** 2 for i in range(len(x1))) ** 0.5

def manhattan(x1, x2):
    return sum(abs(x1[i] - x2[i]) for i in range(len(x1)))

class KNN:
    def __init__(self, k, distance, weighted):
        self.k = k
        self.distance = euclidean if distance == "euclidean" else manhattan
        self.weighted = weighted
    
    def predict(self, X, y, test):
        distances = [(self.distance(x, test), label) for x, label in zip(X, y)] # get distances of all data points from [6, 3, 5]
        neighbors = sorted(distances)[:self.k] # sort the distances and extract the top k neighbors
        if self.weighted:
            votes = {}
            for dist, label in neighbors:
                weight = 1 / (dist ** 2 + 1e-5) # weight = 1 / d ^ 2 adding 1e-5 to avoid zero division
                votes[label] = votes.get(label, 0) + weight # get to avoid key error
            return max(votes, key=votes.get) # key to override default key of comparison being the key of the dict `votes`
        else:
            labels = [label for _, label in neighbors] # get the labels of the neighbors and remove the distances
            return mode(labels) # return the mode, the most common label
        
if __name__ == "__main__":
    df = pd.read_csv('assets/knn_data.csv')
    X = df[["feature1", "feature2", "feature3"]].values
    y = df["label"]
    
    test = [6.0, 3.0, 5]
    
    knn1 = KNN(k=3, distance="euclidean", weighted=False)
    print(f"Euclidean (unweighted): {knn1.predict(X, y, test)}")
    
    knn2 = KNN(k=3, distance="manhattan", weighted=True)
    print(f"Manhattan (weighted): {knn2.predict(X, y, test)}")