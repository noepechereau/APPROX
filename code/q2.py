surveilles = set()

def tree_surveillance(tree, node, parent):
    for n in tree.neighbors(node):
        if n != parent:
            tree_surveillance(tree, n, node)
            if n not in surveilles:
                surveilles.add(node)
    return surveilles


