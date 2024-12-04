def find_dividers(num):
    res = []
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    return sorted(list(set(res)))


for num in range(174457, 174506):
    dividers = find_dividers(num)
    if len(dividers) == 2:
        print(f"{num}: {dividers[0]}, {dividers[1]}")
