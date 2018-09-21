import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

listnode = ListNode(0)
print(listnode.val)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next

class Testsolution(unittest.TestCase):
    def test1(self):
        obj=Solution() 
        print(obj.addTwoNumbers(a,a))


if __name__ == '__main__':
    unittest.main()