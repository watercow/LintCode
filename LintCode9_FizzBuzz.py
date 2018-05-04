class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        list = []
        for i in range(1,n + 1):
            if not (i % 3) and (i % 5):
                list.append('fizz')
            elif not (i % 5) and (i % 3):
                list.append('buzz')
            elif not (i % 3) and not (i % 5):
                list.append('fizz buzz')
            else:
                list.append(str(i))
        return list

if __name__ == '__main__':
    print(Solution().fizzBuzz(15))
