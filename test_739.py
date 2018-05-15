class Solution:
    def dailyTemperatures1(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        num = len(temperatures)
        re = [0]*num
        for i in range(0,num):
            day = 0
            for  j in range(i+1,num):
                if temperatures[i]<temperatures[j]:
                    day = j-i
                    break
            re[i]=day
        return re

    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        num = len(temperatures)
        re = [0]*num
        stack =[0]
        for i in range(1,num):
            while len(stack)>0 and temperatures[stack[-1]]<temperatures[i]:
                re[stack[-1]] = i-stack[-1]
                stack.pop()
            else:
                stack.append(i)      
        return re
def main():
    mstr=[73, 74, 75, 71, 69, 72, 76, 73]
    ret =  Solution().dailyTemperatures(mstr)
    print (ret)


if __name__ == '__main__':
    main()