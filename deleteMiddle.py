# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        curr=head
        arr=[]
        while curr:
            arr.append(curr)
            curr=curr.next
        mid=len(arr)//2
        arr[mid-1].next=arr[mid].next
        return head
        
