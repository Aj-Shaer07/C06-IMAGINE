import pandas as pd;
import numpy as np;


df = pd.read_csv("orders.csv") # here orders.csv is a csv file in the local directory. 
print(df)
 # df is a variable created by me to represent data fram 
 # pd.read_csv is method buitin pandas library it reads what is given to it 

Dictionary_01 = {
    "Name":["Vraj","Hirva","Shrot","Aditi","Krishna"],
    "Age": ["18","18","18","18","18"],
    "Location":["NITK","NITK","NITW","Nirma","NITK"]
}

df = pd.DataFrame(Dictionary_01) 
print(df)
# another way to represent data using the dataframe method 



df.head() # prints the first 5 rows of the dataframe. Used to just look at the basic structure of the frame 
# usefull when you just want to know the basic info about the dataframe 

df.tail() # vice vesa of df.head()

df.columns # returns a list of all columns with their heading. 

# delete data
df = df.drop(39) # drop the index 39 and all its data in the row. 

# Data cleaning
df.dropna() # drop all the index which has a Not Available value
df.fillna({"OrderID":0},inplace=True) # fill all not available in the particular column with 0, 
#inplace = true means do it in the existing dataframe do not create a new one. 

# analysis 
df.sort_values("Price",ascending=False) 
# sorts the values under Price table in descending order

# writing off a new csv file which is processed according to the needs. 
df.to_csv("New_file.csv",index = True)



#######################################---- Numpy ----####################################


array_2d = np.array([[1,2,3],[4,5,6]])
print("2 dimensional array is:" , array_2d)

# numpy arrays are known to work for arrays containing similar datatype 
# this is for better optimisation of operations. 

# scalar multiplication is carried out in this, similar to matrix in maths 
np_array = np.array([1,2,3])
print("Python array multiplied : ", np_array*2)

# creating arrays from scratch. 

zeros = np.zeros((3,4))
print("zeros array \n", zeros)

ones = np.ones((4,5))
print("ones array \n", ones)

full = np.full((2,3),7)
print("full array \n", full)

sequence = np.arange(0,10,2)
print("sequence array \n", sequence)

# array properties. 

arr = np.array([[1,2,3],
                [4,5,6]
                ])

print("shape: ",arr.shape)
print("dimension: ", arr.ndim)
print("size", arr.size)
print("Data type: ",arr.dtype)


## Reshaping of array. 
arr  = np.array([1,2,3,4,5,6,7,8])
print("original ", arr)

reshaped = arr.reshape((2,4))
print("reshaped ", reshaped)

flattened = reshaped.flatten()
print("flattened ", flattened)

# transpose of matrix 
transpose = reshaped.T
print("transpose ", transpose)

# now for 2d array.
#column          0th 1st 2nd 
arr_2d = np.array([[1,2,3],  # 0th row 
                   [4,5,6],  # 1st row  
                   [7,8,9]]) # 2nd row
print("Specific element", arr_2d[1,2]) # arr_2d(row,column)
print("Entire row ", arr_2d[1])
print("Entire column ", arr_2d[:,1:])

## sorting 
arr_2d = [[1,2],[3,1],[2,3]]

print("sorted array :\n", np.sort(arr_2d,axis=0))
# axis = 0 means sort everything columnwise 
# ais = 1 means sort everything row-wise 


#stacking in array.
original = np.array([[1,2],[3,4]])
new_row = np.array([[8,9]])

with_new_row = np.vstack((original,new_row)) # 
# vstack is an inbuilt function used to add new row. 

print(with_new_row)

new_column = np.array([[39],[78]])
with_new_col = np.hstack((original,new_column))

print(with_new_col)