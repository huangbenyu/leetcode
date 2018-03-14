import collections
class DSU:
    def __init__(self):
        self.p = list(range(10001))
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        if len(accounts)<1:
            return []
        em_name = {}
        em_id = {}
        df = DSU()
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_name[email] = name
                if email not in em_id:
                    em_id[email] =i
                    i+=1
                df.union(em_id[acc[1]], em_id[email])
        result = collections.defaultdict(list)
        for  email in em_name:
            result[df.find(em_id[email])].append(email) 
                
        return [[em_name[v[0]]] + sorted(v) for v in result.values()]


     
def main():
    account=[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    ret =  Solution().accountsMerge(  account  )
    print (ret)


if __name__ == '__main__':
    main() 