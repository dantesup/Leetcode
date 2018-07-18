# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    def encode(self,num):
        if num==0:
            l=ListNode(0)
            return l
        else:

            l=ListNode(num%10)
            num=num//10
            p=l
            while num is not 0:
                l2=ListNode(num%10)
                p.next=l2
                num=num//10
                p=l2
        return l
    def decode(self,l):
        val=0
        count=0
        while l is not None:
            val+=l.val*10**count
            count+=1
            l=l.next
        return val
    def addTwoNumbers(self, l1, l2):
        s=Solution()
        val1=s.decode(l1)
        val2=s.decode(l2)
        l=s.encode(val1+val2)
        return l
if __name__=="__main__":
    s=Solution()
    l=s.encode(123)
    print(s.decode(l))

