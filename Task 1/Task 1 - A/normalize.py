#normalize the data of the list 
def normalize(data):
    max_val=max(data)
    min_val=min(data)
    for i in range(len(data)):
        data[i]=(data[i]-min_val)/(max_val-min_val)
    return data

#to ensure that we use this function in other files while making sure the checking only occurs in this 
if __name__ == "__main__":
    data=[10,20,30,40,50]
    print(normalize(data))
