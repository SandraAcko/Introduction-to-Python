def StringChallenge(num):
  
  hours = str(num // 60)
  minutes = str(num % 60)
  return (hours + ":" + minutes)


print(StringChallenge(45))
