surveilles = set()

def tree_surveillance(tree, node, parent):
    surveilles = set()
    tree_surveillance(tree, node, parent)

def tree_surveillance_rec(tree, node, parent):
    for n in tree.neighbors(node):
        if n != parent:
            tree_surveillance(tree, n, node)
            if n not in surveilles:
                surveilles.add(node)
    return surveilles
