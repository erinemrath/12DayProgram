def sequentialsearch(array, item):
  offset = 0
  found = False
  while offset < len(array) and not found:
    if array[offset] == item:
      found = True
      print("Element discovered at array[" + str(offset) + "]")
    else:
      offset += 1
  return found


def binarysearch(array, item):
  start = 0
  last = len(array) - 1
  found = False
  while start <= last and not found:
    mid = (start + last)/2
    if array[mid] == item:
      found = True
    else:
      if item < array[mid]:
        last = mid - 1
      else:
        start = mid + 1
  return found

L1 = [1,2,3,4,5,6,7,8,9]
print(binarysearch(L1, 9))
print(sequentialsearch(L1, 9))
