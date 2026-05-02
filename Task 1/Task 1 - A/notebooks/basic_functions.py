def greet(name, message="Welcome to IMAGIINE"):
    print("Hello", name + ",", message)

greet("dhruva")
greet("dhruva", "Have a good day")


def calculate_stats(numbers):
    def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    
    return total, average, maximum

result= list(map(lambda  x: x*x, numbers))
print(result)
