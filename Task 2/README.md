In this task we learned how to perform linear regression and logistic
regression on a given dataset. Task 2A involved building a linear regression
model to find the relation between x and y values by plotting the best fit
line. The first step is to train the model on sufficient amount of training
data. We can obtain the the parameters that describe the given data best by
minimising the cost function. This is performed by calculating error such as
mean square error, root mean square error and R-squared which is 1-(sum of 
residual squares/total sum of squares). Once we have obtained the parameters
we should save the model and then test on the test data provided. 

The second part of the task aimed at classifying Malignant and Benign based
on several features. For this we find out which features contribute to the
diagnosis more. After this we use the sigmoid function to classify the data.
As in linear regression, this too has a cost function which has to be
minimised. This function is called Binary cross entropy. Finally we evaluate
the model's accuracy by calculation precision, accuracy, sensitivity, F1
score. 

For the third part we were asked to perform linear regression a data
relating several features of wine to the category of wine (0,1,2). 
