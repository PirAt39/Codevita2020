import math


def check(num):
    maxFactor = 1
    for i in range(2, int(math.sqrt(num))+1):
        temp = num % i
        if temp == 0:
            maxFactor = max(maxFactor, i, num//i)
            break

    return maxFactor


def helper():
    m, n = map(int, input().split())
    if m == n:
        return 0
    factorsOfM = [m]
    factorsOfN = [n]

    while m > 1:
        factor = check(m)
        factorsOfM.append(factor)
        m = factor
        if factor == 1:
            break

    while n > 1:
        factor = check(n)
        factorsOfN.append(factor)
        n = factor
        if factor == 1:
            break

    # factorsOfM.sort(reverse=True)
    # factorsOfN.sort(reverse=True)
    # print(factorsOfM)
    # print(factorsOfN)

    while len(factorsOfM) and len(factorsOfN) and factorsOfM[-1] == factorsOfN[-1]:
        factorsOfM.pop()
        factorsOfN.pop()

    count = len(factorsOfN)+len(factorsOfM)
    return count


# for i in range(int(input())):
print(helper())