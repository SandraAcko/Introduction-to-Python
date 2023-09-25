def RecursionChallenge(num):
  total = num * (num -1)
  num = num - 2
  while num > 0:
    total = total * num
    num = num - 1 
    
  return total
 
print(RecursionChallenge(6))
