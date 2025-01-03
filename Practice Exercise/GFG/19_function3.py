def pow(x,n):
    if n == 1:
        return x
    return x*pow(x,n-1)

pow(2,4)

pow(5,3)