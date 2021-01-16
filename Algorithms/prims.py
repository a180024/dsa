INF = float("inf")
def Prims(G, V):
    edges = 0
    selected = [0] * V
    selected[0] = True # Start from the first vertex

    while edges < V - 1:
        minimum = INF
        x, y = 0, 0
        # For every vertex, find the next nearest that has not been visited
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):
                        if G[i][j] < minimum:
                            minimum = G[i][j]
                            x, y = i, j
        print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
        selected[y] = True
        edges += 1


G = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0],
]
Prims(G, 5)
