def array_count9(nums):
  x = len(nums)
  count = 0
  for i in range(x):
    n = nums[i]
    if(n == 9):
      count = count+1
  return count
