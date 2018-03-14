class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #m1=m2=0
        middle = len(nums1)+len(nums2)
        odd = True
        if middle%2==0 :
            odd =False
        middle = middle//2

        if len(nums1) <1:
            if len(nums2) <1:
               return 0
            else:
                if odd:
                    return nums2[middle]
                else:
                 return (nums2[middle-1] + nums2[middle])/2
        elif len(nums2)<1:
            if odd:
                return nums1[middle]
            else:
                return (nums1[middle-1] + nums1[middle])/2

        nums=[]
        i=j=0
       
        if nums1[0]< nums2[0]:
            nums.append(nums1[0])
            i+=1
        else:
            nums.append(nums2[0])
            j+=1

        k =1
        while i<len(nums1) or j<len(nums2):
            if i>=len(nums1):
                nums.append(nums2[j])   
                j+=1
                k+=1
                if k>=middle+1:
                    break
                else:
                    continue

            if j>=len(nums2):
                nums.append(nums1[i])   
                i+=1
                k+=1

                if k>=middle+1:
                    break
                else:
                    continue

            if nums1[i]< nums2[j]:
                nums.append(nums1[i])
                i+=1
                k+=1
            else:
                nums.append(nums2[j])
                j+=1
                k+=1

            if k>=middle+1:
                break

        print("k:%d,middle :%d" %(k,middle))
        print(nums)
        if odd:
            return nums[middle]
        else:
            return (nums[middle-1] + nums[middle])/2

def main():
    nums1=[1,2]
    nums2=[3,4]
    ret =  Solution().findMedianSortedArrays(nums1,nums2)
    print (ret)


if __name__ == '__main__':
    main()