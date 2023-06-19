import importlib.machinery
import importlib.util
import random
import time
from fractions import Fraction
from itertools import combinations, groupby
from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt

script_dir = Path(__file__).parent
mymodule_path = str(script_dir.joinpath('..', '..', 'code', 'q5.py'))

loader = importlib.machinery.SourceFileLoader('q5', mymodule_path)
spec = importlib.util.spec_from_loader('q5', loader)
q5 = importlib.util.module_from_spec(spec)
loader.exec_module(q5)

mymodule_path = str(script_dir.joinpath('..', '..', 'code', 'q2.py'))

loader = importlib.machinery.SourceFileLoader('q2', mymodule_path)
spec = importlib.util.spec_from_loader('q2', loader)
q2 = importlib.util.module_from_spec(spec)
loader.exec_module(q2)


def solution(graph, name, path):
    # OPTI
    start_opti = time.time()
    noeuds_surveilles_opti = q5.general_case(graph)
    elapsed_opti = time.time() - start_opti
    node_colors = ['red' if noeud in noeuds_surveilles_opti else 'lightblue' for noeud in graph.nodes()]
    nx.draw(graph, with_labels=True, node_color=node_colors, node_size=500, font_size=10)
    plt.savefig(path + "/" + name + "_exact")
    plt.close()

    # APPROX
    start_approx = time.time()
    noeuds_surveilles_approx = q2.tree_surveillance(graph, 0, None)
    elapsed_approx = time.time() - start_approx
    node_colors = ['red' if noeud in noeuds_surveilles_approx else 'lightblue' for noeud in graph.nodes()]
    nx.draw(graph, with_labels=True, node_color=node_colors, node_size=500, font_size=10)
    plt.savefig(path + "/" + name + "_approx")
    plt.close()

    ratio = Fraction(len(noeuds_surveilles_approx) / len(noeuds_surveilles_opti)).limit_denominator()

    print("{}:".format(name.replace("_", " ")))
    print("   Algo exact:")
    print("      Temps: {}s".format(round(elapsed_opti, 4)))
    print("      Nombre de noeuds surveillés: {}".format(len(noeuds_surveilles_opti)))

    print("   Algo approx:")
    print("      Temps: {}s".format(round(elapsed_approx, 4)))
    print("      Nombre de noeuds surveillés: {}".format(len(noeuds_surveilles_approx)))
    print("  Ratio approx/opti: {}".format(ratio))
    return ratio


def gnp_random_connected_graph(n, p):
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G
