class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        list = []

        for i in range(1,n + 1):
            insert = ''
            if i % 3 == 0:
                insert += 'fizz'
            if i % 5 == 0:
                insert += 'buzz'
            if i % 3 and i % 5:
                insert = str(i)
            list.append(insert)
        return list

if __name__ == '__main__':
    print(Solution().fizzBuzz(15))
