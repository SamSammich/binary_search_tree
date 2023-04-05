from src.binary_search_tree import BinarySearchTree


def tes_bst_empty():
    """Empty binary search tree"""
    bst = BinarySearchTree()
    assert bst.root is None

def test_bst_root():
    """Adding data to the top of bst"""
    bst = BinarySearchTree()
    data = {'id': 40}
    bst.insert(data)
    assert bst.root.data == data

