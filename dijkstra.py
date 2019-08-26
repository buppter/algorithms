"""
author: buppter
datetime: 2019/8/25 10:51
"""
import heapq

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


class Dijkstra:
    def init_distance(self, graph, start):
        distance = {start: 0}
        for key in graph.keys():
            if key != start:
                distance[key] = float('inf')
        return distance

    def dijkstra(self, graph, start):
        if not graph or not start:
            return None

        distance = self.init_distance(graph, start)
        pqueue = []
        heapq.heappush(pqueue, (0, start))
        seen = set()
        parent = {start: None}

        while pqueue:
            cur_distance, cur_node = heapq.heappop(pqueue)
            seen.add(cur_node)
            nodes = graph[cur_node]

            for node, dist in nodes.items():
                if node in seen:
                    continue
                elif distance[node] > cur_distance + dist:
                    heapq.heappush(pqueue, (dist + cur_distance, node))
                    parent[node] = cur_node
                    distance[node] = cur_distance + dist
        return distance, parent


if __name__ == '__main__':
    s = Dijkstra()
    res, parent = s.dijkstra(graph, "A")
    print(res)
    print(parent)
