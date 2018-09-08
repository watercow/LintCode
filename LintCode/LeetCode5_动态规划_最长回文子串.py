class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        1.动态规划 O(n^2)
        若，矩阵p[i][j]表示以i开始以j结束的子串是回文串
        则p[i+1][j-1]也是回文字符串
        
        dp[i][j] = (s[i] == s[j] && dp[i+1][j-1] == true)
        1: true
        0: false
        '''
        str_len = len(s)

        if str_len == 0:
            return ""
        if str_len == 1:
            return s

        # 生成dp二维数组
        dp = [[0]*str_len for i in range(str_len)]

        max_len = 1 # 当前最长子串的长度
        start_point = 0 # 最长子串的起始位置

        # 初始化dp
        for i in range(str_len):
            dp[i][i] = 1
            if i+1 <= str_len -1 and s[i] == s[i+1]:
                dp[i][i+1] = 1
                max_len = 2
                start_point = i

        # 开始规划最长子串
        for lenths in range(3,str_len + 1):

            for i in range(str_len - lenths + 1):

                j = i + lenths - 1

                if dp[i+1][j-1] == 1 and s[i] == s[j]:

                    dp[i][j] = 1

                    if lenths > max_len:
                        max_len = lenths
                        start_point = i

        return s[start_point : start_point + max_len]
        '''
        2.中心扩展 O(n^2)
        '''

        '''
        3.Manacher算法 O(n)
        '''

if __name__ == '__main__':
    print(Solution().longestPalindrome('ddd'))
