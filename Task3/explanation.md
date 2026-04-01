## Neural networks
- A neural network is a machine model made up of a series of neurons that learns from data to recognize patterns such has hand written text or numbers which dffer from person to person. This system is inspired by the human brain.
- A neural network consists of series of neurons arranged in layers in order to build a pattern in the input. A neuron is a function that takes in outputs from all the neurons in previous layer and gives out the number between 0 and 1.
- A weight is assigned for each one of the connections between the neuron from one layer to all the neurons from the previous layer which represents the strength of the connection between neurons and it computes the weighted sum of all the activations.
- In order to reduce this to a scale of 0 to 1, we take the sigmoid or ReLU of the function (activation functions).
- Lastly, to figure out when it should be activated for particular pattern and when not, we add a bias to shift the activation up or down. 

## Activation function
- Activation functions are the mathematical function applied to the output ( weighted sum of all the activations ) . 
- A neural network calculates the weighted sum of all the activations and can lie anywhere on the number line. 
- The use of activation function is necessary for the network to learn complex curves by adding nonlinearity. Without activation functions, the network would just behave like a linear equation without being able to learn complex data like images or speech. 
- By applying the activation function, this sum can be included withing the range (0 to 1) or (-1 to 1) in some cases so that the range of values is not too big.
- Examples: sigmoid, ReLU, Tanh etc

## Weights and biases
- The weights and biases in the neural network are the learnable parameters. Different weights and biases are assigned in order to identify different patterns and structures.
- Weights – numbers that represent the strength of the connection between neurons.
- Biases – number that allows neurons to shift their activation up or down.
- The network predicts something based on the weights and biases, it then measures how wrong it is. It calculates how each weight and bias contributes to the error and then adjusts the weights and biases to reduce the error.
- Therefore, the AI neural network becomes smarter overtime correcting it’s mistakes. 

## Backpropagation and weights update
- Backpropagation = Forward pass + Loss calculation + Backward pass (gradients)
- Forward pass: Input goes through the network layer by layer, Each neuron computes z=wx+b
- Loss Calculation: Compare prediction with actual value using a loss function. (ex: Mean Squared Error or Cross-Entropy)
- Backward Pass: Compute how much each weight contributed to the error. 
- Weight update: w=w−η⋅(∂L​/∂w), where𝑤 w = weight, η(eta) = learning rate, ∂L​/∂w = gradient 
