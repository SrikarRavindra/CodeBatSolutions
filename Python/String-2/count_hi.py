def count_hi(str):
  count = 0
  x = len(str) - 1
  for i in range(x):
    newStr = str[i:i+2]
    if(newStr == "hi"):
      count = count + 1
  return count
