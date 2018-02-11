class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        diff={}
        other={}
        for i in range(len(s)):  
            if s[i] in diff:
                if ord(s[i])-diff[s[i]]!=ord(t[i]):
                    return False
            else:
                if t[i] in other :
                    return False
                diff[s[i]] = ord(s[i])-ord(t[i])
                other[t[i]]= 1

        return True   



s ="aabbcc"
b ="ccddee"
print(list (map(s.find, s)))
print(list (map(b.find, b)))
