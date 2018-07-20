
from functools import reduce


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = ['' for _ in range(numRows)]
        i = 0
        while i < len(s):
            for column in range(numRows):
                if i == len(s): break
                l[column] += s[i]
                i += 1
            for column in range(numRows)[-2:0:-1]:
                if i == len(s): break
                l[column] += s[i]
                i += 1
        print(l)
        return reduce(lambda x, y: x + y, l)


if __name__ == '__main__':
    s = Solution()
    print(s.convert('PAYPALISHIRING', 3))
    l=[1,3,5,7,9]
    print(reduce(lambda x, y: x + y, l))