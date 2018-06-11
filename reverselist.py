def get_input():
  print("Enter list of data separated by spaces")
  data = input()
  return data

def reverse_list(list_):
  if len(list_) == 1:
    return list_
  reversed_ = reverse_list(list_[1:])
  reversed_.append(list_[0])
  return reversed_

input_ = get_input()
reversed_ = reverse_list(input_)
print(reversed_)
