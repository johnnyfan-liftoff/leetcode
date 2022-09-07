# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    h2 = ListNode(0, None)
    p = head
    while p:
      post = p.next
      save = h2.next
      h2.next = p
      p.next = save
      p = post
    return h2.next


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


print_link(head)
print("---")
h2 = reverseList(head)
print_link(h2)






    