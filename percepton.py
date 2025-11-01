# Single Layer Perceptron
import pandas as pd
import numpy as np

def sign(x): return 1 if x >= 0 else -1
def sigmoid(x): return 1 / (1 + np.exp(-x))
def threshold(x, bipolar): return 1 if x >= 0 else (-1 if bipolar else 0)

class Perceptron:
    def __init__(self, activation, lr=0.1):
        self.activation = activation
        self.lr = lr
        self.weights = None
        self.bias = 0
    
    def fit(self, X, y, epochs=100):
        self.weights = np.zeros(X.shape[1])
        bipolar = -1 in y.values if isinstance(y, pd.Series) else -1 in y
        for _ in range(epochs):
            for i in range(len(X)):
                x = X.iloc[i] if isinstance(X, pd.DataFrame) else X[i]
                net = np.dot(x, self.weights) + self.bias
                pred = threshold(net, bipolar) if self.activation == 'threshold' else (sign(net) if self.activation == 'sign' else sigmoid(net))
                error = (y.iloc[i] if isinstance(y, pd.Series) else y[i]) - pred
                self.weights += self.lr * error * x
                self.bias += self.lr * error
    
    def predict(self, X):
        bipolar = hasattr(self, 'bipolar') and self.bipolar
        results = []
        for i in range(len(X)):
            x = X.iloc[i] if isinstance(X, pd.DataFrame) else X[i]
            net = np.dot(x, self.weights) + self.bias
            pred = threshold(net, bipolar) if self.activation == 'threshold' else (sign(net) if self.activation == 'sign' else sigmoid(net))
            results.append(pred)
        return results

if __name__ == "__main__":
    df = pd.DataFrame({'x1': [0, 0, 1, 1], 'x2': [0, 1, 0, 1], 'y': [0, 0, 0, 1]})
    X, y = df[['x1', 'x2']], df['y']
    
    p1 = Perceptron('threshold')
    p1.fit(X, y, epochs=10)
    print("Threshold:", p1.predict(X))
    
    p2 = Perceptron('sign')
    p2.fit(X, pd.Series([-1, -1, -1, 1]), epochs=10)
    print("Sign:", p2.predict(X))