class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used_dict = {}
        start, maxLen = 0, 0
        for i, c in enumerate(s):
            if c in used_dict and start <= i and used_dict[c]>start:
                start = used_dict[c] + 1
            else:
                maxLen = max(maxLen, i - start + 1)
            used_dict[c] = i

        return maxLen


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))