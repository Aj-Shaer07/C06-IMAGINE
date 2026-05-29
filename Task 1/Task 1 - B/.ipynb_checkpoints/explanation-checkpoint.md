1.Supervised Learning: It is a type of machine learning where a model learns patterns through input data(features) along with the correct labels. That is, the training data includes features and correct answers are fed to the model, and the model guesses a function that maps input to output based on the provided training data.

2.Regression: Regression is a supervised learning task in which outputs are continous numerical values, that is, output value belongs to a range of real numbers. This is used in several real-life scenarios such as predicting house prices, temperature of a region,etc. which are continuous values. Regression primarily uses a linear function y=mx+c as an approximation to the actual function.
Classification: Classification is a supervised learning task in which outputs belong to discrete categories. This includes problems with Yes-No answers such as email-spam detection, face detection, medical diagnosis. Models pertaining to classification problems compute probabilities for the possible outputs, rather than a concrete Yes-or-No prediction.

3.Loss function: It is a function used to measure prediction error, that is, to measure how wrong the model's predicted values are compared to the true values.
Mean squared error: This function is commonly used in regression problems to measure error. 
Formula: Mean squared error={summation(y(pred)-y(true))^2}/n. 
Squaring makes error positive and punishes large errors. This can be used to measure the distance between predicted and true values, thus making it an appropriate loss function for regression with continuous output values.
Binary Cross entropy: This function is commonly used in binary classification problems.
Here, there are only two true labels:0 and 1. The model predicts probability of the output,i.e, it gives a probability close to 0 if 0 happens to be the true label, and a probability close to 1 when 1 is the true label. Binary cross entropy is favoured as it penalizes false confidence of the model,i.e, it pushes the model to be correct and confident and helps minimize error.
Minimizing loss improves our performance as the predictions get closer to the true values and the model thus becomes more and more accurate.
Different loss functions are appropriate for different tasks, for instance, mean squared error has no relevance to classification problems(computing probabilities) and is instead used in continuous numerical value output error measurements like in regression.

4.Gradient descent: Gradient descent is the process of computing gradients followed by descending towards the optimum value by moving in the direction of negative gradient. Gradient represents the direction of steepest increase, therefore moving along the negative gradient means we are descending as steeply as possible. This is often multiplied by learning rate, which represents the steps taken to reach our destination. A very high value of learning rate would result in oscillations about the optimum value or divergence, and a very low learning rate would lead to convergence but at an awfully slow rate.

Numpy is very useful in Machine learning as we're dealing with millions of data points and numpy offers fast vectorized computations compared to the traditional slow python loops.
Pandas help data scientists convert raw, unstructured data into structured,clean data.