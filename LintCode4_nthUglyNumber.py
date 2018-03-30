class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # 偷看了一波攻略
        # 直接寻找丑数,由定义可知,丑书是由2^m,3^n,5^l,因此不断寻找,将它们按从小到大的顺序排列,第n个即为结果。
        # 首先定义一个(数组)存放结果,
        # 使数组的第一个数ugly[0]为1,
        # 然后从ugly[0]乘以2,ugly[0]乘以3,ugly[0]乘以5中选择最小的数为新的丑数,显然ugly[1]=2。
        # 然后再从ugly[1]乘以2,ugly[0]乘以3,ugly[0]乘以5中选择最小的数为下一个丑数,即ugly[2]=3。
        # 然后再从ugly[1]乘以2,ugly[1]乘以3,ugly[0]乘以5中选择最小的数,即ugly[3]=4。
        # 以此类推,得到最终结果。
        if n == 1:
            return 1

        i = 0
        UglyNum_list = []
        backup_list = []
        UglyNum_list.append(1)

        while i != n:
            i += 1
            backup_list.append(UglyNum_list[i - 1] * 2)
            backup_list.append(UglyNum_list[i - 1] * 3)
            backup_list.append(UglyNum_list[i - 1] * 5)
            UglyNum_list.append(min(backup_list))
            # 循环删除(否则会有重复元素：如2*3 = 6 3*2 = 6)
            while UglyNum_list[i] in backup_list:
                backup_list.remove(UglyNum_list[i])

        return UglyNum_list[n-1]
