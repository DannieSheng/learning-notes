# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     custom_cell_magics: kql
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Linked List

# %%
from typing import Optional


# %% [markdown]
# ### Singly Linked List

# %%
class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next  = next


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        node = ListNode(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    @staticmethod
    def printList(head):
        if not head:
            print("empty")
        else:
            curr = head
            while curr:
                ending = "." if not curr.next else "->"
                print(curr.value, end=ending)
                curr = curr.next
        print("\n")


    @staticmethod
    def create_linked_list_with_cycle(values, pos):
        if not values:
            return None

        nodes = [ListNode(val) for val in values]

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        if pos != -1:  # pos = -1 means no cycle
            nodes[-1].next = nodes[pos]

        return nodes[0]

    @staticmethod
    def print_linked_list(head):
        current = head
        visited = set()

        while current:
            if current in visited:
                print("Cycle detected!")
                break

            print(current.value, end=" -> ")
            visited.add(current)
            current = current.next

        print("None")


# %% [markdown]
# ### Challenges

# %% [markdown]
# #### 总结：
# 1. 求链表的中间节点后者求链表的倒数第k个节点，都是用快慢指针来解决；
# 2. 链表排序，一般使用归并排序来解决；
# 3. 如果操作可能会改变链表的表头，应该声明指向链表head的dummy节点，最后返回dummy.next；

# %%
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre   
    
    def split(self, head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        """ 
        Split the list from middle
        even: the splitted lists have the same length
        odd: the 2nd list is longer
        """
        slow, fast = head, head
        while fast and fast.next and fast.next.next and fast.next.next.next:
            slow = slow.next
            fast = fast.next.next
        post_list = slow.next
        slow.next = None
        return head, post_list

    def mergeTwoSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        dummy = ListNode(-1, None)
        p = dummy
        while cur1 and cur2:
            if cur1.value <= cur2.value:
                p.next = cur1
                p = p.next
                cur1 = cur1.next
            else:
                p.next = cur2
                p = cur2
                cur2 = cur2.next
        if cur1:
            p.next = cur1
        if cur2:
            p.next = cur2
        return dummy.next
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        dummy = ListNode(-1, None)
        p = dummy

        while cur1 and cur2:
            p.next = cur1
            p = p.next
            cur1 = cur1.next
            p.next = cur2
            p = p.next
            cur2 = cur2.next
        if cur1:
            p.next = cur1
        if cur2:
            p.next = cur2
        return dummy.next
    
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        head1, head2 = list1, list2
        while head1:
            num1 = num1*10 + head1.value
            head1 = head1.next
        while head2:
            num2 = num2*10 + head2.value
            head2 = head2.next

        dummy = ListNode(-100)
        p = dummy
        for i in str(num1 + num2):
            p.next = ListNode(i)
            p = p.next
        return dummy.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        pre, post = self.split(head)
        SinglyLinkedList.printList(pre)
        SinglyLinkedList.printList(post)
        post = self.reverseList(post)
        SinglyLinkedList.printList(post)
        return self.mergeTwoLists(pre, post)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow, fast = dummy, head
        for i in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pre, post = self.split(head)
        post = self.reverseList(post)
        p1, p2 = pre, post
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
    
    def sortList(self, head):
        """
        Merge Sort
        """
        if not head or not head.next:
            return head
        pre, post = self.split(head)
        pre = self.sortList(pre)
        post = self.sortList(post)
        return self.mergeTwoSortedLists(pre, post)
    

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None



# %% [markdown]
# #### [206](https://leetcode.com/problems/reverse-linked-list/description/). Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# %%
linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

sol = Solution()
reversed_list = sol.reverseList(linked_list.head)
SinglyLinkedList.printList(reversed_list)

# %% [markdown]
# #### [876](https://leetcode.com/problems/middle-of-the-linked-list/description/). Find the middle of the Linked List and Split into Two

# %%
linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
SinglyLinkedList.printList(linked_list.head)

sol = Solution()
pre, mid = sol.split(linked_list.head)
SinglyLinkedList.printList(pre)
SinglyLinkedList.printList(mid)
print(f"\n{mid.value}")

# %%
linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
SinglyLinkedList.printList(linked_list.head)
pre, mid = sol.split(linked_list.head)
SinglyLinkedList.printList(pre)
SinglyLinkedList.printList(mid)
print(f"\n{mid.value}")

# %% [markdown]
# #### [21](https://leetcode.com/problems/merge-two-sorted-lists/description/). Merge Two Sorted Lists
# You are given the heads of two sorted linked lists `list1` and `list2`.
# Merge the two lists into one sorted list.   
# The list should be made by splicing together the nodes of the first two lists.  
# Return the _head of the merged linked list_.

# %%
linked_list1, linked_list2 = SinglyLinkedList(), SinglyLinkedList()
for v in range(1, 6):
    linked_list1.append(v)
SinglyLinkedList.printList(linked_list1.head)

for v in range(2, 5):
    linked_list2.append(v)
SinglyLinkedList.printList(linked_list2.head)

sol = Solution()
merged_list = sol.mergeTwoSortedLists(linked_list1.head, linked_list2.head)
SinglyLinkedList.printList(merged_list)

# %% [markdown]
# #### [445](https://leetcode.com/problems/add-two-numbers-ii/description/). Add Two Numbers II
# You are given two **non-empty** linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# %%
linked_list1, linked_list2 = SinglyLinkedList(), SinglyLinkedList()
for v in range(1, 6):
    linked_list1.append(v)
SinglyLinkedList.printList(linked_list1.head)

for v in range(2, 5):
    linked_list2.append(v)
SinglyLinkedList.printList(linked_list2.head)

sol = Solution()
added_list = sol.addTwoNumbers(linked_list1.head, linked_list2.head)
SinglyLinkedList.printList(added_list)

# %% [markdown]
# #### [143](https://leetcode.com/problems/reorder-list/description/). Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
#
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# %%
linked_list = SinglyLinkedList()
for v in range(1, 6):
    linked_list.append(v)
SinglyLinkedList.printList(linked_list.head)

sol = Solution()
reordered_list = sol.reorderList(linked_list.head)
SinglyLinkedList.printList(reordered_list)

# %% [markdown]
# #### [19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/). Remove Nth Node From End of List
# Given the `head` of a linked list, remove the $n^{th}$ node from the end of the list and return its head.

# %%
linked_list = SinglyLinkedList()
for v in range(1, 6):
    linked_list.append(v)
SinglyLinkedList.printList(linked_list.head)

sol = Solution()
reordered_list = sol.removeNthFromEnd(linked_list.head, n=2)
SinglyLinkedList.printList(reordered_list)

# %% [markdown]
# #### [234](https://leetcode.com/problems/palindrome-linked-list/description/). Palindrome Linked List
# Given the `head` of a singly linked list, return `true` if it is a _palindrome_ or `false` otherwise.
# - A palindrome is a sequence that reads the same forward and backward.

# %%
linked_list = SinglyLinkedList()
for v in [1, 2, 3, 2, 1]:
    linked_list.append(v)

sol = Solution()
sol.isPalindrome(linked_list.head)

# %%
linked_list = SinglyLinkedList()
for v in [1, 2, 3, 3, 1]:
    linked_list.append(v)

sol = Solution()
sol.isPalindrome(linked_list.head)

# %%
linked_list = SinglyLinkedList()
for v in [1, 2, 3, 3, 2, 1]:
    linked_list.append(v)

sol = Solution()
sol.isPalindrome(linked_list.head)

# %% [markdown]
# #### [148](https://leetcode.com/problems/sort-list/). Sort List
# Given the `head` of a linked list, return the list after sorting it in ascending order.

# %%
linked_list = SinglyLinkedList()
for v in [1, 2, 3, 3, 2, 1]:
    linked_list.append(v)

sol = Solution()
sorted_list = sol.sortList(linked_list.head)

SinglyLinkedList.printList(sorted_list)

# %% [markdown]
# #### [142](https://leetcode.com/problems/linked-list-cycle-ii/description/). Linked List Cycle II
# Given the `head` of a linked list, return _the node where the cycle begins_. If there is no cycle, return `null`.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
#
# Do not modify the linked list.

# %%
linked_list = SinglyLinkedList.create_linked_list_with_cycle([3, 2, 0, -4], 1)
SinglyLinkedList.print_linked_list(linked_list)

# %%
sol = Solution()
sol.detectCycle(linked_list)


# %% [markdown]
# ### Doubly Linked List

# %%
class ListNode(object):
    def __init__(self, value=0):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def printList(self):
        if not self.head:
            print("empty")
        else:
            curr = self.head
            
            while curr:
                ending = "." if not curr.next else "->"
                print(curr.value, end=ending)
                curr = curr.next

    def append(self, val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.length += 1

    def prepend(self, val):
        if self.head is None:
            self.append(val)
        else:
            node = ListNode(val)
            temp = self.head
            
            node.next = temp
            temp.prev = node
            self.head = node
            self.length += 1
            # print("xxxx", self.length)

    def insert(self, index, val):
        if index > self.length:
            print("Out of range, end...")
        elif index == self.length:
            self.append(val)
        elif index == 0:
            self.prepend(val)
        else:
            curr = self.head
            node = ListNode(val)
            for i in range(index-1):
                curr = curr.next
            temp = curr.next

            node.next = temp
            node.prev = curr
            curr.next = node
            temp.prev = node
            self.length += 1

    def remove_by_index(self, index):
        if index >= self.length:
            print("Out of range, end...")
        elif index == 0:
            curr = self.head
            self.head = curr.next
            self.length -= 1
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            prev = curr.prev
            next = curr.next
            prev.next = next
            if next is not None:
                next.prev = prev
            self.length -= 1

