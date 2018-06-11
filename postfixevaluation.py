from Stack import Stack

def postfixevaluation(postfix):
  postfix = str(postfix)
  postfixes = postfix.split(" ")
  operations = Stack()
  for postfix in postfixes:
    if postfix.isdigit():
      operations.push(int(postfix))
    else:
      #not enough operations on the stack
      if operations.size() <= 1:
        print("Invalid postfix expression")
        return False
      secondarg = operations.pop()
      firstarg = operations.pop()
      answer = do_math(postfix, firstarg, secondarg)
      if answer is None:
        return answer
      operations.push(answer)
  return operations.pop()


def do_math(operator, first, second):
  if operator == "+":
    return x + y
  elif operator == "-":
    return x - y
  elif operator == "*":
    return x * y
  elif operator == "/":
    return float(x)/y
  elif operator == "^":
    return x ** y
  return None

def get_input():
  print("Enter postfix expression separated by spaces")
  postfix = input()
  return postfix

postfix = get_input()
evaluation = postfixevaluation(postfix)
print(evaluation)

