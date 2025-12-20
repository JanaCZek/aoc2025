namespace csharp;

[TestFixture]
public class PartOneTests
{
    [Test]
    public void Parses_input_line_to_dictionary()
    {
        string line = "nof: eyx uhp xte jod eza\n";
        var expected = new Dictionary<string, List<string>>
        {
            { "nof", new List<string> { "eyx", "uhp", "xte", "jod", "eza" } }
        };

        var result = InputParser.ParseInput(line);

        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Parses_real_input()
    {
        string input = File.ReadAllText(@"C:\Projects\playground\aoc2025\11\input.txt");
        var lines = input.Trim().Split("\n");

        var result = new Dictionary<string, List<string>>();

        foreach (var line in lines)
        {
            var parsedLine = InputParser.ParseInput(line);

            foreach (var kvp in parsedLine)
            {
                result[kvp.Key] = kvp.Value;
            }
        }

        Assert.That(result.Count, Is.GreaterThan(0));

        TestContext.Out.WriteLine($"Parsed {result.Count} entries.");

        foreach (var kvp in result)
        {
            TestContext.Out.WriteLine($"{kvp.Key}: {string.Join(", ", kvp.Value)}");
        }
    }

    [Test]
    public void Part_one()
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

        int pathCount = PathCounter.CountPaths(graph, "you", "out");

        TestContext.Out.WriteLine($"Part one: Number of paths from 'you' to 'out': {pathCount}");

        Assert.Pass();
    }
}
