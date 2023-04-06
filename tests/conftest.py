import pytest

from src.binary_search_tree import BinarySearchTree


@pytest.fixture
def bst_root():
    """Creating Bst with one top"""
    bst = BinarySearchTree()
    bst.insert({'id': 40})
    return bst

@pytest.fixture
def bst_full():
    """Creating Bst with full 3 levels"""
    bst = BinarySearchTree()
    bst.insert({'id': 40})
    bst.insert({'id': 30})
    bst.insert({'id': 50})
    bst.insert({'id': 25})
    bst.insert({'id': 35})
    bst.insert({'id': 45})
    bst.insert({'id': 60})
    return bst
