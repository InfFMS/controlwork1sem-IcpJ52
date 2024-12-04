def to_3_sys(num):
    res = ''
    while True:
        if num < 3:
            res += str(num)
            break
        mod = num % 3
        num //= 3
        res += str(mod)
    return res[::-1]


for x in range(1, 2031):
    n = to_3_sys(3 ** 100 - x)
    cnt = n.count('0')
    if cnt == 2:
        print(x)
        break
# Ответ 9
