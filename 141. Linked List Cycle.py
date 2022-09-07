class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head:
      p1, p2 = head, head.next 
    else:
      return False

    while p2 and p2.next:
      if p1 is p2:
        return True
      else:
        p1 = p1.next
        p2 = p2.next.next            
    return False

def print_link(head):
  p = head
  while p:
    print(p.val)
    p = p.next

    

l5 = ListNode(5, None)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
head = ListNode(1, l2)

l5.next = l3


print(hasCycle(head))