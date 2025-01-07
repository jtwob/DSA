class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        beauties = [len(nums)-k+1]
        for i in range(0, len(nums)):
            negative_count = 0
            lowest = 0
            beauty = 0
            if(i+k <= len(nums)):
                for j in range(i, i+k):
                    print(nums[j])
                    if(nums[j] < 0):
                        negative_count+=1
                    if(nums[j] < lowest):
                        beauty = lowest
                        lowest = nums[j]
                beauties.append(beauty)                   
        return beauties
