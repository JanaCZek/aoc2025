namespace aoc;

public class Dial
{
    private readonly int _maxValue = 99;
    private readonly ValueCounter? _counter = default!;

    public Dial(ValueCounter counter)
    {
        _counter = counter;
    }

    public Dial() { }

    public int Value { get; private set; } = 50;

    public void Turn(string code)
    {
        var direction = code[0];
        var amount = int.Parse(code[1..]);

        if (direction == 'R')
        {
            while (amount > 0)
            {
                ClickRight();
                amount--;

                _counter?.ProcessValue(Value);
            }
        }
        else if (direction == 'L')
        {
            while (amount > 0)
            {
                ClickLeft();
                amount--;

                _counter?.ProcessValue(Value);
            }
        }
    }

    private void ClickRight()
    {
        Value = Value + 1 > _maxValue ? 0 : Value + 1;
    }

    private void ClickLeft()
    {
        Value = Value - 1 < 0 ? _maxValue : Value - 1;
    }
}

public class ValueCounter
{
    private readonly int _targetValue;

    public ValueCounter(int targetValue)
    {
        _targetValue = targetValue;
    }

    public int Value { get; private set; } = 0;

    public void ProcessValue(int dialValue)
    {
        if (dialValue == _targetValue)
        {
            Value++;
        }
    }
}