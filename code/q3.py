visited = set()
overseers = set()
def tree_surveillance(tree, node, overseer):
    if overseer:
        overseers.add(node)
    for n in tree.neighbors(node):
        if n in visited:
            continue
        visited.add(n)
        tree_surveillance(tree, n, not overseer)
    return overseers
        
