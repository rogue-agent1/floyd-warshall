#!/usr/bin/env python3
"""Floyd-Warshall all-pairs shortest paths."""
import sys
INF=float('inf')
def floyd_warshall(n,edges):
    dist=[[INF]*n for _ in range(n)]
    for i in range(n): dist[i][i]=0
    for u,v,w in edges: dist[u][v]=min(dist[u][v],w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k]+dist[k][j]<dist[i][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    return dist
def main():
    edges=[(0,1,3),(0,2,8),(1,2,2),(2,3,1),(3,0,4),(1,3,7)]
    dist=floyd_warshall(4,edges)
    print("All-pairs shortest paths:")
    print("    "+" ".join(f"{i:4d}" for i in range(4)))
    for i in range(4):
        row=" ".join(f"{d:4d}" if d<INF else " inf" for d in dist[i])
        print(f"  {i}: {row}")
if __name__=="__main__": main()
