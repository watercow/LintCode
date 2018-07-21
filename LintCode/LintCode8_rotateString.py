class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        len_str = len(str)
        # 取模用来防止溢出
        offset = offset % len_str
        if not offset:
            new_str = str
        else:
            new_str = str[len_str - offset:] + str[0:len_str - offset]
        return new_str

if __name__ == '__main__':
    print(Solution().rotateString("abcdefg",8))
