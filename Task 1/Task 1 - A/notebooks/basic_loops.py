def is_prime(n):
    k=0
    if type(n)!=int:
        return ValueError
    else:
        for i in range (1,n+1):
            if n%i==0:
                k=k+1
            else:
                k=k
    if k==2:
        return True
    else:
        return False
    

def squares_upto_n(n):
    s=[i*i for i in n]
    return s


def get_even_numbers(nums):
    r=[i for i in nums if i%2==0]
    return r


def primes_upto_n(n):
    r=[i for i in range (1,n+1) if is_prime(i)==True]
    return r


def to_uppercase(words):
    r=[i.upper() for i in words]
    return r