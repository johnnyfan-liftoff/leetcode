# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_link(head):
  p = head
  count = 0
  while p:
    print(p.val, end = '')
    p = p.next
    count += 1
    if count == 20:
      break
  print("")

def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if head:
      h1 = head
      h2 = head.next

    while h2:
      h1 = h1.next
      h2 = h2.next
      if h2:
        h2 = h2.next
      else:
        break
    
    h2 = h1.next
    h1.next = None
    h1 = head

    print_link(h2)

    h2new = ListNode(0, None)
    p2 = h2
    while p2:
      save = p2
      p2 = p2.next
      save.next = h2new.next
      h2new.next = save

    p1 = head
    p2 = h2new.next

    print_link(p2)

    while p2:
      p1s = p1
      p2s = p2

      p1 = p1.next
      p2 = p2.next

      p2s.next = p1s.next
      p1s.next = p2s

    return head


    
l6 = ListNode(6, None)
l5 = ListNode(5, l6)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
head = ListNode(1, l2)

h2 = reorderList(head)
print_link(h2)