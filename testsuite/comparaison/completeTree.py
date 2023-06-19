import time
from fractions import Fraction

import networkx as nx

import importlib.machinery
import importlib.util
from pathlib import Path

import os

path = './assets_tree'
if not os.path.exists(path):
    os.mkdir(path)

script_dir = Path(__file__).parent
mymodule_path = str(script_dir.joinpath('utils_tree.py'))

loader = importlib.machinery.SourceFileLoader('utils', mymodule_path)
spec = importlib.util.spec_from_loader('utils', loader)
utils = importlib.util.module_from_spec(spec)
loader.exec_module(utils)


def data():
    yield nx.full_rary_tree(6, 13), "full_6ary_tree_13_noeuds"
    yield nx.full_rary_tree(3, 16), "full_3ary_tree_16_noeuds"
    yield nx.full_rary_tree(2, 18), "full_2ary_tree_18_noeuds"
    yield nx.full_rary_tree(6, 10), "full_6ary_tree_10_noeuds"
    yield nx.full_rary_tree(3, 20), "full_3ary_tree_20_noeuds"
    yield nx.full_rary_tree(2, 8), "full_2ary_tree_8_noeuds"


start = time.time()
nb = 0
ratio = Fraction(0)
for graph, name in data():
    nb += 1
    ratio += utils.solution(graph, name, path)

end = time.time() - start
print("Ratio moyen: {}".format((ratio / Fraction(nb)).limit_denominator()))
print("Temps écoulé : {}s".format(round(end, 2)))
