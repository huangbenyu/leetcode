class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        for i in range(k):
            for j in range(1,length-i):
                if  nums[j-1]>nums[j]:
                     nums[j-1], nums[j]= nums[j],nums[j-1]

        return nums[length-k]    


testnum = [3,2,1,5,5,6,4]
k = 3
re = Solution().findKthLargest(testnum,k)
 
print("result %d th is %d"%( k,re))

