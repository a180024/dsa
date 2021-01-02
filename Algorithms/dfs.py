def dfs(graph, start, visited=None):
    if not visited:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited: # stack
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')
