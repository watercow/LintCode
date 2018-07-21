class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        '''
        比较简单，密码学上讲过类似的方法
        给出两个数 A * B，求其末尾0的个数：做法是将A和B分别表示为素数乘积的形式，然后统计2和5的个数，因为2*5=10
        可以加快的地方是其实只用统计5的个数，因为2的个数远远比5多，可证明。
        本题类似，
        求n到1的数之间有多少个5，思路同上
        只不过有的数不止能分出一个5，如25=5*5，125=5*5*5
        所以用一个while循环遍历这种情况
        '''
        res = 0
        while n//5:
            res = res +  n//5
            n = n//5
        return res
        

if __name__ == '__main__':
    print(Solution().trailingZeros(11))
