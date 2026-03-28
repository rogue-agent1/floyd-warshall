#!/usr/bin/env python3
"""floyd_warshall - All-pairs shortest paths."""
import sys,json
INF=float('inf')
def floyd(n,edges):
    dist=[[INF]*n for _ in range(n)]
    for i in range(n):dist[i][i]=0
    for u,v,w in edges:dist[u][v]=w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k]+dist[k][j]<dist[i][j]:dist[i][j]=dist[i][k]+dist[k][j]
    return dist
if __name__=="__main__":
    edges=[(0,1,3),(0,2,6),(1,2,2),(2,0,1),(2,3,1),(3,0,7)]
    dist=floyd(4,edges)
    for i in range(4):
        for j in range(4):d=dist[i][j];print(f"{d if d<INF else '∞':>4}",end=" ")
        print()
