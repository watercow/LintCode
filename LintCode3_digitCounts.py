class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        # 暴力解法，一位一位的遍历。。。
        # 抽象
        res = 0
        for num in range(n+1):

            while int(num / 10) :
                if num % 10 == k:
                    res = res + 1
                num = int(num / 10)

            if num == k:
                res = res + 1

        return res


if __name__ == '__main__':
    print(Solution().digitCounts(2,302))
