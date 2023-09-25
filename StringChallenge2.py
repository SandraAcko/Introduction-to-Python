def StringChallenge(strParam):

 strParam = strParam.replace("a","")
 strParam = strParam.replace("e","")
 strParam = strParam.replace("i","")
 strParam = strParam.replace("o","")
 strParam = strParam.replace("u","")
 count = len(strParam)

 return count

print(StringChallenge("balls"))
