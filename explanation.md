Machine learning, as the name suggests, is the process by which a computer
learns to interpret data in different ways, classify data and based on some
patterns, predict the future outcomes.

Artificial intelligence is the tool, that a computer uses to learn from a given
dataset.

First, data with particular features are fed to the machine,often involving a
dependent and independent variable. Based on this, some parameters are generated
which can relate the two variables with the least error. After this, the model
is tested by providing an input and  predicting the output.

A hypothesis is the function that relates the dependent and independent variable.
Prediction error is the error or the difference between the computed value of the
output and the exact value which is already known. For a proper, accurate,
efficent model the parameters must be chosen in such a manner that this error is
the least. This process is known as optimization.

A regression problem involves relating continuous data, and the output of such
a problem is a real number. For example, predicting the relationship between
salary of an individual and his monthly expenses. Classification problem yield
caterogical solutions. Example, identifying whether an email is spam or not.

A loss function measures the error of the predicted value of the model and its
exact value which is known to a human. For example, in the case of a linear
regression model, this error is the difference between the predicted value of
the output based on some parameters and the actual value of the output. On the
other hand, for a classification problem, misclassification rate and binary cross
entropy are errors that are often considered. A minimum loss improves the
accuracy and reliability of the model. The model can run faster, and take
up lesser memory as well.
Different types of problems can have different losses. A linear regression
problem and a classification problem have two different types of losses as
mentioned previously. Hence they require different types of loss functions all
together.

Gradient descent is a loss function used in linear regression models. First,
the loss funtion is generated and then the its gradient is computed. This gives
the direction in which the function increases. As we want to decrease the loss,
we have to move in the negative gradient direction.

Numpy and Pandas are libraries that allow a user to perform a wide range of
mathematical operations on large datasets.

import numpy as np, pandas as pd
a=np.zeros(5,1) #creates a 2D array of only zero elements
b=np.array([1,2,3,4,5]) #creates an 1D array from the given elements.
c=a @ b #performs matrix multiplication on a and b
d=np.linalg.solve(A,B) #solves for the equation Ax=B
e=np.linalg.det(A) #returns determinant of A
f=a+b
g=a*5 #generates a matrix by multipying 5 to each element

df=pd.read_csv("Employee.csv")
print(df.iloc[11]) #displays record at 11th index
print(df.loc[df["Department"]=="Sales"]) #displays details of all Sales employees
df.loc[df["Name"]=="Aaron","Salary"]=200000 #updates salary of Aaron to 200000
df.describe() #displays details of each field
print(set(df["Dept"])) #displays all the departments in the file
