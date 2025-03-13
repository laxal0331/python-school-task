import math

def evaluate_functions(x):
    f_x = math.cos(2 * x)
    f_prime_x = -2 * math.sin(2 * x)
    f_double_prime_x = -4 * math.cos(2 * x)
    return f_x, f_prime_x, f_double_prime_x

x = 1.0
results = evaluate_functions(x)
print(f"f(x) = {results[0]}, f'(x) = {results[1]}, f''(x) = {results[2]}")
