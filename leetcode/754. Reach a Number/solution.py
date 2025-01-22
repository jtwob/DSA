class Solution:
    def reachNumber(self, target: int) -> int:
        if target<0:
            target=-target
        step = 0
        sum = 0
        while(True):
            step += 1
            sum = sum+step
            if(sum == target):
                return step
            elif(sum > target and (sum-target)%2==0):
                return step