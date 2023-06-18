import time
from fractions import Fraction

import networkx as nx

import importlib.machinery
import importlib.util
from pathlib import Path

import os

path = './assets'
if not os.path.exists(path):
    os.mkdir(path)

script_dir = Path(__file__).parent
mymodule_path = str(script_dir.joinpath('utils.py'))

loader = importlib.machinery.SourceFileLoader('utils', mymodule_path)
spec = importlib.util.spec_from_loader('utils', loader)
utils = importlib.util.module_from_spec(spec)
loader.exec_module(utils)


def data():
    yield nx.complete_graph(15), "complet_15_noeuds"
    yield nx.circular_ladder_graph(9), "circular_ladder_18_noeuds"
    yield nx.circular_ladder_graph(8), "circular_ladder_16_noeuds"
    yield nx.circulant_graph(8, [1]), "circulant_8_noeuds",
    yield nx.circulant_graph(8, [1, 2]), "circulant_8_noeuds_2"
    yield nx.circulant_graph(16, [1]), "circulant_16_noeuds"
    yield nx.circulant_graph(18, [1, 3]), "circulant_18_noeuds"
    yield nx.dorogovtsev_goltsev_mendes_graph(3), "dorogovtsev_3"
    yield nx.dorogovtsev_goltsev_mendes_graph(2), "dorogovtsev_2"
    yield nx.full_rary_tree(6, 13), "full_6ary_tree_13_noeuds"
    yield nx.full_rary_tree(3, 16), "full_3ary_tree_16_noeuds"
    yield nx.full_rary_tree(2, 18), "full_2ary_tree_18_noeuds"
    yield nx.ladder_graph(5), "ladder_10_noeuds"
    yield nx.ladder_graph(9), "ladder_18_noeuds"
    yield nx.lollipop_graph(5,5), "lollipop_10_noeuds"
    yield nx.lollipop_graph(10, 2), "lollipop_12_noeuds"
    yield nx.path_graph(15), "path_15_noeuds"
    yield nx.star_graph(14), "star_14_noeuds"
    yield nx.star_graph(15), "star_15_noeuds"
    yield nx.star_graph(16), "star_16_noeuds"
    yield nx.turan_graph(15,7), "turan_15_noeuds_7_r"
    yield nx.turan_graph(15, 3), "turan_15_noeuds_3_r"
    yield nx.turan_graph(15, 2), "turan_15_noeuds_2_r"
    yield nx.wheel_graph(15), "wheel_15_noeuds"
    yield utils.gnp_random_connected_graph(15, 0.3), "random_15_noeuds_30"
    yield utils.gnp_random_connected_graph(16, 0.3), "random_16_noeuds_30"
    yield utils.gnp_random_connected_graph(15, 0.2), "random_15_noeuds_20"
    yield utils.gnp_random_connected_graph(16, 0.2), "random_16_noeuds_20"
    yield utils.gnp_random_connected_graph(15, 0.02), "random_15_noeuds_002"
    yield utils.gnp_random_connected_graph(16, 0.02), "random_16_noeuds_002"


start = time.time()
nb = 0
ratio = Fraction(0)
for graph, name in data():
    nb += 1
    ratio += utils.solution(graph, name, path)

end = time.time() - start
print("Ratio moyen: {}".format((ratio / Fraction(nb)).limit_denominator()))
print("Temps écoulé : {}s".format(round(end, 2)))
