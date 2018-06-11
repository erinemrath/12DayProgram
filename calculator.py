from tokenizer import tokenizer, get_input
from infixtopostfix import infixtopostfix, paren_check
from postfixevaluation import postfixevaluation

def calculator():
  while True:
    expr = get_input()
    tokens = tokenizer(expr)
    parentheses = []
    for tok in tokens:
      if tok == "(" or tok == ")":
        parentheses.append(tok)
    if not paren_check("".join(parentheses)):
      print ("Unmatched parentheses")
    if tokens is not None or len(tokens) > 0:
      postfix = infixtopostfix(tokens)
      evaluation = postfixevaluation(postfix)
    print("press CTRL + C to quit, else press any key to continue")
