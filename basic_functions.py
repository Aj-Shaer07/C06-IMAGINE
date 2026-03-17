def greet(name, message="Welcome to IMAGIINE"):
    print(f"Hello {name}, {message}")

greet("Vraj")
greet("Vraj", "Hope you enjoy learning Python")

def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)

    return total, average, maximum

numbers = [10, 20, 30, 40]

total, avg, max_val = calculate_stats(numbers)

print("Sum:", total)
print("Average:", avg)
print("Maximum:", max_val)


square = lambda x: x * x
squared_numbers = list(map(lambda x: x * x, numbers))

print(square(5))
print(squared_numbers)
