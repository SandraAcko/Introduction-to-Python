def ArrayChallenge(strArr):
  length = min(len(strArr[0]), len(strArr[1]))
  count = 0
  for character in range(length):
    if (strArr[0][character] != strArr[1][character]):
      count = count + 1
  return count
print(ArrayChallenge(["abcdef", "aefdef"]))
