def rec_fib(n):
    if n < 0:
        raise ValueError
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)

n =10
print(rec_fib(n))