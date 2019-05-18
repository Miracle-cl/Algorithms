class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Traversal():
    def __init__(self, root):
        self.root = root
        self.preorder_list = []
        self.inorder_list = []
        self.postorder_list = []
        self.levelorder_list = []

    def pre_order(self, node):
        if node is None:
            return
        self.preorder_list.append(node.val)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def pre_order_stack(self):
        self.preorder_list.clear()
        node = self.root
        stack = []
        while stack or node:
            if node:
                self.preorder_list.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right

        print(self.preorder_list)
        self.preorder_list.clear()

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        self.inorder_list.append(node.val)
        self.in_order(node.right)

    def in_order_stack(self):
        self.inorder_list.clear()
        node = self.root
        stack = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                self.inorder_list.append(node.val)
                node = node.right

        print(self.inorder_list)
        self.inorder_list.clear()

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        self.postorder_list.append(node.val)

    def post_order_stack(self):
        self.postorder_list.clear()
        node = self.root
        stack1 = [node]
        # stack2 = []
        while (stack1):
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            self.postorder_list.append(node.val)
        self.postorder_list.reverse()
        print(self.postorder_list)
        self.postorder_list.clear()

    def level_order_queue(self):
        self.levelorder_list.clear()
        node = self.root
        queue = [node]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            self.levelorder_list.append(node.val)
        print(self.levelorder_list)
        self.levelorder_list.clear()

    def level_order_actual(self):
        # print node in every level (seperate node by level)
        import queue
        node = self.root
        result = []
        if not isinstance(node, TreeNode) or not node:
            return
        q = queue.Queue()
        q.put(node)
        result.append([node.val])
        while not q.empty():
            list = []
            while not q.empty():
                node_dequeued = q.get()
                print(node_dequeued.val, end=" ")
                if node_dequeued.left:
                    list.append(node_dequeued.left)
                if node_dequeued.right:
                    list.append(node_dequeued.right)
            print()
            level_list = [node.val for node in list]
            if level_list:
                result.append(level_list)
            for node in list:
                q.put(node)
        print(result)


if __name__ == "__main__":
    c = TreeNode('c')
    e = TreeNode('e')
    h = TreeNode('h')
    a = TreeNode('a')
    d = TreeNode('d', c, e)
    i = TreeNode('i', h)
    b = TreeNode('b', a, d)
    g = TreeNode('g', None, i)
    f = TreeNode('f', b, g)

    traversal = Traversal(f)

    traversal.pre_order_stack()
    traversal.pre_order(traversal.root)
    print(traversal.preorder_list)

    traversal.in_order_stack()
    traversal.in_order(traversal.root)
    print(traversal.inorder_list)

    traversal.post_order_stack()
    traversal.post_order(traversal.root)
    print(traversal.postorder_list)

    traversal.level_order_queue()

    traversal.level_order_actual()
