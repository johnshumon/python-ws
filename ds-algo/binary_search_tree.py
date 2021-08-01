"""Binary Search Tree module"""

from utils import bst_graph  # pylint: disable=import-error


# Definition for a binary tree node.
class Node:
    "Node structure of the tree"

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    """Solution class"""

    def insert_node(self, node: Node, key: int) -> Node:
        """Inserts a node in the tree"""
        # > Tree is empty
        # ------------------
        if node is None:
            return Node(key)

        # > Node already exists
        #   avoid duplication of keys
        # ---------------------------
        if key == node.key:
            return node

        # > Add node recursively in the sub-tree
        # --------------------------------------
        if key < node.key:
            if node.left:
                self.insert_node(node.left, key)
            else:
                node.left = Node(key)
                node.left.parent = node

        elif key > node.key:
            if node.right:
                self.insert_node(node.right, key)
            else:
                node.right = Node(key)
                node.right.parent = node

        return node

    def search_node(self, root: Node, search_key: int) -> bool:
        """Returns true if a given key exists in the tree
        false otherwise
        """
        # > Empty tree
        if root is None:
            return False

        # > Given key is found
        if root.key == search_key:
            return True

        # > Search key might be in the left subtree
        if search_key < root.key:
            if root.left:
                return self.search_node(root.left, search_key)

        # > Search key might be in the right subtree
        if search_key > root.key:
            if root.right:
                return self.search_node(root.right, search_key)

        return False

    def get_leftmost_node(self, node: Node) -> Node:
        """Returns the left most node of a given
        node if any. i.e. Returns the key with
        the minimum value.
        """
        if node is None:
            return None

        return node if node.left is None else self.get_leftmost_node(node.left)

    def get_rightmost_node(self, node: Node) -> Node:
        """Returns the right most node of a given
        node if any. i.e. Returns the key with
        the maximum value.
        """
        if node is None:
            return None

        return node if node.right is None else self.get_rightmost_node(node.right)

    def tree_height(self, node: Node) -> int:
        """Returns height of the tree if not empty.
        0 otherwise
        """

        if node is None:
            return 0

        left_height = self.tree_height(node.left)
        right_height = self.tree_height(node.right)
        return max(left_height, right_height) + 1

    def distance_from_root(self, root: Node, node: Node) -> int:
        """Returns distance between root and the
        given node.
        """
        if root.key == node.key:
            return 0

        if node.key < root.key:
            return self.distance_from_root(root.left, node) + 1

        # Else block would be unnecessary because if the above
        # condition is false it will automatically fall to the
        # below statement.
        return self.distance_from_root(root.right, node) + 1

    def distance_between_nodes(self, root: Node, node_a: Node, node_b: Node) -> int:
        """Returns distance between nodes if they exist
        in the tree.
        """
        # Calculate distance between nodes if both
        # exists in the tree.
        if self.search_node(root, node_a.key) and self.search_node(root, node_b.key):
            return self._distance_between_nodes(root, node_a, node_b)

        return 0

    def _distance_between_nodes(self, root: Node, node_a: Node, node_b: Node) -> int:
        """Helper function. Calls itself recursively to find
        LCA. Calculates and returns the distance once LCA is
        found.
        """

        # > If both nodes are either in the left or right side
        #   of the tree then root is updated to that side acco-
        #   rdingly. Here root is actually the longest common
        #   ancestor (LCA).
        # -----------------------------------------------------
        if node_a.key < root.key and node_b.key < root.key:
            return self._distance_between_nodes(root.left, node_a, node_b)

        if node_a.key > root.key and node_b.key > root.key:
            return self._distance_between_nodes(root.right, node_a, node_b)

        # > LCA is found, so return the distance.
        return self.distance_from_root(root, node_a) + self.distance_from_root(root, node_b)

    def inorder_successor(self, node: Node) -> Node:
        """Returns in-order successor of a given node
        if exists. None otherwise.
        """
        # > The successor is somewhere lower in the right subtree
        #   successor: one step right and then all the way left.
        if node.right:
            return self.get_leftmost_node(node.right)

        # > The successor is somewhere upper in the tree
        parent = node.parent
        child = node

        while parent.right == child:
            if parent.parent is None:
                return None

            child = parent
            parent = parent.parent

        return parent

    def inorder_traversal(self, node: Node) -> list:
        """Returns in-order traversal list of a given BST.
        > Traverse order: left -> root -> right
        """
        elements = []

        if node is None:
            return None

        if node.left:
            elements += self.inorder_traversal(node.left)

        elements.append(node.key)

        if node.right:
            elements += self.inorder_traversal(node.right)

        return elements

    def preorder_traversal(self, node: Node) -> list:
        """Returns pre-order traversal list of a given BST.
        > Traverse order: root -> left -> right
        """
        elements = []

        if node is None:
            return None

        elements.append(node.key)

        if node.left:
            elements += self.inorder_traversal(node.left)

        if node.right:
            elements += self.inorder_traversal(node.right)

        return elements

    def postorder_traversal(self, node: Node) -> list:
        """Returns post-order traversal list of a given BST.
        > Traverse order: left -> right -> root
        """
        elements = []

        if node is None:
            return None

        if node.left:
            elements += self.inorder_traversal(node.left)
        if node.right:
            elements += self.inorder_traversal(node.right)

        elements.append(node.key)

        return elements

    def build_tree(self, elements: list) -> list:
        """build a binary search tree with the
        given list of elements
        """
        print("build tree with these elements: {}".format(elements))

        root = Node(elements[0])
        for i in range(1, len(elements)):
            self.insert_node(root, elements[i])

        return root


def main():
    solution = Solution()

    # builds the binary search tree
    bst = solution.build_tree([20, 8, 22, 4, 12, 10, 14, 8])
    # bst = None
    # bst = solution.build_tree([17, 4, 1, 20, 9, 23, 18, 34])

    # displays the tree as a graph
    bst_graph.display(bst)

    # in, pre, and post order traversal
    print("in-order-traversal: {}".format(solution.inorder_traversal(bst)))
    print("pre-order-traversal: {}".format(solution.preorder_traversal(bst)))
    print("post-order-traversal: {}".format(solution.postorder_traversal(bst)))

    inorder_succ = solution.inorder_successor(bst.left.right)
    print(
        "in-order successor of {} is: {}".format(bst.left.right.key, inorder_succ.key)
    )

    # search key in the tree
    print("{} in the tree: {}".format(17, solution.search_node(bst, 17)))
    print("{} in the tree: {}".format(14, solution.search_node(bst, 14)))

    # get node with smallest key
    print("smallest node: {}".format(solution.get_leftmost_node(bst).key))

    # get node with largest key
    print("largest node: {}".format(solution.get_rightmost_node(bst).key))

    # get height of the tree
    print("height: {}".format(solution.tree_height(bst)))

    # get distance from root to node
    print(
        "distance between 20 and 4 is: {}".format(
            solution.distance_from_root(bst, bst.left.left)
        )
    )

    # get distance between nodes
    print(
        "distance between 14 and 22 is: {}".format(
            solution.distance_between_nodes(bst, bst.left.right.right, bst.right)
        )
    )


if __name__ == "__main__":
    main()
