class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, node):
        # If list is empty set head and tail to node
        if self.tail is None:
            self.head = node
            self.tail = node
        # Else set tail node's next to current, and set tail of list to current node.
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    
    def prepend(self, node):
        # If list is empty set node to head and tail
        if self.head is None:
            self.head = node
            self.tail = node
        # Else set head node to current, and point current to previous head node
        else:
            node.next, self.head = self.head, node.next
        self.length += 1
    
    def remove(self, node):
        # Base case if current node is head node
        if self.head == node:
            self.head = self.head.next
            return
        # Temp vals to use for checking and deleting
        tmp = self.head.next
        tmp_prev = self.head
        # increment through list until tmp is the node you want to delete
        while tmp is not node:
            tmp_prev = tmp
            tmp = tmp.next
        # if tmp is node to delete set the previous nodes next, to skip tmp and go to the next node in list
        tmp_prev.next = tmp.next
        self.length -= 1
    
    def __str__(self):
        i = 1
        node = self.head
        str = ''
        while i <= self.length:
            # Prints without trailing comma when node is tail, else prints with comma and space
            if node == self.tail:
                str += f'{node.value}'
            else:
                str += f'{node.value}, '
            # If there is a next node, set the next node and incremement i, else break loop
            if node.next:
                node = node.next
                i += 1
            else:
                break

        return str

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
linkedList = LinkedList()
linkedList.append(node1)
linkedList.append(node2)
linkedList.append(node3)
linkedList.append(node4)
linkedList.remove(node2)
print(linkedList)