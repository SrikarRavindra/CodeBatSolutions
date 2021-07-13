def array123(nums):
  x = len(nums)
  for i in range(x-2):
    a = nums[i]
    b = nums[i+1]
    c = nums[i+2]
    if(a==1 and b==2 and c==3):
      return True
  return False
    
