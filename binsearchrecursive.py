def binsearchrecursive(list, left, right, key):
  while True:
    if left > right:
      return False
    mid = (left + right)/2
    if list[mid] == key:
      return mid
    if list[mid] > key:
      right = mid - 1
    else:
      left = mid + 1
    return binsearchrecursive(list, left, right, key)

list = [1,2,3,4,5,6,7,8,9,10]
left = 0
right = len(list)
for key in [3,8,10]:
  index = binsearchrecursive(list, left, right, key)
  print key, index
