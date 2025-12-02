namespace aoc;

[TestFixture]
public class DialTests
{
    [Test]
    public void Dial_starts_at_50()
    {
        var dial = new Dial();
        Assert.That(dial.Value, Is.EqualTo(50));
    }

    [Test]
    public void Dial_turns_right_by_1()
    {
        var dial = new Dial();
        dial.Turn("R1");
        Assert.That(dial.Value, Is.EqualTo(51));
    }

    [Test]
    public void Dial_turns_left_by_1()
    {
        var dial = new Dial();
        dial.Turn("L1");
        Assert.That(dial.Value, Is.EqualTo(49));
    }

    [Test]
    public void Dial_turns_right_by_11()
    {
        var dial = new Dial();
        dial.Turn("R11");
        Assert.That(dial.Value, Is.EqualTo(61));
    }

    [Test]
    public void Dial_turns_left_by_11()
    {
        var dial = new Dial();
        dial.Turn("L11");
        Assert.That(dial.Value, Is.EqualTo(39));
    }

    [Test]
    public void Dial_rotates_when_turning_right_by_1_and_value_is_99()
    {
        var dial = new Dial();
        dial.Turn("R49");

        Assert.That(dial.Value, Is.EqualTo(99));

        dial.Turn("R1");

        Assert.That(dial.Value, Is.EqualTo(0));
    }

    [Test]
    public void Dial_rotates_when_turning_left_by_1_and_value_is_0()
    {
        var dial = new Dial();
        dial.Turn("L50");

        Assert.That(dial.Value, Is.EqualTo(0));

        dial.Turn("L1");

        Assert.That(dial.Value, Is.EqualTo(99));
    }

    [Test]
    public void Dial_turns_right_by_100()
    {
        var dial = new Dial();
        dial.Turn("R100");
        Assert.That(dial.Value, Is.EqualTo(50));
    }

    [Test]
    public void Dial_turns_left_by_100()
    {
        var dial = new Dial();
        dial.Turn("L100");
        Assert.That(dial.Value, Is.EqualTo(50));
    }
}
