class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hashset=set(nums)
        multiple=k
        while multiple in hashset:
            multiple+=k
        return multiple
