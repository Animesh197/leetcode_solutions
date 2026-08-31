# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head is None or head.next is None:
            return [-1,-1]

        p = head
        c = head.next

        pos = 1
        first = -1
        last = -1

        mn = float('inf')

        while c.next is not None:
            n = c.next

            if (c.val>p.val and c.val>n.val) or (c.val < p.val and c.val<n.val):
                if first == -1:
                    first = pos
                else:
                    distance = pos - last
                    mn = min(mn, distance)
                last = pos
            p = c
            c = n
            pos +=1

        if first == last:
            return [-1,-1]

        mx = last - first

        return [mn, mx]