from collections import defaultdict,deque

# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
# The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between 
# vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

def validPath(n,edges):
    graph= defaultdict(list)
    for a,b in edges:
        graph[x].append(y)
        graph[y].append(x)
    seen = [False]*n
    seen[source] = True
    queue = deque([source])

    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        
        for next_node in  graph[node]:
            if nor seen[next_node]:
                seen[next_node] = True
                queue.append(next_node)
    return False


# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.