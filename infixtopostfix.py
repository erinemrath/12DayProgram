from Stack import Stack

def infixtopostfix(tokens):
  operations = Stack()
  precedence = {"(": 1, "+": 2, "-": 2, "*": 3, "/":3, "^": 4}
  postfix_list = []
  chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numbers = "1234567890"
  for token in tokens:
    if token == "(":
      operations.push(token)
    elif token ==")":
      arg = operations.pop()
      while arg != "(":
        postfix_list.append(arg)
        arg = operations.pop()
    elif token in chars or token in numbers or token.isdigit():
      postfix_list.append(token)
    else:
      while (precedence[operations.peek()] >= precedence[token]) \
            and (not operations.is_empty()):
        postfix_list.append(operations.pop())
      operations.push(token)
  while (not operations.is_empty()):
    postfix_list.append(operations.pop())
  return " ".join(postfix_list)

def get_input():
  tokens = False
  while not tokens:
    print("Please enter an infix expression separated by spaces")
    infix_expr = input()
    infix_expr = str(infix_expr)
    tokens = validate_input(infix_expr)
    if tokens == False:
      print("Bad input infix expressiion, try again")
  return tokens

def validate_input(infix):
  if not infix:
    return False
  infix = infix.strip()
  parentheses = []
  for arg in infix:
    if arg == "(" or arg ==")":
      parentheses.append(arg)
  parentheses = "".join(parentheses)
  if not paren_check(parentheses):
    return False
  tokens = infix.split(" ")
  clean = []
  for tok in tokens:
    tok = tok.strip()
    clean.append(tok)
    if tok == "+" or tok == "-" or tok == "/" or tok == "*" or tok == "^":
      continue
    elif tok == "(" or tok == ")":
      continue
    elif tok.isdigit():
      continue
    else:
      return False
  return tokens

def paren_check(parentheses):
  stack = Stack()
  balanced = True
  count = 0
  while count < len(parentheses):
    if parentheses[count] == "(":
      stack.push(parentheses[count])
    else:
      if stack.is_empty():
        balaced = False
      else:
        stack.pop()
    count += 1
  if (not stack.is_empty()):
    balanced = False
  return balanced


infix = get_input()
postfix = infixtopostfix(infix)
print(postfix)

