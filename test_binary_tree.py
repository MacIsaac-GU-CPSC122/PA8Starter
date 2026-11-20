from binary_tree import BinaryTree, _Node

# NOTE: order is actual/received student value, expected/solution
def test_len():
    bt = BinaryTree()

    # empty tree
    assert len(bt) == 0

    # one node tree
    bt = BinaryTree()
    bt._root = _Node("A")
    assert len(bt) == 1

    # three node tree
    bt = BinaryTree()
    root = _Node("A")
    left = _Node("B")
    right = _Node("C")
    root._left = left
    root._right = right
    bt._root = root
    assert len(bt) == 3

    # larger tree
    #         A
    #       /   \
    #      B     C
    #     / \     \
    #    D   E     F
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    e = _Node("E")
    f = _Node("F")

    a._left = b
    a._right = c
    b._left = d
    b._right = e
    c._right = f

    bt._root = a
    assert len(bt) == 6

def test_height():
    bt = BinaryTree()

    # empty tree (commonly defined as having height of -1)
    assert bt.height() == -1

    # one node tree
    bt = BinaryTree()
    bt._root = _Node("A")
    assert bt.height() == 0

    # two level tree has height 1
    #         A
    #       /   \
    #      B     C
    bt = BinaryTree()
    root = _Node("A")
    root._left = _Node("B")
    root._right = _Node("C")
    bt._root = root
    assert bt.height() == 1

    # unbalanced (left-heavy) tree
    #        A
    #       /
    #      B
    #     /
    #    C
    #   /
    #  D
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")

    a._left = b
    b._left = c
    c._left = d

    bt._root = a
    assert bt.height() == 3

    # unbalanced (right-heavy) tree
    #         A
    #          \
    #            B
    #             \
    #              C
    #               \
    #                D
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")

    a._right = b
    b._right = c
    c._right = d

    bt._root = a
    assert bt.height() == 3

    # multi node tree
    #         A
    #       /   \
    #      B     C
    #     /       \
    #    D         E
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    e = _Node("E")

    a._left = b
    a._right = c
    b._left = d
    c._right = e

    bt._root = a
    assert bt.height() == 2

def test_clear():
    bt = BinaryTree()

    # clear empty tree
    bt.clear()
    assert bt._root is None

    # clear single node tree
    bt = BinaryTree()
    bt._root = _Node("A")
    bt.clear()
    assert bt._root is None

    # clear multi node tree
    #         A
    #       /   \
    #      B     C
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    a._left = b
    a._right = c
    bt._root = a

    bt.clear()
    assert bt._root is None

def test_is_empty():
    bt = BinaryTree()

    # empty tree
    assert bt.is_empty() is True

    # non-empty tree (single node)
    bt = BinaryTree()
    bt._root = _Node("A")
    assert bt.is_empty() is False

    # non-empty tree (multiple nodes)
    #         A
    #       /
    #      B
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    a._left = b
    bt._root = a
    assert bt.is_empty() is False

    # back to empty after manual reset
    bt._root = None
    assert bt.is_empty() is True

def test_search():
    bt = BinaryTree()

    # empty tree
    assert bt.search("A") is False

    # single node tree
    bt = BinaryTree()
    bt._root = _Node("A")
    assert bt.search("A") is True
    assert bt.search("B") is False

    # multi node tree
    #         A
    #       /   \
    #      B     C
    #     /       \
    #    D         E
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    e = _Node("E")

    a._left = b
    a._right = c
    b._left = d
    c._right = e
    bt._root = a

    # search for item in root
    assert bt.search("A") is True

    # search for item in internal nodes
    assert bt.search("B") is True
    assert bt.search("C") is True

    # search for item in leaf nodes
    assert bt.search("D") is True
    assert bt.search("E") is True

    # search for non-existent item
    assert bt.search("Z") is False

def test_add_to_first_open_spot():
    bt = BinaryTree()

    # empty tree
    bt.add_to_first_open_spot("A")
    assert bt._root is not None
    assert bt._root._item == "A"
    assert bt._root._left is None
    assert bt._root._right is None

    # tree with root only: fills left first
    bt = BinaryTree()
    bt._root = _Node("A")

    bt.add_to_first_open_spot("B")
    assert bt._root._item == "A"
    assert bt._root._left is not None
    assert bt._root._left._item == "B"
    assert bt._root._right is None

    # root has left but no right: fills right
    #         A
    #       / 
    #      B 
    bt = BinaryTree()
    root = _Node("A")
    root._left = _Node("B")
    bt._root = root

    bt.add_to_first_open_spot("C")
    assert bt._root._left is not None
    assert bt._root._left._item == "B"
    assert bt._root._right is not None
    assert bt._root._right._item == "C"

    # complete first level, so next insertion goes to left child of left subtree
    #         A
    #       /   \
    #      B     C
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    a._left = b
    a._right = c
    bt._root = a

    bt.add_to_first_open_spot("D")
    assert bt._root is a
    assert a._left is b
    assert a._right is c
    assert b._left is not None
    assert b._left._item == "D"
    assert b._right is None
    assert c._left is None
    assert c._right is None

    # B has left child but missing right child, so insertion should go to B's right
    #         A
    #       /   \
    #      B     C
    #     /
    #    D
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    a._left = b
    a._right = c
    b._left = d
    bt._root = a

    bt.add_to_first_open_spot("E")
    assert b._left is d
    assert b._right is not None
    assert b._right._item == "E"
    assert c._left is None
    assert c._right is None

    # B already has two children, so insertion should go to C's left
    #         A
    #       /   \
    #      B     C
    #     / \ 
    #    D   E 
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    e = _Node("E")
    a._left = b
    a._right = c
    b._left = d
    b._right = e
    bt._root = a

    bt.add_to_first_open_spot("F")
    assert a._left is b
    assert a._right is c
    assert b._left is d
    assert b._right is e
    assert c._left is not None
    assert c._left._item == "F"
    assert c._right is None

