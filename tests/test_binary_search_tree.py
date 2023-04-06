import pytest

from src.binary_search_tree import BinarySearchTree


@pytest.fixture
def bst_root():
    """Creating Bst with one top"""
    bst = BinarySearchTree()
    bst.insert({'id': 40})
    return bst


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
