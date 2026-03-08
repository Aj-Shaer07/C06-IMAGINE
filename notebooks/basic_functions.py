def greet(name, message = "Welcome to IMAGINE"): 
	print(f"Hello {name}, {message}")

def calculate_stats(numbers):
	return sum(numbers), sum(numbers)/len(numbers), max(numbers)

square = lambda x: x**2


#main program
greet("Aaron")
greet("Aaron","Have fun with IMAGINE")
L=eval(input("Enter a list of numbers: "))
print(f"Sum: {calculate_stats(L)[0]}, Average: {calculate_stats(L)[1]}, Maximum: {calculate_stats(L)[2]}")
L_new=list(map(lambda x: x**2,L))
print(L_new)
