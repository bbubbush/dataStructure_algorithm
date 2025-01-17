class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for w in tokenList:
        if w == '(':
            opStack.push(w)
        elif w == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        elif prec.get(w) == None:
            postfixList.append(w)
        else:
            while not opStack.isEmpty() and prec.get(opStack.peek()) >= prec.get(w):
                postfixList.append(opStack.pop())
            opStack.push(w)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList


def postfixEval(tokenList):
    stack = ArrayStack()
    prec =['+', '-', '*', '/']
    for w in tokenList:
        if not w in prec:
            stack.push(w)
        else:
            second = stack.pop()
            first = stack.pop()
            if w == '+':
                stack.push(first + second)
            elif w == '-':
                stack.push(first - second)
            elif w == '*':
                stack.push(first * second)
            elif w == '/':
                stack.push(first / second)
    
    return stack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val