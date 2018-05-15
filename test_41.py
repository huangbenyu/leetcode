class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        missingmin = 1
        for i in nums:
            if i>0:
                if missingmin == i:
                    missingmin+=1
                else:
                    break
        return missingmin