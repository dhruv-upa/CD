import random
OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+':1, '-':1, '*':2, '/':2}



### INFIX ===> POSTFIX ###
def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: 
      output += stack.pop()
    #print(f'POSTFIX: {output}')
    return output



def Quadruple(pos):
    print('\nQuadruple Representation\n')
    stack = []
    op = []
    x = 1
    print(' OP  | ARG1 | ARG2 | Result')
    for i in pos:
        if i not in OPERATORS:
            stack.append(i)
        elif i == '-':
            op1 = stack.pop()
            stack.append("t(%s)" %x)
            print("{0:^4s} | {1:^4s} | {2:^4s} |{3:4s}".format(i,op1,"(-)"," t(%s)" %x))
            x = x+1
            if stack != []:
                op2 = stack.pop()
                op1 = stack.pop()
                print("{0:^4s} | {1:^4s} | {2:^4s} |{3:4s}".format("+",op1,op2," t(%s)" %x))
                stack.append("t(%s)" %x)
                x = x+1
        elif i == '=':
            op2 = stack.pop()
            op1 = stack.pop()
            print("{0:^4s} | {1:^4s} | {2:^4s} |{3:4s}".format(i,op2,"(-)",op1))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            print("{0:^4s} | {1:^4s} | {2:^4s} |{3:4s}".format(i,op2,op1," t(%s)" %x))
            stack.append("t(%s)" %x)
            x = x+1
      
def Triple(pos):
    print('Triple Representation\n')
    print('        OP  | ARG1 | ARG2')
    stack = []
    op = []
    x = 0
    for i in pos:
        if i not in OPERATORS:
            stack.append(i)
        elif i == '-':
            op1 = stack.pop()
            stack.append("(%s)" %x)
            print("{0:4s} | {1:^4s} | {2:^4s} | {3:^4s}".format("(%s)" %x,i,op1,"(-)"))
            x = x+1
            if stack != []:
                op2 = stack.pop()
                op1 = stack.pop()
                print("{0:4s} | {1:^4s} | {2:^4s} | {3:^4s}".format("(%s)" %x,"+",op1,op2))
                stack.append("(%s)" %x)
                x = x+1
        elif i == '=':
            op2 = stack.pop()
            op1 = stack.pop()
            print("{0:4s} | {1:^4s} | {2:^4s} | {3:^4s}".format("(%s)" %x,i,op1,op2))
        else:
            op1 = stack.pop()
            if stack != []:           
                op2 = stack.pop()
                print("{0:4s} | {1:^4s} | {2:^4s} | {3:^4s}".format("(%s)" %x,i,op2,op1))
                stack.append("(%s)" %x)
                x = x+1



def intrp(pos):
    print('Indirect Triple Representation\n')
    print('               OP  | ARG1 | ARG2')
    print
    stack = []
    op = []
    x = random.randrange(30,40)
    y = 0
    for i in pos:
        if i not in OPERATORS:
            stack.append(i)
        elif i == '-':
            op1 = stack.pop()
            stack.append("(%s)" %y)
            print("{0:4s} | {1:4s} | {2:^4s} | {3:^4s} | {4:^4s}".format("%s" %x,"(%s)" %y,i,op1,"(-)"))
            x = x+1
            y = y+1
            if stack != []:
                op2 = stack.pop()
                op1 = stack.pop()
                print("{0:4s} | {1:4s} | {2:^4s} | {3:^4s} | {4:^4s}".format("%s" %x,"(%s)" %y,"+",op1,op2))
                stack.append("(%s)" %y)
                x = x+1
                y = y+1
            elif i == '=':
                op2 = stack.pop()
                op1 = stack.pop()
                print("{0:4s} | {1:4s} | {2:^4s} | {3:^4s} | {4:^4s}".format("%s" %x,"(%s)" %y,i,op1,op2))
        else:
            op1 = stack.pop()
            if stack != []:           
                op2 = stack.pop()
                print("{0:4s} | {1:4s} | {2:^4s} | {3:^4s} | {4:^4s}".format("%s" %x,"(%s)" %y,i,op2,op1))
                stack.append("(%s)" %y)
                x = x+1
                y = y+1



expres = input("INPUT THE EXPRESSION: ")
pos = infix_to_postfix(expres)
Quadruple(pos)
print()
Triple(pos)
print()
intrp(pos)
