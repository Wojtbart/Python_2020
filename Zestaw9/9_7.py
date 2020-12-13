class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def bst_max(top):  # znajduje najwiekszy element w drzewie, czyli kierujemy się w prawą stronę
    if top is None:
        return ValueError("Drzewo  jest puste!!!!")
    while top.right != None:
        top = top.right
    return top


def bst_min(top):  # znajduje najmniejszy element w drzewie, czyli kierujemy się w  lewą stronę
    if top is None:
        return ValueError("Drzewo  jest puste!!!!")
    while top.left != None:
        top = top.left
    return top


if __name__ == '__main__':
    # Ręczne budowanie większego drzewa.
    root = Node(25)
    root.left = Node(20)
    root.right = Node(36)
    root.left.left = Node(10)
    root.left.right = Node(22)
    root.right.left = Node(30)
    root.right.right = Node(40)
    root.left.left.left = Node(5)
    root.left.left.right = Node(12)
    root.right.right.left = Node(38)
    root.right.right.right = Node(48)
    print("Największy element w drzewie BST to:", bst_max(root))
    print("Najmniejszy element w drzewie BST to:", bst_min(root))

    #                   25
    #           20              36
    #       10      22      30      40
    #     5    12         28     38    48
    #
