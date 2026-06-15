# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        n=len(arr)
        ans=0
        left=0
        right=n-1
        while left<right:
            ans=max(ans,arr[left]+arr[right])
            left+=1
            right-=1
        return ans
        
