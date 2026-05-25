from typing import Optional


class ListNode:
    def __init__(self, val: int, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next


# Detect whether a linked list contains a cycle using Floyd's two-pointer
# (tortoise and hare) algorithm. A slow pointer advances one node at a time
# while a fast pointer advances two; if they ever meet, a cycle exists.
# Time complexity: O(n)
# Space complexity: O(1)
def has_cycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Find the node where the cycle begins in a linked list, or None if there
# is no cycle. Once the tortoise and hare meet inside the cycle, resetting
# one pointer to the head and advancing both one step at a time guarantees
# they meet exactly at the cycle's entry node.
# Time complexity: O(n)
# Space complexity: O(1)
def find_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
