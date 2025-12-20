namespace csharp;

[TestFixture]
public class PartTwoTests
{
    [Test]
    public void Part_two()
    {
        string input = File.ReadAllText(@"C:\Projects\playground\aoc2025\11\input.txt");
        var lines = input.Trim().Split("\n");

        var graph = new Dictionary<string, List<string>>();

        foreach (var line in lines)
        {
            var parsedLine = InputParser.ParseInput(line);

            foreach (var kvp in parsedLine)
            {
                graph[kvp.Key] = kvp.Value;
            }
        }

        ulong pathCount = PathCounter.CountPathsOverSpecifiedNodes(graph, "svr", "out", new HashSet<string> { "fft", "dac" });

        TestContext.Out.WriteLine($"Part two: Number of paths from 'svr' to 'out' with specified nodes: {pathCount}");

        Assert.Pass();
    }
}
