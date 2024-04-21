import numpy as np

def sigmoid(x):
  """Sigmoid activation function"""
  return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
  """Derivative of the sigmoid function"""
  return x * (1 - x)

class NeuralNetwork:
  def __init__(self, input_size, hidden_size, output_size):
    """
    Initialize the neural network with random weights and biases.

    Args:
      input_size: Number of input features.
      hidden_size: Number of neurons in the hidden layer.
      output_size: Number of output neurons.
    """
    # Initialize weights with random values between -1 and 1
    self.weights1 = 2 * np.random.random((input_size, hidden_size)) - 1
    self.weights2 = 2 * np.random.random((hidden_size, output_size)) - 1
    # Initialize biases with zeros
    self.bias1 = np.zeros((hidden_size, 1))
    self.bias2 = np.zeros((output_size, 1))

  def predict(self, X):
    """
    Predict the output of the network for a given input.

    Args:
      X: Input data (num_samples, input_size)

    Returns:
      Output of the network (num_samples, output_size)
    """
    # Forward propagation
    layer1 = sigmoid(np.dot(X, self.weights1) + self.bias1)
    output = sigmoid(np.dot(layer1, self.weights2) + self.bias2)
    return output

  def train(self, X, y, learning_rate, epochs):
    """
    Train the neural network using backpropagation.

    Args:
      X: Training data (num_samples, input_size)
      y: Target labels (num_samples, output_size)
      learning_rate: Learning rate for weight updates
      epochs: Number of training epochs
    """
    for epoch in range(epochs):
      # Forward propagation
      layer1 = sigmoid(np.dot(X, self.weights1) + self.bias1)
      output = sigmoid(np.dot(layer1, self.weights2) + self.bias2)

      # Calculate the error
      error = y - output

      # Backpropagation
      # Calculate output layer delta
      output_delta = error * sigmoid_derivative(output)

      # Calculate hidden layer delta
      hidden_delta = np.dot(output_delta, self.weights2.T) * sigmoid_derivative(layer1)

      # Update weights and biases
      self.weights2 += learning_rate * np.dot(layer1.T, output_delta)
      self.weights1 += learning_rate * np.dot(X.T, hidden_delta)
      self.bias2 += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
      self.bias1 += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

if __name__ == "__main__":
  # Define network parameters
  input_size = 2
  hidden_size = 3
  output_size = 1

  # Create the neural network
  network = NeuralNetwork(input_size, hidden_size, output_size)

  # Training data for XOR function
  X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
  y = np.array([[0], [1], [1], [0]])

  # Training parameters
  learning_rate = 0.1
  epochs = 10000

  # Train the network
  network.train(X, y, learning_rate, epochs)

  # Print trained weights and biases
  print("Weights after training:")
  print("  W1:", network.weights1)
  print("  W2:", network.weights2)
  print("Biases after training:")
  print("  b1:", network.bias1)
  print("  b2:", network.bias2)

  # Print network output for all possible inputs
  print("Network output for all inputs:")
  for i in range(2):
    for j in range(2):
      test_input






# class Neuralnetwoek:
#     def __init__(self,Input_layer,Hidden_Layer,Output_Layer):
#         self.Input_layer=Input_layer
#         self.Hidden_Layer=Hidden_Layer
#         self.Output_Layer=Output_Layer
#     def sigmoid(self,neurons):
#         self.neurons=neurons

    
