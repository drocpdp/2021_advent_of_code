from day_util import DayUtil
from collections import Counter

class LL:
    def __init__(self, val=None):
        self.next = None
        self.val = val

def get_data():
    data = DayUtil().open_file("day14_test")
    initial = data[0]
    template = {fr.strip():to.strip() for (fr,to) in [data[i].split("->") for i in range(2, len(data))]}
    return (initial,template)

def testLL(head):
    ll = []
    node = head
    while node:
        ll.append(node.val)
        node = node.next
    print(ll)
        

def day14():
    polymer, template = get_data()
    head = LL(-1)
    curr = head
    for p in polymer:
        curr.next = LL(p)
        curr = curr.next

    for _ in range(4):
        ptr1 = head.next
        ptr2 = ptr1.next
        while ptr1.next:
            insertion = LL(template[ptr1.val+ptr2.val])
            ptr1.next = insertion
            insertion.next = ptr2
            ptr1 = ptr2
            ptr2 = ptr1.next
    testLL(head)





print(day14())