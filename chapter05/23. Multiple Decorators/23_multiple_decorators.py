def log_calls(func):
    """
    A decorator that logs the function call.
    """
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper

import time

def measure_time(func):
    """
    A decorator that measures the execution time of the function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # .time()
        result = func(*args, **kwargs)
        end_time = time.perf_counter() # .time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.6f} seconds")
        return result
    return wrapper


# The decorators are applied bottom-to-top (@measure_time first, then @log_calls).
# The execution is top-to-bottom (@log_calls executes first, then @measure_time).
@log_calls
@measure_time 
def fibonacci(n):
    """
    Return the nth Fibonacci number.
    
    Args:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def main():
    # Using the function with multiple decorators
    print(fibonacci(20))

if __name__ == '__main__':
    main()



