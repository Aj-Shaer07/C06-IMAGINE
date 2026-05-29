def is_prime(n):
    c=0
    if (i==0) or (i==1):
        return False
    else:
        for i in range(2, n):
            r=n%i
            if r==0:
                c+=1
            if count==0 :
                return True
            else:
                return False
                

def squares_upto_n(n):
    sum=0
    for i in range(0, n+1):
        sum+=i**2
    return sum


def get_even_numbers(nums):
    ev=[]
    for i in nums:
        if (i%2==0):
            ev.append(i)

def primes_upto_n(n):
    pr=[]
    for i in range(n):
        if is_prime :
            pr.append(i)
        
            
                

def to_uppercase(words):
    up=[]
    for i in range(0, len(words)):
        up[i]=words[i].upper()

    return up
        