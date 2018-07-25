class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=""
        if len(strs)==0:
            return result
        length=100
        for i in strs:
            length=min(length,len(i))
        for i,j in enumerate(strs[0]):
            if i>=length:
                break
            temp=j
            for l in strs[1:]:
                if l[i]!=j:
                    return result
            result=result+temp
        return result

if __name__=="__main__":
    s=Solution()
    print(s.longestCommonPrefix(["ab","ab","ab"]))