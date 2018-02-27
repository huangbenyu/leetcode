class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        sumtime = 0
        laststarttime = 0
        for i in timeSeries:
            if laststarttime >0:
                if laststarttime + duration >i:
                        sumtime-=(laststarttime+duration-i)     
                sumtime+= duration
                laststarttime = i
            else:
                laststarttime = i
                sumtime+= duration
        return sumtime
                