def near_ten(num):
  return True if (num-2)%10 == 0 or (num-1)%10 == 0 or (num+2)%10 == 0 or (num+1)%10 == 0 or num%10 == 0 else False
