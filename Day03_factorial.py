def fact_1(n):
  fact = 1
  for i in range(n,0,-1):
    fact *= i
  return fact

# recursion
def fact_2(n):
  if n < 1:
    return 1
  else:
    return n * fact_2(n-1)
  
