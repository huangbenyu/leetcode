class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.find_substr_max(s,0,len(s))
      
    def find_substr_max(self, s, startpos,endpos):
        flag, maxlen,flp = self.find_max(s,startpos,endpos)
        print("startpos %d, endpos %d,reuslt %s, maxlen %d, flp %d" \
        %(startpos,endpos,flag, maxlen, flp))
        if flag:
            return maxlen
        else:
            maxlen1 = self.find_substr_max(s, startpos,flp)
            maxlen2 = self.find_substr_max(s, flp+1,endpos)
            if maxlen1 >= maxlen2:
                return maxlen1
            else:
                return maxlen2

    def find_max(self, s, startpos,endpos):
        if startpos>=endpos:
            return True ,0,0
        firstleftparenthesepos = -1
        t_stack = []
        maxlen = 0
        t_len = 0
        for  iter in  range(startpos, endpos):
            if s[iter] == '(':
                if len(t_stack)<1:
                    firstleftparenthesepos = iter
                    t_len = 0
                t_stack.append(s[iter])
            if s[iter] == ')':
                if len(t_stack)>0:
                    t_len += 2
                    t_stack.pop()
                else:
                    firstleftparenthesepos =-1
                    t_stack = []
                    if  t_len > maxlen:
                        maxlen = t_len
                    t_len = 0

        if t_len > maxlen:
            maxlen = t_len
                        

        if len(t_stack) < 1 :
            return True, maxlen,firstleftparenthesepos
        else:
            return False, maxlen, firstleftparenthesepos


def main():
    mstr="()()"
    #mstr=")()("
    ret =  Solution().longestValidParentheses(mstr)
    print (ret)


if __name__ == '__main__':
    main()