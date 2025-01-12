class Solution:
    def reachNumber(self, target: int) -> int:
        # Strategy
        # a solution can be found by moving, determining the distance to target, and determining the distance to the target on the next branch either + or -
        stepCount = 0
        return 0