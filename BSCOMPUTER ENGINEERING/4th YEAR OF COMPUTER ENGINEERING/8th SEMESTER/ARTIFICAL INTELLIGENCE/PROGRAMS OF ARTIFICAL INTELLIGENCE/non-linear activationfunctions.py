import numpy as np
import matplotlib.pyplot as plt
# Activation Functions
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))
def tanh(x):
    return np.tanh(x)
def relu(x):
    return np.maximum(0, x)
def softmax(z):
    e = np.exp(z - np.max(z))  
    return e / np.sum(e)
x = np.linspace(-10, 10, 400)
z = np.array([2.0, 1.0, 0.1, -1.0, 3.0]) 
softmax_probs = softmax(z)
plt.figure(figsize=(12, 10))
plt.subplot(2, 2, 1)
plt.plot(x, sigmoid(x), color='orange')
plt.title("Sigmoid Activation Function")
plt.xlabel("Input (x)")
plt.ylabel("σ(x)")
plt.grid(True)
plt.axis('square')
# Tanh Plot
plt.subplot(2, 2, 2)
plt.plot(x, tanh(x), color='green')
plt.title("Tanh Activation Function")
plt.xlabel("Input (x)")
plt.ylabel("tanh(x)")
plt.grid(True)
plt.axis('square')
# ReLU Plot
plt.subplot(2, 2, 3)
plt.plot(x, relu(x), color='blue')
plt.title("ReLU Activation Function")
plt.xlabel("Input (x)")
plt.ylabel("ReLU(x)")
plt.grid(True)
plt.axis('square')
plt.subplot(2, 2, 4)
labels = [str(val) for val in z]
plt.bar(range(len(z)), softmax_probs, color='purple')
plt.xticks(range(len(z)), labels)
plt.title("Softmax Output Probabilities")
plt.xlabel("Input Value")
plt.ylabel("Probability")
plt.grid(True, axis='y')
plt.axis('square')
plt.tight_layout()
plt.show()
