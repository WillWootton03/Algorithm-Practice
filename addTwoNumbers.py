class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def addToNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy

    # if added number is over 10 set a carry var 
    carry = 0
    # While either listNode is available or there is a carry to add
    while l1 or l2 or carry:
        # Sets either var to listnode var or to 0 if there is no node
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # new digit
        # adds all digits plus a prev carry
        val = v1 + v2 + carry
        # carry is 1 or 0 depending on 2 numbers added then divided by ten floored
        carry = val // 10
        # if val is > 10 mod it to be just 1's digit
        val = val % 10
        curr.next = ListNode(val)

        # update
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next
