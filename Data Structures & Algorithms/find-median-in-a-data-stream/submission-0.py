import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):

        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)

        else:
            heapq.heappush(self.large, num)
        
        if len(self.small) > len(self.large) + 1 :
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)
        
        elif len(self.large) > len(self.small) + 1 :
            value = heapq.heappop(self.large)
            heapq.heappush(self.small , -value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]        
        
        elif len(self.large) > len(self.small):
            return self.large[0]

        else:
            return (self.large[0] - self.small[0])/2   