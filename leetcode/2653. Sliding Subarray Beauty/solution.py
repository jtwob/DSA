class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        for i in range(0, len(nums)):
            if(i+k <= len(nums)):
                for j in range(i, i+k):
                    print(nums[j])