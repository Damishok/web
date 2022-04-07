'''
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
'''


'''
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False
'''

'''
def sum_double(a, b):
 
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum
'''

'''
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2
'''

'''
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
'''

'''
def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)
'''

'''
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
'''

'''
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
'''

'''
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
'''

'''
def missing_char(str, n):
  front = str[:n]  
  back = str[n+1:]  
  return front + back
'''


'''
def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1] 
  return str[len(str)-1] + mid + str[0]
'''


'''
def string_times(str, n):
  result = ""
  for i in range(n):  
    result = result + str  
  return result
'''

'''
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result
'''


'''
def last2(str):
  if len(str) < 2:
    return 0
  
  last2 = str[len(str)-2:]
  count = 0
  
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1
  return count
'''


'''
def array123(nums):
  
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False
'''