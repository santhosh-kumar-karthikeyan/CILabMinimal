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

class MultiLayerPerceptron:
    def __init__(self, layer_sizes, activation='sigmoid', theta=0.5, t1=-0.5, t2=0.5, lr=0.1):
        """
        layer_sizes: list of integers like [input, h1, h2, ..., output]
        """
        self.layer_sizes = layer_sizes
        self.activation = activation
        self.theta = theta
        self.t1 = t1
        self.t2 = t2
        self.lr = lr
        self.bipolar = False

        # Initialize weights and biases
        self.weights = [np.zeros((layer_sizes[i], layer_sizes[i+1])) for i in range(len(layer_sizes)-1)]
        self.biases = [np.zeros(layer_sizes[i+1]) for i in range(len(layer_sizes)-1)]

    def _activate(self, y_in):
        if self.activation == 'threshold':
            return np.vectorize(lambda y: threshold(y, self.theta, self.bipolar))(y_in)
        elif self.activation == 'step':
            return np.vectorize(lambda y: step(y, self.t1, self.t2, self.bipolar))(y_in)
        else:
            return np.vectorize(lambda y: sigmoid(y, self.theta, self.bipolar))(y_in)

    def forward(self, x):
        activations = [x]
        for W, b in zip(self.weights, self.biases):
            x = self._activate(np.dot(x, W) + b)
            activations.append(x)
        return activations

    def fit(self, X, y, epochs=10):
        self.bipolar = -1 in y.values
        for _ in range(epochs):
            for i in range(len(X)):
                x = X.iloc[i].values
                t = y.iloc[i]

                # Forward pass
                activations = self.forward(x)
                
                # Update all layers independently (no backprop)
                for l in range(len(self.weights)):
                    inp = activations[l]
                    out = activations[l+1]
                    self.weights[l] += self.lr * t * np.outer(inp, out)
                    self.biases[l] += self.lr * t * out

    def predict(self, X):
        preds = []
        for i in range(len(X)):
            x = X.iloc[i].values
            output = self.forward(x)[-1]
            preds.append(output)
        return np.round(np.array(preds)).astype(int)

if __name__ == "__main__":
    # XOR dataset
    df = pd.DataFrame({
        'x1': [0, 0, 1, 1],
        'x2': [0, 1, 0, 1],
        'y':  [0, 1, 1, 0]
    })
    
    X, y = df[['x1', 'x2']], df['y']

    # Example: 2 inputs → 3 hidden → 2 hidden → 1 output
    layer_config = [2, 3, 2, 1]

    mlp = MultiLayerPerceptron(layer_config, activation='sigmoid', theta=0.5, lr=0.2)
    mlp.fit(X, y, epochs=20)
    
    preds = mlp.predict(X)
    print("\nPredictions:")
    print(pd.DataFrame({'x1': X['x1'], 'x2': X['x2'], 'Predicted': preds.flatten(), 'Actual': y}))
