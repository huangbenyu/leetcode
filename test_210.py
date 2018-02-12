class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        relist=[]
        self.initgraph(numCourses,prerequisites)
        self.kahn(relist)
        return  relist
    
    def initgraph(self, nums, prerequisites):
        self.nums = [0]*nums
        self.adj = {}
        for edge in prerequisites:
            if len(edge) != 2:
                continue
            if edge[1] in self.adj:
                self.adj[edge[1]].append(edge[0])
            else:
                a = []
                a.append(edge[0])
                self.adj[edge[1]] = a
            self.nums[edge[0]] += 1

    def kahn(self,retunlist):
        #define zero  point
        zeropointlist = []
        
        for i in range(len(self.nums)):
            if self.nums[i] == 0:
                zeropointlist.append(i)
        
        count = 0
        while len(zeropointlist)!=0 :
            i = zeropointlist.pop()
            retunlist.append(i)
            if  i in self.adj:
                for vex in self.adj[i]:
                    self.nums[vex]-=1
                    if self.nums[vex]==0:
                        zeropointlist.append(vex)
                del self.adj[i]
            count+=1

        if count != len(self.nums):          
            return False

        return True