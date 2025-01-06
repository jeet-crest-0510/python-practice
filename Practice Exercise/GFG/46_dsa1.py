class Stack:
    def __init__(self):
        self.Element = []
    
    def push(self,val):
        self.Element.append(val)

    def pop(self):
        return self.Element.pop()
    
    def isEmpty(self):
        return self.Element == []
    
    def print(self):
        for i in self.Element[::-1]:
            print(i)

    def reverse(s):
        s1 = Stack()
        while not s.isEmpty():
            popElement = s.pop()
            s1.push(popElement)
        s.Element = s1.Element


s = Stack()
print("Original Stack: ")
s.push(5)
s.push(3)
s.push(7)
s.print()

print("Reversed Stack: ")
s.reverse()
s.print()