class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # [ [ 3 4 ] [ 4 6 ]]  [1 2], case 1

        # [[ 1 4 ] [ 4 6]] , [2 3] or can be [0 3]

        # [ 1 4 ] and [0 3] --> [ 0 4]
        i = 0
        n = len(intervals)

        merge_intervals = []

        # Add all before new intervals
        while i < n and intervals[i][1] < newInterval[0]:
            merge_intervals.append(intervals[i])
            i += 1

        # intervals=[[1,2],[3,5],[9,10]]
        # newInterval=[6,7]

        # a   b ,  c d for overlap a <= d  
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        merge_intervals.append(newInterval)
        
        while i < n:
            merge_intervals.append(intervals[i])
            i += 1
        

        return merge_intervals
        

                



                    
                




            
        