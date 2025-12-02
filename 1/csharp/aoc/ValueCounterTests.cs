namespace aoc;

[TestFixture]
public class ValueCounterTests
{
    [Test]
    public void Value_counter_counts_1()
    {
        var counter = new ValueCounter(1);

        counter.ProcessValue(0);
        counter.ProcessValue(1);
        counter.ProcessValue(1);
        counter.ProcessValue(2);
        counter.ProcessValue(1);

        Assert.That(counter.Value, Is.EqualTo(3));
    }
}
