def first_last6(nums):
  if nums[0] == 6:
    return True
  if nums[-1] == 6:
    return True
  else:
    return False

def common_end(a, b):
  if a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]:
    return True
  else:
    return False

def reverse3(nums):
  nums.reverse()
  return nums

def middle_way(a, b):
  new_array = []
  new_array.append(a[1])
  new_array.append(b[1])
  return new_array

def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums) - 1]:
    return True
  else:
    return False

def sum3(nums):
  res = 0
  for i in nums:
    res = res + i
  return res

def max_end3(nums):
  large = 0
  if nums[0] >= nums[2]:
    large = nums[0]
  else:
    large = nums[2]
  nums = []
  for i in range(3):
    nums.append(large)
  return nums

def make_ends(nums):
  new_array = []
  new_array.append(nums[0])
  new_array.append(nums[-1])
  return new_array

def make_pi():
  arr = []
  three = 3
  one = 1
  four = 4
  arr.append(three)
  arr.append(one)
  arr.append(four)
  return arr

def rotate_left3(nums):
  new_arr = []
  new_arr.append(nums[1])
  new_arr.append(nums[2])
  new_arr.append(nums[0])
  return new_arr

def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0

def has23(nums):
  if nums[0] == 2:
    return True
  if nums[0] == 3:
    return True
  if nums[1] == 2:
    return True
  if nums[1] == 3:
    return True
  else:
    return False