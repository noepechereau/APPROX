import networkx as nx
import matplotlib.pyplot as plt
from pulp import *

def vertex_cover(graph):
    # Création du problème de PLNE
    prob = LpProblem("VertexCoverProblem", LpMinimize)

    # Création des variables binaires pour chaque sommet
    vertex_vars = LpVariable.dicts("Vertex", graph.nodes, cat='Binary')

    # Définition de la fonction objectif
    prob += lpSum(vertex_vars)

    # Contrainte : chaque arête doit être couverte
    for edge in graph.edges:
        prob += vertex_vars[edge[0]] + vertex_vars[edge[1]] >= 1

    # Résolution du PLNE
    prob.solve()

    # Récupération de la solution
    cover = [v for v in vertex_vars if value(vertex_vars[v]) == 1]

    # Retourner l'ensemble de sommets couvrant
    return cover


# Exemple de test

# Générer un graphe aléatoire avec 10 sommets et 20 arêtes
graph = nx.gnm_random_graph(10, 20)

# Appeler la fonction de couverture de sommets
cover = vertex_cover(graph)

# Créer une liste de couleurs pour les sommets du graphe
node_colors = ['blue' if node in cover else 'red' for node in graph.nodes]

# Dessiner le graphe avec les sommets de la couverture en couleur différente
nx.draw(graph, with_labels=True, node_color=node_colors, node_size=500)
plt.show()
