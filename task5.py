def to_5_sys(num):
    res = ''
    while True:
        if num < 5:
            res += str(num)
            break
        mod = num % 5
        num //= 5
        res += str(mod)
    return res[::-1]


print(to_5_sys(125 ** 5 + 25 ** 9 - 30).count('4'))
# Ответ 13
