import numpy as np


class SimpleLinearRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.slope = 0
        self.intercept = 0

    def fit(self, x, y):
        n = len(x)

        # Gradient Descent loop
        for _ in range(self.iterations):
            # 1. Make a prediction
            y_pred = self.slope * x + self.intercept

            # 2. Calculate gradients (derivatives)
            d_slope = (-2 / n) * np.sum(x * (y - y_pred))
            d_intercept = (-2 / n) * np.sum(y - y_pred)

            # 3. Update slope and intercept
            self.slope -= self.lr * d_slope
            self.intercept -= self.lr * d_intercept

    def predict(self, x):
        return self.slope * x + self.intercept


# Demo usage with simple data
if __name__ == "__main__":
    # Sample data: y = 2x + 1
    X = np.array([1, 2, 3, 4, 5])
    Y = np.array([3, 5, 7, 9, 11])

    model = SimpleLinearRegression(learning_rate=0.01, iterations=2000)
    model.fit(X, Y)

    print(f"Predicted slope: {model.slope:.2f} (Target: 2.00)")
    print(f"Predicted intercept: {model.intercept:.2f} (Target: 1.00)")
