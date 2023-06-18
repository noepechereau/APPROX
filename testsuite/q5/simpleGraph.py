import importlib.machinery
import importlib.util
from pathlib import Path

script_dir = Path( __file__ ).parent
mymodule_path = str( script_dir.joinpath( '..', '..', 'code', 'q5.py' ) )

loader = importlib.machinery.SourceFileLoader( 'q5', mymodule_path )
spec = importlib.util.spec_from_loader( 'q5', loader )
q5 = importlib.util.module_from_spec( spec )
loader.exec_module( q5 )

import networkx as nx
import matplotlib.pyplot as plt


# Test 1: Simple tree with 4 nodes
arbre = nx.Graph()
arbre.add_edges_from([(1, 2), (1, 3), (2,3)])
noeuds_surveilles = q5.general_case(arbre)
pos = nx.spring_layout(arbre)
node_colors = ['red' if noeud in noeuds_surveilles else 'lightblue' for noeud in arbre.nodes()]
nx.draw(arbre, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10)
plt.title("Surveillance de l'arbre")
plt.show()


