namespace aoc;

[TestFixture]
public class InputTests
{
    private readonly string _filePath = @"C:\Projects\playground\aoc2025\1\input.txt";

    [Test]
    public void Reads_file_and_turns_dial()
    {
        var lines = File.ReadAllLines(_filePath);
        var dial = new Dial();
        var turnHistory = new List<int>();

        foreach (var line in lines)
        {
            dial.Turn(line);
            turnHistory.Add(dial.Value);
        }

        var countOfZeroValues = turnHistory.Count(v => v == 0);

        TestContext.Out.WriteLine($"Count of zero values: {countOfZeroValues}");

        Assert.Pass();
    }

    [Test]
    public void Reads_file_and_turns_dial_part_two()
    {
        var lines = File.ReadAllLines(_filePath);
        var valueCounter = new ValueCounter(0);
        var dial = new Dial(valueCounter);

        foreach (var line in lines)
        {
            dial.Turn(line);
        }

        var countOfZeroValues = valueCounter.Value;

        TestContext.Out.WriteLine($"Count of zero values: {countOfZeroValues}");

        Assert.Pass();
    }
}
