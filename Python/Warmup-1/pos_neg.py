def pos_neg(a, b, negative):
  if(not negative):
      return True if(a > 0 and b < 0) or (a < 0 and b > 0) else False
  else:
      return (a < 0 and b < 0)
