"""
CS2302
Lab3
Purpose: learn how to work with arrays and binary search trees
Created on Wed Feb 25, 2019
Last modified Mon Mar 8, 2019
Olac Fuentes
@author: Nancy Hernandez
"""


class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


def Insert(T, newItem):
    if T == None:
        T = BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left, newItem)
    else:
        T.right = Insert(T.right, newItem)
    return T


def Delete(T, del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left, del_item)
        elif del_item > T.item:
            T.right = Delete(T.right, del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None:  # T is a leaf, just remove it
                T = None
            elif T.left is None:  # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left
            else:  # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right, m.item)
    return T


def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item, end=' ')
        InOrder(T.right)


def InOrderD(T, space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right, space + '   ')
        print(space, T.item)
        InOrderD(T.left, space + '   ')


def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T


def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)


def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)


def Find(T, k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item < k:
        return Find(T.right, k)
    return Find(T.left, k)


def FindAndPrint(T, k):
    f = Find(T, k)
    if f is not None:
        print(f.item, 'found')
    else:
        print(k, 'not found')


# Number two
def iterativeSearch(T, k):
    while True:
        # if number isn't in list
        if T is None:
            print("Number", k, "not found")
            print()
            break
        # checks once k has been targeted
        if T.item == k:
            print("Number", k, "found")
            print()
            break
        # checks what side k will be on(left or right)
        if (k < T.item):
            T = T.left

        elif (T.right != None):
            T = T.right
    return T


# Number three
def sortedListToBST(A2):
    # if not list provided
    if not A2:
        return None

    middle = len(A2) // 2
    root = BST(A2[middle])

    # finds middle for left and right sides
    root.left = sortedListToBST(A2[:middle])
    root.right = sortedListToBST(A2[middle + 1:])

    return root


# Number four
def BSTToArray(T, Arr, index):
    if T is None:
        return index
    # keeps track of which index it is at currently
    index = BSTToArray(T.left, Arr, index)

    Arr[index] = T.item
    index += 1

    index = BSTToArray(T.right, Arr, index)

    return index


# Number five
def PrintCurrentDepth(T, depth):
    if T == None:
        return 0
    # if its the root of tree
    if depth == 0:
        print('Keys at depth', depth, ':', T.item)
    # when rigth side and left side are non existant
    if T.left is not None and T.right is not None:
        print('Keys at depth', depth + 1, ':', T.left.item, ',', T.right.item)
    # when left side is non existant
    if T.right is not None and T.left is None:
        print('Keys at depth', depth + 1, ':', T.right.item)
    # wheb right side is non existant
    if T.left is not None and T.right is None:
        print('Keys at depth', depth + 1, ':', T.left.item)

    depth1 = PrintCurrentDepth(T.left, depth + 1)
    depth1 = PrintCurrentDepth(T.right, depth + 1)

    return depth1


# Code to test the functions above
T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]

for a in A:
    T = Insert(T, a)

A2 = [1, 2, 3, 4, 5, 6, 7]

# NUMBER TWO
iterativeSearch(T, 1)

# NUMBER THREE
SortedLIST = sortedListToBST(A2)
print("Sorted list", A2, "now converted to BST:")
print()
InOrderD(SortedLIST, ' ')
print()

# NUMBER FOUR
BSTToArray(T, A, 0)
print("BST now converted to sorted list:")
for i in A:
    print(i, end=' ')
print()
print()

# NUMBER FIVE
print("Elements printed by depth:")
print()
PrintCurrentDepth(T, 0)
