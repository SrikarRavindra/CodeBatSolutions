def make_ends(nums):
  return [nums[0], nums[0]] if (len(nums)==1) else [nums[0], nums[len(nums)-1]]
