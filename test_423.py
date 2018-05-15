class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        ret = []
        ret.extend( ['0'] * dic.get('z', 0) )
        ret.extend( ['1'] * (dic.get('o', 0)-dic.get('z', 0)-dic.get('w', 0)-dic.get('u', 0)) )
        ret.extend( ['2'] * dic.get('w', 0) )
        ret.extend( ['3'] * (dic.get('h', 0)-dic.get('g', 0)) )
        ret.extend( ['4'] * dic.get('u', 0) )
        ret.extend( ['5'] * (dic.get('f', 0)-dic.get('u', 0)) )
        ret.extend( ['6'] * dic.get('x', 0) )
        ret.extend( ['7'] * (dic.get('s', 0)-dic.get('x', 0)) )
        ret.extend( ['8'] * dic.get('g', 0) )
        ret.extend( ['9'] * (dic.get('i', 0)-dic.get('g', 0)-dic.get('x', 0)-dic.get('f', 0)+dic.get('u', 0) ) )
        return ''.join( ret )