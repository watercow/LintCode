class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        C = []
        i = j = 0
        # 双指针遍历
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        # 将长数组剩余内容添加
        if i < len(A):
            for z in range(i,len(A)):
                C.append(A[z])
        if j < len(B):
            for z in range(j,len(B)):
                C.append(B[z])
        return C

if __name__ == '__main__':
    print(Solution().mergeSortedArray([5,7],[7]))
