class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        print(s)
        if len(nums) == len(s):
            return False
        else:
            return True