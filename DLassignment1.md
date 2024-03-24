The provided code is an implementation of a Deep Learning assignment focusing on building and training neural networks using various configurations and techniques. Here's a breakdown of the code:

**Setup and Libraries:** The code begins by installing the Weights & Biases (WandB) library and importing necessary libraries such as NumPy, scikit-learn, and TensorFlow/Keras.

**Loading Dataset:** The Fashion-MNIST dataset is loaded using Keras' built-in dataset module. This dataset consists of grayscale images of fashion items like shirts, shoes, and trousers.

**Visualization:** A subset of the training images and their corresponding labels are visualized using WandB's logging functionality.

**Neural Network Implementation (Q2):** Two implementations of a Neural Network class are provided. The first implementation defines a simple feedforward neural network with methods for forward pass, activation functions (sigmoid and softmax), and prediction.

**Training and Evaluation (Q3):** The second implementation extends the Neural Network class to support training, evaluation, and different optimization techniques such as stochastic gradient descent (SGD), momentum, Nesterov accelerated gradient (NAG), RMSprop, Adam, and NAdam. Various activation functions (sigmoid, tanh, and ReLU) and loss functions (Mean Squared Error (MSE) and Cross Entropy) are also supported.

**Experimentation (Q4, Q5, Q6):** Experiments are conducted to find the best hyperparameters using a hyperparameter sweep. WandB is used for logging and tracking the experiments. The sweep explores different configurations including the number of epochs, hidden layers, hidden layer sizes, activation functions, loss functions, weight decay, learning rate, optimizer, batch size, and weight initialization methods.

**Confusion Matrix (Q7):** A confusion matrix is generated for the best model configuration based on validation accuracy. This provides insights into the model's performance on the test data.

**Comparison with Squared Error Loss (Q8):** The code also compares the performance of the model using Cross Entropy loss with that using Mean Squared Error (MSE) loss on the MNIST dataset.

**MNIST Dataset (Q10):** Finally, the code includes an implementation for training and evaluating neural networks on the MNIST dataset, experimenting with different configurations similar to the Fashion-MNIST dataset.

Overall, the code provides a comprehensive framework for experimenting with neural networks, exploring various architectures, activation functions, loss functions, optimization algorithms, and hyperparameters to improve model performance on image classification tasks. It leverages WandB for experiment tracking and visualization, making it easier to analyze and compare different configurations.




