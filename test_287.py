class Solution(object):
    def findDuplicate1(self, nums):
        """
            Time Limit Exceeded
        :type nums: List[int]
        :rtype: int
        """
        length =len(nums)
        for i in range(1,length):
            for j in range(0,i):
                if nums[i]==nums[j]:
                    return nums[i]

    def findDuplicate(self, nums):
            """
                Time Limit Exceeded
            :type nums: List[int]
            :rtype: int
            """
            length = len(nums)
            nums_count = [ 0 ] * (length-1)
            for i in range(length):
                if nums_count[nums[i]-1]==1:
                    return nums[i]
                else:
                    nums_count[nums[i]-1]=1 