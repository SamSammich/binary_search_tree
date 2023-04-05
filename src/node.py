class Node:
    """Class for saving data"""

    def __init__(self, data: dict) -> None:
        """Saving data initializing left and right attribute"""
        self.data = data
        self.left = None
        self.right = None
