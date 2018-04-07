class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        sorted_list = sorted(A,reverse=True)
        return sorted_list[k-1]

if __name__ == '__main__':
    print(Solution().kthLargestElement(10,[1,2,3,4,5,6,8,9,10,7]))
