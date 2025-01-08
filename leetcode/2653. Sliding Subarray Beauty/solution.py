class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        beauties = []
        for i in range(0, len(nums)-k+1):
            negatives = []
            for j in range(i, i+k):
                print(nums[j])
                if(nums[j] < 0):
                    negatives.append(nums[j])
            if(len(negatives) >= x):
                negatives.sort()
                beauties.append(negatives[x-1])
            else:
                beauties.append(0)                   
        return beauties