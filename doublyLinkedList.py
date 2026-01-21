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
        curr = self.head
        str = ''
        # If the list head is None means there is no list return an empty string
        if not curr:
            return ''
        while curr is not None:
            if curr == self.tail:
                str += f'{curr.value}'
                return str  
            str += f'{curr.value}, '
            curr = curr.next


    def append(self, node):
        # If list is empty
        if self.length == 0:
            self.head, self.tail = node, node
            self.length += 1
        # Sets new nodes prev to the tail and sets it as the tail of the list.
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
            self.length += 1

    # get previous and next of current node and point them to each other or none if node was head or tail
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
        self.length -= 1

    # set list head prev to node, and set list head to new node
    def prepend(self, node):
        if self.length == 0:
            self.head, self.tail = node, node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1

    # if curr node is tail just append node, else set node next to curr next, next prev to node, curr next to node, node prev to curr, in order
    def insertAfter(self, curr, new):
        if curr == self.tail:
            self.tail = new
        else:
            new.next = curr.next
            new.next.prev = new
        new.prev, curr.next= curr, new
        self.length += 1

    def traversal(self):
        curr = self.head
        all = []
        while curr is not None:
            all.append(curr.value)
            curr = curr.next
        return all

    def reverseTraversal(self):
        curr = self.tail 
        all = []
        while curr is not None:
            all.append(curr.value)
            curr = curr.prev
        return all




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
dbList = DoublyLinkedList()
dbList.append(node1)
dbList.append(node2)
dbList.append(node3)
dbList.append(node4)
dbList.remove(node2)
dbList.insertAfter(node3, node5)
print(dbList)
print(node3.getNext().value)
print(node4.getPrev().value)
print(dbList.traversal())
print(dbList.reverseTraversal())
