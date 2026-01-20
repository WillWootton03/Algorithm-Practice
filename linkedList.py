class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

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
    
    def insertAfter(self, curr, new):
        if self.head is None:
            self.head, self.tail = new
        elif curr == self.tail:
            curr.next, self.tail = new
        else:
            new.next = curr.next
            curr.next = new
        self.length += 1

    def find(self, val):
        # Checks base cases making search O(1) if node is head or tail
        if self.head.value == val:
            return self.head
        if self.tail.value == val:
            return self.tail
        
        i = 1
        # Because base case check we know it cant be head
        curr = self.head.next
        while i < self.length:
            if curr.value == val:
                return curr
            else:
                # Increment curr and i if val not found
                curr= curr.next
                # We know it can't be tail so if after moving curr its tail it has to be none meaning we can stop loop before it happens
                if curr == self.tail:
                    return None
                i += 1


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
node5 = Node(5)
linkedList.insertAfter(node3, node5)
print(linkedList)
# Catch so no error happens if you dont find a node
if linkedList.find(2):
    print(linkedList.find(2).value)