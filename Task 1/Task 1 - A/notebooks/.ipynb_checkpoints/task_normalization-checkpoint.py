def normalize(data):
    Minval=min(data)
    Maxval=max(data)
    Normalized=[]
    n=0
    if(Minval==Maxval)
    for i in data:
        Normalized.append(0)
    else
    for i in data:
       n=(i-Minval)/(Maxval-Minval)
       Normalized.append(n)

    return Normalized