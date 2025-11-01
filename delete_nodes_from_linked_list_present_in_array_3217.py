from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        to_remove = set(nums)

        # res = ListNode()
        # cur = res

        # while head:
        #     print(head)
        #     if head.val in to_remove:
        #         head = head.next
        #         continue
        #     else:
        #         cur.next = ListNode(head.val)
        #         cur = cur.next
        #         head = head.next
            
        # return res.next

        while head and head.val in to_remove:
            head = head.next

        cur = head

        while cur.next:

            if cur.next.val in to_remove:
                cur.next = cur.next.next
            else:
                cur = cur.next

        
        return head