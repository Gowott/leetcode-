
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        #1 2 3 4 5
        #f   f   f
        #s s s
asdad
        #1 2 3 4
        #f   f
        #s s

        def reverse(head):
            if not head.next:
                return head
            first = reverse(head.next)
            head.next.next = head
            head.next = None
            return first
        fast = head #回到头节点

        second_list = slow.next
        slow.next = None
        cur = reverse(second_list)

        while cur and fast:
            if cur.val == fast.val:
                cur = cur.next
                fast = fast.next
            else:
                return False
        if not cur:
            return True




# leetcode submit region end(Prohibit modification and deletion)
