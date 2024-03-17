**DLAssignment1**
This is deep learning assignment in which feedforward neural networks of varying architectures have been implemented from scratch with the use of packages like numpy and pandas. 
The following links describe the problem given, the datasets used and how the hyperparameter sweeps were done using WANDB.

**Contents**
assignment1.py
This file contains the implementation of a feed forward NN with back propogation supported by various optimisers. The sweep features are also configured.

**Optimisers**
The following optimisers have been implemented:
Stochatic gradient Descent
Momentum based gradient descent
Nesterov Accelarated gradient descent
RMSprop
Adam
Nadam

**Hyperparameter tuning**
The best hyperparameters are to be selected based on validation results. Following are the key parameters of interest.
number of epochs: 5, 10
number of hidden layers: 3, 4, 5
size of every hidden layer: 32, 64, 128
weight decay (L2 regularisation): 0, 0.0005, 0.5
learning rate: 1e-3, 1 e-4
optimizer: sgd, momentum, nesterov, rmsprop, adam, nadam
batch size: 16, 32, 64
weight initialisation: random, Xavier
activation functions: sigmoid, tanh, ReLU
Note: There are other parameters that can be tuned but have not been experimented with.
