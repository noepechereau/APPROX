import importlib.machinery
import importlib.util
from pathlib import Path

script_dir = Path( __file__ ).parent
mymodule_path = str( script_dir.joinpath( '..', '..', 'code', 'q3.py' ) )

loader = importlib.machinery.SourceFileLoader( 'q3', mymodule_path )
spec = importlib.util.spec_from_loader( 'q3', loader )
q3 = importlib.util.module_from_spec( spec )
loader.exec_module( q3 )

import networkx as nx
import matplotlib.pyplot as plt

# Test 4: Complex tree with 8 nodes
arbre = nx.Graph()
arbre.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (7, 8)])
noeuds_surveilles = q3.tree_surveillance(arbre)
pos = nx.spring_layout(arbre)
node_colors = ['red' if noeud in noeuds_surveilles else 'lightblue' for noeud in arbre.nodes()]
nx.draw(arbre, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10)
plt.title("Surveillance de l'arbre")
plt.show()
