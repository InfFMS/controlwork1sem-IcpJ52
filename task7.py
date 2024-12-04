for i in range(1000, 10000):
    el = str(i)
    a1 = int(el[0]) + int(el[1])
    a2 = int(el[1]) + int(el[2])
    a3 = int(el[2]) + int(el[3])
    lst = [a1, a2, a3]
    lst.remove(min(a1, a2, a3))
    lst = sorted(lst)
    res = int(str(lst[0]) + str(lst[1]))
    if res == 1418:
        print(i)
        break
