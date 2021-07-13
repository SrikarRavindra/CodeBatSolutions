def string_bits(str):
  finalString = ""
  x = len(str)
  for i in range(x):
    if i%2 == 0:
      finalString += str[i:i+1];
  return finalString
