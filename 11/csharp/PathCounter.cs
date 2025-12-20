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

    public static ulong CountPathsOverSpecifiedNodes(Dictionary<string, List<string>> graph, string start, string end, HashSet<string> specifiedNodes)
    {
        return CountPathsRecursive(graph, start, end, new HashSet<string>(), specifiedNodes);
    }

    private static ulong CountPathsRecursive(Dictionary<string, List<string>> graph, string current, string end, HashSet<string> visited, HashSet<string> specifiedNodes)
    {
        if (current == end)
        {
            foreach (var node in specifiedNodes)
            {
                if (!visited.Contains(node))
                {
                    return 0;
                }
            }
            return 1;
        }

        visited.Add(current);
        ulong pathCount = 0;

        if (graph.ContainsKey(current))
        {
            foreach (var neighbor in graph[current])
            {
                if (!visited.Contains(neighbor))
                {
                    pathCount += CountPathsRecursive(graph, neighbor, end, new HashSet<string>(visited), specifiedNodes);
                }
            }
        }

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
