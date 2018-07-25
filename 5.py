class Solution:

    def find(self,s,low,high,temp,maxlen):
        while low>= 0and high<=len(s)-1:
            if s[high]==s[low]:
                if (high-low+1)>maxlen:
                    maxlen=high-low+1
                    temp=s[low:high+1]
                low-=1
                high+=1
            else:
                break
        return temp,maxlen

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=0:
            return 0
        temp=[]
        maxlen=0
        a=Solution()
        for i,j in enumerate(s):
            temp,maxlen=a.find(s,i,i,temp,maxlen)
            temp,maxlen=a.find(s,i,i+1,temp,maxlen)
        return "".join(temp)

if __name__=="__main__":
    s=Solution()
    print(s.longestPalindrome("cbbd"))

