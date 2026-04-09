def normalize(data):
    mi=min(data)
    ma=max(data)
    nrm=[]
    if ma==mi:
        for i in data:
            nrm.append(0)
    else:
        for i in data:
            n=(i-mi)/(ma-mi)
            nrm.append(n)
    return nrm
    