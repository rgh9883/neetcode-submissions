class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A)-1
        total = len(A) + len(B)
        half = total // 2
        while True:
            m = (l + r) // 2
            n = half - m - 2
            al = A[m] if m >= 0 else float('-inf')
            ar = A[m+1] if m+1 < len(A) else float('inf')
            bl = B[n] if n >= 0 else float('-inf')
            br = B[n+1] if n+1 < len(B) else float('inf')

            if al <= br and bl <= ar:
                if total % 2 != 0:
                    # odd
                    return min(ar, br)
                return (max(al, bl) + min(ar, br)) / 2
            elif bl > ar:
                l = m + 1
            else:
                r = m - 1