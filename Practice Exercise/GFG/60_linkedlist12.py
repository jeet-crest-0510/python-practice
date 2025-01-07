class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, val):

        node = Node(val)
        if self.front is None:
            self.front = node
        else:
            temp = self.front
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp

    def dequeue(self):
        if self.front is None:
            return -1
        else:
            temp = self.front
            val = temp.data
            self.front = self.front.next
            self.front.prev = None
            del temp
            return val

    def first(self):
        return self.front.data

    def size(self):
        temp = self.front
        c = 0

        while temp is not None:
            c+=1
            temp = temp.next
        
        return c

    def isempty(self):
        return self.front is None

    def printqueue(self):
        temp = self.front
        s = ''
        while temp:
            s += str(temp.data) + " "
            temp = temp.next
        print(s)

if __name__ == "__main__":
    q = Queue()

    print(f"Is Queue Empty? {q.isempty()}")
    print(f"Size of Queue: {q.size()}")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.printqueue()

    val = q.dequeue()
    q.printqueue()

    print(f"Is Queue Empty? {q.isempty()}")
    print(f"Size of Queue: {q.size()}")
    print(f"Front Element: {q.first()}")

    q.enqueue(4)
    q.enqueue(5)
    q.printqueue()
    val = q.dequeue()
    q.printqueue()