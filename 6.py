class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        if len(s)<=0:
            return 0
        create=locals()
        for i in range(numRows):
            create["row"+str(i)]=[]
        flag=0
        current=0
        j=0
        while current<len(s):
            if flag==0:
                create["row"+str(j)].append(s[current])
                if j == numRows-1:
                    flag=1
                    i = numRows - 2
                j+=1
                current += 1
            elif flag==1:
                if i==0:
                    flag=0
                    j=0
                    continue
                create["row" + str(i)].append(s[current])
                current+=1
                i-=1
                if i==0:
                    flag=0
                    j=0
        result=[]
        for i in range(numRows):
            result+=create["row"+str(i)]
        return ''.join(result)



if __name__ == "__main__":
    s=Solution()
    print(s.convert("abcd",2))