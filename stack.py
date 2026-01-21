class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        curr = self.head
        str = ''
        while curr is not None:
            if curr is self.tail:
                str += f'{curr.val}'
                return str
            str += f'{curr.val}, '
            curr = curr.next
    
    def push(self, node):
        node.next = self.head
        self.head = node
        if self.length == 0:
            self.tail = node
        self.length += 1
    
    def pop(self):
        self.head = self.head.next
        self.length -= 1
    
    def peek(self):
        return self.head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

stack = Stack()

stack.push(node1)
stack.push(node2)
stack.push(node3)
stack.push(node4)
print(stack.peek().val)
stack.pop()
print(stack)