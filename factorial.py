def factorial(n):
    x=1
    y=2
    while y<=n:
        x=x*y
        y=y+1
    return x

print(factorial(4))