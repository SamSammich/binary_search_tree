from src.node import Node


class BinarySearchTree:
    def __init__(self) -> None:
        """Initialing empty Binary Search Tree """
        self.__root = None

    @property
    def root(self) -> Node | None:
        """Returning url to the top bst"""
        return self.__root

    def insert(self, data: dict) -> None:
        """Adding data to the structure Binary Search Tree"""
        if self.__root is None:
            self.__root = Node(data)
        else:
            self._insert_recursively(self.__root, data)

    def _insert_recursively(self, node: Node, data: dict):
        """recursively looking for place for putting new data"""
        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursively(node.left, data)

        if data['id'] > node.data['id']:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursively(node.right, data)

    def search(self, post_id: int) -> dict:
        """Searching and returning dictionary by his id"""
