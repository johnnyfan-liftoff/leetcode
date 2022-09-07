class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_link(head):
  p = head
  while p:
    print(p.val, end = '')
    p = p.next
  print("")

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    nh = ListNode(0, head)
    s, f = nh, nh
    for i in range(n):
      f = f.next
    
    pre = s
    while f:
      f = f.next
      pre = s
      s = s.next
    
    pre.next = s.next

    return nh.next
    


l6 = ListNode(6, None)
l5 = ListNode(5, l6)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
head = ListNode(1, l2)

h2 = removeNthFromEnd(head, 3)
print_link(h2)