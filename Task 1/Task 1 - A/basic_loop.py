#prime number checker and list comperhension
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def list_prime(n):
    primes=[i for i in range(2,n+1) if is_prime(i)]
    return primes
if __name__ == "__main__":
    n=100
    print(list_prime(n))
