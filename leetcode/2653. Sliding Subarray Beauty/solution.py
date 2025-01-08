from bisect import insort, bisect_left

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        beauties = []
        negatives = []
        for i in range(len(nums)):
            if (nums[i] < 0):
                insort(negatives, nums[i])

            if (i >= k and nums[i - k] < 0):
                negatives.pop(bisect_left(negatives, nums[i - k]))      

            if (i >= k - 1):
                if (len(negatives) >= x):
                    beauties.append(negatives[x - 1])
                else:
                    beauties.append(0)
        return beauties