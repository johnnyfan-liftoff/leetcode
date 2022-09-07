# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    head = ListNode(0, None)
    p1 = list1
    p2 = list2
    p = head
    
    while p1 and p2:
      if p1.val > p2.val:
        save = p2
        p2 = p2.next

        p.next = save
        save.next = None
        p = p.next

      else:
        save = p1
        p1 = p1.next

        p.next = save
        save.next = None
        p = p.next

    if p1:
      p.next = p1
    
    if p2:
      p.next = p2
    
    return head.next

def print_link(head):
  p = head
  while p:
    print(p.val)
    p = p.next

l4 = ListNode(5, None)
l3 = ListNode(4, l4)
l2 = ListNode(2, l3)
head1 = ListNode(1, l2)

m4 = ListNode(5, None)
m3 = ListNode(4, m4)
m2 = ListNode(3, m3)
head2 = ListNode(1, m2)

a = mergeTwoLists(head1, head2)
print_link(a)