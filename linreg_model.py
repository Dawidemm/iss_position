import numpy as np

class LinearRegression:

    def __init__(self, eta, iteratios):
        self.eta = eta
        self.iterations = iteratios

    def fit2(self, X, y):
        self.w_ = np.zeros(1+X.shape[1])
        self.cost_ = []

        for i in range(self.iterations):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)

        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return self.net_input(X)