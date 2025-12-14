def create_graph(lines: list[str]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for line in lines:
        device, outputs = line.split(": ")
        graph[device] = outputs.split()
    return graph

def num_paths_part_one(graph: dict[str, list[str]], start: str, end: str) -> int:
    if start == end:
        return 1
    return sum(
        num_paths_part_one(graph, next_node, end)
        for next_node in graph.get(start, [])
    )

graph = create_graph(open(r"c:/Projects/playground/aoc2025/11/input.txt", encoding='utf-8').read().strip().splitlines())
paths = num_paths_part_one(graph, 'you', 'out')
print(f"Part One: {paths}")

from collections.abc import Iterable
from functools import cache

def num_paths(
        graph: dict[str, list[str]],
        start: str,
        end: str,
        middle: list[str] | None = None,
) -> int:
    middle_set = frozenset(middle if middle is not None else ())

    @cache
    def _num_paths(node: str, seen: frozenset[str]) -> int:
        if node == end:
            # Path is only valid if we've seen every "middle" device
            return 1 if seen == middle_set else 0

        new_seen = seen
        if node in middle_set:
            new_seen = seen | {node}
        return sum(
            _num_paths(next_node, new_seen)
            for next_node in graph.get(node, [])
        )

    return _num_paths(start, frozenset[str]())

graph = create_graph(open(r"c:/Projects/playground/aoc2025/11/input.txt", encoding='utf-8').read().strip().splitlines())
paths = num_paths(graph, "svr", "out", middle=["dac", "fft"])

print(f"Part Two: {paths}")