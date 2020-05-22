class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        l=len(A)
        m = [0]*l
        n = [0]*l
        w=0
        m[0] = A[0] 
        n[l-1]=A[l-1]
        for i in range( 1, l): 
            m[i] = max(m[i-1], A[i]) 
        for i in range(l-2, -1, -1): 
            n[i] = max(n[i + 1], A[i])
        for i in range(0, l): 
            w += min(m[i], n[i]) - A[i] 
        return w 
