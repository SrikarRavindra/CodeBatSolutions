def front_back(str):
  return str[len(str)-1] + str[1:len(str)-1] + str[0:1] if len(str) > 1 else str
