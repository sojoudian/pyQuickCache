from functools import wraps

def cache(func):
    memo = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result
    
    return wrapper

# Usage example
@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# This will run faster on subsequent calls due to caching
print(fibonacci(35))
