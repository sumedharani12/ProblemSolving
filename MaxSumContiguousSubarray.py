class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        n=len(A)
        s=A[0]
        m=A[0]
        for i in range(1,n):
            s=max(A[i],s+A[i])
            m=max(m,s)
        return m
