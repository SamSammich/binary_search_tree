from src.node import Node


def test_node_init():
    """Testing object Node initializing correct """
    data = {'id': 40}
    node = Node(data)
    assert node.data == data
    assert node.left is None
    assert node.right is None
