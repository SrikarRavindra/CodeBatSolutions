def caught_speeding(speed, is_birthday):
  return 0 if (is_birthday and speed <= 65) or (speed <= 60) else 1 if (is_birthday and speed >= 66 and speed <= 85) or (speed >= 61 and speed <=80) else 2
 
