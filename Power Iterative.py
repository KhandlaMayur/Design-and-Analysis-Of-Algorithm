def power_function(base,exponent):
    result=1
    for i in range (exponent):
        result=base*result
    return result
    
base=2
exponent=5

print(power_function(base,exponent))
