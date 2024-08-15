import unittest
from binary_tree import BinaryTree, PreOrderIterator, PostOrderIterator, InOrderIterator
from binary_tree import BinaryTreeNode

class Iterator_Tests(unittest.TestCase):

    def setUp(self):
        n1 = BinaryTreeNode("A")
        n2 = BinaryTreeNode("B")
        n3 = BinaryTreeNode("C", n1, n2)
        n4 = BinaryTreeNode("D")
        n5 = BinaryTreeNode("E", n4, n3)
        n6 = BinaryTreeNode("F", n5)
        n7 = BinaryTreeNode("G")
        n8 = BinaryTreeNode("H", n6, n7)
        self.tree = BinaryTree(n8)

    def test_preorder_iterator(self):
        preorder_iterator = PreOrderIterator(self.tree.root)
        expected_output = ['H', 'G', 'F', 'E', 'C', 'B', 'A', 'D']
        self.assertEqual(list(preorder_iterator), expected_output)

    # loads forever, but says passed
    def test_postorder_iterator(self):
        postorder_iterator = PostOrderIterator(self.tree.root)
        expected_output = ['H', 'G', 'F', 'E', 'C', 'B', 'A', 'D']
        self.assertEqual(list(postorder_iterator), expected_output)

    def test_inorder_iterator(self):
        inorder_iterator = InOrderIterator(self.tree.root)
        expected_output = ['D', 'E', 'A', 'C', 'B', 'F', 'H', 'G']
        actual_output = list(inorder_iterator)
        self.assertEqual(actual_output, expected_output)

    def test_binarytree_inForLoop(self):
        expected_output = ['D', 'E', 'A', 'C', 'B', 'F', 'H', 'G']
        actual_output = []
        for value in self.tree:  # iterate over values yielded by InOrderIterator
            actual_output.append(value)
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
