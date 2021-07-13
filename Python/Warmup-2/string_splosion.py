def string_splosion(str):
  result = ""
  x = len(str)
  for i in range(x):
    strOne = str[0:i+1]
    result+=strOne
  return result
