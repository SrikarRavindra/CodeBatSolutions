def sum13(nums):
  return sum(nums[i] for i in range(1) if nums[i]!=13)+ sum([nums[i] for i in range(1, len(nums)) if nums[i] != 13 and nums[i-1] != 13]) if len(nums) > 0 else 0
