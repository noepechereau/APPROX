import networkx as nx
import matplotlib.pyplot as plt

def surveillance_arbre(arbre):
    # Initialisation des variables
    surveilles = set()  # Ensemble des routeurs surveillés

    # Parcours de l'arbre en profondeur
    def dfs(noeud, parent):
        for voisin in arbre.neighbors(noeud):
            if voisin != parent:
                dfs(voisin, noeud)
                # Ajout du voisin à surveiller si nécessaire
                if voisin not in surveilles:
                    surveilles.add(noeud)

    # Appel initial à la fonction DFS
    dfs(0, None)

    return surveilles

# Exemple de réseau en forme d'arbre
arbre = nx.Graph()
arbre.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (6, 5), (5, 7)])

# Résolution du problème de surveillance dans l'arbre
noeuds_surveilles = surveillance_arbre(arbre)

# Affichage du réseau avec les nœuds surveillés
pos = nx.spring_layout(arbre)
node_colors = ['red' if noeud in noeuds_surveilles else 'lightblue' for noeud in arbre.nodes()]
nx.draw(arbre, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10)
plt.title("Surveillance de l'arbre")
plt.show()

print("Nombre de routeurs surveillés :", len(noeuds_surveilles))
print("Nombre total de routeurs :", arbre.number_of_nodes())
