from floyd_warshall import floyd_warshall, reconstruct_path, has_negative_cycle
edges = [(0,1,3),(1,2,1),(0,2,6),(2,0,2)]
dist, nxt = floyd_warshall(3, edges)
assert dist[0][0] == 0
assert dist[0][1] == 3
assert dist[0][2] == 4  # 0->1->2
assert dist[2][1] == 5  # 2->0->1
path = reconstruct_path(nxt, 0, 2)
assert path == [0, 1, 2]
assert not has_negative_cycle(dist, 3)
# Unreachable
dist2, nxt2 = floyd_warshall(3, [(0,1,1)])
assert dist2[0][2] == float("inf")
assert reconstruct_path(nxt2, 0, 2) is None
print("floyd_warshall tests passed")
