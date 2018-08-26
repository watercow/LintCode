# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        else:
            retNode = ListNode(0)
            Node_next = retNode
            carry = 0

            # 开始遍历l1和l2进行加操作
            while(1):
                sum = 0
                if(l1):
                    sum += l1.val
                    l1 = l1.next
                if(l2):
                    sum += l2.val
                    l2 = l2.next

                val = (sum + carry) % 10
                carry = (sum + carry) // 10

                Node_next.val = val

                # 循环结束条件
                if l1 == None and l2 == None and carry == 0:
                    break
                # 生成下一个节点
                Node_next.next = ListNode(0)
                Node_next = Node_next.next

        return retNode
