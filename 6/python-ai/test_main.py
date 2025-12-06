def test_addition():
    assert addition(2, 3) == 5

def addition(a, b):
    return a + b

def test_cephlapod_math():
        input = """123 328  51 64 
 45 64  387 23 
    6 98  215 314
*   +   *   +  """
        result = cephlapod_math(input)
        print("cephlapod_math result:", result)
        assert result == 4277556

def cephlapod_math(input: str) -> int:
    # Split input into lines and columns
    lines = input.strip().split('\n')
    # Remove empty lines and strip each line
    lines = [line.rstrip() for line in lines if line.strip()]
    # The last line contains the operators
    operators = lines[-1].split()
    # The rest are numbers
    number_lines = lines[:-1]
    # Parse numbers into columns
    import re
    # Use regex to split by whitespace, preserving column alignment
    columns = list(zip(*[re.findall(r"\d+", line) for line in number_lines]))
    # Convert to int
    columns = [[int(x) for x in col] for col in columns]
    # Now, for each column, apply the operator at the bottom
    result = 0
    for col, op in zip(columns, operators):
        if op == '+':
            val = sum(col)
        elif op == '*':
            val = 1
            for x in col:
                val *= x
        else:
            raise ValueError(f"Unknown operator: {op}")
        result += val
    return result

def test_count_fresh_ingredient_ids_final():
    with open(r"c:/Projects/playground/aoc2025/6/input.txt", encoding='utf-8') as f:
        input_str = f.read()
        result = cephlapod_math(input_str)
        print("Final result:", result)
    assert True
    