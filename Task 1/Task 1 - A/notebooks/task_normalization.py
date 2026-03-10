def normalize(data):
    minimum=min(data)
    maximum=max(data)
    r=[]
    for x in data:
        x1=(x-minimum)/(maximum-minimum)
        r.append(x1)
    return r
    