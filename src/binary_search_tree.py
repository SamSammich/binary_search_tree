from src.node import Node
class BinarySearchTree:
    def __init__(self) -> None:
        """Initialing empty Binary Search Tree """
        self.__root = None

    @property
    def root(self):
        """Returnin url to the top bst"""
        return self.__root

    def insert(self, data: dict) -> None:
        """Adding data to the structure Binary Search Tree"""
        if self.__root is None:
            self.__root = Node(data)
    def search(self, post_id: int) -> dict:
        """Searching and returning dictionary by his id"""
