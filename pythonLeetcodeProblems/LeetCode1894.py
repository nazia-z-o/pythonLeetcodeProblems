class Solution:
    def BinarySearch(self, arr, s, e, k) -> int:
        if s > e:
            return 0
        if s == e and arr[s] > k:
            return s
        mid = int(s + (e - s) / 2)

        if arr[mid] == k:
            return mid + 1
        elif arr[mid] > k:
            return self.BinarySearch(arr, s, mid, k)
        return self.BinarySearch(arr, mid + 1, e, k)

    def chalkReplacer(self, chalk, k) -> int:
        n = len(chalk)
        if n == 1:
            return 0
        presum = [0] * n
        presum[0] = chalk[0]
        for i in range(1, n):
            presum[i] = presum[i - 1] + chalk[i]
        while presum[n - 1] <= k:
            k -= presum[n - 1]
        if k == 0:
            return 0
        # print(k)
        ix = self.BinarySearch(presum, 0, n - 1, k)
        if ix == n:
            return 0
        return ix
