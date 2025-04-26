def factorial(n): 
  #using math knowledge reursion of factorials 
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(8))#sample