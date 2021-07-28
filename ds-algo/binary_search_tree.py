"""Binary Search Tree module"""


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
        """inserts node in the tree"""
        # > tree is empty
        # ------------------
        if node is None:
            return Node(key)

        # > node already exists
        #   avoid duplication of keys
        # ---------------------------
        if key == node.key:
            return node

        # > add node recursively in the sub-tree
        # --------------------------------------
        elif key < node.key:
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
        """returns true if a given node is in the tree
        false otherwise
        """
        if root.key == search_key:
            return True

        # > search key might be in the left subtree
        if search_key < root.key:
            if root.left:
                return self.search_node(root.left, search_key)
            else:
                return False

        # > search key might be in the right subtree
        if search_key > root.key:
            if root.right:
                return self.search_node(root.right, search_key)
            else:
                return False

        return False

    def get_leftmost_node(self, node: Node) -> Node:
        """Returns the left most node of a
        given node if any. i.e. return the key
        with minimum value.
        """
        return node if node.left is None else self.get_leftmost_node(node.left)

    def get_rightmost_node(self, node: Node) -> Node:
        """Returns the right most node of a
        given node if any. i.e. return the key
        with maximum value.
        """
        return node if node.right is None else self.get_rightmost_node(node.right)

    def inorder_successor(self, node: Node) -> Node:
        """returns in-order successor of a given node
        if exists. None otherwise.
        """
        # > the successor is somewhere lower in the right subtree
        #   successor: one step right and then all the way left.
        if node.right:
            return self.get_leftmost_node(node.right)

        # > the successor is somewhere upper in the tree
        parent = node.parent
        child = node

        while parent.right == child:
            if parent.parent is None:
                return None

            child = parent
            parent = parent.parent

        return parent

    def inorder_traversal(self, node: Node) -> list:
        """returns in-order traversal list of a given BST.
        traverse order: left -> root -> right
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
        """returns pre-order traversal list of a given BST.
        traverse order: root -> left -> right
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
        """returns post-order traversal list of a given BST.
        traverse order: left -> right -> root
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
    # bst = solution.build_tree([20, 8, 22, 4, 12, 10, 14, 8])
    bst = solution.build_tree([17, 4, 1, 20, 9, 23, 18, 34])

    # displays the tree as a graph
    display(bst)

    # in, pre, and post order traversal
    print("in-order-traversal: {}".format(solution.inorder_traversal(bst)))
    print("pre-order-traversal: {}".format(solution.preorder_traversal(bst)))
    print("post-order-traversal: {}".format(solution.postorder_traversal(bst)))

    inorder_succ = solution.inorder_successor(bst.left.right)
    print("in-order successor of {} is: {}".format(bst.left.right.key, inorder_succ.key))

    # search key in the tree
    print("{} in the tree: {}".format(17, solution.search_node(bst, 17)))
    print("{} in the tree: {}".format(2, solution.search_node(bst, 2)))

    # get node with smallest key
    print("smallest node: {}".format(solution.get_leftmost_node(bst).key))

    # get node with largest key
    print("largest node: {}".format(solution.get_rightmost_node(bst).key))


# dirty hack copied from stackoverflow
# to display the BST as a graph.
# ref: https://stackoverflow.com/a/54074933/1453339
def display(node):
    """Display BST as a graph like we draw
    using pen and paper.
    """
    lines, *_ = display_aux(node)
    for line in lines:
        print(line)


def display_aux(node):
    """Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.right is None and node.left is None:
        line = "%s" % node.key
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right is None:
        lines, n, p, x = display_aux(node.left)
        s = "%s" % node.key
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s
        second_line = x * " " + "/" + (n - x - 1 + u) * " "
        shifted_lines = [line + u * " " for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left is None:
        lines, n, p, x = display_aux(node.right)
        s = "%s" % node.key
        u = len(s)
        first_line = s + x * "_" + (n - x) * " "
        second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
        shifted_lines = [u * " " + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = display_aux(node.left)
    right, m, q, y = display_aux(node.right)
    s = "%s" % node.key
    u = len(s)
    first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
    second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
    if p < q:
        left += [n * " "] * (q - p)
    elif q < p:
        right += [m * " "] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


if __name__ == "__main__":
    main()


# take print function to a separate module
# add height funciton
