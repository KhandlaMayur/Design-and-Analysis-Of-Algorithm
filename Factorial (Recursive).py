def factorial(n):
    if (n==0 and n==1):
        return 1
    else:
      fact=1
      for i in range(2,n+1):
         fact=fact*i
      return fact

n=5


print(factorial(n))
