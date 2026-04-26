"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
         
        if not node:
            return None
        # maintaining dict of node with its value
        clones = {node : Node(node.val)}

        q = deque([node])

        while q:
            current = q.popleft()

            for neig in current.neighbors:
                if neig not in clones:
                    q.append(neig)
                    clones[neig] = Node(neig.val)
                clones[current].neighbors.append(clones[neig])
        
        return clones[node]
        