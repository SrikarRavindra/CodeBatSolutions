def sum2(nums):
  x = len(nums)
  if(x == 0):
    return 0
  if(x == 1):
    return nums[0]
  else:
    c = nums[0] + nums[1]
    return c
