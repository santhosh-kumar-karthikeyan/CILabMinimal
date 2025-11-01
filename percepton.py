# Single Layer Perceptron
import pandas as pd
import numpy as np

def threshold(y_in, theta, bipolar):
    return 1 if y_in > theta else (-1 if bipolar else 0)

def step(y_in, t1, t2, bipolar):
    if y_in < t1:
        return -1 if bipolar else 0
    elif t1 <= y_in <= t2:
        return 0 if bipolar else 0.5
    else:
        return 1

def sigmoid(y_in, theta, bipolar):
    sig_val = 1 / (1 + np.exp(-y_in))
    return 1 if sig_val > theta else (-1 if bipolar else 0)

class Perceptron:
    def __init__(self, activation, theta=0.0, t1=None, t2=None, lr=0.1):
        self.activation = activation
        self.theta = theta
        self.t1 = t1
        self.t2 = t2
        self.lr = lr
        self.weights = None
        self.bias = 0
        self.bipolar = False
    
    def _activate(self, y_in):
        if self.activation == 'threshold':
            return threshold(y_in, self.theta, self.bipolar)
        elif self.activation == 'step':
            return step(y_in, self.t1, self.t2, self.bipolar)
        else:  # sigmoid
            return sigmoid(y_in, self.theta, self.bipolar)
    
    def fit(self, X, y, epochs=100):
        self.weights = np.zeros(X.shape[1])
        self.bipolar = -1 in (y.values if isinstance(y, pd.Series) else y)
        
        for _ in range(epochs):
            for i in range(len(X)):
                x = X.iloc[i] if isinstance(X, pd.DataFrame) else X[i]
                net = np.dot(x, self.weights) + self.bias
                pred = self._activate(net)
                error = (y.iloc[i] if isinstance(y, pd.Series) else y[i]) - pred
                self.weights += self.lr * error * x
                self.bias += self.lr * error
    
    def predict(self, X):
        results = []
        for i in range(len(X)):
            x = X.iloc[i] if isinstance(X, pd.DataFrame) else X[i]
            net = np.dot(x, self.weights) + self.bias
            results.append(self._activate(net))
        return results

if __name__ == "__main__":
    df = pd.DataFrame({'x1': [0, 0, 1, 1], 'x2': [0, 1, 0, 1], 'y': [0, 0, 0, 1]})
    X, y = df[['x1', 'x2']], df['y']
    
    p1 = Perceptron('threshold', theta=0)
    p1.fit(X, y, epochs=10)
    print("Binary Threshold:", p1.predict(X))
    
    p2 = Perceptron('sigmoid', theta=0.5)
    p2.fit(X, pd.Series([-1, -1, -1, 1]), epochs=10)
    print("Bipolar Sigmoid:", p2.predict(X))
    
    p3 = Perceptron('step', t1=-0.5, t2=0.5)
    p3.fit(X, pd.Series([-1, -1, -1, 1]), epochs=10)
    print("Bipolar Step:", p3.predict(X))