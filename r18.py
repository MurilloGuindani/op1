# -*- coding: utf-8 -*-

def rec(n):
    if n == 0:
        return 4
    else:
        return (3 * (4 ** (n - 1)) + 2 ** n) + rec(n - 1)


t = 0
while True:
    p = int(input())
    if p == -1:
        break
    else:
        t += 1
        i = rec(p)
        print("Teste %d" % (t))
        print(i)
        print("")
