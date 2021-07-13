def array_front9(nums):
  x = len(nums)
  if(x == 5):
    return find_nine(nums)
  else:
    for i in range(x):
      if (nums[i] == 9):
        return True
    return False
    
def find_nine(l):
  m = len(l)
  for i in range(4):
    if(l[i] == 9):
      return True
  return False
