class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        @使用双指针的方法遍历
        :type s: str
        :rtype: int
        """
        lenths = len(s)
        maxlen = 0
        str_list = []
        lencur = 0

        # 头指针
        i = 0
        # 尾指针
        j = 0

        while i < lenths and j < lenths:
            if s[j] not in str_list:
                str_list.append(s[j])
                lencur += 1
                j += 1
            else:
                while s[j] in str_list:
                    str_list.remove(s[i])
                    i += 1
                    lencur -= 1
            maxlen = max(maxlen, lencur)
        return maxlen
