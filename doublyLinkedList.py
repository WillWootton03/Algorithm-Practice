class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        i = 1
        curr = self.head
        str = ''
        if not curr:
            return ''
        while i <= self.length:
            if curr == self.tail:
                str += f'{curr.value}'
                return str  
            str += f'{curr.value}, '
            i += 1
            curr = curr.next


    def append(self, node):
        if self.length == 0:
            self.head, self.tail = node, node
            self.length += 1
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
            self.length += 1

    def remove(self, node):
        prev = node.prev
        next = node.next
        if self.head == node:
            self.head = next
            next.prev = None
        elif self.tail == node:
            self.tail = prev
            prev.next = None
        else:
            prev.next, next.prev = next, prev




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
dbList = DoublyLinkedList()
dbList.append(node1)
dbList.append(node2)
dbList.append(node3)
dbList.append(node4)
dbList.remove(node2)
print(dbList)
print(node1.getNext().value)
print(node3.getPrev().value)
