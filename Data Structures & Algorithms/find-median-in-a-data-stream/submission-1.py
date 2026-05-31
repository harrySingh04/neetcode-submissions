import heapq
class MedianFinder:

    def __init__(self):
        self.left = [] # max heap for getting max element from top
        self.right = [] # min heap for getting min element from top

        

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right, num)
        

        # balance the heap

        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))


    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        else:
            return (-self.left[0] + self.right[0])/2
        
        