def solve(numbers, op):
    if op == '*':
        result = 1
        for n in numbers:
            result *= n
        return result
    elif op == '+':
        return sum(numbers)
    else:
        raise ValueError(f"Unknown operation: {op}")

def parse_worksheet(lines):
    # Remove empty lines and strip
    lines = [line.rstrip('\n') for line in lines if line.strip()]
    if not lines:
        return []
    # Transpose columns
    rows = [list(map(str.strip, line.split())) for line in lines]
    # Pad rows to max length
    max_len = max(len(row) for row in rows)
    for row in rows:
        while len(row) < max_len:
            row.append('')
    columns = list(zip(*rows))
    problems = []
    for col in columns:
        nums = [int(x) for x in col[:-1] if x.isdigit()]
        op = col[-1]
        problems.append((nums, op))
    return problems

def solve_worksheet(lines):
    problems = parse_worksheet(lines)
    results = [solve(nums, op) for nums, op in problems]
    return sum(results)

def test_example():
    # Example from prompt
    lines = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  "
    ]
    problems = parse_worksheet(lines)
    assert problems == [([123, 45, 6], '*'), ([328, 64, 98], '+'), ([51, 387, 215], '*'), ([64, 23, 314], '+')]
    assert solve([123, 45, 6], '*') == 33210
    assert solve([328, 64, 98], '+') == 490
    assert solve([51, 387, 215], '*') == 4243455
    assert solve([64, 23, 314], '+') == 401
    assert solve_worksheet(lines) == 4277556

import os
def test_real_input():
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "input.txt"))
    with open(input_path, encoding="utf-8") as f:
        lines = f.readlines()
    total = solve_worksheet(lines)
    print(f"Grand total: {total}")
    assert isinstance(total, int)