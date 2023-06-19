import queue

def tree_surveillance(E, src, a):
    S = set()
    E_prime = set(E.edges)

    while E_prime:
        u, v = E_prime.pop()
        S.add(u)
        S.add(v)

        # Supprime toutes les arêtes contenant u ou v de E_prime
        E_prime = {e for e in E_prime if u not in e and v not in e}

    return S
