class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t_stack=[]
        for  iter in  range(0, len(s)):
            if s[iter] == '(' or s[iter] == '[' or s[iter] == '{':
                t_stack.append(s[iter])
            else:
                if s[iter] == ')':
                    if len(t_stack)<1:
                        return False
                    else:
                        if t_stack[-1]!='(':
                            return False
                        else:
                            t_stack.pop()
                elif s[iter] == '}':
                    if len(t_stack)<1:
                        return False
                    else:
                        if t_stack[-1]!='{':
                            return False
                        else:
                            t_stack.pop()
                elif s[iter] == ']':
                    if len(t_stack)<1:
                        return False
                    else:
                        if t_stack[-1]!='[':
                            return False
                        else:
                            t_stack.pop()

        return len(t_stack)==0