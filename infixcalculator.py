from infixtopostfix import infixtopostfix
from infixtopostfix import get_input
from postfixevaluation import postfixevaluation

def infixcalculator(infix):
  postfix = infixtopostfix(infix)
  answer = postfixevaluation(postfix)
  return answer

infix = get_input()
answer = infixcalculator(infix)
print(answer)
