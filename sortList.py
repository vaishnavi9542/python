class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr.sort()

        dummy = ListNode(0)
        temp = dummy

        for val in arr:
            temp.next = ListNode(val)
            temp = temp.next

        return dummy.next
