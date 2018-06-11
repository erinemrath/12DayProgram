def factorial(num):
  if num <= 1:
    return 1
  return num * factorial(num - 1)

def get_input():
  while True:
    num = input("Enter number:")
    num = str(num)
    if num.isdigit():
      num = int(num)
      return num
    else:
      print("Input a number")

num = get_input()
factorial = factorial(num)
print(factorial)
