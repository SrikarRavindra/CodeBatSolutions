def end_other(a, b):
  s1 = a.lower()
  s2 = b.lower()
  x = len(s1)
  y = len(s2)
  if(x > y):
    for i in range(x):
      s3 = s1[x-y:x]
      if(s3 == b.lower()):
        return True
  else:
    for i in range(y):
      s3 = s2[y-x:y]
      if(s3 == s1):
        return True
  return False
