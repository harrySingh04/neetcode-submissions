class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # [ [ 3 4 ] [ 4 6 ]]  [1 2], case 1

        # [[ 1 4 ] [ 4 6]] , [2 3] or can be [0 3]

        # [ 1 4 ] and [0 3] --> [ 0 4]

        merge_interval = []
        is_new_inserted = False
 
        for current in intervals:
            # case 1: current [0] > newInterval[1] , newinterval  is before can be inserted now
            # case 2: current[1] < newInterval[0] , then new interval is after the current
            # case 3 : overlap: get minimum of first tuple and maximum of second tuple

            if not is_new_inserted and newInterval[0] <= current[1]:
                if current[0] > newInterval[1]:
                    merge_interval.append(newInterval)
                    merge_interval.append(current)
                else:
                    first = min(current[0], newInterval[0])
                    second = max(current[1] , newInterval[1])
                    merge_interval.append((first,second))
                
                is_new_inserted = True
            elif is_new_inserted:
                last = merge_interval[-1]
                if last[1] >= current[0]:
                    merge_interval[-1] = (last[0], max(last[1], current[1]))
                else:
                    merge_interval.append(current)
            else:
                merge_interval.append(current)

        
        if not is_new_inserted:
            merge_interval.append(newInterval)
        

        return merge_interval
        

                



                    
                




            
        