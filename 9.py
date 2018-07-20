class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result=[]
        if x==0:
            return x
        if x>2147483647 or x<-2147483647:
            return 0
        if x<0:
            result.append("-")
            x = -x
        while x != 0:
            result.append(str(x % 10))
            x //= 10
        result=int("".join(result))
        if result>2147483647 or result<-2147483647:
            return 0
        return result
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 :
            return False
        s=Solution()
        temp=s.reverse(x)
        if temp==x:
            return  True
        else:
            return False

if __name__ =="__main__":
    s=Solution()
    print(s.isPalindrome(-0))



