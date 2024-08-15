"""
Include tests for class iterators and test that the BinaryTree
can be included in a for loop for in-order traversal
"""

class BinaryTreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.parent = None
        self._left_child = left_child
        self._right_child = right_child
        if left_child:
            left_child.parent = self
        if right_child:
            right_child.parent = self

    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, r):
        self._root = r

    def __iter__(self): # must return an InorderIterator over the tree
        # begin traveral for binarytree from root node
        return InOrderIterator(self.root)

# 'depth first' strategy for each iterator
# 'Learning Python' by Mark Lutz, 4th ed. pages711-715

# visit each node in the tree
# NeetCodeIO, Binary Tree Preorder, Postorder Traversal
# https://www.youtube.com/watch?v=QhszUQhGGlA
# https://www.youtube.com/watch?v=afTpieEZXck
# https://stackoverflow.com/questions/41622174/inorder-binary-tree-traversal-using-python
# https://www.tutorialspoint.com/python_data_structure/python_tree_traversal_algorithms.htm
# https://www.enjoyalgorithms.com/blog/iterative-binary-tree-traversals-using-stack
class PreOrderIterator:
    def __init__(self, root=None):
        self.node_list = [root] # initialize itr with list containing root

    def __iter__(self):
        return self # same for all

    def __next__(self):
        # return next element in iterations
        if not self.node_list:
            # if empty, raise stopiteration
            raise StopIteration

        while self.node_list: # iterate while stack is not empty
            # use depth first search, use pop method to return last item from node_list
            node = self.node_list.pop()
            if node:
                value = node.value
                # preorder sorted, (root, left, right)
                if node.left_child:
                    self.node_list.append(node.left_child)
                if node.right_child:
                    self.node_list.append(node.right_child)
                return value

        raise StopIteration


class PostOrderIterator:
    def __init__(self, root=None):
        self.node_list = [root]

    def __iter__(self):
        return self

    def __next__(self):
        while self.node_list:
            # process node in postorder (pop)
            node = self.node_list.pop()
            if node:
                # Postorder sorted (left, right, root)
                self.node_list.append(node.left_child)
                self.node_list.append(node.right_child)
                self.node_list.append(node)
                return node.value # return value of node

        raise StopIteration # if there are no more nodes, stop

class InOrderIterator:
    def __init__(self, root=None):
        self.node_list = []
        self.root = root

    def __iter__(self):
        return self

    def __next__(self):
        while self.node_list or self.root: # continue until empty
            # inorder sorted (left, root, right)
            while self.root: # after visiting each node, pop node
                self.node_list.append(self.root)
                self.root = self.root.left_child
            node = self.node_list.pop()
            result = node.value
            # move to the right
            self.root = node.right_child
            return result

        raise StopIteration


if __name__ == '__main__':
    n1 = BinaryTreeNode("A")
    n2 = BinaryTreeNode("B")
    n3 = BinaryTreeNode("C", n1, n2)
    n4 = BinaryTreeNode("D")
    n5 = BinaryTreeNode("E", n4, n3)
    n6 = BinaryTreeNode("F", n5)
    n7 = BinaryTreeNode("G")
    n8 = BinaryTreeNode("H", n6, n7)
    tree = BinaryTree(n8)
    print(tree.root.value)
    print(tree.root.left_child.left_child.value)
