"""
author: buppter
datetime: 2019/8/25 10:51
"""

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


class Dijkstra:
    def init_unvisited(self, graph):
        unvisited = {}
        for key in graph.keys():
            unvisited[key] = None
        return unvisited

    def dijkstra(self, graph, start):
        if not graph or not start:
            return None

        unvisited = self.init_unvisited(graph)
        visited = {}
        cur_node = start
        cur_distance = 0
        # 父节点记录
        parent = {start: None}
        while True:
            nodes = graph[cur_node]
            for node, distance in nodes.items():
                if node in visited:
                    continue
                if unvisited[node] is None or unvisited[node] > cur_distance + distance:
                    unvisited[node] = cur_distance + distance
                    parent[node] = cur_node
            visited[cur_node] = cur_distance
            unvisited.pop(cur_node)
            if not unvisited:
                break
            candidates = [node for node in unvisited.items() if node[1]]
            # 进行调整，得到新的最短路径
            candidates = sorted(candidates, key=lambda x: x[1])
            cur_node, cur_distance = candidates[0]

        return visited, parent


if __name__ == '__main__':
    s = Dijkstra()
    res, parent = s.dijkstra(graph, "A")
    print(res)
    print(parent)
