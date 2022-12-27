def phi (n) :
    res = n;
    
    for i in range(2,n):
        if n % i == 0 :
            while n % i == 0:
                n /= i
            res -= res / i;
        i = i*i

    if n != 1:
        res -= res / n
    return res


print(phi(9))