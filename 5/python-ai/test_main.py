def test_addition():
    assert addition(2, 3) == 5

def addition(a, b):
    return a + b
def count_fresh_ingredient_ids(input_str):
    # Split input into ranges and IDs
    parts = input_str.strip().split('\n\n')
    if len(parts) != 2:
        raise ValueError('Input must have ranges, blank line, then IDs')
    range_lines = parts[0].splitlines()
    id_lines = parts[1].splitlines()

    # Parse ranges into list of (start, end) tuples
    ranges = []
    for line in range_lines:
        if '-' in line:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))

    # Parse available IDs
    available_ids = [int(line) for line in id_lines if line.strip()]

    # For each available ID, check if it falls within any range
    def is_fresh(id_):
        for start, end in ranges:
            if start <= id_ <= end:
                return True
        return False

    return sum(1 for id_ in available_ids if is_fresh(id_))

def test_count_fresh_ingredient_ids_sample():
    sample_input = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''
    result = count_fresh_ingredient_ids(sample_input)
    assert result == 3

def test_count_fresh_ingredient_ids_overlap():
    input_str = '''1-5\n3-7\n\n2\n4\n6\n8'''
    # Fresh IDs: 1-7, available: 2,4,6,8; fresh: 2,4,6
    assert count_fresh_ingredient_ids(input_str) == 3

def test_count_fresh_ingredient_ids_single():
    input_str = '''10-10\n\n10\n11'''
    # Only 10 is fresh
    assert count_fresh_ingredient_ids(input_str) == 1

def test_count_fresh_ingredient_ids_none():
    input_str = '''1-2\n\n3\n4\n5'''
    # No available IDs are fresh
    assert count_fresh_ingredient_ids(input_str) == 0

def test_count_fresh_ingredient_ids_final():
    with open(r"c:/Projects/playground/aoc2025/5/input.txt", encoding='utf-8') as f:
        input_str = f.read()
    result = count_fresh_ingredient_ids(input_str)
    print(f"Final answer: {result}")
    

