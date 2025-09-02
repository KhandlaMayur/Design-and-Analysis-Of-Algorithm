def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter number of terms: "))
print("Fibonacci Series:", [fib(i) for i in range(n)])
