class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = sorted(list(s))
        tt = sorted(list(t))
        return  ss == tt
        


def main():
    left = "anagram"
    right = "nagaram"
    ret =  Solution().isAnagram(left, right)
    print ("return: %d" % ret)


if __name__ == '__main__':
    main()
