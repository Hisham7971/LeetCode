# Definition for singly-linked list.
from math import ceil


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head): #Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head)
            head = head.next
        return arr[ceil((len(arr)-1)/2 )]
    
#********************************************************


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head): #Optional[ListNode]) -> Optional[ListNode]:
        valList = {}
        i=0
        while head:
            valList[i] = head
            head=head.next
            i+=1
        mid = len(valList)//2
        return list(valList.values())[mid]