"""
author: buppter
datetime: 2019/8/25 10:35
"""
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C"],
    "E": ["C", "F"],
    "F": ["E"]
}


def dfs(graph, start):
    if not graph or not start:
        return [], []

    stack = [start]
    seen = [start]
    res = []
    parent = {start: None}
    while stack:
        cur = stack.pop()
        nodes = graph[cur]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.append(node)
                parent[node] = cur
        res.append(cur)

    return res, parent


if __name__ == '__main__':
    res, parent = dfs(graph, "A")
    print(res)
    print(parent)
