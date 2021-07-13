def parrot_trouble(talking, hour):
  return True if((hour < 7 and talking) or (hour > 20 and talking)) else False
  
