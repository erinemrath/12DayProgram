def tokenizer(expr):
  if expr is None:
    return None
  expr = str(expr)
  expr = expr.strip()
  tok_list = []
  numbers = []
  for arg in expr:
    if len(numbers) >= 1:
      tok_list.append("".join(numbers))
      numbers = []
    elif arg.isdigit():
      numbers.append(arg)
      continue
    if arg == "(" or arg == ")":
      tok_list.append(arg)
    elif arg == "+" or arg == "-" or arg == "*" or arg == "/" or arg == "^":
      tok_list.append(arg)
  if len(numbers) > 0:
    tok_list.append("".join(numbers))
  return tok_list

def get_input():
  print("Enter calculator expression separated by spaces")
  expr = input()
  return expr

expr = get_input()
tokens = tokenizer(expr)
