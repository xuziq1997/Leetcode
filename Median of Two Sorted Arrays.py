'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
'''

class Solution:

    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(A);
        m = len(B);
        ## n>=m: keep it n<m change it

        if n < m:
            A, B, n, m = B, A, m, n

        j = 0

        for i in range(m):
            while (j < n and A[j] < B[i]):
                j += 1

            if j == n:
                A.append(B[i])
                n += 1
                j -= 1

            if B[i] <= A[j]:
                A.insert(j, B[i])
                n += 1
                j += 1

        if n % 2 == 1:
            return A[n // 2]

        return ((float)(A[n // 2] + A[(n // 2) - 1]) / 2)

test = Solution()
print(test.findMedianSortedArrays([1,3], [2,4]))