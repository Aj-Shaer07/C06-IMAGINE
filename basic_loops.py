def sieve(limit):
    if limit <= 1:
        raise ValueError("Invalid input")

    if limit >= 10000:
        print("Long list")

    all_num = list(range(2, limit + 1))
    i = 0
    while i < len(all_num): 
        for k in range(2 * all_num[i], limit + 1, all_num[i]): 
            if k in all_num:
                all_num.remove(k)
        i = i + 1
    return all_num