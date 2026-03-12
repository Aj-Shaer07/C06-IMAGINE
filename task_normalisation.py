def normalize(data):
    min_val = min(data)
    max_val = max(data)
    
    if max_val == min_val:
        return [0 for _ in data]
    
    return [(x - min_val) / (max_val - min_val) for x in data]

if __name__ == "__main__": 
    data = [10, 20, 30, 40, 50]
    print(normalize(data))

print(normalize([10,20,30]))

    