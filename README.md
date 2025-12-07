Machine Learning Foundations: Linear Regression from Scratch
🎯 Overview
This project demonstrates a fundamental implementation of Simple Linear Regression built entirely from scratch using only Python and NumPy. The goal was to master the mathematical mechanics of machine learning—specifically Gradient Descent and Mean Squared Error (MSE)—without relying on high-level libraries like Scikit-Learn.

🧠 Core Concepts Implemented
Gradient Descent Optimizer: Custom logic to iteratively update model parameters (slope and intercept) based on the calculated error gradient.

Cost Function: Implementation of Mean Squared Error to evaluate model performance during training.

Vectorized Operations: Efficiently handled data arrays using NumPy for performance and readability.

Pythonic OOP: Encapsulated the model within a clean, reusable Class structure following industry standard design patterns.

🛠️ Tech Stack
Language: Python 3.x

Libraries: NumPy (for vectorization)

📈 Results
The model successfully converges on the target parameters for linear datasets.

Input Data: y = 2x + 1

Target: Slope: 2.0, Intercept: 1.0

Model Output: Slope: 1.99, Intercept: 1.01 (after 2000 iterations)
