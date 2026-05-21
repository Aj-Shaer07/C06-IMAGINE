def greet(name, message="Welcome to IMAGINE"):
    return f"Hello {name}! {message}"
greet("Inchara")
greet("Inchara","Hope you're doing fine")


def calculate_stats(number):
    for i in number:
        if type(i)!=int:
            return 0,0,0
    s=0
    a=0
    m=0
    for i in number:
        s=s+i
    a=s/len(number)
    m=max(number)
    return s,a,m


def square(n):
    s=lambda x:x*x
    return s


def square_list(n):
    s=list(map(lambda x:x*x,n))
    return s



