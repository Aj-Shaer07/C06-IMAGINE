def is_prime(n):
	if n==1: return False
	for x in range(2,n//2):
		if n%x==0: return False
	else: return True

def squares_upto_n(n):
	L=[x**2 for x in range(1,n+1)]
	return L

def get_even_numbers(nums):
	L=[x for x in nums if x%2==0]
	return L

def primes_upto_n(n):
	L=[x for x in range(1,n+1) if is_prime(x)]
	return L

def to_uppercase(words):
	L=[x.upper() for x in words]
	return L

#main program
print(squares_upto_n(10))
print(get_even_numbers([3,4,2,15,16,8,10,9]))
print(primes_upto_n(25))
print(to_uppercase(["my", "Hello", "MalAYaam"]))
