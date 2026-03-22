#Exercise 1
def is_prime(n):
    flag=0
    if(n==0 OR n==1):
    return(False)
    else
    for i in range(2,n):
        if n%i==0:
        flag=1
        return(False)
        break
    if flag==0:
        return(True)

#Exercise 2
def squares_upto_n(n):
    sum=0
    for i in range(n+1):
        sum+=n*n
    return sum

#Exercise 3
def get_even_numbers(nums):
    even=[]
    for i in nums:
        if(i%2==0):
            even.append(i)
    return even

#Exercise 4
def primes_upto_n(n):
    listofprimes=[]
    for i in range(n+1):
        if(is_prime(i)):
        listofprimes.append(i)
    return (listofprimes)

#Exercise 5
def to_uppercase(words):
    up=[]
    for i in range(0,len(words)):
        up[i]=words[i].upper()
    return up