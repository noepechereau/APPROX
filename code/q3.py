import queue
import networkx as nx

visited = set()
overseers = set()

def tree_surveillance(graph, src, a):
    q = queue.Queue()
    q.put(src)
    q.put(None)
    visited.add(src)
    overseer = True

    while not q.empty():
        node = q.get()
        if node == None and q.empty():
            break
        if node == None:
            overseer = not overseer
            q.put(None)
            continue
        if overseer:
            overseers.add(node)
        for n in graph.neighbors(node):
            if n not in visited:
                visited.add(n)
                q.put(n)
    for (x,y) in nx.edges(graph):
        if x not in overseers and y not in overseers:
            overseers.add(x)

    return overseers
