import time

def measure_time(runs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(runs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                total_time += end_time - start_time
            average_time = total_time / runs
            print(f"Average Execution Time of {func.__name__} over {runs} runs: {average_time} seconds")
            return result
        return wrapper
    return decorator

@measure_time(100000)
def suda():
    for i in range(100):
        marks = 0

        for j in range(i):
            j += 1
            if i % j == 0:
                marks += 1
        
        if 1 < marks < 3:
            #print(i, end=", ")
            pass

@measure_time(100000)
def Dula():
    for i in range(100):
        marks = 0

        for j in range(i):
            j += 1
            if marks > 2:
                continue
            elif i % j == 0:
                marks += 1
        
        if 1 < marks < 3:
            #print(i, end=", ")
            pass
@measure_time(100000)
def GPT():
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            #print(range(2, int(num**0.5) + 1))
            if num % i == 0:
                return False
        return True

    def find_primes(limit):
        primes = []
        for n in range(2, limit + 1):
            if is_prime(n):
                primes.append(n)
        return primes

    find_primes(10)  # Output: [2, 3, 5, 7]


suda()
Dula()
GPT()
 #2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
 #2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,