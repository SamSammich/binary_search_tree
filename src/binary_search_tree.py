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
        if self.__root is not None:
             return  self._search_recursively(self.__root, post_id)

    def _search_recursively(self, node: Node, data_id: int) -> dict | None:
        """Ищем рекурсивно данные и возвращаем, если наши, иначе None."""
        if data_id == node.data['id']:
            return node.data
        if data_id < node.data['id']:
            if node.left is None:
                return None
            else:
                return self._search_recursively(node.left, data_id)
        if data_id > node.data['id']:
            if node.right is None:
                return None
            else:
                return self._search_recursively(node.right, data_id)
