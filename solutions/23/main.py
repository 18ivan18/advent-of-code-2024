#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin


def dfs(graph, node, visited, component):
    visited.add(node)
    component.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)


start_letter = 't'


def bron_kerbosch(R, P, X, graph, largest_clique):
    """
    Bron-Kerbosch recursive algorithm to find maximal cliques.
    - R: current clique being formed
    - P: potential candidates to extend the clique
    - X: excluded vertices
    """
    if not P and not X:
        # If P and X are empty, we found a maximal clique
        if len(R) > len(largest_clique[0]):
            largest_clique[0] = R
        return

    # Choose a pivot vertex from P union X (heuristic to optimize performance)
    pivot = next(iter(P.union(X)))
    # Iterate over candidates in P \ N(pivot)
    for v in P - set(graph[pivot]):
        bron_kerbosch(R.union([v]), P.intersection(
            graph[v]), X.intersection(graph[v]), graph, largest_clique)
        P.remove(v)
        X.add(v)


def find_largest_clique(graph):
    """
    Finds the largest maximal clique using the Bron-Kerbosch algorithm.
    """
    P = set(graph.keys())  # Start with all nodes as potential candidates
    R = set()  # Start with an empty clique
    X = set()  # No excluded vertices at the beginning

    largest_clique = [set()]  # To store the largest clique found

    bron_kerbosch(R, P, X, graph, largest_clique)

    return largest_clique[0]


def solve() -> None:
    input = stdin.read().splitlines()
    graph = defaultdict(list)
    for line in input:
        first, second = line.split('-')
        graph[first].append(second)
        graph[second].append(first)

    triplets = set()
    for node, neighbours in graph.items():
        for neighbour in neighbours:
            for third in graph[neighbour]:
                if third in neighbours:
                    triplet = [node, neighbour, third]
                    if any([True if x.startswith(start_letter) else False for x in triplet]):
                        triplets.add(
                            '-'.join(sorted([node, neighbour, third])))
    print(len(triplets))

    print(','.join(sorted(list(find_largest_clique(graph)))))


if __name__ == '__main__':
    solve()
