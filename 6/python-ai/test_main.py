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
        assert result == 4277556

def test_cephlapod_math_part_two():
        input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
        result = cephlapod_math_part_two(input)
        assert result == 3263827

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

def cephlapod_math_part_two(input: str) -> int:
    lines = input.strip().split('\n')
    max_index = len(lines[0])
    max_height = 4
    current_operator = None
    results = []
    numbers = []

    for index in range(0, max_index):
        if index < len(lines[-1]) and lines[-1][index] in ('+', '*'):
            current_operator = lines[-1][index]
        number_str = ""
        for line in lines[:-1]:
            if line[index].isdigit():
                number_str += line[index]
        if number_str.isdigit():
            numbers.append(int(number_str))
        if ((index + 1) < len(lines[-1]) and lines[-1][index + 1] in ('+', '*')) or index == max_index - 1:
            if current_operator == '+':
                col_result = sum(numbers)
            elif current_operator == '*':
                col_result = 1
                for num in numbers:
                    col_result *= num
            else:
                col_result = 0
            results.append(col_result)
            numbers = []
    final_result = sum(results)
    
    return final_result

def test_input_part_one():
    with open(r"c:/Projects/playground/aoc2025/6/input.txt", encoding='utf-8') as f:
        input_str = f.read()
        result = cephlapod_math(input_str)
        print("Final result:", result)
    assert True
    
def test_input_part_two():
    with open(r"c:/Projects/playground/aoc2025/6/input.txt", encoding='utf-8') as f:
        input_str = f.read()
        result = cephlapod_math_part_two(input_str)
        print("Final result:", result)
    assert True
    