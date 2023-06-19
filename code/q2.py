def tree_surveillance(tree, node, parent):
    surveilles = set()
    return tree_surveillance_rec(tree, node, parent, surveilles)


def tree_surveillance_rec(tree, node, parent, surveilles):
    for n in tree.neighbors(node):
        if n != parent:
            tree_surveillance_rec(tree, n, node, surveilles)
            if n not in surveilles:
                surveilles.add(node)
    return surveilles