def test_pre_order():
    bt = BinaryTree()

    # empty tree
    assert bt.pre_order() == []

    # one node tree
    bt = BinaryTree()
    bt._root = _Node("A")
    assert bt.pre_order() == ["A"]

    # larger tree
    #         A
    #       /   \
    #      B     C
    #     / \     \
    #    D   E     F
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    e = _Node("E")
    f = _Node("F")

    a._left = b
    a._right = c
    b._left = d
    b._right = e
    c._right = f

    bt._root = a
    assert bt.pre_order() == ["A", "B", "D", "E", "C", "F"]

def test_post_order():
    bt = BinaryTree()

    # empty tree
    assert bt.post_order() == []

    # one node tree
    bt = BinaryTree()
    bt._root = _Node("A")
    assert bt.post_order() == ["A"]

    # larger tree
    #         A
    #       /   \
    #      B     C
    #     / \     \
    #    D   E     F
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    e = _Node("E")
    f = _Node("F")

    a._left = b
    a._right = c
    b._left = d
    b._right = e
    c._right = f

    bt._root = a
    assert bt.post_order() == ["D", "E", "B", "F", "C", "A"]

def test_in_order():
    bt = BinaryTree()

    # empty tree
    assert bt.in_order() == []

    # one node tree
    bt = BinaryTree()
    bt._root = _Node("A")
    assert bt.in_order() == ["A"]

    # larger tree
    #         A
    #       /   \
    #      B     C
    #     / \     \
    #    D   E     F
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    e = _Node("E")
    f = _Node("F")

    a._left = b
    a._right = c
    b._left = d
    b._right = e
    c._right = f

    bt._root = a
    assert bt.in_order() == ["D", "B", "E", "A", "C", "F"]

def test_level_order():
    bt = BinaryTree()

    # empty tree
    assert bt.level_order() == []

    # one node tree
    bt = BinaryTree()
    bt._root = _Node("A")
    assert bt.level_order() == ["A"]

    # larger tree
    #         A
    #       /   \
    #      B     C
    #     / \     \
    #    D   E     F
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    e = _Node("E")
    f = _Node("F")

    a._left = b
    a._right = c
    b._left = d
    b._right = e
    c._right = f

    bt._root = a
    assert bt.level_order() == ["A", "B", "C", "D", "E", "F"]

# for BONUS task
def test_delete():
    bt = BinaryTree()

    # empty tree
    bt.delete("A")
    assert bt._root is None

    # delete root when root is only node in tree
    bt = BinaryTree()
    bt._root = _Node("A")
    bt.delete("A")
    assert bt._root is None

    # delete root when root has only a left child
    #         A
    #       /
    #      B
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    a._left = b
    bt._root = a

    bt.delete("A")
    assert bt._root is b
    assert bt._root._item == "B"
    assert bt._root._left is None
    assert bt._root._right is None

    # delete root when root has only a right child
    #         A
    #           \
    #            C
    bt = BinaryTree()
    a = _Node("A")
    c = _Node("C")
    a._right = c
    bt._root = a

    bt.delete("A")
    assert bt._root is c
    assert bt._root._item == "C"
    assert bt._root._left is None
    assert bt._root._right is None

    # delete root when root has two children, do nothing
    #         A
    #       /   \
    #      B     C
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    a._left = b
    a._right = c
    bt._root = a

    bt.delete("A")
    assert bt._root is a
    assert bt._root._left is b
    assert bt._root._right is c

    # delete a leaf in the left subtree
    #         A
    #       /   \
    #      B     C
    #     /
    #    D
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    a._left = b
    a._right = c
    b._left = d
    bt._root = a

    bt.delete("D")
    assert a._left is b
    assert a._right is c
    assert b._left is None
    assert b._right is None
    assert c._left is None
    assert c._right is None

    # delete a node with one left child
    #         A
    #       /   \
    #      B     C
    #     /
    #    D
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    a._left = b
    a._right = c
    b._left = d
    bt._root = a

    bt.delete("B")
    assert a._left is d
    assert a._right is c
    assert d._left is None
    assert d._right is None

    # delete a node with one right child
    #         A
    #       /   \
    #      B     C
    #       \
    #        E
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    e = _Node("E")
    a._left = b
    a._right = c
    b._right = e
    bt._root = a

    bt.delete("B")
    assert a._left is e
    assert a._right is c
    assert e._left is None
    assert e._right is None

    # delete a node with two children, do nothing
    #         A
    #       /   \
    #      B     C
    #     / \ 
    #    D   E 
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    e = _Node("E")
    a._left = b
    a._right = c
    b._left = d
    b._right = e
    bt._root = a

    bt.delete("B")
    assert a._left is b
    assert a._right is c
    assert b._left is d
    assert b._right is e

    # item not found, tree should not change
    #         A
    #       /   \
    #      B     C
    bt = BinaryTree()
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    a._left = b
    a._right = c
    bt._root = a

    bt.delete("Z")
    assert bt._root is a
    assert a._left is b
    assert a._right is c

    # preorder "first match" behavior, only first matching node is deleted
    #         A
    #       /
    #      X
    #     /
    #    B
    #   /
    #  X
    bt = BinaryTree()
    a = _Node("A")
    x1 = _Node("X")
    b = _Node("B")
    x2 = _Node("X")
    a._left = x1
    x1._left = b
    b._left = x2
    bt._root = a

    bt.delete("X")

    # using preorder, x1 should be deleted
    assert a._left is b
    assert b._left is x2
    assert bt._root is a
    assert a._right is None