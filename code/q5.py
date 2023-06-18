import networkx as nx

def create_subsets(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in create_subsets(seq[1:]):
            yield [seq[0]] + item
            yield item

def general_case(graph):
    best_solution = list(graph)
    for s in create_subsets(list(graph)):
        if len(s) == 0:
            continue
        adj_list = [(n, list(adj.keys())) for n, adj in graph.adjacency() if n in s]
        edges = {(min(u, v), max(u, v)) : False for (u, v) in list(graph.edges)}
        for u, all_v in adj_list:
            for v in all_v:
                if (min(u, v), max(u, v)) in edges:
                     edges[(min(u, v), max(u, v))] = True
        all_true = True
        for edge in edges.values():
            if not edge:
                all_true = False
                break
        if all_true:
            if len(s) < len(best_solution):
                best_solution = s
    return best_solution
