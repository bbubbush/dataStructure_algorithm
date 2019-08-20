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

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for w in S:
        if w == '(':
            opStack.push(w)
        elif w == ')':
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
        elif prec.get(w) == None:
            answer += w
        else:
            while not opStack.isEmpty() and prec.get(opStack.peek()) >= prec.get(w):
                answer += opStack.pop()
            opStack.push(w)
    while not opStack.isEmpty():
        answer += opStack.pop()
    return answer