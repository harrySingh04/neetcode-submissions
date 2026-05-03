class MinStack:

    # [(1,1),(2,1)]

    # push val--> check 

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        min_value = float("inf")
        if len(self.stack) > 0:
            min_value = self.getMin()

        min_value = min(val,min_value)
        self.stack.append((val,min_value))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else -1
        

    def getMin(self) -> int:
        top_pair = self.stack[-1]
        return top_pair[1]
        
