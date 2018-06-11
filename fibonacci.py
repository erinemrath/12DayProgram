import time

def get_input():
  while True:
    num = input("Input a fibonacci number: ")
    num = str(num)
    if not num.isdigit():
      print("Bad input")
    num = int(num)
    if num < 0:
      print("Please input a positive integer")
    return num

def fibonacci_iter(num):
  if num == 0 or num == 1:
    return num
  fib_1 = 1
  fib_2 = 1
  count = 2
  result = 2
  while count <= num:
    newfib = fib_1 + fib_2
    fib_1, fib_2 = fib_2, newfib
    count += 1
  return newfib

def fibonacci_recursive(num):
  if num <= 2:
    return 1
  return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)

num = get_input()
start_time = time.clock()
iter_ = fibonacci_iter(num)
end_time = time.clock()
print("Fibonacci number %d is: %d and takes %f to calculate iteratively" %(num, iter_, round((end_time - start_time), 3)))
start_time = time.clock()
rec = fibonacci_recursive(num)
end_time = time.clock()
print("Fibonacci number %d is: %d and takes %f to calculate recursively" %(num, rec, round((end_time - start_time), 3)))
