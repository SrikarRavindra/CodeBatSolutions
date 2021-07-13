def double_char(str):
  result = ""
  x = len(str)
  for i in range(x):
    result = result + str[i:i+1] + str[i:i+1]
  return result
