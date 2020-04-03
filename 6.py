import math
import copy

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def DivAppend( n):
    n1=copy.deepcopy(n)
    n0 = round(math.sqrt(n))
    i=2
    rez=[]
    while i <= n0:
        if IsPrime(n):
            i=n
            rez.append(int(i))
            break

        if n % i ==0:
            rez.append(int(i))
            n=n/i
        else:
            i+=1

    if IsPrime(n1):
        if rez.__len__() ==0:
            rez.append(n1)
    return rez