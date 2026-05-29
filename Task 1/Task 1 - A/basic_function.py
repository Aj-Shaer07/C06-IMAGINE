def greet(name,message="Hello"):
    return f"{message}, {name}!"
def calculate_stats(nums):
    sums=sum(nums)
    avg=sums/len(nums)
    maxi=max(nums)
    return sums, avg, maxi
def square(x):
    mapped=map(lambda num: num**2,x)
    return list(mapped)

    

if __name__ == "__main__":
    print(greet("Alice"))
    print(greet("Bob", "Hi"))
    print(calculate_stats([1, 2, 3, 4, 5]))
    print(square([1, 2, 3, 4, 5]))