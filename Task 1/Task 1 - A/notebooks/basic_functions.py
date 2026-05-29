def greet(name,message="Welcome To IMAGINE!"):
    print("Hello ",name +",",message)

greet("Dhruva")
greet("Dhruva","Nice to meet you!")

def calculate_stats(numbers):
    total=0
    average =0
    maximum=max(numbers)
    for i in numbers:
        total+=i
    average=total/len(numbers)
    return(total,average,maximum)

numbers=[1,2,3,4.5]
square_numbers=map(lambda x:x*x,numbers)
print(square_numbers)
    