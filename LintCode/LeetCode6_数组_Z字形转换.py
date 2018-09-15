class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        '''
        采用二维数组
        慢慢填充
        一次遍历填充一行中的某一个位置
        然后换到下一行
        '''
        if numRows == 1:
            return s

        # 生成有numRows行的list
        array = [[] for i in range(numRows)]
        row_num = 0
        go_direct = 1 # 1代表Z字形向下走，-1代表向上

        # 遍历填充二维数组
        for c in s:
            array[row_num].append(c)

            if row_num >= numRows - 1:
                go_direct = -1

            if row_num == 0:
                go_direct = 1

            row_num += go_direct
        # 按照Z字形构造返回字符(逐行读取array二维数组)
        res_str = ''
        for row in range(numRows):
            for c in array[row]:
                res_str += c

        return res_str

if __name__ == '__main__':
    print(Solution().convert('asdfghhj',3))