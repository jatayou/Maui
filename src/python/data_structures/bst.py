from util.Utility import timeit
# TODO: 1) insert(D, x)
# TODO: 2) search(D, k)
# TODO: 3) delete(D, x)
# TODO: 4) Max(D), Min(D)
# TODO: 5) Predecessor(D,k) or Sucessor(D,k)


class Node:

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None


class BST:

    def __init__(self, root):
        self.root = root

    def insert(self, x):
        pass

    def search(self, k):
        pass

    def delete(self, x):
        pass

    def max(self):
        pass

    def min(self):
        pass

    def previous(self, k):
        pass

    def next(self, k):
        pass



if __name__ == "__main__":


