def find_dividers(num):
    res = []
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    return sorted(list(set(res)))


num = 300000000
cnt = 0
while True:
    num += 1
    dividers = find_dividers(num)
    if len(dividers) >= 5:
        cnt += 1
        print(num, dividers[4])
    if cnt == 5:
        break
