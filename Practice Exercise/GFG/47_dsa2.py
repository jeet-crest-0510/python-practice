class Stack:
    def __init__(self):
        self.Element = []
    
    def push(self,val):
        self.Element.append(val)

    def pop(self):
        return self.Element.pop()
    
    def top(self):
        return self.Element[-1]
    
    def size(self):
        return len(self.Element)
    
s = Stack()
s.push('m')
s.push('a')
s.push('d')
s.push('a')
s.push('a')
s.push('m')

n = s.size()

palin = True
str=""
for i in range(n//2):
    str += s.pop()

if n%2 == 0:
    for i in range(n//2):
        if str[-1-i] != s.pop():
            palin = False
            break
else:
    s.pop()
    for i in range(n//2):
        if str[-1-i] != s.pop():
            palin = False

if palin:
    print("It is palindrome")
else:
    print("It is not a Palindrome")

