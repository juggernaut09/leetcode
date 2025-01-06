# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # BFS
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N")

        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        if data[0] == "N":
            return None

        root = TreeNode(int(data[0]))

        queue = collections.deque([root])

        index = 1
        while queue:
            node = queue.popleft()
            if data[index] != "N":
                node.left = TreeNode(int(data[index]))
                queue.append(node.left)
            index += 1
            if data[index] != "N":
                node.right = TreeNode(int(data[index]))
                queue.append(node.right)
            index += 1

        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))