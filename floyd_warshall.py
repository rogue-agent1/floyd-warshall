#!/usr/bin/env python3
"""Floyd-Warshall — all-pairs shortest paths."""
import sys
INF = float("inf")
def floyd_warshall(n, edges):
    dist = [[INF]*n for _ in range(n)]
    nxt = [[None]*n for _ in range(n)]
    for i in range(n): dist[i][i] = 0
    for u, v, w in edges: dist[u][v] = w; nxt[u][v] = v
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]; nxt[i][j] = nxt[i][k]
    return dist, nxt
def path(nxt, u, v):
    if nxt[u][v] is None: return []
    p = [u]
    while u != v: u = nxt[u][v]; p.append(u)
    return p
def cli():
    edges = [(0,1,3),(0,2,6),(1,2,2),(2,0,1),(2,3,4),(3,1,1)]
    dist, nxt = floyd_warshall(4, edges)
    print("  All-pairs shortest paths:")
    for i in range(4):
        for j in range(4):
            d = dist[i][j]; p = path(nxt,i,j)
            if i != j and d < INF: print(f"    {i}→{j}: {d} via {p}")
if __name__ == "__main__": cli()
