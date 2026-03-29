#!/usr/bin/env python3
"""Floyd-Warshall all-pairs shortest path. Zero dependencies."""

INF = float("inf")

def floyd_warshall(n, edges):
    """edges: list of (u, v, weight). Returns distance matrix and next-hop matrix."""
    dist = [[INF]*n for _ in range(n)]
    nxt = [[None]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w
        nxt[u][v] = v
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]
    return dist, nxt

def reconstruct_path(nxt, u, v):
    if nxt[u][v] is None: return None
    path = [u]
    while u != v:
        u = nxt[u][v]
        path.append(u)
    return path

def has_negative_cycle(dist, n):
    return any(dist[i][i] < 0 for i in range(n))

if __name__ == "__main__":
    edges = [(0,1,3),(1,2,1),(0,2,6),(2,0,2)]
    dist, nxt = floyd_warshall(3, edges)
    for i in range(3):
        print(f"From {i}: {dist[i]}")
