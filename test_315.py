class Solution:
    #双循环
    def countSmaller1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        for i in range(0,len(nums)):
            sum = 0
            for  j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    sum +=1
            result[i]=sum
        return result


    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) // 2
            if half:
                print("half %d"% half)
                left = sort(enum[0:half])
                right = sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


def main():
    mstr=[5, 2, 6, 1]
    ret =  Solution().countSmaller(mstr)
    print (ret)


if __name__ == '__main__':
    main()