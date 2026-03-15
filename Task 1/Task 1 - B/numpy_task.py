import numpy as np
#l=eval(input("Enter the list of numbers: "))
l = [1, 2, 3, 4, 5]  # Example list
arr=np.array(l)
print("The array is: ",arr)
print(len(arr))
#alpha 
for i in range(len(arr)): #trversing like a normal list 
    print(arr[i])
    arr[i]=arr[i]**2
print("The squared array is: ",arr)
# multiplication of matrix
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c=a*b
print(c) #carries out  multiplication ai*bi
print("="*25)
d=a@b #carries out matrix multiplication 
print(d)
print("="*25)
e=np.matmul(a,b) #also carries out matrix multiplication
print(e)
# @ is similar to np.matmul cise way for matrix multiplication
print("="*25)
#understanding the array shape
print("Shape of arrays: ")
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1.shape) 
arr2=np.array([[1,2],[3,4],[5,6]])
print(arr2.shape) 
arr3 = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(arr3.shape)
print("="*25)
#simple vectorized computation

#instead of alpha we can do this 
x=arr**2
print("The squared array using vectorized computation is: ",x)
