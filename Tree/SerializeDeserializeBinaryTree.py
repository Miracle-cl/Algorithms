# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CodecLevelOrder:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return str(res)
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')
        while res:
            if res[-1] == 'null':
                res.pop()
            else:
                break
        return '[' + ','.join(res) + ']'


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if len(data) < 3:
            return None
        arr = [None if s == 'null' else int(s) for s in data[1:-1].split(',')]
        root = TreeNode(arr[0])
        queue = [root]
        arr.pop(0)
        while queue:
            node = queue.pop(0)
            if arr:
                val = arr.pop(0)
                if val is not None:
                    node.left = TreeNode(val)
                    queue.append(node.left)
            if arr:
                val = arr.pop(0)
                if val is not None:
                    node.right = TreeNode(val)
                    queue.append(node.right)
        return root


class CodecPreOrder:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return ",".join(res)

        def preorder(root):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = iter(data.split(','))

        def recursive():
            val = next(data)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = recursive()
            node.right = recursive()
            return node

        return recursive()


class CodecLevelOrder0:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return ''
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('#')
        while res:
            if res[-1] == '#':
                res.pop()
            else:
                break
        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        # arr = [None if s == '#' else int(s) for s in data.split(',')]
        arr = iter(data.split(','))
        root = TreeNode(int(next(arr)))
        queue = [root]
        while queue:
            node = queue.pop(0)
            try:
                val = next(arr)
                if val != '#':
                    node.left = TreeNode(int(val))
                    queue.append(node.left)
            except StopIteration:
                break

            try:
                val = next(arr)
                if val != '#':
                    node.right = TreeNode(int(val))
                    queue.append(node.right)
            except StopIteration:
                break
        return root

if __name__ == "__main__":
    # Your Codec object will be instantiated and called as such:
    # codec = CodecLevelOrder()
    # # codec.deserialize(codec.serialize(root))
    # data = "[1,2,null,3,null,4,null,5]"
    # root = codec.deserialize(data)
    # res = codec.serialize(root)

    # codec = CodecPreOrder()
    # # codec.deserialize(codec.serialize(root))
    # data = "1,2,#,#,3,4,#,#,5,#,#"
    # root = codec.deserialize(data)
    # res = codec.serialize(root)

    data = '1,2,3,#,#,4,5'
    codec = CodecLevelOrder0()
    root = codec.deserialize(data)
    res = codec.serialize(root)
    assert res == data
    print(res)
8,3,1,null,null,6,4,7
