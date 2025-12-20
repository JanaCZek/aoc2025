namespace csharp;

public static class PathCounter
{
    public static int CountPaths(Dictionary<string, List<string>> graph, string start, string end)
    {
        return CountPathsRecursive(graph, start, end, new HashSet<string>());
    }

    private static int CountPathsRecursive(Dictionary<string, List<string>> graph, string current, string end, HashSet<string> visited)
    {
        if (current == end)
        {
            return 1;
        }

        visited.Add(current);
        int pathCount = 0;

        if (graph.ContainsKey(current))
        {
            foreach (var neighbor in graph[current])
            {
                if (!visited.Contains(neighbor))
                {
                    pathCount += CountPathsRecursive(graph, neighbor, end, new HashSet<string>(visited));
                }
            }
        }

        return pathCount;
    }

    public static ulong CountPathsOverSpecifiedNodes(
        Dictionary<string, List<string>> graph,
        string start,
        string end,
        HashSet<string> specifiedNodes)
    {
        var cache = new Dictionary<(string, string), ulong>();

        return CountPathsRecursive(graph, start, end, new HashSet<string>(), specifiedNodes, cache);
    }

    private static ulong CountPathsRecursive(
        Dictionary<string, List<string>> graph,
        string current,
        string end,
        HashSet<string> seen,
        HashSet<string> specifiedNodes,
        Dictionary<(string, string), ulong> cache)
    {
        var seenKey = string.Join(",", seen);
        var cacheKey = (current, seenKey);

        if (cache.TryGetValue(cacheKey, out var cachedResult))
        {
            return cachedResult;
        }

        if (current == end)
        {
            return seen.SetEquals(specifiedNodes) ? 1UL : 0UL;
        }

        var newSeen = new HashSet<string>(seen);
        if (specifiedNodes.Contains(current))
        {
            newSeen.Add(current);
        }

        ulong pathCount = 0;
        if (graph.ContainsKey(current))
        {
            foreach (var neighbor in graph[current])
            {
                pathCount += CountPathsRecursive(graph, neighbor, end, newSeen, specifiedNodes, cache);
            }
        }

        cache[cacheKey] = pathCount;

        return pathCount;
    }
}

public static class InputParser
{
    public static Dictionary<string, List<string>> ParseInput(string input)
    {
        var parts = input.Trim().Split(": ");
        var result = new Dictionary<string, List<string>>();

        if (parts.Length == 2)
        {
            var key = parts[0];
            var values = parts[1].Split(" ");
            result[key] = new List<string>(values);
        }

        return result;
    }
}
