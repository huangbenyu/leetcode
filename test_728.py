class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for  num in  range(left, right):
            flag = True
         
            consult = num
            while consult> 0:
                consult, remainder = divmod(consult, 10)
                if  remainder == 0 or consult % remainder != 0:
                    flag = False
                    break
            if flag:
                 result.append(num)
        
        return  result

def main():
    left = 1
    right = 22+1
    ret =  Solution().selfDividingNumbers(left, right)
    print (ret)


if __name__ == '__main__':
    main()