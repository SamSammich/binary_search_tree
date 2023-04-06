import pytest

from src.binary_search_tree import BinarySearchTree


def test_bst_empty():
    """Empty binary search tree"""
    bst = BinarySearchTree()
    assert bst.root is None


def test_bst_root():
    """Adding data to the top of bst"""
    bst = BinarySearchTree()
    data = {'id': 40}
    bst.insert(data)
    assert bst.root.data == data


def test_bst_insert_left(bst_root):
    """Adding data to the left from the top"""
    bst_root.insert({'id': 30})
    assert bst_root.root.left.data['id'] == 30


def test_bst_insert_right(bst_root):
    """Adding data to the right from the top"""
    bst_root.insert({'id': 50})
    assert bst_root.root.right.data['id'] == 50


def test_bst_insert_left_left(bst_root):
    """Adding data to the left 2 times from the top"""
    bst_root.insert({'id': 30})
    bst_root.insert({'id': 25})
    assert bst_root.root.left.left.data['id'] == 25


def test_bst_insert_right_right(bst_root):
    """Adding data to the right 2 times from the top"""
    bst_root.insert({'id': 50})
    bst_root.insert({'id': 60})
    assert bst_root.root.right.right.data['id'] == 60


def test_bst_search_empty():
    """Search in empty BST returning None"""
    assert BinarySearchTree().search(40) is None


@pytest.mark.parametrize('data_id, data', [(40, {'id': 40}),
                                           (30, {'id': 30}),
                                           (25, {'id': 25}),
                                           (35, {'id': 35}),
                                           (50, {'id': 50}),
                                           (45, {'id': 45}),
                                           (60, {'id': 60}),
                                           (444, None),
                                           (4, None),
                                           ])
def test_bst_search(bst_full, data_id, data):
    assert bst_full.search(data_id) == data
