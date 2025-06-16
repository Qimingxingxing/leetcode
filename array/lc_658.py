class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        minDiff, minDiffIndex = float("inf"), 0
        for i in range(len(arr)):
            if minDiff > abs(arr[i] - x):
                minDiff = abs(arr[i] - x)
                minDiffIndex = i
        cnt = 1
        res = [arr[minDiffIndex]]
        l, r = minDiffIndex - 1, minDiffIndex + 1
        while cnt < k:
            if l < 0:
                res.append(arr[r])
                cnt += 1
                r += 1
                continue
            if r > len(arr) - 1:
                res.append(arr[l])
                cnt += 1
                l -= 1
                continue
            if abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            cnt += 1
        return sorted(res)