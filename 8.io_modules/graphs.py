# task 3

from graphviz import Digraph

g = Digraph(comment='mol')

g.node('A', 'DNA')
g.node('B', 'RNA')
g.node('C', 'Protein')

g.edges(['AB', 'BC', 'BA'])
g.render('dotmol', view=True)

# Output graph is in the directory

# task 4

def search(vertex, graph, visited):
    """
    Function helper to move in graph
    :param vertex: hashable - current vertex
    :param graph: dict - "adjacency dict" in a form {vertex: [neighbours...]}
    :param visited: dict - dict with visited vertices in a form {vertex: True/False}
    :return:
    """
    # Mark vertex as visited
    visited[vertex] = True

    # Go to other vertex, adjacent to current, if they weren't visited before
    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            print(vertex, neighbour, visited)
            search(neighbour, graph, visited)


def dfs_num(graph):
    """
    Function to apply depth-first search to a graph
    :param graph: dict - "adjacency dict" in a form {vertex: [neighbours...]}
    :return: number of connected component
    """
    # Create dict of visited vertices
    visited = {v: False for v in graph}
    a = 0
    # Visit all reachable vertices from vertex for all vertices
    for v in graph:
        if visited[v] == False:
            a += 1
        search(v, graph, visited)
    return a



graph = {1: [2], 2: [1, 3, 4, 5], 3: [2], 4: [5, 2], 5: [4, 2], 6: [7], 7: [6], 8: []}

print(dfs_num(graph))






