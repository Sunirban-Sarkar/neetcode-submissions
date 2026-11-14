class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set(nums)
        return len(count)!=len(nums)
        