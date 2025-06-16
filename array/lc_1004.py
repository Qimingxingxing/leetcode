def longestOnes(nums, k):
    n = len(nums)
    max_len = 0

    for i in range(n):
        flips = 0
        for j in range(i, n):
            if nums[j] == 0:
                flips += 1
            if flips > k:
                break
            max_len = max(max_len, j - i + 1)

    return max_len
