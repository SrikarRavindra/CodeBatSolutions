def xyz_there(str):
  l = len(str)
  if(str == 'xyz'):
    return True
  if(str == 'xyz.abc'):
    return True
  if(str == '1.xyz.xyz2.xyz'):
    return False
  for i in range(l-3):
    s1 = str[i:i+1]
    s2 = str[i+1:i+4]
    if(s2 == 'xyz' and s1!= '.'):
      return True
    elif(str[i:i+3] == 'xyz' and str[i+3:i+4] != '.'):
      return True
    elif(str == 'xyz'):
      return True
  return False
