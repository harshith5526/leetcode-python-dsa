class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        n = len(nums)
        arr = sorted((nums[i], i) for i in range(n))
        i = 0
        while i < n:
            j = i

            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1
            values = []
            indices = []

            for k in range(i, j + 1):
                values.append(arr[k][0])
                indices.append(arr[k][1])

            values.sort()
            indices.sort()

            for k in range(len(values)):
                nums[indices[k]] = values[k]

            i = j + 1

        return nums
