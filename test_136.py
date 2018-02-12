class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length= len(nums)
        for i in range(length):
            flag =False
            for j in range(length):
                if nums[i]== nums[j] and i!=j:
                    flag =True
                    break
            if not flag:
                return nums[i]
        return 0
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}
        for i in nums:
            if i in table:
                if table[i]==1:
                    table[i] =2
                elif table[i]==2:
                   table.pop(i)
                else:
                    pass
            else:
                table[i]=1 
        return table.popitem()[0]
