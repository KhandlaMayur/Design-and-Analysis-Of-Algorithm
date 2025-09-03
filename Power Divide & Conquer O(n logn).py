def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2) 
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half

x = int(input("Enter Base: "))
n = int(input("Enter Exponent: "))
print("Result:", power(x, n))
