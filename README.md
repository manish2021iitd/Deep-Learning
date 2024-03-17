This code implement a neural network class with various activation functions and optimization algorithms.

Fashion-MNIST Dataset: The code loads the Fashion-MNIST dataset, preprocesses it, and converts labels to one-hot encoding.

NeuralNetwork Class: It initializes a neural network with parameters like input size, number of hidden layers, sizes of hidden layers, and output size. It also initializes weights and biases for each layer, along with parameters for different optimization algorithms such as momentum, RMSprop, Adam, etc.

Activation Functions: The class defines several activation functions like sigmoid, tanh, and ReLU. These functions are used during forward propagation.

Forward Propagation: The forward method performs forward propagation through the neural network, computing pre-activations and activations at each layer.

Backward Propagation: The backward method computes gradients of the loss function with respect to the weights and biases using backpropagation.

Update Weights and Biases: The update method updates the weights and biases of the neural network using different optimization algorithms like SGD, momentum, RMSprop, Adam, etc.

Training: The train method trains the neural network using the specified optimizer, activation function, epochs, batch size, and learning rate.

Testing: The test method performs inference on the test data and returns the predicted probabilities.

Compute Accuracy: The compute_accuracy function calculates the accuracy of the model predictions.

Training and Testing: Finally, the code trains the neural network on the training data and evaluates its performance on the test data.
