def rec_fib(n):
    assert isinstance(n,int)
    assert n >= 0

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)

assert isinstance(rec_fib(0), int)
assert isinstance(rec_fib(1), int)
assert isinstance(rec_fib(10), int)

assert rec_fib(0) == 0
assert rec_fib(1) == 1
assert rec_fib(2) == 1
assert rec_fib(3) == 2
assert rec_fib(10) == 55

