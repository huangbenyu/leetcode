class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        t_max = 0
        length =len(heights)

        for i in range(length):
            l_min= heights[i]
            if heights[i]>t_max:
                t_max = heights[i]
            for j in range(i+1,length):
                if heights[j]<l_min:
                    l_min = heights[j]
                if l_min*(j-i+1)> t_max:
                    t_max = l_min*(j-i+1)
        return  t_max

    def largestRectangleArea1(self, heights):
        t_max = 0
        heights.append(0)
        length = len(heights)
        t_stack = [-1]
        for i in range(length):
            while heights[i] < heights[t_stack[-1]]:
                h = heights[t_stack.pop()]
                w = i - t_stack[-1] - 1
                t_max =max (t_max, h*w)
                pass
            t_stack.append(i)
        heights.pop()
        return t_max

def main():
    mstr=[2,1,5,6,2,3]
    ret =  Solution().largestRectangleArea1(mstr)
    print (ret)


if __name__ == '__main__':
    main()