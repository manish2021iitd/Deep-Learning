This is PyTorch implementation of a Convolutional Neural Network (CNN) for image classification tasks which has the following different components and steps in code:

**CNN Model Definition:**
Defined a CNN class inheriting from nn.Module. This class represents the architecture of CNN.
The init method initializes the layers of the CNN such as convolutional layers, batch normalization layers, activation functions, max-pooling layers, and fully connected layers.
The forward method defines the forward pass of the CNN, where input data flows through the defined layers.

**Data Loading and Preprocessing:**
The get_data_loaders function prepares the data loaders for training, validation, and testing.
It applies transformations such as resizing, data augmentation , and normalization to the input images.

**Training Function:**
The train function trains the CNN model using the provided training data.
It iterates over the training data for a specified number of epochs, computes the loss, performs backpropagation, and updates the model's parameters.
After each epoch, it evaluates the model on the validation set and logs the validation accuracy.

**Testing Function:**
The test function evaluates the trained model on the test dataset and computes the test accuracy.

**Hyperparameter Sweep Configuration:**
Defined a hyperparameter sweep configuration using Weights & Biases (wandb) for hyperparameter optimization.
It specifies the method (e.g., bayesian optimization), metric to optimize (validation accuracy), and the range of hyperparameters to search over.

**Main Function and Sweep Agent:**
The main function initializes the model, criterion, and optimizer based on the hyperparameters specified in the configuration.
It trains the model, evaluates it on the test set, and logs the test accuracy.
