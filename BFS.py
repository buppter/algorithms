"""
author: buppter
datetime: 2019/8/25 10:09
"""

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C"],
    "E": ["C", "F"],
    "F": ["E"]
}


def bfs(graph, start):
    if not graph or not start:
        return [], []

    stack = [start]
    seen = set()
    seen.add(start)
    parent = {start: None}
    res = []
    while stack:
        cur = stack.pop(0)

        nodes = graph[cur]

        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
                parent[node] = cur
        res.append(cur)
    return res, parent


if __name__ == "__main__":
    res, parent = bfs(graph, "A")
    print(res)
    print(parent)
