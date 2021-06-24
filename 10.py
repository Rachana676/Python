import time

def timeit(func):
    def timed(*args, **kw):
        print("BEFORE THE Timeit DECORATOR")
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()

        minutes, seconds = divmod((te-ts), 60)
        print(minutes,seconds)
        print ("TIME TAKEN IS : ",((te-ts)*10**6))
        print("AFTER THE Timeit DECORATOR")
        return result
    return timed


@timeit
def fib():
    a,b=0,1
    while(1):
        yield a
        a, b=b ,a+b

num = int(input("ENTER SIZE OF FIBONACCI SERIES: "))

fibonacci = fib()

for x in range(num):
    print(next(fibonacci))  
