from hash import hash

class HashTable:

  def __init__(self, size=20):
    self.size = size
    self.data = [None] * self.size
    self.slots = [None] * self.size

  def __setitem__(self, key, data):
    self.put(key, data)

  def __getitem__(self, key):
    self.get(key)

  def show_slots(self):
    print(self.slots)

  def show_data(self):
    print(self.data)

  def hash_function (self, key, size):
    return hash(key, size)

  def rehash(self, old, size):
    return (old + 1) % size

  def print_hash_table(self):
    for index in range(len(self.slots)):
      key = self.slots[index]
      value = self.data[index]
      print("%d: %s:%s" % (index, key, value))

  def get(self, key):
    start = self.hash_function(key, len(self.slots))
    data = None
    index = start
    while self.slots[index] is not None:
      if self.slots[index] == key:
        data = self.data[index]
        break
      else:
        index = self.rehash(index, len(self.slots))
        if index == start:
          break
    return data

  def put(self, key, data):
    hashval = self.hash_function(key, len(self.slots))
    if self.slots[hashval] is None:
      self.slots[hashval] = key
      self.data[hashval] = data
    elif self.slots[hashval] == key:
      self.data[hashval] = data
    else:
      next_ = self.rehash(hashval, len(self.slots))
      while self.slots[next_] is not None and self.slots[next_] != key:
        next = self.rehash(next, len(self.slots))
      if self.slots[next_] is None:
        self.slots[next_] = key
        self.data[next_] = data
      else:
        self.data[next_] = data
