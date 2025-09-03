def power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    
    left = power(x, n // 2)
    right = power(x, n - n // 2)
    
    return left * right
x = int(input("Enter Base: "))
n = int(input("Enter Exponent: "))
print("Result:", power(x, n))
