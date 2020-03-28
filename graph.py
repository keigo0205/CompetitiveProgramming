import heapq


class Graph:
    def __init__(self):
        self.edge = {}
        self.cost = {}
        self.vertex = set()
        return

    def addEdgeCost(self, i, j, c, directed=False):
        self.vertex.add(i)
        self.vertex.add(j)

        if i not in self.edge:
            self.edge[i] = []
        self.edge[i].append(j)
        self.cost[(i, j)] = c

        if directed is False:
            return

        if j not in self.edge:
            self.edge[j] = []
        self.edge[j].append(i)
        self.cost[(j, i)] = c
        return


def dijkstra(g: Graph, s=None) -> dict:
    def solve(v_start):
        ret_cost = {v: float("inf") for v in g.vertex}
        ret_cost[v_start] = 0
        heap = [(0, v_start)]

        while heap:
            _, v_from = heapq.heappop(heap)
            for v_to in g.edge.get(v_from, []):
                nc = ret_cost[v_from] + g.cost[(v_from, v_to)]
                if ret_cost[v_to] > nc:
                    ret_cost[v_to] = nc
                    heapq.heappush(heap, (nc, v_to))
        return ret_cost

    if s is None:
        V = g.vertex
    else:
        V = [s]

    ret = {}
    for v in V:
        ret[v] = solve(v)
    return ret
