# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sum = 0
        counter = 0
        temp = head
        while head:
            counter += 1
            head = head.next
        for index in range(counter-1, -1, -1):
            sum = 2**(index)*temp.val + sum
            temp  = temp.next
        return sum
