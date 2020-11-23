def make_bricks(small, big, goal):
    if (goal//5 <= big) and ((goal - 5*(goal//5))<= small): return True
    elif (goal//5 >= big) and ((goal - 5*(big)) <= small): return True
    return False

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
def fix_teen(n):
    if 13 <= n and n <= 19 and n != 15 and n!= 16:
        return 0
    return n

def make_chocolate(small, big, goal):
  if (goal>(small+big*5))or((goal%5)>small):
    return -1
  elif big*5>goal:
    return goal%5
  else:
    return goal-big*5

def lone_sum(a, b, c):
  if a == b == c:
      return 0
  if a == b:
      return c
  if b == c:
      return a
  if a == c:
      return b
  else:
       return a + b + c

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
def round10(nums):
  return (((nums+5)/10)*10)

def lucky_sum(a, b, c):
  sum = 0
  list = [a,b,c,13]
  for n in list[:list.index(13)]:
    sum += n
  return sum

def close_far(a, b, c):
  return (abs(abs(b)-abs(c))>=2) and \
  ((abs(abs(b)-abs(a))<=1 and abs(abs(c)-abs(a))>=2) \
  or (abs(abs(c)-abs(a))<=1 and abs(abs(b)-abs(a))>=2))
