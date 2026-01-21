class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = None
    
    def __str__(self):
        curr = self.head
        str = ''
        while curr is not None:
            str += f'{curr.val}, '
            curr = curr.next
            if curr.next is None:
                str += f'{curr.val}'
                return str


    def push(self, val):
        if self.length == 0:
            self.head = val
            self.tail = val
        else:
            self.tail.next = val
        self.length += 1
    
    def pop(self):
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        return temp
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

queue = Queue()

queue.push(node1)
queue.push(node2)
queue.push(node3)
queue.push(node4)
print(queue)
queue.pop()
print(queue)
