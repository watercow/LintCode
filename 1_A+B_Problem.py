class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        """
        不考虑进位用异或 ^: No_carry = a^b
        考虑进位: carry = (a&b) << 1
        递归求解：不考虑进位的结果 + 进位 直到不再产生进位
        Memory Limit...
        """
        if not b:
            return a
        No_carry = a^b
        carry = (a&b) << 1
        return self.aplusb(No_carry,carry)

    def aplusb2(self, a, b):
        """
        递归对于负数测试错误
        C++可以通过
        Time out...
        """
        while b != 0:
            No_carry = a^b
            carry = (a&b) << 1
            a = No_carry
            b = carry
        return a

    def aplusb(self, a, b):
        """
        Python不定长的设定使得位运算模拟全加器的操作失败
        修正的方法就是模拟溢出
        参考博客:
        https://shawnhardy.me/index.php/2018/02/27/lintcode-001-a-b-wen-ti/
        """
        limit = 0xfffffffff
        while b != 0:
            a, b = (a ^ b) & limit, (a & b) << 1
        return a if a & 1 << 32 == 0 else a | (~limit)

if __name__ == '__main__':
    print(Solution().aplusb2(100,-100))
