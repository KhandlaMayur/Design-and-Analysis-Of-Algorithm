def recursive_funtion(base,exponent):
    if (exponent==0):
        return 1
    else:
        return base*recursive_funtion(base,exponent-1)
    
base=5
exponent=5
print(recursive_funtion(base,exponent))
