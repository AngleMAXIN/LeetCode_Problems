import collections

# bfs
class Solution(object):
    def levelOrder(self,root):
        if not root:
            return []
            
        queue = collections.deque()
        queue.append(root)
        result = []

        while queue:
            level_size = len(queue)
            levle_item = list()

            for _ in range(level_size):
                node = queue.popleft()
                levle_item.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(levle_item)
        
        return result

# dfx
class Solution(object):
    def levelOrder(self,root):
        if not root:
            return []

        self.result = []

        self._dfs(root,0)

        return self.result

    def _dfs(self,root,level):
        if not root:
            return 
        
        if len(self.result) < level +1:
            self.result.append([])
        self.result[level].append(root.val)
        
        self._dfs(root.right,level+1)
        self._dfs(root.left,level+1)


