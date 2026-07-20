import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i in range(k):
            heapq.heappush(heap , nums[i])
        #top = heap[0]

        for i in range(k , len(nums)):
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
        return heap[0]




        