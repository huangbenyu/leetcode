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
                if  remainder == 0 or num % remainder != 0:
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

"""
    Alternate implementation of self_dividing:
        def self_dividing(n):
            x = n
            while x > 0:
                x, d = divmod(x, 10)
                if d == 0 or n % d > 0:
                    return False
            return True
"""