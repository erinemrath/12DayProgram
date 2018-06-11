def get_table_size():
  while True:
    size = input("Enter table size: ")
    if isinstance(size, int):
      return size
    size = size.strip()
    size = int(size)
    return size

def hash(string, tsize):
  sum_ = 0
  for index in range(len(string)):
    sum_ += ord(string[index])
  return sum_ % tsize

def hash_weighted(string, tsize):
  sum_ = 0
  for index in range(len(string)):
    sum_ += ord(string[index])*(index + 1)
  return sum_ % tsize

def get_string():
  print("Enter string: ")
  string = input()
  string = str(string)
  string = string.strip()
  return string

string = get_string()
tsize = get_table_size()
hashval = hash(string, tsize)
weightedhashval = hash_weighted(string, tsize)
print("Hash Value: %s" % hashval)
print("Hash Weighted Value: %s" % weightedhashval)
