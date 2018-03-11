from util.Utility import timeit
# TODO: 1) insert(D, x)
# TODO: 2) search(D, k)
# TODO: 3) delete(D, x)
# TODO: 4) Max(D), Min(D)
# TODO: 5) Predecessor(D,k) or Sucessor(D,k)


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None


class BST:

    def __init__(self):
        self.root = None
        self.current_root = self.root

    def insert(self, node):
        """
        Inserts a node into the bst.
        :param node: A node object
        :return: None
        """




        pass

    def search(self, key):
        """
        Searches for a particular key in the binary search tree
        :param key: key to be searched
        :return: the value of the corresponding key if found in the tree otherwise -1
        """
        if key == self.current_root.key:
            return self.current_root

        elif key > self.current_root.key:
            if self.current_root.right_child is None:
                return -1
            else:
                self.current_root = self.current_root.right_child
                self.search(key)

        else:
            if self.current_root.left_child is None:
                return -1
            else:
                self.current_root = self.current_root.left_child
                self.search(key)

    def delete(self, key):
        pass

    def max(self):
        pass

    def min(self):
        pass

    def previous(self, key):
        pass

    def next(self, key):
        pass



if __name__ == "__main__":


