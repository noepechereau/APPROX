visited = set()
visited_edges = set()
overseers = set()
def tree_surveillance(tree, node, overseer):
    if overseer:
        overseers.add(node)
        for e in tree.edges(node):
            visited_edges.add(e)

    for n in tree.neighbors(node):
        if n in visited:
            continue
        visited.add(n)
        tree_surveillance(tree, n, not overseer)

    for e in tree.edges():
        if e not in visited_edges:
            overseers.add(e[0])
            for e in tree.edges(e[0]):
                visited_edges.add(e)
    return overseers

